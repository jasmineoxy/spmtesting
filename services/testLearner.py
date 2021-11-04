import unittest
from learner import Learner


class testLearner(unittest.TestCase):
    def test_to_dict(self):
        TestLearner = Learner(
            employeeId="3",
            employeeName="John Doe",
            learnerCoursesCompleted="X7845",
            learnerCoursesInProgress="X7846",
        )

        self.assertEqual(
            TestLearner.to_dict(),
            {
                "employeeId": "3",
                "employeeName": "John Doe",
                "learnerCoursesCompleted": "X7845",
                "learnerCoursesInProgress": "X7846",
            },
        )


if __name__ == "__main__":
    unittest.main()
