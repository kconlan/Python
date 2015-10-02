#Kevin J Conlan Python CSCI 6651-01 Professor Gulnora Nurmatova Homework 4 Shelve Speed

import shelve
from datetime import datetime


s = shelve.open("data")
s = {'Name': 'Kevin', 'Age': 27, 'Nationality': 'American'};
d1 = datetime.now()
print(s["Name"])
d2=datetime.now()
print(d2.microsecond-d1.microsecond)
