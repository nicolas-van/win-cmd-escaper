
# see https://www.robvanderwoude.com/escapechars.php
_char_to_escape_sequence = {
    "%": "%%",
    #"^": "^^",
    #"&": "^&",
    #"<": "^<",
    #">": "^>",
    #"|": "^|",
    #"'": "^'",
    #"`": "^`",
    #",": "^,",
    #";": "^;",
    #"=": "^=",
    #"(": "^(",
    #")": "^)",
    #"!": "^^!",
    '"': '""',
    "\\": "\\\\",
    #"[": "\[",
    #"]": "\]",
    #'"': '\\"',
    #".": "\.",
    #"*": "\*",
    #"?": "\?",
}


def escape_cmd_argument(str):
    """
    Escapes an argument for the CMD command in Windows.
    """
    acc = ""
    for c in str:
        if c in _char_to_escape_sequence:
            acc += _char_to_escape_sequence[c]
        else:
            acc += c
    # naive implementation for now
    return f'"{acc}"'
