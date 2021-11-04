import unittest
from course import Course


class testGetCourse(unittest.TestCase):
    def testJSON(self):
        Testcourse = Course(courseId='X7846',
            courseName='Programming for Xerox WorkCentre with Card Access and Integration',
            courseDescription='Programming for Xerox WorkCentre with Card Access and Integration',
            coursePrereq='X7845')

        self.assertEqual(Testcourse.json(),{
            'courseId': 'X7846',
            'courseName': 'Programming for Xerox WorkCentre with Card Access and Integration',
            'courseDescription':'Programming for Xerox WorkCentre with Card Access and Integration',
            'coursePrereq':'X7845'})

    def test_to_dict(self):
        Testcourse = Course(courseId='X7846',
        courseName='Programming for Xerox WorkCentre with Card Access and Integration',
        courseDescription='Programming for Xerox WorkCentre with Card Access and Integration',
        coursePrereq='X7845')

        self.assertEqual(Testcourse.to_dict(),{
        'courseId': 'X7846',
        'courseName': 'Programming for Xerox WorkCentre with Card Access and Integration',
        'courseDescription': 'Programming for Xerox WorkCentre with Card Access and Integration',
        'coursePrereq': 'X7845'
        })


if __name__ == '__main__':
    unittest.main()
