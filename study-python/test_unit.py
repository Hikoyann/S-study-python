import unittest
import test

class CalTest(unittest.TestCase):
    def test_add_num_and_double(self):
        cal = test.Cal()
        self.assertEqual(cal.add_num_and_double(1, 1), 5)

    def test_add_num_and_double_raise(self):
        cal = test.Cal()
        with self.assertRaises(ValueError):
            cal.add_num_and_double("1", "1")

if __name__ == '__main__':
    unittest.main()
# unittest.main()
# python -m unittest test_unit.py