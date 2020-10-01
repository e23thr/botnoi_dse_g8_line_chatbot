import base64
import hashlib
import hmac


import os
import os.path
from dotenv import load_dotenv

from flask import Flask, send_from_directory, Response, render_template, abort

from flask_restful import Resource, Api,reqyest

from flask_cors import CORS

from dseg8.line import LinebotApp

from dseg8.gsheets import read_friends, write_friends

from dseg8.utility import BMI_Calculator

load_dotenv()

app = Flask(__name__)
api = Api(app)


app.url_map.strict_slashes = False

app.config['TEMPLATES_AUTO_RELOAD'] = True

CORS(app)


api.add_resource(LinebotApp, '/api/linebot')

# Adding route for liff app


@app.route('/liff/<path:filename>')  # ใช้ static html จาก folder static
def static_files(filename):
    print(filename)
    file_name = os.path.join(
        os.path.dirname(os.path.abspath(__file__)), "templates", filename)

    if os.path.exists(file_name):
        print("render {}".format(file_name))
        return render_template(filename)
    else:
        # Return not found http status code 404 and use browser default 404 page
        return abort(404)

# @app.after_request
# def add_header(response):
#     # response.cache_control.no_store = True
#     if 'Cache-Control' not in response.headers:
#         response.headers['Cache-Control'] = 'no-cache, no-store, must-revalidate'
#     if 'Pragma' not in response.headers:
#         response.headers['Pragma'] = 'no-cache'
#     if 'Expires' not in response.headers:
#         response.headers['Expires'] = '0'
#     return response

###BMI API Function
class get_BMI(Resource):
    def get(self):
        parser = reqparse.RequestParser()
        dictp['weight'] = float(reqyest.args.get("weight"))
        dictp['height'] = float(reqyest.args.get("height"))

        return BMI_Calculator(dictp['weight'],dictp['height'])

api.add_resource(get_BMI, '/get_BMI',endpoint='get_BMI')
###





if __name__ == "__main__":
    app.run(threaded=False)
