# !/usr/local/bin/python
# -*- coding: utf-8 -*-

from msilib.schema import Error
from flask import Flask, jsonify, request
from RidgeRegression import CalculateByRidge

#http://localhost:5000/calculate?location=9&article=25&articleLevel=3&studentLevel=9&lessonTime=35

app = Flask(__name__)

@app.route("/")
def mainPage():
    return jsonify({"success": True, "backend": "FY", "frontend": "OD"})

@app.route("/calculate", methods=["GET", "POST"])
def calculate():
    print("XXXXXXXXXXXX")

    
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
            return jsonify({"success": False, "result": "resultFromRidge"})
    else:
        return jsonify({"success": False, "message": "GET method is not supported"})
    
if __name__ == "__main__":
    app.run(debug=True, host='127.0.0.1')