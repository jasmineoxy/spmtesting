import os
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


class Section(db.Model):
    __tablename__ = "section"

    classId = db.Column(db.VARCHAR(64), primary_key=True)
    courseId = db.Column(db.VARCHAR(64), primary_key=True)
    sectionId = db.Column(db.VARCHAR(64), primary_key=True)
    sectionTitle = db.Column(db.VARCHAR(200), nullable=False)
    estimatedTime = db.Column(db.VARCHAR(64), nullable=False)
    content = db.Column(db.TEXT, nullable=True)

    def to_dict(self):
        columns = self.__mapper__.column_attrs.keys()
        result = {}
        for column in columns:
            result[column] = getattr(self, column)
        return result

    # -------------------------------
    # Get all section information in a particular class
    @app.route("/myCourses/<string:courseId>/<string:classId>")
    def getAllSectionsInAClass(courseId, classId):
        sections = Section.query.filter(
            Section.courseId.like(courseId), Section.classId.like(classId)
        ).all()
        if sections:
            return jsonify(
                {"code": 200, "data": [section.to_dict() for section in sections]}
            )
        return (
            jsonify({"message": "There are no sections created for this course"}),
            404,
        )

    # -------------------------------
    # Get a particular section information in a particular class
    @app.route("/myCourses/<string:courseId>/<string:classId>/<string:sectionId>")
    def getASectionInAClass(courseId, classId, sectionId):
        sections = Section.query.filter(
            Section.courseId.like(courseId),
            Section.classId.like(classId),
            Section.sectionId.like(sectionId),
        ).first()
        if sections:
            return jsonify({"code": 200, "data": sections.to_dict()})
        return (
            jsonify({"message": "There are no sections created for this course"}),
            404,
        )


if __name__ == "__main__":
    print("This is flask for " + os.path.basename(__file__) + ": SPM ...")
    app.run(host="0.0.0.0", port=5006, debug=True)
