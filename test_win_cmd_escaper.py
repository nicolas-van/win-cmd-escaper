import unittest
import win_cmd_escaper
import test_ressources.test_utils as test_utils

class AllTests:

    def _test_str(self, string):
        with self.subTest(string=string):
            processed = self.run_echoer(self.escape(string))
            self.assertEqual(processed, string)

    def test_basic_calls(self):
        self._test_str("hello")
        self._test_str("hello world")

    @unittest.skip('found no way to make it work in powershell')
    def test_empty(self):
        self._test_str("")

    def test_printable_ascii_only_char(self):
        for i in range(32, 127):
            character = chr(i)
            self._test_str(f"{character}")

    def test_printable_ascii_starts_text(self):
        for i in range(32, 127):
            character = chr(i)
            self._test_str(f"{character}a")

    def test_printable_ascii_ends_text(self):
        for i in range(32, 127):
            character = chr(i)
            self._test_str(f"a{character}")

    def test_printable_ascii_in_text(self):
        for i in range(32, 127):
            character = chr(i)
            self._test_str(f"a{character}b")

    def test_printable_ascii_doubled_only_char(self):
        for i in range(32, 127):
            character = chr(i)
            self._test_str(f"{character}{character}")

    def test_printable_ascii_doubled_starts_text(self):
        for i in range(32, 127):
            character = chr(i)
            self._test_str(f"{character}{character}a")

    def test_printable_ascii_doubled_ends_text(self):
        for i in range(32, 127):
            character = chr(i)
            self._test_str(f"a{character}{character}")

    def test_printable_ascii_doubled_in_text(self):
        for i in range(32, 127):
            character = chr(i)
            self._test_str(f"a{character}{character}b")

    @unittest.skip("Found no way to make it work in both CMD and powershell")
    def test_crlf(self):
        self._test_str("hello\r\nworld")
        self._test_str("\r\n")
        self._test_str("\n\r")
        self._test_str("\n\n\n\n")
        self._test_str("\\n")
        self._test_str("\\r")
        self._test_str("hello\rworld")
        self._test_str("hello\nworld")
        self._test_str("\n\nhello\nworld  this \n is \n the\n\n  time\n\n")

    def test_no_variable_substitution_batch(self):
        self._test_str("%a%")
        self._test_str("%%a%%")

    def test_backslash(self):
        self._test_str("\\")
        self._test_str("\\\\")
        self._test_str("\\\\\\")
        self._test_str("\\\\\\\\")
        self._test_str("a\\")
        self._test_str("a\\\\")
        self._test_str("a\\\\\\")
        self._test_str("a\\\\\\\\")
        self._test_str("\\a")
        self._test_str("\\\\a")
        self._test_str("\\\\\\a")
        self._test_str("\\\\\\\\a")

    def test_double_quotes(self):
        self._test_str('"')
        self._test_str('""')
        self._test_str('"""')
        self._test_str('\\"')
        self._test_str('\\\\"')
        self._test_str('\\\\\\"')
        self._test_str('hello\\"')
        self._test_str('hello\\\\"')
        self._test_str('hello\\\\\\"')
        self._test_str('"\\')
        self._test_str('"\\\\')
        self._test_str('"\\\\\\')


@unittest.skip('')
class CmdScriptTests(unittest.TestCase, AllTests):

    def escape(self, str):
        return win_cmd_escaper.escape_cmd_argument_script(str)

    def run_echoer(self, str):
        return test_utils.run_echoer_with_cmd_through_script(str)


@unittest.skip('')
class CmdPythonSubprocessTests(unittest.TestCase, AllTests):

    def escape(self, str):
        return win_cmd_escaper.escape_cmd_argument_direct(str)

    def run_echoer(self, str):
        return test_utils.run_echoer_with_cmd_through_python_subprocess(str)


class PowershellScriptTests(unittest.TestCase, AllTests):

    def escape(self, str):
        return win_cmd_escaper.escape_powershell_argument_script(str)

    def run_echoer(self, str):
        return test_utils.run_echoer_with_powershell_through_script(str)
