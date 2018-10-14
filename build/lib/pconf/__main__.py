"""
Pong Configuration Tool

Usage:
    pconf push   CONFIG_FILEPATH
    pconf delete CONFIG_ID
    pconf get    CONFIG_ID
    pconf list

Options:
    -h --help     Show this screen.
    --version     Show version.
"""

import os
import sys
import json
from docopt import docopt
from .config import push, pretty, delete, get, scan


__version__ = "0.0.1"


def main():
    arguments = docopt(__doc__, version=__version__)

    if arguments['push']:
        filepath = arguments['CONFIG_FILEPATH']

        if not os.path.isfile(filepath):
            print(f'{filepath} not found')
            sys.exit(1)

        try:
            with open(filepath) as fp:
                config = json.load(fp)
        except ValueError:
            print(f'{filepath} is not valid json')
            sys.exit(1)

        if 'id' not in config:
            print('{filepath} does not contain an id')
            sys.exit(1)

        row = push(config['id'], config)

        print(pretty(row))

    if arguments['delete']:
        id_ = arguments['CONFIG_ID']
        row = delete(id_)

        if not row:
            print(f'{id_} does not exist')
            sys.exit(0)

        print(pretty(row))

    if arguments['get']:
        id_ = arguments['CONFIG_ID']
        row = get(id_)

        if not row:
            print(f'{id_} does not exist')
            sys.exit(1)

        print(pretty(row))

    if arguments['list']:
        rows = scan()

        for row in rows:
            print(pretty(row))


if __name__ == '__main__':
    main()
