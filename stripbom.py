#!python

import json
import sys


def main():
    target = sys.argv[1]
    data = None
    with open(target, 'r', encoding='utf-8-sig') as fh:
        data = json.load(fh)
    with open(target, 'wb') as fh:
        json_stream = json.dumps(data, indent=4)
        fh.write(json_stream.encode('utf-8'))

if __name__ == '__main__':
    main()