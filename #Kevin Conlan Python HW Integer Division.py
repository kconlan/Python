#Kevin Conlan Python HW Integer Division


from random import randrange


while True:
    a = randrange(5)
    b = randrange(1, 5)
    print("Integer division")
    try:
        answer = integer(input("{}/{}=".format(a, b)))
        if a//b == answer:
            print("Correct!")
        else:
            print("Sorry, that is not correct…")
        replay = input("Do you want to try again?")
        if replay == "no":
            break
    except ValueError:
        print("This program only uses integers as variables")
    except:
        print("An error has occurred…")
