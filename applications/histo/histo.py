from string import ascii_lowercase

def word_count(s):
    longest = 0
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
                        if len(new_word) > longest:
                            longest = len(new_word)
                    

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
    output_obj = sorted(output_obj.items(),key=lambda x: x[1])
    whitespace = " " * 25
    output = ""
    for tup in output_obj:
        hashes = "#" * tup[1]
        remaining = longest - len(tup[0]) + 2
        whitespace = " " * remaining
        # print(hashes)
        right_hashes = f"{whitespace}{hashes}"
        # print(right_hashes)

        output += f"{tup[0]}"
        output += f"{right_hashes}\n"
    return output


if __name__ == "__main__":
    with open("robin.txt", errors="ignore") as f:
        words = f.read()
        print(word_count(words))
