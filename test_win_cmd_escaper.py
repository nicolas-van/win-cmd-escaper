import unittest
from win_cmd_escaper import escape_cmd_argument


class Test(unittest.TestCase):

    def test_basic_call(self):
        escape_cmd_argument("test string")
