
import os

import base64
import hashlib
import hmac
import json

from flask_restful import Resource
from flask import request, abort, redirect
import requests

from linebot import LineBotApi, WebhookHandler

from linebot.exceptions import InvalidSignatureError

from linebot.models import MessageEvent, TextMessage, TextSendMessage, FollowEvent, UnfollowEvent
from dotenv import load_dotenv

load_dotenv()

LINE_TOKEN = os.getenv('LINE_CHANNEL_TOKEN')
LINE_SECRET = os.getenv('LINE_CHANNEL_SECRET')

# print('line.py {}'.format(LINE_TOKEN))

linebotapi = LineBotApi(LINE_TOKEN)
webhook_handler = WebhookHandler(LINE_SECRET)


class LinebotApp(Resource):
    def post(self):
        signature = request.headers['X-Line-Signature']
        body = request.get_data(as_text=True)
        print('body')
        print(body)
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
    # need to pass to botnoi platform
    # https://api-gateway.botnoinoi.com/webhook/5f573d677c3ff7000ac2248c/line
    # print("message detected")
    # print(event.type)
    # print(event)
    # print(request.headers)
    # print(request.get_data(as_text=True))
    BOTNOI_ENDPOINT = os.getenv("BOTNOI_ENDPOINT")
    LINE_CHANNEL_SECRET = os.getenv("LINE_CHANNEL_SECRET")
    data = request.get_data(as_text=True)
    signature = hmac.new(LINE_CHANNEL_SECRET.encode(
        'utf-8'), data.encode('utf-8'), hashlib.sha256).digest()
    signature = base64.b64encode(signature)
    headers = {}
    headers['X-Line-Signature'] = signature
    # headers['X-Line-Signature'] = request.headers['X-Line-Signature']
    # headers['Host'] = 'api-gateway.botnoinoi.com'
    headers['User-Agent'] = request.headers['User-Agent']

    # headers['Authorization'] = 'Bearer {}'.format(os.getenv(
    # "LINE_CHANNEL_TOKEN"))
    json_data = request.get_data(as_text=True)
    print(request.headers)
    resp = requests.post(BOTNOI_ENDPOINT, headers=headers,
                         json=json.loads(json_data))
    # print("HEADERS")
    # print(request.headers)
    print(BOTNOI_ENDPOINT)
    print("STATUS_CODE")
    print(resp.status_code)
    print("REQUEST_HEADERS")
    print(resp.request.headers)
    print("REQUEST_BODY")
    print(resp.request.body)

    print("RESPONSE BODY")
    print(resp.content)
    # print(BOTNOI_ENDPOINT)
    # return redirect(BOTNOI_ENDPOINT)
    # request.post(BOTNOI_ENDPOINT, body=request.get_data())
    # pass
    return resp.content


@webhook_handler.add(UnfollowEvent)
def handle_unfollow():
    pass
