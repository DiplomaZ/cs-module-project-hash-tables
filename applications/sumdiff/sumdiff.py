"""
find all a, b, c, d in q such that
f(a) + f(b) = f(c) - f(d)
"""

#q = set(range(1, 10))
#q = set(range(1, 200))
q = (1, 3, 4, 7, 12)


def f(x):
    return x * 4 + 6

# Your code here
sum_storage = {}
diff_storage = {}
for x in q:
    for y in q:
        sum_storage[(x,y)] = (f(x), f(y))
        
        diff_storage[(x,y)] = (f(x), f(y))

print(diff_storage)
#get sum_key from sum_dict
#use sum_key to get sum_value
#compare sum_value to values in diff_dict
#find the diff_value=sum_value
#use diff_value to get diff_key from diff_dict
#diff_key = f(c)-f(d) that is equal to f(a)+f(b)
for sum_tuple in sum_storage:
    for diff_tuple in diff_storage:
        a = sum_storage[sum_tuple][0]
        b = sum_storage[sum_tuple][1]
        c = diff_storage[diff_tuple][0]
        d = diff_storage[diff_tuple][1]



        if a + b == c - d:
            print(f"{a} + {b} = {c} - {d}")




