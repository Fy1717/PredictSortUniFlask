# !/usr/local/bin/python
# -*- coding: utf-8 -*-

from flask import Flask, jsonify, request
from RidgeRegression import CalculateByRidge

#http://localhost:5000/calculate?locationPoint=9&broadcastingNumber=25&broadcastingDegree=3&studentDegree=9&lessonTime=35

app = Flask(__name__)

@app.route("/")
def mainPage():
    return jsonify({"success": True, "backend": "FY", "frontend": "OD"})

@app.route("/calculate", methods=["GET", "POST"])
def calculate():
    #print("XXXXXXXXXXXX")

    if request.method == "POST":
        locationPoint = request.args.get("locationPoint")
        broadcastingNumber = request.args.get("broadcastingNumber")
        broadcastingDegree = request.args.get("broadcastingDegree")
        studentDegree = request.args.get("studentDegree")
        lessonTime =  request.args.get("lessonTime")

        resultFromRidge = CalculateByRidge(locationPoint, broadcastingNumber, broadcastingDegree, studentDegree, lessonTime)
        print("RESULT FROM RIDGE: ", resultFromRidge)

        #print("\nLocationPoint: " + locationPoint + "\n" + "broadcastingNumber: " + broadcastingNumber + "\n" + "broadcastingDegree: " + broadcastingDegree + "\n" + "studentDegree: " + studentDegree + "\n" + "lessonTime: " + lessonTime)

        return jsonify({"success": True, "result": resultFromRidge})
    else:
        return jsonify({"success": False, "message": "GET method is not supported"})
    
if __name__ == "__main__":
    app.run(debug=True, host='127.0.0.1')