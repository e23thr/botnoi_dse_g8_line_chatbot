from flask_restful import Resource
from flask import request, abort, redirect


class PersonalSupplement(Resource):
    def post(self):
        data = request.get_data()
        return data
