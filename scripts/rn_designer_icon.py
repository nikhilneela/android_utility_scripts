import sys
import os
import shutil
import ntpath

def files(path):
    for file in os.listdir(path):
        if os.path.isfile(os.path.join(path, file)):
            yield os.path.join(path, file)
			
def copyFile(srcPath, desPath):
	print (srcPath)
	print (desPath)
	if not os.path.exists(desPath):
		os.makedirs(desPath)
	
	shutil.copy2(srcPath, desPath)
	

designDirectories = ["drawable-hdpi", "drawable-mdpi", "drawable-xhdpi", "drawable-xxhdpi", "drawable-xxxhdpi"]
if len(sys.argv) != 4:
	print ("Usage : python " + sys.argv[0] + " <file-name> <new-file-name> <path>")
	sys.exit(0)
	
if not os.path.exists(sys.argv[3]):
	print ("<path> does not exists");
	sys.exit(0)


for x in designDirectories:
	path = sys.argv[3] + '/' + x
	if not os.path.exists(path):
		print (path + " does not exist")
		continue
	for y in os.walk(path):
		for file in files(y[0]):
			if ntpath.basename(file) == sys.argv[1]:
				os.rename(file, os.path.join(y[0], sys.argv[2]))
