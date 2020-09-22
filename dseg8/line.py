
import os

from flask_restful import Resource
from flask import request, abort, redirect
import requests

from linebot import LineBotApi, WebhookHandler
from linebot.exceptions import InvalidSignatureError
from linebot.models import (
    MessageEvent, TextMessage, TextSendMessage, FollowEvent, UnfollowEvent,
    LocationMessage, TextSendMessage, TemplateSendMessage, CarouselColumn, URIAction, CarouselTemplate
)

from dotenv import load_dotenv

from .botnoi import forward_to_botnoi
from .gmap import gmap_pipeline

load_dotenv()

LINE_TOKEN = os.getenv('LINE_CHANNEL_TOKEN')
LINE_SECRET = os.getenv('LINE_CHANNEL_SECRET')

linebotapi = LineBotApi(LINE_TOKEN)
webhook_handler = WebhookHandler(LINE_SECRET)


class LinebotApp(Resource):
    def post(self):
        signature = request.headers['X-Line-Signature']
        body = request.get_data(as_text=True)
        try:
            webhook_handler.handle(body, signature)
        except InvalidSignatureError:
            print("Invalid signature. Please check your channel token/secret")
            abort(400)
        return 'OK'


@webhook_handler.add(FollowEvent)
def handle_follow():
    pass


@webhook_handler.add(MessageEvent, message=TextMessage)
def handle_message(event):
    resp = forward_to_botnoi(data_as_str=request.get_data(
        as_text=True), request_headers=request.headers)
    return resp.content


@webhook_handler.add(MessageEvent, message=LocationMessage)
def handle_location(event):
    lat = event.message.latitude
    lon = event.message.longitude
    shops_list = gmap_pipeline(lat, lon)
    columns = []
    for shop in shops_list:
        actions = []
        actions.append(URIAction(
            label="แผนที่", uri="https://www.google.com/maps/@{},{},16z".format(shop['lat'], shop['lon'])))

        if (shop['phone'] != ''):
            actions.append(URIAction(label="T:{}".format(shop['phone']), uri="tel:{}".format(
                shop['phone'].replace(" ", ""))[:20]))
        else:
            actions.append(URIAction(label="No phone", uri="tel:000"))

        column = CarouselColumn(
            thumbnail_image_url=shop['photo_url'],
            title=shop['shop_name'],
            text="ที่อยู่: {}".format(shop['address'])[:60],
            actions=actions
        )
        # print(column)
        columns.append(column)
        # print(len(columns))

    template_message = TemplateSendMessage(
        alt_text="ร้านขายยา",
        template=CarouselTemplate(
            columns=columns
        )
        # columns=columns
    )

    print(template_message)

    return linebotapi.reply_message(
        event.reply_token,
        template_message
    )

    # linebotapi.reply_message(event.reply_token, TextSendMessage(
    #     text="lat {}, lon {}".format(lat, lon)))


@webhook_handler.add(UnfollowEvent)
def handle_unfollow():
    pass
