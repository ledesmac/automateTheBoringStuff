#! python3
#! madlibs.py - interactive python program to allow user to make madlib files

import sys
import argparse

# Create argument parser to take in arguments from command line
parser = argparse.ArgumentParser(description="interactive python program to allow user to create madlib files")
parser.add_argument("-f", "--file", help="File to load for MadLib script")

args = parser.parse_args()