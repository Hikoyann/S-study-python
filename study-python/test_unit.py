import unittest
import test

class CalTest(unittest.TestCase):
    def test_add_num_and_double(self):
        cal = test.Cal()
        self.assertEqual(cal.add_num_and_double(1, 1), 4)

    def test_add_num_and_double_raise(self):
        cal = test.Cal()
        with self.assertRaises(ValueError):
            cal.add_num_and_double("1", "1")

unittest.main()