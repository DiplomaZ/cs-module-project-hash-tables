# Hash Table Sandbox

🔍 This repository showcases a custom implementation of a hash table that uses collision avoidance techniques such as linked list chaining. The implementation includes the HashTable class, which is dependent on the HashTableEntry class that represents a key-value pair. This implementation is inspired by fundamental computer science concepts such as hash functions (specifically FNV-1 and DJB2), load factors, and resizing.

```python
def fnv1(self, key):
        """
        FNV-1 Hash, 64-bit
        """
        FNV_prime = 1099511628211
        offset_basis = 14695981039346656037
        hash = offset_basis
        for c in key:
            hash = hash*FNV_prime
            hash = hash ^ ord(c)

        return hash
```

👀 **Why Use Hash Tables?**

Hash tables are an essential data structure that provide fast access to data by using a key-value pair approach. They are used in a wide range of applications, including:

Application | Description
------------|------------
🗄️ Databases | Efficiently store and retrieve large amounts of data
🔐 Cryptography | Securely store and transmit sensitive information
💾 Caching Systems | Improve system performance by storing frequently accessed data
👨‍💻 Compiler Symbol Tables | Store and access information about variables and functions in programming languages
📝 Spell Checkers | Quickly check whether a word is spelled correctly
... | And much more!

📂 **Folder Structure**

This repository contains the following folder:

- `hashtable/` - This folder contains the implementation of the hash table data structure, including the HashTable and HashTableEntry classes, and several test programs for different use cases.

📦 **Applications**

This repository also includes several example applications that showcase the use of hash tables in solving various problems. These applications are located in the `applications/` folder:

Application | Description
------------|------------
🔒 crack_caesar/ | Caesar cipher cracking application
📈 expensive_seq/ | Big O(n) optimization of a fibonacci-like sequence
📊 histo/ | Word-frequency histogram generator
🔎 lookup_table/ | O(n) lookup table application
🔗 markov/ | Markov chain application with demo input.txt file
🗑️ no_dups/ | O(n^2) solution to removing duplicate words from a string
➕ sumdiff/ | O(n^2) solution to finding pairs of numbers in a list whose sum equals the difference of two other numbers in the list.
📝 word_count/ | O(n) solution to counting the number of times each word appears in a string

🔧 **Usage**

To use the hash table implementation or any of the example applications, simply download or clone the repository and run the desired Python script.

📝 **Contributing**

Contributions to this repository are welcome! If you have any improvements, bug fixes, or additional example applications that you would like to contribute, please open a pull request with your changes.