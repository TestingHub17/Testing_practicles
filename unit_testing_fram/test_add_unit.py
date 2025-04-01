import unittest

def add(a, b):
    return a+b

def division(a, b):
    return a/b


class Myclass:
    x = 5


class Myclass2:
    x = 6


class TestAddFunction(unittest.TestCase):

    def setUp(self):
        # Code to run before every test
        print("Set up method......")

    def tearDown(self):
        # Code to run after every test
        print("tear down method.....")

    def test_add_positive_number(self):
        self.assertEqual(add(2,3),5)

    def test_add_negative_number(self):
        self.assertEqual(add(-1,-3), -4)

    def test_add_mixed_number(self):
        self.assertEqual(add(-1,6), 5)

    def test_NotEqual(self):
        firstValue = "testing"
        secondValue = "tester"
        message = "First value and second value are not unequal !"
        self.assertNotEqual(firstValue, secondValue, message)

    def test_Equal(self):
        # Failing test: comparing different strings
        self.assertEqual("testing", "testing", "'geeks' is equal to 'geeks'.")

    def test_assertIn(self):
        key = "testing"
        container = "automationtesting"
        message = "key is not in container."
        self.assertIn(key, container, message)

    def test_NotIn(self):
        key = "gfg"
        container = "automationtesting"
        message = "key is present in container."
        self.assertNotIn(key, container, message)

    def test_NotIsInstance(self):
        obj = Myclass2()
        message = "given object is instance of Int"
        self.assertNotIsInstance(obj, Myclass, message)

    def test_IsInstance(self):
        obj = Myclass2()
        # error message in case if test case got failed
        message = "given object is not instance of Int"
        self.assertIsInstance(obj, Myclass2, message)

    def test_negativeWithPlaces(self):
        first = 4.4555
        second = 4.4566
        decimalPlace = 2
        message = "first and second are not almost equal."
        self.assertAlmostEqual(first, second, decimalPlace, message)

    def test_negativeWithPlaces_two(self):
        first = 4.4555
        second = 4.4566
        decimalPlace = 3
        message = "first and second are almost equal."
        self.assertNotAlmostEqual(first, second, decimalPlace, message)

    def test_division_denominatorIsZero(self):
        first = 5
        second = 6
        message = "first value is not less than second value."
        self.assertLess(first, second, message)

    def test_division_negativeForLessEqual(self):
        first = 5
        second = 6
        message = "first value is not less than or equal to second value."
        self.assertLessEqual(first, second, message)

    def test_IsNotNone(self):
        firstValue = "Testing"
        message = "Test value is none."
        self.assertIsNotNone(firstValue, message)

    def test_IsNone(self):
        firstValue = None
        message = "Test value is not none."
        self.assertIsNone(firstValue, message)

    def test_False(self):
        testValue = False
        message = "Test value is not false."
        self.assertFalse(testValue, message)

    def test_True(self):
        testValue = True
        message = "Test value is not true."
        self.assertTrue(testValue, message)

if __name__ == '__main__':
    unittest.main()
















"""
Outcomes Possible in Unit Testing
There are three types of possible test outcomes :

OK – This means that all the tests are passed.
FAIL – This means that the test did not pass and an AssertionError exception is raised.
ERROR – This means that the test raises an exception other than AssertionError."""