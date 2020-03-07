#!/usr/bin/env python

import argparse
import json
import toml
import sys

def main():
    parser = argparse.ArgumentParser(description='shell out TOML vals via dotted keys')
    parser.add_argument('-c', '--config', nargs='?', type=argparse.FileType('r'), default=sys.stdin)
    parser.add_argument('-d', '--debug', action="store_true")
    parser.add_argument('-j', '--json', action="store_true", help="force json output") #, even of single value")
    parser.add_argument('entry', nargs='*', help="key(s) to extract; output all if none")
            
    args = parser.parse_args()
    conf = toml.load(args.config)

    if not args.entry or args.debug:
        print(json.dumps(conf, indent=2))

    # drill down dotted keys
    for e in args.entry:
        nconf = conf
        for p in e.split('.'):
            nconf = nconf.get(p)

        if args.json: # or not isinstance(nconf, str):
            print(json.dumps(nconf))
        else:
            print(nconf)

if __name__ == "__main__":
    main()
