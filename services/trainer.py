# import os
from flask import Flask, jsonify
from flask_sqlalchemy import SQLAlchemy
# from sqlalchemy import *
from flask_cors import CORS

from os import environ

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


class Trainer(db.Model):
    __tablename__ = "trainer"

    employeeId = db.Column(db.String(64), primary_key=True)

    def __init__(self, employeeId):
        self.employeeId = employeeId

    def json(self):
        return {"employeeId": self.employeeId}


@app.route("/trainer")
def getAllTrainers():
    trainerlist = Trainer.query.all()
    if len(trainerlist):
        return jsonify(
            {
                "code": 200,
                "data": {"trainers": [trainer.json() for trainer in trainerlist]},
            }
        )
    return jsonify({"code": 404, "message": "There are no trainers."}), 404


@app.route("/trainer/<string:employeeId>")
def getTrainerById(employeeId):
    trainer = Trainer.query.filter_by(employeeId=employeeId).first()
    if trainer:
        return jsonify({"code": 200, "data": trainer.json()})
    return jsonify({"code": 404, "message": "Trainer not found."}), 404


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5003, debug=True)
