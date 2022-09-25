import unittest
from win_cmd_escaper import escape_cmd_argument
import test_ressources.test_utils as test_utils

class Test(unittest.TestCase):

    def run_and_assert(self, str):
        escaped = escape_cmd_argument(str)
        processed = test_utils.run_echoer_with_cmd(escaped)
        self.assertEqual(processed, str)

    def test_basic_calls(self):
        self.run_and_assert("hello")
        self.run_and_assert("hello world")