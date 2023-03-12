# Implementing a Hash Table

# ╔══════════════════════════════════════════════╗
# ║                                              ║
# ║          IMPLEMENTING A HASH TABLE           ║
# ║                                              ║
# ╚══════════════════════════════════════════════╝

# Imagine walking into a magical library, filled with every book imaginable. This library has a unique feature that sets it apart
# from all others - a librarian who can find any book instantly, simply by knowing its title. This librarian doesn't waste time
# searching through endless shelves, but instead uses a map to locate any book in a matter of seconds.

# As you enter the ancient library, you are immediately engulfed in an aura of otherworldly energy. The shelves tower above you,
# packed with tomes of knowledge, scrolls of ancient wisdom, and stones inscribed with cryptic symbols. The air is thick with the
# scent of potions and elixirs, and the occasional glimmer of a precious gem catches your eye.

# As you wander through the maze-like corridors, you can't help but feel that something is stirring within you. The energy of the
# library seems to be seeping into your bones, awakening a deep curiosity within you. You come across a section devoted to the
# arcane arts of mathematics and algorithms, and your heart quickens as you realize that these are the keys to understanding the
# very fabric of reality itself.

# You reach for a worn leather-bound grimoire, its pages yellowed with age, and begin to read. As the symbols and equations dance
# before your eyes, you feel a sudden shift in your perception. It's as if a veil has been lifted, and you can see the world in a
# new light.

# You start to realize that everything around you, from the patterns in the tapestries to the movements of the stars, can be
# quantified and analyzed through the lens of mathematics. And at the heart of this understanding lies the concept of the hash
# table.

# It is through the power of the hash table that wondrous machines can be created, machines that can go so far as to simulate the
# human mind itself. The implications of this realization are staggering, and you feel as if you are standing on the precipice of a
# new era of human understanding.


# The Magic of Hash Tables

#  ╔══════════════════════════════════════════╗
#  ║                                          ║
#  ║    THE MAGIC OF HASH TABLES              ║
#  ║    (And the quest for O(n))              ║
#  ╚══════════════════════════════════════════╝


# In the world of computer science, hash tables are like the magical library described earlier. They are a powerful tool used to store and retrieve
# data, and work much like our librarian. Instead of books and titles, hash tables store data in key/value pairs. When new data is
# added, a mathematical function(the "hashing function") is used to assign each entry a unique index on an array or list.
# 
# This process is similar to creating a map of the library, where each book is assigned a specific Dewey Decimal number. When we want
# to find a book, we simply give the librarian its title, and they use the map to locate it instantly. With hash tables, we give them
# the key(the data's name) and the hashing function is used to find its corresponding location in the table, giving us instant access
# to its value.
# 
# Hash tables are also commonly referred to as "dictionaries" because they share similarities with how dictionaries are structured. In
# a dictionary, each word(key) has a corresponding definition(value). Similarly, in a hash table, each data element(key/value pair) is
# assigned a unique index on an array or list using a hashing function. This can be thought of as creating a map of a library, where
# each book is assigned a specific Dewey Decimal number. Just as we give a librarian the title of a book to locate it, we give a hash
# table the key(the data's name) and the hashing function is used to find its corresponding location in the table, giving us instant
# access to its value.
# 
# The magic of hash tables lies in their ability to retrieve data in O(1) time - essentially instantly. No matter how large the data
# set becomes, hash tables can retrieve any piece of data the moment we search for it by its key.
# 
# The power of math to describe and traverse complex systems is awe-inspiring. By using mathematical functions to sort and classify
# data based on their names, we tap into an arcane world that enables the creation of advanced computer systems. These mathematical
# functions are incredibly fast and accurate, allowing real-time processing and analysis of vast amounts of data. They form the
# backbone of many important technologies such as AI, machine learning, cryptography, and data analysis.
# 
# As computer scientists, we are the wizards wielding this power, creating magical systems that can do amazing things. By harnessing
# the power of math, we can unlock new frontiers of knowledge and open up endless possibilities for innovation and discovery.
# 
# So, next time you hear about hash tables, think of them as magical libraries or dictionaries where data can be found instantly with
# just a key!

# ╔════════════════════════════════════════════════╗
# ║                                                ║
# ║    CREATING AND ADDING ITEMS TO THE HASH TABLE ║
# ║                                                ║
# ╚════════════════════════════════════════════════╝

# We'll start by examining the initial state of a hash table with three indices
# and then see how new entries are added and how the table is resized when necessary.
# Initial state of the hash table with three indices
#   0     1     2
#  ---   ---   ---
# |   | |   | |   |
#  ---   ---   ---
#   |     |     |
#  None  None  None

# When an entry is added to the hash table, its key is hashed
# to determine which index it should be stored in. The hash
# function takes the key as input and returns an integer index.

# For example, the key "apple" might hash to index 1:
# hash("apple") -> 1

# Add entry with key "apple" and value "red" to index 1
# |==============List Indices======================|
# |    0           1                      2         |
# |   ---         ---                    ---        |
# |  |   | ----> |   | ---------------> |   |       |
# |   ---         ---                    ---        |
# |    |           |                      |         |
# |   None   ("apple", "red")            None       |


# When another entry is added to the hash table with a key
# that hashes to the same index, it is stored in a linked
# list at that index.

# For example, the key "banana" might also hash to index 1:
# hash("banana") -> 1

# Add entry with key "banana" and value "yellow" to index 1
# |==============List Indices=======================|
# |    0           1                      2         |
# |   ---         ---                    ---        |
# |  |   | ----> |   | ---------------> |   |       |
# |   ---         ---                    ---        |
# |    |           |                      |         |
# |  None   ("apple", "red")    ("banana", "yellow")|

# If too many entries are added to one index, the linked list
# can become too long and degrade performance. To avoid this,
# the hash table can be resized to provide more indices.

# For example, if more entries are added with keys that all hash
# to index 1, the linked list at index 1 could become very long:

# hash("cherry") -> 1
# hash("date") -> 1
# hash("elderberry") -> 1
# ...

# Resize hash table to six indices
#   0     1     2     3     4     5
#  ---   ---   ---   ---   ---   ---
# |   | |   | |   | |   | |   | |   |
#  ---   ---   ---   ---   ---   ---
#   |     |     |     |     |     |
#  None  None  None  None  None  None

# Resize hash table to six indices
# |==============List Indices======================|
# |   0     1     2     3     4     5               |
# |  ---   ---   ---   ---   ---   ---              |
# | |   | |   | |   | |   | |   | |   |             |
# |  ---   ---   ---   ---   ---   ---              |
# |   |     |     |     |     |     |               |
# | None  None  None  None  None  None              |
# |                                                 |


# Entries are rehashed and redistributed to the new indices.
# This is due to the fact that the hash function's resultant index values are calculated with several coefficients, including the resized number of indices in the hash table.
# This significantly shifts the math, resulting in potentially wildly different index values for the same keys.
# |==============List Indices===================================================|
# |   0     1           2            3            4                  5         |
# |  ---   ---         ---          ---          ---                ---        |
# | |   | |   | ----> |   | ---->  |   | -----  |   | -----------> |   |       |
# |  ---   ---         ---          ---          ---                ---        |
# |   |     |           |            |            |                  |         |
# | None  None   ("apple", "red")   None   ("banana", "yellow")    None        |
# |                     |                                                      |
#                ("cherry", "red")

class Node:
    """
    A class representing a node in a linked list.
    """

    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None


class HashTable:
    """
    A class representing a hash table.
    """

    def __init__(self, capacity=4):
        self.capacity = capacity
        self.size = 0
        self.table = [None] * self.capacity

    def hash_index(self, key):
        """
        A helper function to compute the hash index of a given key.
        """
        return hash(key) % self.capacity

    def get_load_factor(self):
        """
        A helper function to compute the load factor of the hash table.
        """
        return self.size / self.capacity

    def put(self, key, value):
        """
        Add a key-value pair to the hash table. If the key already exists,
        update its value.

        Implement this.
        """
        index = self.hash_index(key)
        node = self.table[index]
        while node:
            if node.key == key:
                node.value = value
                return
            node = node.next
        new_node = Node(key, value)
        new_node.next = self.table[index]
        self.table[index] = new_node
        self.size += 1
        if self.get_load_factor() > 0.7:
            self.resize(self.capacity * 2)

    def delete(self, key):
        """
        Remove the value stored with the given key.

        Print a warning if the key is not found.

        Implement this.
        """
        index = self.hash_index(key)
        node = self.table[index]
        if node and node.key == key:
            self.table[index] = node.next
            self.size -= 1
            return
        prev = None
        while node:
            if node.key == key:
                prev.next = node.next
                self.size -= 1
                return
            prev, node = node, node.next
        print("Warning: Key not found")

    def get(self, key):
        """
        Retrieve the value stored with the given key.

        Returns None if the key is not found.

        Implement this.
        """
        index = self.hash_index(key)
        node = self.table[index]
        while node:
            if node.key == key:
                return node.value
            node = node.next
        return None

    def resize(self, new_capacity):
        """
        Changes the capacity of the hash table and rehashes all key/value pairs.

        Implement this.
        """
        old_table = self.table
        self.table = [None] * new_capacity
        self.capacity = new_capacity
        self.size = 0
        for node in old_table:
            while node:
                self.put(node.key, node.value)
                node = node.next

    def __str__(self):
        """
        Return a string representation of the hash table.

        This is not a required method of the class, but can be useful
        for debugging purposes.
        """
        res = "{\n"
        for i in range(self.capacity):
            res += f"    {i}: "
            node = self.table[i]
            if node:
                res += f"({node.key}, {node.value})"
                node = node.next
            while node:
                res += f" -> ({node.key}, {node.value})"
                node = node.next
            res += "\n"
        res += "}"
        return res


if __name__ == "__main__":
    ht = HashTable()

    # Test size, capacity and load factor before adding any items.
    print("Checking out the hash table stats...\n")
    print("Size: ", ht.size)
    print("Capacity: ", ht.capacity)
    print("Load factor: ", ht.get_load_factor())
    print()

    # Let's put some items in the hash table
    ht.put("key-0", "val-0")
    ht.put("key-1", "val-1")
    ht.put("key-2", "val-2")
    ht.put("key-3", "val-3")
    print("Four items added successfully to the hash table!")
    print(ht)
    print()

    # Let's get some items from the hash table
    print("Retrieving items from the hash table...")
    print("key-0:", ht.get("key-0"))
    print("key-1:", ht.get("key-1"))
    print("key-2:", ht.get("key-2"))
    print("key-3:", ht.get("key-3"))
    print("key-4:", ht.get("key-4"))
    print()

    # Let's delete some items from the hash table
    ht.delete("key-0")
    ht.delete("key-2")
    print("Two items successfully deleted from the hash table!")
    print(ht)
    print()
