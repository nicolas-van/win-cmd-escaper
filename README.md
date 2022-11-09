# win-cmd-escaper

A Python library to properly handle escaping of command line arguments in both Windows' CMD.exe and Powershell.

This library was born out of frustration due to the apparent *completely unknown* behavior of CMD and Powershell regarding command line argument parsing. While bash is very well supported on that subject (notably having an Python module in the standard library handling both formatting and parsing) that's far from being the case for CMD and Powershell. Concretely, *no one on earth* seems to have a real understanding of how those things are supposed to work. A huge part of ressources available on Internet are just *wrong* or *lying*, including official documentation from Microsoft.

Due to the necessity to get the job done with those scripting languages I decided to create a pure *reverse engineering* project to try, as much as possible, to get something that really works in the real world of real things that work for real. Also, while this library is in Python, it aims to be a reference implementation for anyone having the same need. The code is purposedly designed to be easy to read and to port to other programming languages.

## Known limitations

* ASCII control codes are not supported. This notably includes `\t`, `\r` and `\n`. (There doest't seem to have proper ways to encode these characters in CMD nor Powershell anyway.)
* Behavior with non-ASCII characters is mostly *unknown* at the current state. Well, what we know is that if you are doing things like encoding a path to file with Latin-1 characters *on a Windows system configured in Latin-1 C locale* it *should* work *most of the time*. Unfortunately CMD, Powershell, and mostly all command line stuff in Windows rely heavily on those damn C locales that are completely inconsistent from one Windows installation to another. And those are mostly impossible to test reliably. So we will probably stay in the dark realm of "we don't know" forever on the point.
* Empty strings are not supported in Powershell. (It doesn't seem to be possible at all to pass an empty string as a command line argument in that *super well designed* language.)

## Contributing to this project

This project is, before anything else, a reverse engineering attempt. As such it is heavily centered around automatic tests.

Please note that "blog posts", "forum threads" and "official documentation" about CMD and Powershell *do* lie. As opposed to whatever piece of *** any Windows programmer or even Microsoft engineer could have written at one stage or another, this project only cares about making things that are *proven* to work.

So if you want to contribute to this project, which you are very welcome to do, please:

* Do not cite any Internet link in the issues supposedly explaining the behavior of CMD or Powershell. I made my point clear regarding the fact I'm very convinced they are a total waste of time.
* Try to mostly work using the unit tests, they are our one and only source of truth.
* Take into account the fact that the unit tests *must* run in Github Actions using Github's Windows runners.
