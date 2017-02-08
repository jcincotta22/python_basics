import unittest
from censor import censor
from is_lucky import is_lucky
from class_example import Employee
from remove_dups import display_duplicates
import pdb

class MyTestCase(unittest.TestCase):
    def test_censor(self):
        # this test will fail until you change the Greeter to return this expected message
        self.assertEqual(censor('Hello jeff', 'jeff'), 'Hello ****')
    def test_is_lucky(self):
        self.assertEqual(is_lucky('123321'), True)
        self.assertEqual(is_lucky('1233219'), False)
        self.assertEqual(is_lucky('000000'), True)
    def test_employee(self):
        emp1 = Employee("Zara", 2000)
        emp2 = Employee("Jeff", 5000)
        # pdb.set_trace()
        self.assertEqual(emp1.displayCount(), 'Total Employee 2')
        self.assertEqual(emp1.displayEmployee(), ('Name : ', 'Zara', ', Salary: ', 2000))
    def test_display_duplicates(self):
        nums = [1, 2, 2, 3, 4, 5, 5, 7, 8, 11, 12, 11, 1, 2, 15, 12, 99]
        self.assertEqual(display_duplicates(nums), [1, 2, 5, 11, 12])
        self.assertNotEqual(display_duplicates(nums), [11, 1, 2, 5, 12])

if __name__ == '__main__':
    unittest.main()
