## py-cleanimgdir

Checks image files for their sizes in a given folder (and its subfolders) and moves the matching images to a temporary folder.

__Author:__ Mario Cuba <[mario@mariocuba.net](mailto:mario@mariocuba.net)>  
__License:__ Released to the Public Domain under the [Creative Commons Attribution 3.0 Unported License](http://creativecommons.org/licenses/by/3.0).

## Requirements

- [Python 2.7.2](http://python.org) (tested, may work with other versions)
- [Python Imaging Library (PIL)](http://www.pythonware.com/products/pil/)

## Instructions

Just run `python img.py <directory>` and the script will take care of the rest. Once the script is running, define the minimum width (in pixels) that the script will search for.

Image files with a width lower than the defined will be moved to a temporary folder inside <directory> so you can process those files later.

## Warning

This script has been tested in Mac OS X 10.6.8, and it should work in other Unix-like systems.

The script is __not desctructive__, but if you execute the script in a root folder with a lot of subfolders, you might have a hard time moving them back to where they were. It is __reccommended__ to make a copy in an isolated folder then process the files. If you're satisfied with the result, replace the original folder.

## To-do's

1. Add option to recurse through directories, or just process the root directory
2. Add option to choose the temporary folder name
3. Add option to check for height, or both
4. Add Windows support
5. Add confirmation of moved files.
6. Add logging.