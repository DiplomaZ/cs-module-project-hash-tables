from string import ascii_lowercase

def no_dups(s):
    output_str = ""
    output_obj = {}
    new_word = ""
    words = 0
    in_new_word = True
    first = True
    first_word = True
    for c in s:

        if c.lower() in ascii_lowercase or c == "'":
            if first == True:
                words += 1
                first = False
            elif in_new_word == False:
                words += 1
                in_new_word = True
            new_word += c

        else:
            if in_new_word == True or first_word == True:
                first_word = False
                if  new_word.lower() in output_obj:
                    output_obj[new_word.lower()] += 1
                else:
                    if first == False and new_word != "'":
                        
                        output_obj[new_word.lower()] = 1
                        output_str += new_word + " "
                new_word = ""
                in_new_word = False
    if first_word == True:
        
        if  new_word.lower() in output_obj:
            first_word = False
            output_obj[new_word.lower()] += 1
        else:
            first_word = False
            
            output_obj[new_word.lower()] = 1
            output_str += new_word + " "
            
                    


    allowed = True

    if len(new_word) < 1:
        allowed = False
    else:
        for c in new_word:
            if c.lower() in ascii_lowercase:
                pass #This character may have passed our test, but we will see...
            else:
                allowed = False
    if new_word not in output_obj and allowed == True:
        output_obj[new_word] = 1
    elif new_word in output_obj and allowed == True:
        output_obj[new_word] += 1

    # print(output_str)
    return output_str.strip()


if __name__ == "__main__":
    print("dingle")
    print(no_dups(""))
    print(no_dups("hello"))
    print(no_dups("hello hello"))
    print(no_dups("cats dogs fish cats dogs"))
    print(no_dups("spam spam spam eggs spam sausage spam spam and spam"))