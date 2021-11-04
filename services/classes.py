import os
# from flask import Flask, request, jsonify
from flask import Flask, jsonify
from flask_sqlalchemy import SQLAlchemy
# from sqlalchemy import *
from flask_cors import CORS

# import json
# import os, sys
from os import environ

# from sqlalchemy.orm import query

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = (
    environ.get("dbURL")
    or "mysql+mysqlconnector://root@localhost:3306/allinone"
    or "mysql+mysqlconnector://root:root@localhost:3306/allinone"
)
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
app.config["SQLALCHEMY_ENGINE_OPTIONS"] = {"pool_recycle": 299}

db = SQLAlchemy(app)

CORS(app)


class Class(db.Model):
    __tablename__ = "classes"

    classId = db.Column(db.VARCHAR(64), primary_key=True)
    courseId = db.Column(db.VARCHAR(64), primary_key=True)
    courseName = db.Column(db.VARCHAR(500), nullable=False)
    classStartDate = db.Column(db.VARCHAR(50), nullable=False)
    classEndDate = db.Column(db.VARCHAR(50), nullable=False)
    classStartTime = db.Column(db.VARCHAR(50), nullable=False)
    classEndTime = db.Column(db.VARCHAR(50), nullable=False)
    classDay = db.Column(db.VARCHAR(50), nullable=False)
    currentClassSize = db.Column(db.VARCHAR(100), nullable=False)
    maxClassSize = db.Column(db.VARCHAR(100), nullable=False)
    employeeId = db.Column(db.VARCHAR(64), nullable=True)
    employeeName = db.Column(db.VARCHAR(64), nullable=True)

    def to_dict(self):
        columns = self.__mapper__.column_attrs.keys()
        result = {}
        for column in columns:
            result[column] = getattr(self, column)
        return result

    # -------------------------------
    # Get all classes information
    @app.route("/class/all")
    def getAllClasses():
        myClass = Class.query.all()
        if len(myClass):
            return jsonify(
                {"code": 200, "data": [classes.to_dict() for classes in myClass]}
            )
        return jsonify({"message": "There are no classes."}), 404

    # -------------------------------
    # Get the all the available classes for a particular course (e.g. get the available classes for class 1)
    @app.route("/class/<string:courseId>")
    def getClassesByCourse(courseId):
        myClass = Class.query.filter_by(courseId=courseId).all()
        if myClass:
            return jsonify(
                {"code": 200, "data": [classes.to_dict() for classes in myClass]}
            )
        return (
            jsonify({"message": "There is no such available classes for this course"}),
            404,
        )


if __name__ == "__main__":
    print("This is flask for " + os.path.basename(__file__) + ": SPM ...")
    app.run(host="0.0.0.0", port=5001, debug=True)
