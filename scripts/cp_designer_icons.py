import sys
import os
import shutil

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
if len(sys.argv) != 3:
	print ("Usage : python " + sys.argv[0] + " <src-path> <dest-path>")
	sys.exit(0)
	
if not os.path.exists(sys.argv[1]):
	print ("<src-path> does not exists");
	sys.exit(0)
	
if not os.path.exists(sys.argv[2]):
	print ("<dest-path> does not exists");
	sys.exit(0)
	
for x in os.walk(sys.argv[1]):
	if os.path.basename(x[0]) in designDirectories:
		dir = x[0]
		index = designDirectories.index(os.path.basename(dir))
		for file in files(dir):
			copyFile(file, os.path.join(sys.argv[2], designDirectories[index]))
			
	
	
