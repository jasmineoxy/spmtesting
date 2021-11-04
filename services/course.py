from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from os import environ
from flask_cors import CORS


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


# Sql Alchemy may rearrange to the alphabetical order
class Course(db.Model):
    __tablename__ = "course"

    courseId = db.Column(db.VARCHAR(64), primary_key=True)
    courseName = db.Column(db.VARCHAR(64))
    courseDescription = db.Column(db.VARCHAR(64))
    coursePrereq = db.Column(db.VARCHAR(1000))

    def __init__(self, courseId, courseName, courseDescription, coursePrereq):
        self.courseId = courseId
        self.courseName = courseName
        self.courseDescription = courseDescription
        self.coursePrereq = coursePrereq

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
        # print(self)
        return {
            "courseId": self.courseId,
            "courseName": self.courseName,
            "courseDescription": self.courseDescription,
            "coursePrereq": self.coursePrereq,
        }


# db.create_all()
# NEW
# Function 1 Get all courses


@app.route("/course")
def get_courses():
    course_list = Course.query.all()
    if len(course_list):
        return jsonify(
            {
                "code": 200,
                "data": {
                    "course": [course_list.to_dict() for course_list in course_list]
                },
            }
        )

    return jsonify({"message": "There are no courses."}), 404


# Function 2 Get a course details
# Default method is GET
@app.route("/course/<string:courseId>")
def get_course_detail(courseId):

    print("this is courseid ", courseId)
    # #shows that is a string
    print(type(courseId))

    course_detail = Course.query.filter_by(courseId=courseId).first()
    print("this is the course details", course_detail)

    if course_detail:
        return jsonify({"code": 200, "data": course_detail.to_dict()})

    return jsonify({"message": "Course details not found."}), 404


# Function 3 Get course Pre-Req
@app.route("/course/pre_req/<string:courseId>")
def get_pre_req(courseId):
    print("This is the ", courseId)
    pre_reqs = Course.query.filter_by(courseId=courseId).first()

    print("This is the Preq_req", pre_reqs)
    if pre_reqs:
        return jsonify({"code": 200, "data": pre_reqs.to_dict()})

    return jsonify({"message": "There are errors trying to get the Pre-Req."}), 404


# Function 4 Add a course
@app.route("/course/newcourse", methods=["POST"])
def add_course():
    # Check the all data are added correctly  (Look at Keys)
    data = request.get_json()
    # Check if data works Postman
    # print(data)
    if not all(
        key in data.keys()
        for key in ("courseId", "courseName", "courseDescription", "coursePrereq")
    ):
        return jsonify({"message": "Incorrect JSON object provided."}), 500

    # Validate Course
    courseId = Course.query.filter_by(courseId=data["courseId"]).first()
    # Does not exist
    if courseId:
        return jsonify({"message": "Course ID already inside."}), 500

    # Create course
    course = Course(
        courseId=data["courseId"],
        courseName=data["courseName"],
        courseDescription=data["courseDescription"],
        coursePrereq=data["coursePrereq"],
    )

    # print(course.courseId)
    # print(course.courseDescription)
    # print(course.courseName)
    # print(course.coursePrereq)

    # Add it in DB
    try:
        db.session.add(course)
        db.session.commit()
        return jsonify(course.to_dict()), 201

    except Exception:
        return jsonify({"message": "An error occurred creating the course."}), 500
# Note may have to change the port number cause we need to use different ones


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
