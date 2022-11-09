
from io import UnsupportedOperation


def escape_cmd_argument_direct(str):
    """
    Escapes an argument for the CMD command in Windows.
    """
    acc = ""
    for i in range(len(str)):
        c = str[i]
        if ord(c) < 32:
            raise UnsupportedOperation("ASCII control codes are not supported")
        elif c == '"':
            acc += '""'
        elif c == "\\":
            bs_esc = False
            for j in range(i + 1, len(str) + 1):
                if j == len(str) + 1 or str[j] == '"':
                    bs_esc = True
                    break
                elif str[j] == "\\":
                    continue
                else:
                    break
            acc += "\\\\" if bs_esc else "\\"
        else:
            acc += c
    return f'"{acc}"'

def escape_cmd_argument_script(str):
    """
    Escapes an argument for the CMD command in Windows.
    """
    acc = ""
    for i in range(len(str)):
        c = str[i]
        if ord(c) < 32:
            raise UnsupportedOperation("ASCII control codes are not supported")
        elif c == "%":
            acc += "%%"
        elif c == '"':
            acc += '""'
        elif c == "\\":
            bs_esc = False
            for j in range(i + 1, len(str) + 1):
                if j == len(str) + 1 or str[j] == '"':
                    bs_esc = True
                    break
                elif str[j] == "\\":
                    continue
                else:
                    break
            acc += "\\\\" if bs_esc else "\\"
        else:
            acc += c
    return f'"{acc}"'

def escape_powershell_argument_script(str):
    """
    Escapes an argument for the CMD command in Windows.
    """
    if str == "":
        raise UnsupportedOperation("Empty strings are not supported")
    acc = ""
    for i in range(len(str)):
        c = str[i]
        if ord(c) < 32:
            raise UnsupportedOperation("ASCII control codes are not supported")
        elif c == "'":
            acc += "''"
        elif c == '"':
            bs_count = 0
            for j in range(i - 1, -1, -1):
                if str[j] == '\\':
                    bs_count += 1
                else:
                    break
            acc += ('\\' * bs_count) + '\\"'
        else:
            acc += c
    return f"'{acc}'"