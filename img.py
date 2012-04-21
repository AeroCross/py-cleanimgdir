# img.py – Checks image files for their sizes in a given folder (and its subfolders) and moves the matching images to a temporary folder.

# Version 1.0
# Author: Mario Cuba <mario@mariocuba.net>
# License: Creative Commons Attribution 3.0 Unported License (see: http://creativecommons.org/licenses/by/3.0)

print # padding

# import the requiered modules
import os, shutil
from sys import argv
from PIL import Image

script, path = argv # set the argument variables

def getMinWidth():
	minwidth = raw_input('Minimum image width: ')

	try:
		minwidth = int(minwidth)
	except ValueError:
		print '"' + str(minwidth) + '" isn\'t an integer.'
		minwidth = getMinWidth()
	
	return minwidth

# program start
minwidth = getMinWidth()

# check if there's a trailing slash in the path name - add if if there isn't
if (path.endswith('/') == False):
	path = path + '/'

tpath = 'Temporary Files'

files = os.walk(path, False) # list with all files in "path"
dirs = [] # initizalize directories
imgs = [] # initialize images list

# check for all subfolders and save their abspaths
for r, d, f in files: # root, directories, filenames
	if (r.endswith('/') == False):
		r = r + '/'
		dirs.append(r)
	else:
		dirs.append(r)

# grab all images inside those foldes
for dirname in dirs:
	dir = os.listdir(dirname)

	for fname in dir:
		if (
				fname.endswith(".jpg") == True or 
				fname.endswith(".jpeg") == True or 
				fname.endswith(".png") == True or 
				fname.endswith(".bmp") == True or 
				fname.endswith(".gif") == True
			):
				imgs.append(dirname + fname)
		# endfor
# endfor

print "The image minimum width is: " + str(minwidth) + '.'

for file in imgs:
	fullpath = file.rsplit('/', 1);
	
	dname = fullpath[0] + '/'
	fname = fullpath[1]
	
	img = Image.open(file)
	if (img.size[0] < minwidth):
		print "Image '" + fname + "' is not wide enough. (Width: " + str(img.size[0]) + ')'
		
		try: 
			os.makedirs(dname + tpath)
		except:
			pass
		
		shutil.move(file, dname + tpath)
# endfor

print # padding