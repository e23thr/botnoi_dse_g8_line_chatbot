import json
from flask_restful import Resource
from flask import request
import numpy as np
from dseg8.gsheets import GoogleSheet, SHEET_FRIENDS
from dseg8.recommendation import get_recommendation, intent_to_answer, answer_to_supplement


class RecommendationKeep(Resource):
    def get(self):
        intent = request.args.get("i")
        line_id = request.args.get("customer_id")
        ps = GoogleSheet(SHEET_FRIENDS)
        existing_row = ps.df.loc[ps.df.line_id == line_id]
        result = ""
        if len(existing_row) == 0:
            ps.df = ps.df.append({"line_id": line_id, "intents": intent}, ignore_index=True)
            result = "NEW"
        else:
            result = "INTENT_ADDED"
            intents = existing_row.iloc[0]['intents']  # ps.df.loc[ps.df.lineId == line_id, "intents"]
            if intents is None:
                intents = ""
            intents = intents.split(",")
            intents.append(intent)
            intents = list(set(intents))  # discard duplicate
            ps.df.loc[ps.df.line_id == line_id, "intents"] = ",".join(intents)

        ps.df = ps.df.fillna("")
        ps.save()
        return {"result": result}


class RecommendationRecommend(Resource):
    def get(self):
        line_id = request.args.get("customer_id")
        ps = GoogleSheet(SHEET_FRIENDS)
        existing_row = ps.df.loc[ps.df.line_id == line_id]
        intents = [""]
        if len(existing_row) > 0:
            intents = existing_row.iloc[0]['intents']  # ps.df.loc[ps.df.lineId == line_id, "intents"]
            if intents is None:
                intents = ""
            intents = intents.split(",")

        # recommend for each intent
        recommends = []
        for intent in intents:
            answer_text = intent_to_answer.get(intent, "")
            recommendations = get_recommendation(answer_text, 5)
            # print("answer_text = {}".format(answer_text))
            # print("recommendations", recommendations)
            recommends.extend(recommendations)
        # convert answers to nutrition_data
        nutrition_data = []
        for recommend in recommends:
            nutrition_data.extend(answer_to_supplement[recommend])
        # random the recommendations
        nutrition_data = np.random.choice(nutrition_data, 5)
        # remove duplicate
        nutrition_data = list(set(nutrition_data))

        response_data = {
            "nutrition_data": ", ".join(nutrition_data),
            "intent": "in_recommendation"}
        response_header = {
            "Response-Type": "object"}

        return response_data, 200, response_header
