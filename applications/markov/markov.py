import random

# Read in all the words in one go
with open("input.txt", errors="ignore") as f:
    words = f.read()
dictionary = {}
# TODO: analyze which words can follow other words
# Your code here
splitted = words.split()
stop_words = {".": '.',"?": '?', "!": '!', '"': '"'}
for word in splitted: 
    # print(c)
    if word not in dictionary:

        dictionary[word] = []

prev_word = ""
for word in splitted:
    
    for root in dictionary:
        if prev_word == root:
            
            dictionary[root].append(word)
    prev_word = word


#get array of random word
start_word = random.choice(list(dictionary.keys()))



# print(start_word)
count = 0
current_word = start_word
while True:
    last_letter = len(current_word) -1
    if current_word[last_letter] in stop_words:
        
        print(current_word,end=" ")
        while True:
            current_word = random.choice(list(dictionary.keys()))
            if current_word[0].isupper() == True:
                break
    else:
        print(current_word,end=" ")
        if len(dictionary[current_word]) > 0:

            current_word = random.choice(dictionary[current_word])
        else:
            current_word = random.choice(list(dictionary.keys()))


    # print(dictionary)

        # if len(temp_list) > len(dictionary[root]):
        #     for w in temp_list:














# TODO: construct 5 random sentences
# Your code here

