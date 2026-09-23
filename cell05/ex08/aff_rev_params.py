#!/usr/bin/env python3

from sys import argv

if len(argv) > 2:
    for arg in reversed(argv[1:]):
        print(arg)
else:
    print('none')