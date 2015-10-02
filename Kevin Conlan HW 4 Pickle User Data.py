#Kevin J Conlan Python CSCI 6651-01 Professor Gulnora Nurmatova Homework 4 Pickle User Data

import pickle

f = open("data.txt", "bw")
mypickle = input("Enter your name, age, and country")
pickle.dump(data, f)
f.close()