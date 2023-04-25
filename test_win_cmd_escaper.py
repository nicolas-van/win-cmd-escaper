
import unittest
import win_cmd_escaper
import test_ressources.test_utils as test_utils

powershell_supported_control_characters = ['\n', '\t', '\b', '\v']

class AllTests:

    def _test_str(self, string):
        with self.subTest(string=string):
            processed = self.run_echoer(self.escape(string))
            self.assertEqual(processed, string)

    def _test_unsupported(self, string):
        with self.subTest(string=string):
            with self.assertRaises(ValueError):
                self.escape(string)

    def test_basic_calls(self):
        self._test_str("hello")
        self._test_str("hello world")

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

    def test_unsupported_control_characters(self):
        for i in range(0, 32):
            character = chr(i)
            if character in set(powershell_supported_control_characters):
                continue
            self._test_unsupported(character)

    def test_no_variable_substitution_batch(self):
        self._test_str("%a%")
        self._test_str("%%a%%")

    def test_no_variable_substitution_powershell(self):
        self._test_str("$a")
        self._test_str("hello $a world")

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
        self._test_str('\\"hello')
        self._test_str('\\\\"hello')
        self._test_str('\\\\\\"hello')
        self._test_str('"\\')
        self._test_str('"\\\\')
        self._test_str('"\\\\\\')

    def test_backticks(self):
        self._test_str('`')
        self._test_str('``')
        self._test_str('```')
        self._test_str('\\`')
        self._test_str('\\\\`')
        self._test_str('\\\\\\`')
        self._test_str('hello\\`')
        self._test_str('hello\\\\`')
        self._test_str('hello\\\\\\`')
        self._test_str('\\`hello')
        self._test_str('\\\\`hello')
        self._test_str('\\\\\\`hello')
        self._test_str('`\\')
        self._test_str('`\\\\')
        self._test_str('`\\\\\\')

class AllCmdTests(AllTests):

    def test_empty(self):
        self._test_str("")

    def test_other_control_characters(self):
        for c in powershell_supported_control_characters:
            self._test_unsupported(c)

class CmdScriptTests(unittest.TestCase, AllCmdTests):

    def escape(self, str):
        return win_cmd_escaper.escape_cmd_argument_script(str)

    def run_echoer(self, str):
        return test_utils.run_echoer_with_cmd_through_script(str)

class CmdDirectTests(unittest.TestCase, AllCmdTests):

    def escape(self, str):
        return win_cmd_escaper.escape_cmd_argument_direct(str)

    def run_echoer(self, str):
        return test_utils.run_echoer_with_cmd_direct(str)


class PowershellScriptTests(unittest.TestCase, AllTests):

    def escape(self, str):
        return win_cmd_escaper.escape_powershell_argument_script(str)

    def run_echoer(self, str):
        return test_utils.run_echoer_with_powershell_through_script(str)

    def test_empty(self):
        self._test_unsupported("")

    def test_other_control_characters(self):
        for c in powershell_supported_control_characters:
            self._test_str(c)

    def test_latin_1(self):
        self._test_str('Aéèàù')

    def test_emoji(self):
        self._test_str('😊❤️😍😁👍')
