#Kevin Conlan Python HW Animal Class

Class Animal:
    def __init__(self, name):
        self.name = name

    def guess_who_am_I(self):
        if self.name == "Elephant":             # Elephant 
            hints = ["I have a long nose", "I like peanuts", "I have big, grey, floppy ears"]
            print("With three hints, can you guess what animal I am?")
            for i in range(len(hints)):          #loop for guessing
                print(hints[i])
                guess = input("Who am I?")
                if guess == self.name:        #answer is correct
                    print("Correct! I am", self.name)
                    break
                else:
                    print("Nope, try again!")
                    if i == len(hints)-1:        
                        print("I'No more hints! The animal is:", self.name)
        if self.name == " Tyrannosaurus Rex":                #Tyrannosaurus Rex
            hints = ["I am the king of tyrannical lizards ", "I have really short arms", "I love Jurassic Park"]
            print("With three hints, can you guess what animal I am?")
            for i in range(len(hints)):
                print(hints[i])
                guess = input("Who am I?")
                if guess == self.name:
                    print("Correct! I am", self.name)
                    break
                else:
                    print("Nope, try again!")
                    if i == len(hints)-1:
                        print("No more hints! The answer is:", self.name)
        if self.name == "Puppy":                  #Puppy
            hints = ["I have a cold wet nose", "I bark too much", "My name is either Spot or Wishbone or Rover"]
            print("With three hints, can you guess what animal I am?")
            for i in range(len(hints)):
                print(hints[i])
                guess = input("Who I am?")
                if guess == self.name:
                    print("Correct! I am", self.name)
                    break
                else:
                    print("Nope, try again!")
                    if i == len(hints)-1:
                        print("No more hints! The answer is:", self.name)


e = Animal("Elephant")
t = Animal(Tyrannosaurus Rex")
b = Animal("Puppy")

e.guess_who_am_I()
t.guess_who_am_I()
b.guess_who_am_I()
