import os
import requests
import json
from math import sin, cos, sqrt, atan2, radians
from dotenv import load_dotenv

load_dotenv()

GMAP_KEY = os.getenv("GMAP_KEY")


def find_nearby(lat, lon):
    url = "https://maps.googleapis.com/maps/api/place/nearbysearch/json?location={},{}&radius=1500&type=drugstore&keyword=&key={}".format(
        lat, lon, GMAP_KEY)
    # print("URL: {}".format(url))
    resp = requests.get(url)
    return resp.json()


def get_place_info(place_id):
    url = "https://maps.googleapis.com/maps/api/place/details/json?place_id={}&fields=name,formatted_address,rating,formatted_phone_number&key={}".format(
        place_id, GMAP_KEY)
    resp = requests.get(url)
    return resp.json()


def format_place(place_data):
    data = {}
    data['name'] = place_data['name']
    if ('photos' in place_data and len(place_data['photos']) > 0):
        data['photo_url'] = "https://maps.googleapis.com/maps/api/place/details/json?place_id={}&fields=name,rating,formatted_phone_number,formatted_address&key={}".format(
            place_data['photos'][0]['photo_reference'], GMAP_KEY)
    else:
        # need temporary image placeholder
        # https://lunawood.com/wp-content/uploads/2018/02/placeholder-image.png
        # https://dunlite.com.au/wp-content/uploads/2019/04/placeholder.jpg
        data['photo_url'] = "https: // dunlite.com.au/wp-content/uploads/2019/04/placeholder.jpg"
    data['lat'] = place_data['geometry']['location']['lat']
    data['lon'] = place_data['geometry']['location']['lng']
    data['address'] = place_data['vicinity']
    data['is_open'] = place_data['opening_hours']['open_now']
    return data


def calculate_distance(lat1, lon1, lat2, lon2):
    R = 6373.0

    dlon = lon2 - lon1
    dlat = lat2 - lat1

    a = sin(dlat / 2)**2 + cos(lat1) * cos(lat2) * sin(dlon / 2)**2
    c = 2 * atan2(sqrt(a), sqrt(1 - a))

    distance = R * c
    return distance


def gmap_pipeline(lat, lon):
    result = find_nearby(lat, lon)
    # print("RESULT find_nearby")
    # print(result)
    places_list = result['results']
    data_list = []
    print("places: {}".format(len(places_list)))
    for place in list(places_list[:10]):
        data = {}
        # print("\n\n{}".format(place['name']))
        # print(place)
        data['lat'] = place['geometry']['location']['lat']
        data['lon'] = place['geometry']['location']['lng']
        data['is_open'] = "ไม่ระบุ"
        if ('opening_hours' in place and 'open_now' in place['opening_hours']):
            data['is_open'] = 'เปิดให้บริการ' if place['opening_hours']['open_now'] else "ปิดร้านอยู่"
        if ('photos' in place and len(place['photos']) > 0):
            # resp = requests.get("https://maps.googleapis.com/maps/api/place/photo?maxwidth=400&photoreference={}&key={}".format(
            #     place['photos'][0]['photo_reference'], GMAP_KEY))
            # data['photo_url'] = resp.url
            data['photo_url'] = "https://maps.googleapis.com/maps/api/place/photo?maxwidth=400&photoreference={}&key={}".format(
                place['photos'][0]['photo_reference'], GMAP_KEY)
        else:
            # need temporary image placeholder
            # https://lunawood.com/wp-content/uploads/2018/02/placeholder-image.png
            # https://dunlite.com.au/wp-content/uploads/2019/04/placeholder.jpg
            data['photo_url'] = "https://dunlite.com.au/wp-content/uploads/2019/04/placeholder.jpg"

        place_info = get_place_info(place['place_id'])['result']

        data['shop_name'] = place['name']
        if 'formatted_phone_number' in place_info:
            data['phone'] = place_info['formatted_phone_number']
        else:
            data['phone'] = ''

        if 'formatted_address' in place_info:
            data['address'] = place_info['formatted_address']
        else:
            data['address'] = 'ไม่ระบุ'

        # data['place_info'] = place_info

        if 'rating' in place_info:
            data['rating'] = place_info['rating']
        else:
            data['rating'] = -1

        data_list.append(data)

    return data_list
