#Kevin J Conlan Python CSCI 6651-01 Professor Gulnora Nurmatova Homework 4 Security Scanner

import os
import fnmatch

directory= input("Starting path:")   
fileName = input("File name:")    
for dirpath, dirs, files in os.walk(directory):
    for singleFile in files:
        if fnmatch.fnmatch(singleFile, fileName): 
            f = open( os.path.join(dirpath, singleFile) )
            for text in f:
                if "password=" in text:
                    print("find \"password=\" in the file") #text "password="
