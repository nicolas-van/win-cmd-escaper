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

    @unittest.skip('found no way to make it work in powershell')
    def test_empty(self):
        self.run_and_assert("")

    def test_printable_ascii_only_char(self):
        for i in range(32, 127):
            character = chr(i)
            with self.subTest(character=character):
                self.run_and_assert(f"{character}")

    def test_printable_ascii_starts_text(self):
        for i in range(32, 127):
            character = chr(i)
            with self.subTest(character=character):
                self.run_and_assert(f"{character}a")

    def test_printable_ascii_ends_text(self):
        for i in range(32, 127):
            character = chr(i)
            with self.subTest(character=character):
                self.run_and_assert(f"a{character}")

    def test_printable_ascii_in_text(self):
        for i in range(32, 127):
            character = chr(i)
            with self.subTest(character=character):
                self.run_and_assert(f"a{character}b")

    def test_printable_ascii_doubled_only_char(self):
        for i in range(32, 127):
            character = chr(i)
            with self.subTest(character=character):
                self.run_and_assert(f"{character}{character}")

    def test_printable_ascii_doubled_starts_text(self):
        for i in range(32, 127):
            character = chr(i)
            with self.subTest(character=character):
                self.run_and_assert(f"{character}{character}a")

    def test_printable_ascii_doubled_ends_text(self):
        for i in range(32, 127):
            character = chr(i)
            with self.subTest(character=character):
                self.run_and_assert(f"a{character}{character}")

    def test_printable_ascii_doubled_in_text(self):
        for i in range(32, 127):
            character = chr(i)
            with self.subTest(character=character):
                self.run_and_assert(f"a{character}{character}b")

    @unittest.skip("Found no way to make it work in CMD")
    def test_crlf(self):
        self.run_and_assert("hello\r\nworld")
        self.run_and_assert("\r\n")
        self.run_and_assert("\n\r")
        self.run_and_assert("\n\n\n\n")
        self.run_and_assert("\\n")
        self.run_and_assert("\\r")
        self.run_and_assert("hello\rworld")
        self.run_and_assert("hello\nworld")
        self.run_and_assert("\n\nhello\nworld  this \n is \n the\n\n  time\n\n")

    def test_no_variable_substitution_batch(self):
        self.run_and_assert("%a%")
        self.run_and_assert("%%a%%")

    def test_backslash(self):
        self.run_and_assert("\\")
        self.run_and_assert("\\\\")
        self.run_and_assert("\\\\\\")
        self.run_and_assert("\\\\\\\\")
        self.run_and_assert("a\\")
        self.run_and_assert("a\\\\")
        self.run_and_assert("a\\\\\\")
        self.run_and_assert("a\\\\\\\\")
        self.run_and_assert("\\a")
        self.run_and_assert("\\\\a")
        self.run_and_assert("\\\\\\a")
        self.run_and_assert("\\\\\\\\a")


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


class PowershellScriptSubprocessTests(unittest.TestCase, AllTests):

    def escape(self, str):
        return win_cmd_escaper.escape_powershell_argument_script(str)

    def run_echoer(self, str):
        return test_utils.run_echoer_with_powershell_through_script(str)
