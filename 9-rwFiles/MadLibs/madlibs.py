#! python3
#! madlibs.py - interactive python program to allow user to make madlib files

import sys
import argparse
import re

# Create argument parser to take in arguments from command line
parser = argparse.ArgumentParser(description="interactive python program to allow user to create madlib files")
parser.add_argument("file", help="File to load for MadLib script")

args = parser.parse_args()

if args.file:
    madLib = open(args.file, 'r')
    words = re.split(' |\n', madLib.read())
    #doesnt work for specific cases, such as 'VERB.', need to figure out how to work with that
    for word in words:
        if word == 'ADJECTIVE' or word == 'NOUN' or word == 'VERB':
            replace = input(f'Enter a {word.lower()}:')

    print(words)