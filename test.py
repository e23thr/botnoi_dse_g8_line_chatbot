from dseg8.gmap import find_nearby, format_place

response = find_nearby(13.7183498, 100.4630065)

for r in response['results']:
    print(format_place(r))
    # print("name: {}".format(r['name']))
    # if ('photos' in r and len(r['photos']) > 0):
    #     print("Photo Reference: {}".format(r['photos'][0]['photo_reference']))
    # print("lat/lon: {},{}".format(r['geometry']['location']
    #                               ['lat'], r['geometry']['location']['lng']))
