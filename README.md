# win-cmd-escaper

A Python library to properly handle escaping of command line arguments in both Windows' CMD.exe and Powershell.

This library was born out of frustration due to the apparent *unknown* behavior of CMD and Powershell regarding command line argument parsing. While bash is very well supported on that subject (notably having an Python module in the standard library handling both formatting and parsing) that's far from being the case for CMD and Powershell. Concretely, *no one on earth* seems to have a real understanding of how those things are supposed to work. A huge part of ressources available on Internet are just *wrong* or *lying*, including official documentation from Microsoft.

Due to the necessity to get the job done with those scripting languages I decided to create a pure *reverse engineering* project to try, as much as possible, to get something that really works in the real world of real things that work for real.

## Known limitations

* ASCII control codes are not supported. This notably includes `\t`, `\r` and `\n`. (There doest't seem to have proper ways to encode these characters in CMD nor Powershell anyway.)
* Non-ASCII characters are not supported. (While there could possibly have some ways to make them work in Powershell it's quite probably a lost cause in CMD anyway.)
* Empty strings are not supported in Powershell. (It doesn't seem to be possible at all to pass an empty string as a command line argument in that *super well designed* language.)