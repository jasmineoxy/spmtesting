from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
import os
from os import environ

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = environ.get('dbURL') or 'mysql+mysqlconnector://root@localhost:3306/allinone' or 'mysql+mysqlconnector://root:root@localhost:3306/allinone'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_ENGINE_OPTIONS'] = {'pool_recycle': 299}

db = SQLAlchemy(app)

CORS(app)


class Learner(db.Model):

    __tablename__ = 'learner'

    employeeId = db.Column(db.String(64), primary_key=True)
    employeeName = db.Column(db.String(64), nullable=False)
    learnerCoursesCompleted = db.Column(db.String(64), nullable=False)
    learnerCoursesInProgress = db.Column(db.String(64), nullable=False)

    def to_dict(self):
        columns = self.__mapper__.column_attrs.keys()
        result = {}
        for column in columns:
            result[column] = getattr(self,column)
        return result

    @app.route("/learner/<string:employeeId>")
    def getLearnerById(employeeId):
        LearnerById = Learner.query.filter_by(employeeId=employeeId).first()
        if LearnerById:
            return jsonify(
                {
                    "code": 200,
                    "data": LearnerById.to_dict()
                }
            )
        return jsonify(
            {
                "code": 404,
                "message": "There is no such learner. "
            }
        ), 404

    @app.route("/learner")
    def getAllLearners():
        allLearnersList = Learner.query.all()
        if allLearnersList:
            return jsonify(
                {
                    "code": 200,
                    "data": [allLearnersList.to_dict() for allLearnersList in allLearnersList]
                }
            )
        return jsonify(
            {
                "code": 404,
                "message": "There is no learners at all. "
            }
        ), 404

    @app.route("/learner/coursesCompleted/<string:courseId>")
    def getLearnerIdListByCoursesCompleted(courseId):
        LearnersOfCoursesCompleted = Learner.query.filter_by(learnerCoursesCompleted=courseId).all()
        if LearnersOfCoursesCompleted:
            return jsonify(
                {
                    "code": 200,
                    "data": [eachLearner.to_dict()["employeeId"] for eachLearner in LearnersOfCoursesCompleted]
                }
            )
        return jsonify(
            {
                "code": 404,
                "message": "There is no learners who have completed this course. "
            }
        ), 404

    @app.route("/learner/coursesInProgress/<string:courseId>")
    def getLearnerIdListByCoursesInProgress(courseId):
        LearnersOfCoursesInProgress = Learner.query.filter_by(learnerCoursesInProgress=courseId).all()
        if LearnersOfCoursesInProgress:
            return jsonify(
                {
                    "code": 200,
                    "data": [eachLearner.to_dict()["employeeId"] for eachLearner in LearnersOfCoursesInProgress]
                }
            )
        return jsonify(
            {
                "code": 404,
                "message": "There is no learners who are in progress in this course. "
            }
        ), 404

    @app.route("/learner/<string:employeeId>/coursesInProgress")
    def getLearnerCoursesInProgress(employeeId):
        LearnersCoursesInProgress = Learner.query.filter_by(employeeId=employeeId).first()
        if LearnersCoursesInProgress:
            return jsonify(
                {
                    "code": 200,
                    "data": LearnersCoursesInProgress.to_dict()["learnerCoursesInProgress"]
                }
            )
        return jsonify(
            {
                "code": 404,
                "message": "There is no record of this learner. "
            }
        ), 404


class EnrollClassList(db.Model):
    __tablename__ = 'enrolledClassList'

    classId = db.Column(db.String(64), primary_key=True)
    courseId = db.Column(db.String(64), primary_key=True)
    employeeId = db.Column(db.String(64), primary_key=True)
    employeeName = db.Column(db.String(64), nullable=False)

    def to_dict(self):
        columns = self.__mapper__.column_attrs.keys()
        result = {}
        for column in columns:
            result[column] = getattr(self,column)
        return result

    @app.route("/enrollClassList")
    def getEnrollClassList():
        enrollClassList = EnrollClassList.query.all()
        if enrollClassList:
            return jsonify(
                {
                    "code": 200,
                    "data": [enrollClassList.to_dict() for enrollClassList in enrollClassList]
                }
            )
        return jsonify(
            {
                "code": 404,
                "message": "There is no enroll class list at all. "
            }
        ), 404

    @app.route("/enrollClassList/<string:courseId>")
    def getEnrollClassListByCourseId(courseId):
        enrollClassList = EnrollClassList.query.filter_by(courseId=courseId).all()
        if enrollClassList:
            return jsonify(
                {
                    "code": 200,
                    "data": [enrollClassList.to_dict() for enrollClassList in enrollClassList]
                }
            )
        return jsonify(
            {
                "code": 404,
                "message": "There is no enroll class list of this course at all. "
            }
        ), 404

    @app.route("/enrollClassList", methods=['POST'])
    def addLearnerToEnrolledClassList():
        data = request.get_json()
        if not all(key in data.keys() for
                    key in ('classId','courseId','employeeId', 'employeeName')):
            return jsonify({
                "message": "Incorrect JSON object provided."
            }), 500

        learner = Learner.query.filter_by(employeeId=data['employeeId']).first
        if not learner:
            return jsonify({
                "message": "Learner not valid."
            }), 500

        enrollLearner = EnrollClassList(
            classId=data['classId'],
            courseId=data['courseId'],
            employeeId=data['employeeId'],
            employeeName=data['employeeName']
        )

        try:
            db.session.add(enrollLearner)
            db.session.commit()
            return jsonify(enrollLearner.to_dict()), 201
        except Exception:
            return jsonify({
                "message": "Unable to commit to database."
            }), 500


if __name__ == '__main__':
    print("This is flask for " + os.path.basename(__file__) + ": SPM ...")
    app.run(host='0.0.0.0', port=5004, debug=True)
