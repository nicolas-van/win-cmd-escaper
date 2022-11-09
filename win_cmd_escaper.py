
def escape_cmd_argument_direct(str):
    """
    Escapes an argument for the CMD command in Windows.

    This variant is the one to use when using direct system call invoking CMD on Windows. If
    you are intending to integrate the result of this function in a .bat script you should use
    `escape_cmd_argument_script()` instead.
    """

    return __escape_cmd_common(str, False)

def escape_cmd_argument_script(str):
    """
    Escapes an argument for the CMD command in Windows.

    This variant is the one to use when you want to create a .bat script. If you are intending to
    integrate the result of this function in direct system call to CMD you should use
    `escape_cmd_argument_direct()` instead.
    """

    return __escape_cmd_common(str, True)

def __escape_cmd_common(str, is_script):
    acc = ""
    for i in range(len(str)):
        c = str[i]
        if ord(c) < 32:
            raise ValueError("ASCII control codes are not supported")
        elif is_script and c == "%":
            acc += "%%"
        elif c == '"':
            acc += '""'
        elif c == "\\":
            bs_esc = False
            for j in range(i + 1, len(str) + 1):
                if j == len(str) or str[j] == '"':
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
    Escapes an argument for Powershell.
    """
    if str == "":
        raise ValueError("Empty strings are not supported")
    
    acc = ""
    for i in range(len(str)):
        c = str[i]
        if ord(c) < 32:
            raise ValueError("ASCII control codes are not supported")
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