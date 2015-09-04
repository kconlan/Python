#Kevin J Conlan Python CSCI 6651-01 Professor Gulnora Nurmatova Homework 1

#The user will choose a number within the gven range, and the program will guess it

HIGH = 100
LOW = 1

def getnumber():
    # Gets a number from the user
    x = ""
    while not x or x > HIGH or x < LOW:
        print("Please enter a number between %s and %s" % (LOW, HIGH))
        x = input()
        try:
            x = int(x)
        except ValueError:
            x = getnumber()
    return(x)

def halfway(low, high):
    # Find an integer that is halfway point between two values
    x = abs(round((low+high)/2))
    return x

def guessnumber():
    # Computer finds number through halving
    number1 = LOW
    number2 = HIGH
    usernumber = getnumber()
    compguess = ""
    count = 0

    while compguess != usernumber:
        count += 1
        compguess = halfway(number1, number2)

        if abs(number2-number1) > 2 or compguess == usernumber:
            print('%s. Is it... %s' % (count, compguess))
            if compguess > usernumber:
                number2 = compguess
            elif compguess < usernumber:
                number1 = compguess
            elif compguess == usernumber:
                print("Got it!")
            else:
                print("Ahh...")
        
def main():
    while True:
        guessnumber()
        print('\n')

main()
