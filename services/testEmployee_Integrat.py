import unittest
import flask_testing
import json
from employee import app, db, Employee

# This is for the SQL Database and Stuff
# Add, Removing , Editing , CRUD Of the DB

# Testing the app


class TestEmployee(flask_testing.TestCase):
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


class TestEmployeeFunction(TestEmployee):
# Function 1. Getting all senior engineers
    def test_getAllSeniorEngineers(self):
        new_employee = Employee(
            employeeId='1',
            employeeName='Ms Preethi',
            department='seniorEngineer',
            role='trainer')

        new_employee2 = Employee(
            employeeId='2',
            employeeName='Mr Alan',
            department='seniorEngineer',
            role='trainer')

        db.session.add(new_employee)
        db.session.add(new_employee2)
        db.session.commit()

        # Fake a request body to send over the network body
        request_body = {}
        response = self.client.get("/seniorEngineers",
                                    data=json.dumps(request_body),
                                    content_type='application/json')

        print('this is the request body   ', request_body)

        print('this is the response json data', response.json['data']['seniorEngineer'])

        self.assertEqual(response.json['data']['seniorEngineer'], [
            {
                "department": "seniorEngineer",
                "employeeId": "1",
                "employeeName": "Ms Preethi",
                "role": "trainer"
            },
            {
                "department": "seniorEngineer",
                "employeeId": "2",
                "employeeName": "Mr Alan",
                "role": "trainer"
            }
        ])
# Function 2. Getting all junior engineers

    def test_getAllJuniorEngineers(self):

        new_employee = Employee(
            employeeId='3',
            employeeName='John Doe',
            department='juniorEngineer',
            role='learner')

        new_employee2 = Employee(
            employeeId='4',
            employeeName='Jane Goh',
            department='juniorEngineer',
            role='learner')

        new_employee3 = Employee(
            employeeId='5',
            employeeName='Jackson Ong',
            department='juniorEngineer',
            role='learner')

        new_employee4 = Employee(
            employeeId='7',
            employeeName='Janet Jackson',
            department='juniorEngineer',
            role='learner')

        db.session.add(new_employee)
        db.session.add(new_employee2)
        db.session.add(new_employee3)
        db.session.add(new_employee4)

        db.session.commit()

        # Fake a request body to send over the network body
        request_body = {}
        response = self.client.get("/juniorEngineers",
                                    data=json.dumps(request_body),
                                    content_type='application/json')

        print('this is the request body   ', request_body)

        print('this is the response json data', response.json['data']['juniorEngineer'])

        self.assertEqual(response.json['data']['juniorEngineer'], [
            {
                "department": "juniorEngineer",
                "employeeId": "3",
                "employeeName": "John Doe",
                "role": "learner"
            },
            {
                "department": "juniorEngineer",
                "employeeId": "4",
                "employeeName": "Jane Goh",
                "role": "learner"
            },
            {
                "department": "juniorEngineer",
                "employeeId": "5",
                "employeeName": "Jackson Ong",
                "role": "learner"
            },
            {
                "department": "juniorEngineer",
                "employeeId": "7",
                "employeeName": "Janet Jackson",
                "role": "learner"
            }
        ])


# Need Test Error Cases
if __name__ == '__main__':
    unittest.main()
