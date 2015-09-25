#Kevin J Conlan Python CSCI 6651-01 Professor Gulnora Nurmatova Homework 3

def earsFunc(bunnies):
  if (bunnies == 0):
    return 0
  else:
    return 2 + earsFunc (bunnies - 1)
