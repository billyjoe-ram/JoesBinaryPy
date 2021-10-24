# Joe's Binary Py

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
- **Oct. 23<sup>th</sup>**: As it was pointed by other developers,
the binary representation in the script wasn't quite right...
Two complements doesn't work that simply so I, as efficient as
possible, am currently thinking and coding a better solution.
Until there, the negative numbers will be represented with only
one bit to represent the sign followed by another to separate sign
from actual value.


Also, in this day, more tests were added and the main class for 
the program was refactored using decorators

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
- [X] Use TDD;

Version Beta 1.2:
- [X] Handle alphanumerics;
- [ ] Refactor number representation;
- [ ] Implement support for decimal numbers;
- [ ] Simple math operations (Sum and Subtraction).

# Support
This repository will be available under the MIT license,
and my if you like to suggest improvements, please open
an issue and submit your PR.
