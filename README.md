# Joe's BinaryPy

Are you looking for a simple way to know how to represent
a number, let's say "33", in binary? Or maybe you really
don't care about binaries, but your teacher of algorithms
gave you a list of exercises to convert from decimal to
various bases (2, 8, 16) but last night you were at a
party and totally forgot it. Quoting Uncle Bob, in a set of
lectures about clean code he gave in 2019, "if a computer
can do it, a computer should do it"!

![Code section to exemplify how it work](https://user-images.githubusercontent.com/67481026/138018105-29a4142e-b83e-4f54-9930-aa01a218a43e.png)

# Updates
- **Nov. 12<sup>th</sup>**: Since the adding method was kind of broken,
it was rewritten used TDD, and because the users must be able to
operate the software properly, all the user interface (unfortunately not
graphical with Tkinter or similar) had to be rewritten and tested.
The executable is still only available to Linux, until I put my hands
in a Windows again.

# How to run the executable?
This repository contains a simple code and an executable
of the program and its files were created using a Linux
environment (Ubuntu) and PyCharm.

**Windows:** Go to the file /dist/main.exe and run the
executable by clicking it twice.

**Linux:**
Open the folder mentioned in terminal and run the
file by typing "./main" (with no extension) 

# The script

To practice Python in a program that would interest 
**me**, I created this simple script that converts
positive integer numbers applying a method humans are
used to (remainders of a number divided by 2 and its
rest, inverted).

A recent feature now allows continuous running of the
script, and also visual representation of negative
numbers

# Testing
Open the folder in terminal, type "python test_main.py",
and you'll see a tiny spark of what the Test Driven
Development can do!

![Unit Tests in Python](https://user-images.githubusercontent.com/67481026/138018202-50d1373e-691c-417b-b21b-b4c736c0470f.png)


If you, as a developer, think of new possible test
cases, please consider following the recommended
steps mentioned in the Support section of this README.

# Ideas for updates
Version Beta 1.1:
- [X] Support for Windows;
- [X] Implement support for negative numbers;
- [X] Use TDD

Version Beta 1.2:
- [X] Handle alphanumerics;
- [X] Refactor number representation;
- [X] Sum operations

Version Beta 1.3:
- [ ] Subtraction operations;
- [ ] Add logs  for math operations;
- [ ] Implement support for converting decimal numbers

Version Beta 1.4:
- [ ] Improve the interface with colors and os control (preferably
cleaning the screen);
- [ ] Multiplication operations;
- [ ] Division operations;

Final Beta Version (1.5):
- [ ] Create a GUI

# Support
This repository will be available under the MIT license,
and my if you like to suggest improvements, please open
an issue and submit your PR.
