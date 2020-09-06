dist = {
"E":11.53,
"T":9.75,
"A":8.46,
"O":8.08,
"H":7.71,
"N":6.73,
"R":6.29,
"I":5.84,
"S":5.56,
"D":4.74,
"L":3.92,
"W":3.08,
"U":2.59,
"G":2.48,
"F":2.42,
"B":2.19,
"M":2.18,
"Y":2.02,
"C":1.58,
"P":1.08,
"K":0.84,
"V":0.59,
"Q":0.17,
"J":0.07,
"X":0.07,
"Z":0.03
}
logs = {
"E":0,
"T":0,
"A":0,
"O":0,
"H":0,
"N":0,
"R":0,
"I":0,
"S":0,
"D":0,
"L":0,
"W":0,
"U":0,
"G":0,
"F":0,
"B":0,
"M":0,
"Y":0,
"C":0,
"P":0,
"K":0,
"V":0,
"Q":0,
"J":0,
"X":0,
"Z":0}


# from hashtable import HashTable
# Use frequency analysis to find the key to ciphertext.txt, and then
# decode it.
# Your code here

# Write a hash table that extracts the contents of the cipher and individually stores each letter as a node.
# This will be a massive table. We will then scan the table for all instances of each letter, and collect the total occurences.

# The most frequent instances will be assigned in order of frequency, as: "ETAOIN SHRDLU".


# This is the default permutation we will try, but we will attempt many other possible permutations, however they will
# restrict the most frequently occurring letters to be some combination of the aforementioned.
# We will likely need to test based on "statistical likelihood", i.e. if ETA... doesn't work, shift the leading letter one position to the right, continue shifting it until it is at the very end of the "priority ranking" string. Do this for each 


# Unsure how to measure success. Possibly integrate a "dictionary" that can intelligently locate english words, perhaps we can have a condition that loops through the "solution" and checks to be sure all of the characters are complete words, adn then separates them automatically with spaces.




cipher = {}



with open('./ciphertext.txt', 'r+') as f:
    for line in f:

        for c in line:
            if c in logs:
                if logs[c] == None:
                    logs[c] = 1
                else:
                    logs[c] += 1
    logsum = sum(logs.values())
    print(logs)
    for c in logs:
        logs[c] = (logs[c]/logsum)*100
    completed = {    "E":False,
"T":False,
"A":False,
"O":False,
"H":False,
"N":False,
"R":False,
"I":False,
"S":False,
"D":False,
"L":False,
"W":False,
"U":False,
"G":False,
"F":False,
"B":False,
"M":False,
"Y":False,
"C":False,
"P":False,
"K":False,
"V":False,
"Q":False,
"J":False,
"X":False,
"Z":False}

    for c in dist:
        lowest = 0
        letter = "*"

        for k in logs:
            print(completed)
            if abs((dist[c]-logs[k])/dist[c]) < abs((dist[c]-lowest)/dist[c]):
                if completed[k] == False:
                    lowest = logs[k]
                    letter = k 
                #we found em, yep
            elif abs((dist[c]-logs[k])/dist[c]) == abs((dist[c]-lowest)/dist[c]):
                if completed[k] == False:
                    lowest = logs[k]
                    letter = k 
        print(f"assigning {letter} to {c}")
        #We finished looping, we found the letter to add, make sure to list it in completed so duplicate values don't break everything
        completed[letter] = True
        cipher[letter] = c
    f.seek(0)
    z = f.read()
    output = ""
    for letter in z:
        # print(letter)
        if letter in cipher:
            # print(cipher)
            # print(letter, cipher[letter])
            output += cipher[letter]
        else: 
            output += letter


    print(output)

        

print(cipher)
