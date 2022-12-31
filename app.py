# !/usr/local/bin/python
# -*- coding: utf-8 -*-

from flask import Flask, jsonify, request
from RidgeRegression import CalculateByRidge
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route("/")
def mainPage():
    return jsonify({"success": True})

@app.route("/calculate", methods=["GET", "POST"])
def calculate():
    try:
        if request.method == "POST":
            try:
                print("REQUEST JSON:", request.json)

                location = request.json["location"]
                article = request.json["article"]
                articleLevel = request.json["articleLevel"]
                studentLevel = request.json["studentLevel"]
                lessonTime = request.json["lessonTime"]
                
                #print("LOCATION : ", location, " ARTICLE : ", article, " ARTICLE LEVEL : ", articleLevel, " STUDENT LEVEL : ", studentLevel, " LESSON TIME : ", lessonTime)
            
                resultFromRidge = CalculateByRidge(location, article, articleLevel, studentLevel, lessonTime)
                #print("RESULT FROM RIDGE: ", resultFromRidge)
            
                return jsonify({"success": True, "result": resultFromRidge})

            except Exception as e:
                print("ERROR : ", e)
                return jsonify({"success": False, "result": str(e)})
        else:
            return jsonify({"success": False, "message": "GET method is not supported"})
    except Exception as e:
        print("ERROR 2 : ", e)
        return jsonify({"success": False, "result": str(e)})