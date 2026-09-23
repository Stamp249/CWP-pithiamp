#!/usr/bin/env python3

from sys import argv

def main():
    if len(argv) >= 2:
        for txt in argv[1:]:
            if not txt.endswith('ism'):
                print(txt + 'ism')
    else:
        print('none')

if __name__ == "__main__":
    main()