import sys
import os
import shutil


designDirectories = ["drawable-hdpi", "drawable-mdpi", "drawable-xhdpi", "drawable-xxhdpi", "drawable-xxxhdpi"]
switcher = {
        1: "drawable-mdpi",
        1.5: "drawable-hdpi",
		2: "drawable-xhdpi",
		3: "drawable-xxhdpi",
		4: "drawable-xxxhdpi"
    }
def files(path):
    for file in os.listdir(path):
        if os.path.isfile(os.path.join(path, file)):
            yield os.path.join(path, file)
			
def generate_icon_name(icon):
		if '@' in icon:
			return icon.split('@')[0] + '.png'
			
def copyFile(file, srcPath, desPath, rename):
	print ("Copying " + file + " from " + srcPath + " to " + desPath);
	if not os.path.exists(desPath):
		os.makedirs(desPath)
	shutil.copy2(os.path.join(srcPath, file), desPath)
	if rename:
		os.rename(os.path.join(desPath, file), os.path.join(desPath, generate_icon_name(file)))
	
def compute_density(icon):
		if '@' in icon:
			return float(icon.split('@')[1].split('x')[0])
		else:
			return -1
	
def copy_from_design_folders(srcPath, desPath):
	for x in os.walk(srcPath):
		if os.path.basename(x[0]) in designDirectories:
			dir = x[0]
			index = designDirectories.index(os.path.basename(dir))
			for file in files(dir):
				copyFile(os.path.basename(file), dir, os.path.join(desPath, designDirectories[index]), False)
	
def copy_from_folder(srcPath, desPath):
	icons = [file for file in os.listdir(srcPath) if file.endswith('.png')]
	rename = True
	for icon in icons:
		x = compute_density(icon)
		cp_dir = switcher.get(x)
		copyFile(icon, srcPath, os.path.join(desPath, cp_dir), rename)
		
def print_usage(exit):
	print ("Usage : python " + sys.argv[0] + " <src-path> <dest-path> --file|--dir")
	print("--file : use to copy asset files from single folder to destination design directories")
	print("--dir  : use to copy asset files from design directories to destination design directories")
	if exit:
		sys.exit(0)

if len(sys.argv) != 4:
	print_usage(True)
	
if not os.path.exists(sys.argv[1]):
	print_usage(True)
	
if not os.path.exists(sys.argv[2]):
	print_usage(True)
	
if sys.argv[3] == "--file":
	copy_from_folder(sys.argv[1], sys.argv[2]);
elif sys.argv[3] == "--dir":
	copy_from_design_folders(sys.argv[1], sys.argv[2]);
else:
	print_usage(True)
	
