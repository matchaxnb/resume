#!python

import json
import sys
import win_unicode_console
win_unicode_console.enable()


def main():
    target = sys.argv[1]
    data = None
    with open(target, 'r', encoding='utf-8-sig') as fh:
        data = json.load(fh)
    print(json.dumps(data, indent=4))

if __name__ == '__main__':
    main()