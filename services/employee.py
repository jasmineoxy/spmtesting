# from flask import Flask, request, jsonify
from flask import Flask, jsonify
from flask_sqlalchemy import SQLAlchemy
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


class Employee(db.Model):
    __tablename__ = "Employee"
    employeeId = db.Column(db.String(64), primary_key=True)
    employeeName = db.Column(db.String(64), nullable=False)
    department = db.Column(db.String(64), nullable=False)
    role = db.Column(db.String(64), nullable=False)

    def __init__(self, employeeId, employeeName, department, role):
        self.employeeId = employeeId
        self.employeeName = employeeName
        self.department = department
        self.role = role

    # Chris
    # Adding stuff inside , Use a dictionary
    def to_dict(self):
        """
        'to_dict' converts the object into a dictionary,
        in which the keys correspond to database columns
        """
        columns = self.__mapper__.column_attrs.keys()
        result = {}
        for column in columns:
            result[column] = getattr(self, column)
        return result

    def json(self):
        return {
            "employeeId": self.employeeId,
            "employeeName": self.employeeName,
            "department": self.department,
            "role": self.role,
        }


@app.route("/seniorEngineers")
def getAllSeniorEngineers():
    seniorEngineerList = Employee.query.filter_by(department="seniorEngineer")
    if seniorEngineerList:
        return jsonify(
            {
                "code": 200,
                "data": {
                    "seniorEngineer": [
                        seniorEngineer.json() for seniorEngineer in seniorEngineerList
                    ]
                },
            }
        )
    return jsonify({"code": 404, "message": "There are no senior engineers. "}), 404


@app.route("/juniorEngineers")
def getAllJuniorEngineers():
    juniorEngineerList = Employee.query.filter_by(department="juniorEngineer")
    if juniorEngineerList:
        return jsonify(
            {
                "code": 200,
                "data": {
                    "juniorEngineer": [
                        juniorEngineer.json() for juniorEngineer in juniorEngineerList
                    ]
                },
            }
        )
    return jsonify({"code": 404, "message": "There are no junior engineers. "}), 404


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5002, debug=True)
