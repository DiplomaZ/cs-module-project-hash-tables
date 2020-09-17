"""
find all a, b, c, d in q such that
f(a) + f(b) = f(c) - f(d)
"""
import profile
#q = set(range(1, 10))
q = set(range(1, 10000))
# q = (1, 3, 4, 7, 12)


def f(x):
    return x * 4 + 6



def functer():
    entries = {x:f(x) for x in q}


    # Your code here
    sum_storage = {}
    diff_storage = {}
    for x in q:
        for y in q:
            if entries[x]+entries[y] not in sum_storage:
                sum_storage[entries[x]+entries[y]] = (entries[x], entries[y])
            if entries[x]-entries[y] not in diff_storage:

                diff_storage[entries[x]-entries[y]] = (entries[x], entries[y])


    #get sum_key from sum_dict
    #use sum_key to get sum_value
    #compare sum_value to values in diff_dict
    #find the diff_value=sum_value
    #use diff_value to get diff_key from diff_dict
    #diff_key = f(c)-f(d) that is equal to f(a)+f(b)
    output = ""
    for curr_sum in sum_storage.keys():
        if curr_sum in diff_storage.keys():
            a,b = sum_storage[curr_sum][0],sum_storage[curr_sum][1]
            c,d = diff_storage[curr_sum][0],diff_storage[curr_sum][1]



            if a + b == c - d:
                output = f"{a} + {b} = {c} - {d}\n"

                print(output)



profile.run("functer()")
