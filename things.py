def my_hash(s):
    sb = s.encode()
    total = 0
    for b in sb:
        total += b

    return total


my_array = [None] * 8
print(f'my_array {my_array}')

hash_index = my_hash("hello world") % 8
print(f'hash index {hash_index}')

my_array[hash_index] = 'my value'
print(f'my_array {my_array}')
print(f"my array {my_array}" )

hash_index = my_hash("hello world") % 8
print(my_array[hash_index])

my_array[hash_index] = None
print("anything???? ",my_array[hash_index])

  unsigned long
    hash(str)
    {
        unsigned long hash = 5381;
        int c;

        while (c = *str++)
            hash = ((hash << 5) + hash) + c; /* hash * 33 + c */

        return hash;
    }