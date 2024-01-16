#!/usr/bin/env python

# noop.py - a NOOP program

import logging, os
logging.basicConfig(level=os.environ.get('LOGLEVEL', 'INFO').upper())

import emoji

import traceback

def main():
    try:
        logging.info("nothing to see here")
        print(emoji.emojize(':slightly_smiling_face:'))
    except Exception as e:
        traceback.print_exc(e)

if __name__ == "__main__":
    exit(main())
