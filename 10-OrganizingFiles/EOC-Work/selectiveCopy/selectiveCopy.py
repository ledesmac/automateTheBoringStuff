#! python3
#! selectiveCopy.py - Program that will walk through a folder tree searching for and copying all 
#                     files of a certain extension (ie. .pdf, .jpg, .txt, etc)
import argparse
import os
import shutil

from pathlib import Path


def selectiveCopy(folder, extension):
    
    folder = os.path.abspath(folder)
    
    newFolder = Path.cwd() / Path(f'{folder}_{extension[1:]}')

    newFolder.mkdir()

    for foldername, subfolders, filenames in os.walk(folder):
        # Add all the files in this folder to the ZIP file.
        for filename in filenames:
            
            if filename.endswith(extension):
                shutil.copy(f'{foldername}/{filename}', newFolder)
            


parser = argparse.ArgumentParser(description="""Program that will walk through a folder tree searching for 
                                                and copying all files of a certain extension (ie. .pdf, .jpg, .txt, etc)""")
parser.add_argument("folder", help="Source Folder to copy files with matching extension from")
parser.add_argument("extension", help="File extension to search source folder for")

args = parser.parse_args()

if args.folder and args.extension:
    selectiveCopy(args.folder, args.extension)
