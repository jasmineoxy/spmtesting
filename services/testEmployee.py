import unittest
# import json
# from employee import app, db, Employee
from employee import Employee

# Unit Testing

# Function inside the Class itself
# JSON


class testGetEmployee(unittest.TestCase):
    def testJSON(self):

        # Testing Employee id = 1
        testEmployee = Employee(
            employeeId="3",
            employeeName="John Doe",
            department="juniorEngineer",
            role="learner",
        )

        self.assertEqual(
            testEmployee.json(),
            {
                "employeeId": "3",
                "employeeName": "John Doe",
                "department": "juniorEngineer",
                "role": "learner",
            },
        )

    def test_to_dict(self):
        # Testing Employee id = 1
        testEmployee = Employee(
            employeeId="3",
            employeeName="John Doe",
            department="juniorEngineer",
            role="learner",
        )

        self.assertEqual(
            testEmployee.to_dict(),
            {
                "employeeId": "3",
                "employeeName": "John Doe",
                "department": "juniorEngineer",
                "role": "learner",
            },
        )


if __name__ == "__main__":
    unittest.main()
