## py-cleanimgdir

Simple Python script that checks for image sizes in a given folder (and its subfolders) and moves the matching images to a temporary folder, which you'll be able to edit, move, or delete.

## Requirements:

- [Python 2.7.2](http://python.org) (tested, may work with other versions)
- [Python Imaging Library (PIL)](http://www.pythonware.com/products/pil/)

## To-do's:

1. Add option to recurse through directories, or just process the root directory
2. Add option to choose the temporary folder name
3. Add option to check for height, or both
4. Add Windows support
5. Add confirmation of moved files.
6. Add logging.

## Instructions:

Just run `python img.py <directory>` and the script will take care of the rest. Once the script is running, define the minimum width (in pixels) that the script will search for.

Image files with a width lower than the defined will be moved to a temporary folder inside <directory> so you can process those files later.

## Warning!:

This script has been tested in Mac OS X 10.6, and I'm guessing it'll work in Unix-like systems. Sorry Windows.

The script is __not desctructive__, but if you execute the script in a root folder with a lot of subfolders, well, good luck moving them back to place. It is __reccommended__ to make a copy in an isolated folder then process the files. If you're satisfied with the result, replace the original folder.