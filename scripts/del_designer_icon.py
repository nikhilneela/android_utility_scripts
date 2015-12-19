import sys
import os
import shutil
import ntpath

def files(path):
    for file in os.listdir(path):
        if os.path.isfile(os.path.join(path, file)):
            yield os.path.join(path, file)
			
designDirectories = ["drawable-hdpi", "drawable-mdpi", "drawable-xhdpi", "drawable-xxhdpi", "drawable-xxxhdpi"]
if len(sys.argv) != 3:
	print ("Usage : python " + sys.argv[0] + " <file-name> <path>")
	sys.exit(0)
	
if not os.path.exists(sys.argv[2]):
	print ("<path> does not exists");
	sys.exit(0)


for x in designDirectories:
	path = os.path.join(sys.argv[2], x)
	path = os.path.join(path, sys.argv[1])
	if not os.path.exists(path):
		print (path + " does not exist")
		continue
	else:
		os.remove(path)
