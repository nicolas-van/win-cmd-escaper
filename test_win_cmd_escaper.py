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

    def test_ascii_only_char(self):
        for i in range(32, 127):
            character = chr(i)
            with self.subTest(character=character):
                self.run_and_assert(f"{character}")

    def test_ascii_starts_text(self):
        for i in range(32, 127):
            character = chr(i)
            with self.subTest(character=character):
                self.run_and_assert(f"{character}a")

    def test_ascii_ends_text(self):
        for i in range(32, 127):
            character = chr(i)
            with self.subTest(character=character):
                self.run_and_assert(f"a{character}")

    def test_ascii_in_text(self):
        for i in range(32, 127):
            character = chr(i)
            with self.subTest(character=character):
                self.run_and_assert(f"a{character}b")

    def test_ascii_doubled_only_char(self):
        for i in range(32, 127):
            character = chr(i)
            with self.subTest(character=character):
                self.run_and_assert(f"{character}{character}")

    def test_ascii_doubled_starts_text(self):
        for i in range(32, 127):
            character = chr(i)
            with self.subTest(character=character):
                self.run_and_assert(f"{character}{character}a")

    def test_ascii_doubled_ends_text(self):
        for i in range(32, 127):
            character = chr(i)
            with self.subTest(character=character):
                self.run_and_assert(f"a{character}{character}")

    def test_ascii_doubled_in_text(self):
        for i in range(32, 127):
            character = chr(i)
            with self.subTest(character=character):
                self.run_and_assert(f"a{character}{character}b")
