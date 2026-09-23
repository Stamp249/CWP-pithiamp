#!/usr/bin/env python3

from sys import argv

if len(argv) == 2:
    result = ""
    for char in argv[1]:
        if char == "z":
            result += "z"
    if result:
        print(result)
    else:
        print("none")
else:
    print("none")