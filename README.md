# win-cmd-escaper

[![Windows Tests](https://github.com/nicolas-van/win-cmd-escaper/actions/workflows/python-app.yml/badge.svg)](https://github.com/nicolas-van/win-cmd-escaper/actions/workflows/python-app.yml) [![PyPI](https://img.shields.io/pypi/v/win-cmd-escaper)](https://pypi.org/project/win-cmd-escaper/)

A Python library to properly handle escaping of command line arguments in both Windows' CMD.exe and Powershell.

## Usage

First install with `pip`:

```bash
pip install win_cmd_escaper
```

Then import the library and use the functions it provides:

```python
import win_cmd_escaper

print(win_cmd_escaper.escape_powershell_argument_script("hello world")) # escapes for Powershell

print(win_cmd_escaper.escape_cmd_argument_script("hello world")) # escapes for CMD

print(win_cmd_escaper.escape_cmd_argument_direct("hello world")) # escapes for CMD when using direct calls
```

## Rationale

This library was born out of frustration due to the apparent *completely unknown* behavior of CMD and Powershell regarding command line argument parsing. While bash is very well supported on that subject (notably having a [standard Python module](https://docs.python.org/3/library/shlex.html?highlight=shlex#module-shlex) handling both formatting and parsing) that's far from being the case for CMD and Powershell.

Concretely, *no one on earth* seems to have a real understanding of how those things are supposed to work and to have a clean algorithm to format command line arguments in those languages. A huge part of ressources available on Internet are just *wrong* or *lying*, including official documentation from Microsoft. Globally, *all* "smart" formatters you can find on whatever forums *do not work*. Well, to be fair, they usually work "at least a little". But none of them work *all the time*, for *all strings* (which is clearly what any serious programmer expects from a well designed formatter).

Due to the necessity to get the job done with those scripting languages I decided to create a pure *reverse engineering* project to try, as much as possible, to get something that really works in the real world of real things that work for real.

Also, while this library is in Python, it aims to be a reference implementation for anyone having the same need. The code is purposedly designed to be easy to read and to port to other programming languages.

## Known limitations

* ASCII control codes are not supported. This notably includes `\t`, `\r` and `\n`. (There doest't seem to have proper ways to encode these characters in CMD nor Powershell anyway.)
* Empty strings are not supported in Powershell. (It doesn't seem to be possible at all to pass an empty string as a command line argument in that *super well designed* language.)

## About non-ASCII characters

This library stays at the string level, which means it doesn't use any kind of magic related to Unicode or the current Windows code page. This is by design as it allows to generate valid strings that can be copy pasted and encoded as needed, not opaque blobs of bytes.

Concretely if you ask "could it work with non-ASCII character?", the answer could vastly depend. You should first know the following details:

* CMD doesn't seem to have any form of character encoding handling. For CMD a byte is a byte and will be forwarded as-is to underlying commands.
* Powershell is the opposite, it has encoding handling. It should be noted that its default encoding is assumed to be Windows' current code page unless you specify a BOM at the beginning of your `.ps1` file. It will then use whatever is specified by the BOM.
* To be short, Windows command-line arguments characters encoding is a global mess. Some programs will expect them to be in Windows' code page, other to be in UTF-8, some will use some kind of auto-detecting, auto-magic, auto-mojibake-making conversion layer between current code page and Unicode or vice-versa, etc...

Due to all this non-sense, non-ASCII characters in command line arguments is just unreliable on Windows and it will probably stay that way for as long as Microsoft doesn't publicly acnowledge that having C locale not using UTF-8 is both stupid, dysfunctional and racist. That means forever.

Normally, if you try to format a file path containing say, Latin-1 characters, on a Windows using cp-1252 code page, that you save that in a `.bat` or `.ps1` using that same cp-1252 encoding and that your destination program is kind of a "typical" Windows program, it "should" kinda works most of the time. That's about it for any kind of Unicode support we could expect related to command line arguments on Windows.

If you can, I would recommend to try to avoid these questions completely, as example using JSON (that has Unicode escapes handling) on top of ASCII for program-to-program communication. You will save yourself a lot of time.

## Contributing to this project

This project is, before anything else, a reverse engineering attempt. As such it is heavily centered around automatic tests.

Please note that "blog posts", "forum threads" and "official documentation" about CMD and Powershell *do* lie. As opposed to whatever piece of *** any Windows programmer or even Microsoft engineer could have written at one stage or another, this project only cares about making things that are *proven* to work.

So if you want to contribute to this project, which you are very welcome to do, please:

* Do not cite any Internet link in the issues supposedly explaining the behavior of CMD or Powershell. If you did not understand already I'm 100% convinced they are a total waste of time.
* Try to mostly work using the unit tests, they are our one and only source of truth in this arsh world.
* Take into account the fact that the unit tests *must* run in Github Actions using Github's Windows runners.
