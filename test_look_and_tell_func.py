import unittest
from look_and_tell_func import look_and_tell


class TestLookAndTell(unittest.TestCase):
    def test_is_correct_number(self):
        self.assertEqual(look_and_tell(1), "1")
        self.assertEqual(look_and_tell(3), "21")
        self.assertEqual(look_and_tell(5), "111221")
        self.assertEqual(look_and_tell(7), "13112221")
        self.assertEqual(look_and_tell(9), "31131211131221")
