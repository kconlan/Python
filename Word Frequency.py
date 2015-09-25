
#Kevin J Conlan Python CSCI 6651-01 Professor Gulnora Nurmatova Homework 3

Def word_frequency(wordlist ):
    i = [ None ] * len( wordlist )         #creates a new list
    for n in range( len(wordlist ) ):
        i[n] = wordlist.count( wordlist[n] )    #Counts how many times the word appears
    wordlist = dict( zip(wordlist, i ) )        #Creates a dictionary
    return worldlist


wordlist=["apple", "dog","tiger",  "sofa", "tree", "table", "backpack", "wolf", "newspaper", "pizza", ]
print( count_frequency( wordlist ) )






