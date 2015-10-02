import os
import fnmatch

directory = input("Starting path:")   
fileName = input("File name:")   
for dirpath, dirs, files in os.walk(directory):
    for singleFile in files:
        if fnmatch.fnmatch(singleFile, fileName): 
            print(os.path.join(dirpath, singleFile)) 
