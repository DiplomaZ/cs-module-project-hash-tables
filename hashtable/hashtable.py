class HashTableEntry:
    """
    Linked List hash table key/value pair
    """
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None


# Hash table can't have fewer than this many slots
MIN_CAPACITY = 8


class HashTable:
    """
    A hash table that with `capacity` buckets
    that accepts string keys

    Implement this.
    """

    def __init__(self, capacity ):
        # Your code here
        self.capacity = capacity
        self.table = [None] * self.capacity
        self.elements = 0
        # Add A PROPERTY THAT ALLOWS YOU TO TRACK CURRENT ELEMENTS INSTEAD OF TRAVERSING LIST EVERY TIME!!!



    def get_num_slots(self):
        """
        Return the length of the list you're using to hold the hash
        table data. (Not the number of items stored in the hash table,
        but the number of slots in the main list.)

        One of the tests relies on this.

        Implement this.
        """
        return self.capacity

        # Your code here


    def get_load_factor(self):
        """
        Return the load factor for this hash table.

        Implement this.
        """
        num_slots = len(self.table)

        num_vals = self.elements




        return num_vals/num_slots
        # Your code here


    def fnv1(self, key):
        """
        FNV-1 Hash, 64-bit

        Implement this, and/or DJB2.
        """

        FNV_prime = 1099511628211
        offset_basis = 14695981039346656037
        hash = offset_basis
        for c in key:
            hash = hash*FNV_prime
            hash = hash ^ ord(c)

        return hash




        # 240 + 28 + 0xb3
# hash = offset_basis
# for each octet_of_data to be hashed
#  hash = hash * FNV_prime
#  hash = hash xor octet_of_data
# return hash
        # Your code here


    def djb2(self, key):
        """
        DJB2 hash, 32-bit

        Implement this, and/or FNV-1.
        """
        # Your code here


    def hash_index(self, key):
        """
        Take an arbitrary key and return a valid integer index
        between within the storage capacity of the hash table.
        """
        #return self.fnv1(key) % self.capacity
        return self.fnv1(key) % self.capacity

    def put(self, key, value):
        """
        Store the value with the given key.

        Hash collisions should be handled with Linked List Chaining.

        Implement this.
        """ 
        index = self.hash_index(key)
        if self.table[index] == None:
            self.table[index] = HashTableEntry(key, value)
            self.elements += 1
        else:
            curr_node = self.table[index]
            while True:
                if curr_node.key == key:
                    #Don't increase num elements here, we found a dupe
                    curr_node.value = value
                if curr_node.next == None:
                    self.elements += 1
                    curr_node.next = HashTableEntry(key, value)
                    break
                else:
                    curr_node = curr_node.next



    def delete(self, key):
        """
        Remove the value stored with the given key.

        Print a warning if the key is not found.

        Implement this.
        """

        index = self.hash_index(key)
        node = self.table[index]
        if node != None and node.key == key:
            self.table[index].value = None
            return
        while True:

            if node != None and node.next != None:
                next_node = node.next
                if next_node.key == key:
                    node.next = next_node.next
                    self.elements -= 1
                    break
                else:
                    node = node.next
            else:
                print("this node isn't here I'm really sorry please call back later this value is totally invalid")
                break

    def get(self, key):
        """
        Retrieve the value stored with the given key.

        Returns None if the key is not found.

        Implement this.
        """
        index = self.hash_index(key)
        value = None
        node =self.table[index]
        while True:

            if node != None:
                if node.key == key:
                    value = node.value
                    break
                else:
                    node = node.next
            else:
                return None
        return value

    def resize(self, new_capacity):
        """
        Changes the capacity of the hash table and
        rehashes all key/value pairs.
        
        Implement this.
        """
        while ht.get_load_factor() < 0.2 or ht.get_load_factor() > 0.7:

        
            self.capacity = new_capacity
            if self.get_load_factor() > 0.7:
                new_capacity *= 2
                print(self.get_load_factor())
                self.capacity = new_capacity
                old_table = self.table
                self.table = [None]*self.capacity
                self.elements = 0


                #Traverse the old table and pass each previous val into the put method of our new empty table
                for node in old_table:

                    while True:
                        if node != None:
                            self.put(node.key, node.value)

                            if node.next == None:
                                break
                            node = node.next
                        else: break



            if self.get_load_factor() < 0.2:

                new_capacity //= 2
                self.capacity = new_capacity
                old_table = self.table
                self.table = [None]*self.capacity
                self.elements = 0



                #Traverse the old table and pass each previous val into the put method of our new empty table
                for node in old_table:

                    while True:
                        if node != None:
                            self.put(node.key, node.value)

                            if node.next == None:
                                break
                            node = node.next
                        else: break




if __name__ == "__main__":
    ht = HashTable(8)

    print(ht.get_load_factor())

    ht.put("line_1", "'Twas brillig, and the slithy toves")
    ht.put("line_2", "Did gyre and gimble in the wabe:")
    ht.put("line_3", "All mimsy were the borogoves,")
    ht.put("line_4", "And the mome raths outgrabe.")
    ht.put("line_5", '"Beware the Jabberwock, my son!')
    ht.put("line_6", "The jaws that bite, the claws that catch!")
    ht.put("line_7", "Beware the Jubjub bird, and shun")
    ht.put("line_8", 'The frumious Bandersnatch!"')
    ht.put("line_9", "He took his vorpal sword in hand;")
    ht.put("line_10", "Long time the manxome foe he sought--")
    ht.put("line_11", "So rested he by the Tumtum tree")
    ht.put("line_12", "And stood awhile in thought.")

    print("")

    # Test storing beyond capacity
    for i in range(1, 13):
        print(ht.get(f"line_{i}"))
    print(ht.get_load_factor())

    # Test resizing
    old_capacity = ht.get_num_slots()

    ht.resize(ht.capacity)
    new_capacity = ht.get_num_slots()

    print(f"\nResized from {old_capacity} to {new_capacity}.\n")
    print(ht.get_load_factor())
    print(ht.elements)
    print(ht.capacity)


    # Test if data intact after resizing
    for i in range(1, 13):
        print(ht.get(f"line_{i}"))

    print("")
    print(ht.get_load_factor())

    # ht.delete("line_6")

    # for i in range(1, 13):
    #     print(ht.get(f"line_{i}"))