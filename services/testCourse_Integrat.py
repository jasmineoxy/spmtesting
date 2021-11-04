import unittest
import flask_testing
import json
from course import app,db,Course

# This is for the SQL Database and Stuff
# Add, Removing, Editing, CRUD Of the DB
# Testing the app


class TestCourse(flask_testing.TestCase):
    # Flask In build , Sqlite is a in memory DB , To run quick test
    # Set it as testing function , No need for a network allows you to call them directly
    app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite://"
    app.config['SQLALCHEMY_ENGINE_OPTIONS'] = {}
    app.config['TESTING'] = True

    # Create and Removes the DB
    # Will not override existing database
    def create_app(self):
        return app

    def setUp(self):
        db.create_all()

    def tearDown(self):
        db.session.remove()
        db.drop_all()


class TestCourseFunction(TestCourse):
# Function 1. Getting All Course
    def test_get_course(self):
        new_course = Course(courseId='X7847',
                    courseName='Print paper',
                    courseDescription='Learn how to print paper',
                    coursePrereq='')

        db.session.add(new_course)
        db.session.commit()
        # Fake a request body to send over the network body
        request_body = {}
        response = self.client.get("/course",
                                    data=json.dumps(request_body),
                                    content_type='application/json')
        # Use a print statement to check to see
        # print('This is the' , response.json['data']['course'])

        self.assertEqual(response.json['data']['course'], [{
            "courseDescription": 'Learn how to print paper',
            "courseId": 'X7847',
            "courseName": 'Print paper',
            "coursePrereq": ''
        }])

# Function 2. Getting A Course
    def test_a_course(self):
        new_course = Course(courseId='X7847',
                    courseName='Print paper',
                    courseDescription='Learn how to print paper',
                    coursePrereq='')

        db.session.add(new_course)
        db.session.commit()

        # Fake a request body to send over the network body
        request_body = {'courseId':new_course.courseId}
        # print('this is the request bodyy   ', request_body)
        # print(request_body['courseId'])

        url = "/course/{courseId}".format(courseId=new_course.courseId)

        # Oringial
        response = self.client.get(url,
                            data=json.dumps(request_body),
                            content_type='application/json')

        # print('this is the response json data' , response.json['data'])

        self.assertEqual(response.json['data'], {
            "courseId": 'X7847',
            "courseName": 'Print paper',
            "courseDescription": 'Learn how to print paper',
            "coursePrereq": ''
        })

# Function 3. Getting prereq
    def test_prereq_course(self):

        new_course1 = Course(courseId='X7846',
            courseName='Ink in Printer',
            courseDescription='Put Ink',
            coursePrereq='')

        new_course2 = Course(courseId='X7847',
                    courseName='Print paper',
                    courseDescription='Learn how to print paper',
                    coursePrereq='X7846')

        db.session.add(new_course1)
        db.session.add(new_course2)
        db.session.commit()
        # Fake a request body to send over the network body
        request_body = {'courseId':new_course2.courseId}

        # print(new_course2.courseId)
        url = "/course/pre_req/{courseId}".format(courseId=new_course2.courseId)

        response = self.client.get(url,
                                    data=json.dumps(request_body),
                                    content_type='application/json')

        # print(response.json['data'])

        self.assertEqual(response.json['data'], {
            "courseId":'X7847',
            "courseName":'Print paper',
            "courseDescription": 'Learn how to print paper',
            "coursePrereq": 'X7846'
        })

# 4 Add Course
    def test_add_new_course(self):
        # What I am trying to add , New Data

        new_course = Course(courseId='X7848',
                            courseName='Print paper',
                            courseDescription='Learn how to print paper',
                            coursePrereq='')

        # Fake a request body to send over the network body
        request_body = {
            'courseId': new_course.courseId,
            'courseName': new_course.courseName,
            'courseDescription': new_course.courseDescription,
            'coursePrereq': new_course.coursePrereq
            }

        response = self.client.post("/course/newcourse",
                                    data=json.dumps(request_body),
                                    content_type='application/json')
        # See the Print
        # print('This is the ' , response.json)

        self.assertEqual(response.json, {
            "courseId": 'X7848',
            "courseName": 'Print paper',
            "courseDescription": 'Learn how to print paper',
            "coursePrereq": ''
        })

# Function 2 Invalid Course detail
    def test_Invalid_course(self):
        new_course = Course(courseId='X7847',
                    courseName='Print paper',
                    courseDescription='Learn how to print paper',
                    coursePrereq='')

        db.session.add(new_course)
        db.session.commit()

        # Fake a request body to send over the network body
        request_body = {'courseName': new_course.courseName}
        url = "/course/{courseName}".format(courseName=new_course.courseName)

        # Oringial
        response = self.client.get(url,
                            data=json.dumps(request_body),
                            content_type='application/json')

        self.assertEqual(response.json,{
             "message": "Course details not found."
        })

    # Function 4 Invalid new course
    def test_Invalid_new_course(self):
        # Missing Data
        new_course = Course(courseId='X7848',
                            courseName='Print paper',
                            courseDescription='Learn how to print paper',
                            coursePrereq='')

        # Fake a request body to send over the network body
        request_body = {
            'courseId':new_course.courseId,
            'courseId':new_course.courseId,
            'courseDescription':new_course.courseDescription,
            'coursePrereq':new_course.coursePrereq
            }

        response = self.client.post("/course/newcourse",
                                    data=json.dumps(request_body),
                                    content_type='application/json')

        # print('This is the ', response.json)

        self.assertEqual(response.status_code, 500)
        self.assertEqual(response.json, {
           "message": "Incorrect JSON object provided."
        })


if __name__ == '__main__':
    unittest.main()
