import unittest
import win_cmd_escaper
import test_ressources.test_utils as test_utils

class AllTests:

    def run_and_assert(self, str):
        processed = self.run_echoer(self.escape(str))
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

    def test_crlf(self):
        self.run_and_assert(r"\r\n")
        self.run_and_assert(r"\n\r")
        self.run_and_assert(r"\n\n\n\n")
        self.run_and_assert(r"\\n")
        self.run_and_assert(r"\\r")
        self.run_and_assert(r"hello\rworld")
        self.run_and_assert(r"hello\r\nworld")
        self.run_and_assert(r"hello\nworld")
        self.run_and_assert(r"\n\nhello\nworld  this \n is \n the\n\n  time\n\n")

    def test_no_variable_substitution(self):
        self.run_and_assert(r"%a%")
        self.run_and_assert(r"%%a%%")


class CmdScriptTests(unittest.TestCase, AllTests):

    def escape(self, str):
        return win_cmd_escaper.escape_cmd_argument_script(str)

    def run_echoer(self, str):
        return test_utils.run_echoer_with_cmd_through_script(str)


class CmdPythonSubprocessTests(unittest.TestCase, AllTests):

    def escape(self, str):
        return win_cmd_escaper.escape_cmd_argument_direct(str)

    def run_echoer(self, str):
        return test_utils.run_echoer_with_cmd_through_python_subprocess(str)