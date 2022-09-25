
_direct_char_to_escape_sequence = {
    '"': lambda *args: '""',
    "\\": lambda previous, next: "\\\\" if all(x == "\\" for x in next) else "\\"
}


def escape_cmd_argument_direct(str):
    """
    Escapes an argument for the CMD command in Windows.
    """
    acc = ""
    for i in range(len(str)):
        c = str[i]
        if c in _direct_char_to_escape_sequence:
            acc += _direct_char_to_escape_sequence[c](str[0:i], str[i+1:])
        else:
            acc += c
    # naive implementation for now
    return f'"{acc}"'

_script_char_to_escape_sequence = {
    "%": lambda *args: "%%",
    '"': lambda *args: '""',
    "\\": lambda previous, next: "\\\\" if all(x == "\\" for x in next) else "\\"
}

def escape_cmd_argument_script(str):
    """
    Escapes an argument for the CMD command in Windows.
    """
    acc = ""
    for i in range(len(str)):
        c = str[i]
        if c in _script_char_to_escape_sequence:
            acc += _script_char_to_escape_sequence[c](str[0:i], str[i+1:])
        else:
            acc += c
    # naive implementation for now
    return f'"{acc}"'