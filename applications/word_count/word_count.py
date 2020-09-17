from string import ascii_lowercase

def word_count(s):
    output_str = ""
    output_obj = {}
    new_word = ""
    words = 0
    in_new_word = True
    first = True
    for c in s:

        if c.lower() in ascii_lowercase or c == "'":
            if first == True:
                words += 1
                first = False
            elif in_new_word == False:
                words += 1
                in_new_word = True
            new_word += c
            output_str += c
        else:
            if in_new_word == True:
                if  new_word.lower() in output_obj:
                    output_obj[new_word.lower()] += 1
                else:
                    if first == False and new_word != "'":
                        
                        output_obj[new_word.lower()] = 1
                    

                new_word = ""
                in_new_word = False
            output_str += c
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
    return output_obj

# if last character and we're still in new word, add wordcount by 1 and trim ittttt

if __name__ == "__main__":
    print(word_count(""))
    print(word_count("Hello"))
    print(word_count("Hello hello"))

    print(word_count('Hello, my cat. And my cat doesn\'t say "hello" back.'))
    print(word_count('":;,.-+=/\\|[]{}()*^&'))
    print(word_count("Wh>...At♣♣○didyou just say to ♥♥♥'1=1--breakmeplease"))