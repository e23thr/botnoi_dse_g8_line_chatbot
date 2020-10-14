import json
from flask_restful import Resource
from flask import request
from dseg8.gsheets import GoogleSheet, SHEET_PERSONAL_SUPPLEMENTS


class TestApi(Resource):
    def get(self):
        print("request.args")
        print(request.args)
        print("request.headers")
        print(request.headers)
        return {"args": request.args}


class PersonalSupplement(Resource):
    def post(self):
        data = json.loads(request.get_data(as_text=True))
        data["อายุ"] = int(data["อายุ"])
        ps = GoogleSheet(SHEET_PERSONAL_SUPPLEMENTS)
        # ps.df = ps.df.astype({'อายุ': 'int32'}).dtypes
        # print("data", data)
        ps.df['อายุ'] = ps.df['อายุ'].astype(int)
        existing_row = ps.df.loc[ps.df.lineId == data['lineId']]
        # print('existing_row', existing_row)
        if len(existing_row) == 0:
            # print("Create a new row")
            ps.df = ps.df.append(data, ignore_index=True)
        else:
            # print("Update row")
            for k in data.keys():
                # print("Update key ", k, data[k])
                ps.df.loc[ps.df.lineId == data['lineId'], k] = data[k]
            # ps.df.loc[ps.df.lineId == data.lineId] =
        ps.df = ps.df.fillna("")
        # print(ps.df)
        ps.save()
        return data
