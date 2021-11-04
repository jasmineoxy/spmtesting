import unittest
import flask_testing
import json
from classes import app, db, Class


class testClass(flask_testing.TestCase):
    app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite://"
    app.config['SQLALCHEMY_ENGINE_OPTIONS'] = {}
    app.config['TESTING'] = True

    def create_app(self):
        return app

    def setUp(self):
        db.create_all()

    def tearDown(self):
        db.session.remove()
        db.drop_all()


class testClassFunction(testClass):

    # Get all classes test
    def test_get_all_classes(self):
        new_class = Class(
            classId='G4',
            courseId='X888',
            courseName='Scanning Documents',
            classStartDate='01/12/2021',
            classEndDate='21/12/2021',
            classStartTime='1200',
            classEndTime='1700',
            classDay='Monday',
            currentClassSize=3,
            maxClassSize=45,
            employeeId='2',
            employeeName='Mr Alan'
        )
        db.session.add(new_class)
        db.session.commit()

        request_body = {}
        response = self.client.get("/class/all", data=json.dumps(request_body), content_type='application/json')
        # print("This is the reponse", response.json['data'])

        self.assertEqual(response.json['data'], [{
            'classId': 'G4',
            'courseId': 'X888',
            'courseName': 'Scanning Documents',
            'classStartDate': '01/12/2021',
            'classEndDate': '21/12/2021',
            'classStartTime': '1200',
            'classEndTime': '1700',
            'classDay': 'Monday',
            'currentClassSize': '3',
            'maxClassSize': '45',
            'employeeId': '2',
            'employeeName': 'Mr Alan'
        }])

    # Get all the available classes for a particular course test
    def test_available_classes_for_a_course(self):
        new_class = Class(
            classId='G4',
            courseId='X888',
            courseName='Scanning Documents',
            classStartDate='01/12/2021',
            classEndDate='21/12/2021',
            classStartTime='1200',
            classEndTime='1700',
            classDay='Monday',
            currentClassSize=3,
            maxClassSize=45,
            employeeId='2',
            employeeName='Mr Alan'
        )
        db.session.add(new_class)
        db.session.commit()

        request_body = {'courseId': new_class.courseId}
        url = "/class/{courseId}".format(courseId=new_class.courseId)

        response = self.client.get(url, data=json.dumps(request_body), content_type='application/json')
        # print("this is the response", response.json['data'])

        self.assertEqual(response.json['data'], [{
            'classId': 'G4',
            'courseId': 'X888',
            'courseName': 'Scanning Documents',
            'classStartDate': '01/12/2021',
            'classEndDate': '21/12/2021',
            'classStartTime': '1200',
            'classEndTime': '1700',
            'classDay': 'Monday',
            'currentClassSize': '3',
            'maxClassSize': '45',
            'employeeId': '2',
            'employeeName': 'Mr Alan'
        }])


if __name__ == '__main__':
    unittest.main()
