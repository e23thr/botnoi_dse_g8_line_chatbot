import base64
import hashlib
import hmac


import os
import os.path
from dotenv import load_dotenv

from flask import Flask, Response, render_template

from flask_restful import Resource, Api, reqparse

from flask_cors import CORS

from dseg8.line import LinebotApp

from dseg8.gsheets import read_friends, write_friends

load_dotenv()

app = Flask(__name__)
api = Api(app)


app.url_map.strict_slashes = False

CORS(app)


@app.route("/")
def root_route():
    return "OK"


api.add_resource(LinebotApp, '/api/linebot')

if __name__ == "__main__":
    app.run(threaded=True)

# for testing
# https://developers.google.com/sheets/api/quickstart/python
# rows = read_friends()
# print(rows)
# write_friends('myid', 'myname')
