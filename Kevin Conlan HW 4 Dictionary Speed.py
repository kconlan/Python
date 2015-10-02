#Kevin J Conlan Python CSCI 6651-01 Professor Gulnora Nurmatova Homework 4 Dictionary Speed

from datetime import datetime

dict = {'Name': 'Kevin', 'Age': 27, 'Nationality': 'American'};
d1 = datetime.now()
print(dict['Name'])
d2=datetime.now()
print(d2.microsecond-d1.microsecond)
