import os
import base64
import hashlib
import hmac
import json

import requests

BOTNOI_ENDPOINT = os.getenv("BOTNOI_ENDPOINT")
LINE_CHANNEL_SECRET = os.getenv("LINE_CHANNEL_SECRET")


def forward_to_botnoi(data_as_str, request_headers):
    # data = request.get_data(as_text=True)
    signature = hmac.new(LINE_CHANNEL_SECRET.encode(
        'utf-8'), data_as_str.encode('utf-8'), hashlib.sha256).digest()
    signature = base64.b64encode(signature)
    headers = {}
    headers['X-Line-Signature'] = signature
    headers['User-Agent'] = request_headers['User-Agent']

    resp = requests.post(BOTNOI_ENDPOINT, headers=headers,
                         json=json.loads(data_as_str))
    return resp
