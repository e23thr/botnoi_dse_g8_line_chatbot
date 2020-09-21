
import os
from flask_restful import Resource
from flask import request, abort

from linebot import LineBotApi, WebhookHandler

from linebot.exceptions import InvalidSignatureError

from linebot.models import MessageEvent, TextMessage, TextSendMessage, FollowEvent, UnfollowEvent
from dotenv import load_dotenv

load_dotenv()

LINE_TOKEN = os.getenv('LINE_CHANNEL_TOKEN')
LINE_SECRET = os.getenv('LINE_CHANNEL_SECRET')

print('line.py {}'.format(LINE_TOKEN))

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


@webhook_handler.add(MessageEvent)
def hanlde_message():


@webhook_handler.add(UnfollowEvent)
def handle_unfollow():
    pass
