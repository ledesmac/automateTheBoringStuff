#! python3
#! fileGaps.py - Program to scan a folder and remove the gaps between filenames

import argparse
import os
import shutil
import re

from pathlib import Path


def closeGaps(folder, prefix):
    reg = re.compile(r'[0-9]?[0-9]?[0-9]?[0-9]?[0-9?]')
    files = list(folder.glob(f'{prefix}*'))
    workingFolder = os.path.abspath(folder)
    fileNamesOld = []
    fielNamesNew = []

    for file in files:
        fileNamesOld.append(file.name)
    match = reg.findall(' '.join(fileNamesOld))
    print(match)
    print(fileNamesOld)


parser = argparse.ArgumentParser(description="""Program to scan a folder and remove the gaps between filenames""")

parser.add_argument("folder", help="Source Folder to copy files with matching extension from")

parser.add_argument("prefix", help="File extension to search source folder for")

args = parser.parse_args()

if args.folder and args.prefix:
    folder = Path(args.folder)

    if folder.exists():
        closeGaps(folder, args.prefix)