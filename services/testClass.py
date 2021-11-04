import unittest
from classes import Class


class testClass(unittest.TestCase):
    def test_to_dict(self):
        c1 = Class(classId='G1',
                   courseId='X7845',
                   courseName='Fundamentals of Xerox WorkCentre 7845',
                   classStartDate='23/09/2021',
                   classEndDate='01/10/2021',
                   classStartTime='0900',
                   classEndTime='1200',
                   classDay='Wednesday',
                   currentClassSize=0,
                   maxClassSize=45,
                   employeeId='1',
                   employeeName='Ms Preethi')

        self.assertEqual(c1.to_dict(), {
            'classId': 'G1',
            'courseId': 'X7845',
            'courseName': 'Fundamentals of Xerox WorkCentre 7845',
            'classStartDate': '23/09/2021',
            'classEndDate': '01/10/2021',
            'classStartTime': '0900',
            'classEndTime': '1200',
            'classDay': 'Wednesday',
            'currentClassSize': 0,
            'maxClassSize': 45,
            'employeeId': '1',
            'employeeName': 'Ms Preethi'
        })


if __name__ == '__main__':
    unittest.main()
