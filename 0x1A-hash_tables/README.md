# Hash tables in C

## Files in this directory and what they do
### Task 0
- File: 
- Function: 
- Notes: 

### Task 1
- File: [1-djb2.c](./1-djb2.c)
- Function: defines a hash function depending on the DJB2 algorithm
- Notes:
The DJB2 (Daniel J. Bernstein 2) hash function is a simple and widely used hash function that is known for its speed and simplicity. It's often used in various applications, including hash tables and string hashing. While it's a decent hash function, it's important to note its characteristics and limitations:

Pros:
1. Speed: DJB2 is quite fast due to its simple bitwise operations and multiplication.

2. Simplicity: The implementation is straightforward, making it easy to understand and use.

Cons:
1. Not Cryptographically Secure: DJB2 is not suitable for cryptographic applications as it's vulnerable to hash collision attacks. It's not designed to resist malicious attempts to find two different inputs that produce the same hash.

2. Limited Distribution of Output: DJB2 has a somewhat limited distribution of hash values, which means that it may not evenly distribute keys in a hash table. This can lead to clustering and suboptimal performance in certain cases.

3. Limited Avalanche Effect: It may not have a strong avalanche effect, meaning small changes in the input may not produce significantly different hash values.

For non-cryptographic use cases where security isn't a concern, DJB2 can be a good choice due to its speed and simplicity. However, for cryptographic applications or when a more robust hash function is needed, consider using stronger alternatives like SHA-256 or SHA-3. Additionally, for hash tables with a risk of collision, you may want to use a more advanced hash function to improve distribution and reduce clustering.

## Learning Objectives
### What is a hash function ?
A hash function is a mathematical function that takes an input (or "message") and returns a fixed-size string of characters, which is typically a hexadecimal number. The output, often referred to as the hash code or hash value, is a unique representation of the input data. Hash functions are commonly used in computer science and cryptography for various purposes, including data indexing, data retrieval, and data integrity verification.

Hash functions have a wide range of applications, including indexing and searching in data structures like hash tables, cryptographic applications like password hashing, and ensuring data integrity through checksums or digital signatures. Different hash functions may be chosen based on the specific requirements of a given application.

### What makes a good hash function ?
Some key characteristics of a good hash function include:

1. Deterministic: For the same input, a hash function should always produce the same hash value.
2. Fast computation: Hash functions should be efficiently calculable, even for large inputs.
3. Avalanche effect: A small change in the input data should result in a significantly different hash value.
4. Pre-image resistance: Given a hash value, it should be computationally infeasible to determine the original input.
5. Collision resistance: It should be unlikely for two different inputs to produce the same hash value.

### What is a collision and what are the main ways of dealing with collisions in the context of a hash table ?
In the context of a hash table, a collision occurs when two different keys produce the same hash value. Collisions are inevitable because there are typically more possible keys than there are buckets (slots) in the hash table. Dealing with collisions is a critical aspect of designing and implementing an effective hash table. There are several main ways to handle collisions:

1. **Separate Chaining (Open Hashing)**:
   - In separate chaining, each bucket in the hash table contains a linked list (or another data structure like a tree) to store multiple key-value pairs that have the same hash.
   - When a collision occurs, a new key-value pair is simply added to the linked list at the corresponding bucket.
   - This approach is simple and efficient when the number of collisions is low.

2. **Linear Probing (Closed Hashing)**:
   - Linear probing is a technique where, when a collision occurs, the algorithm checks the next slot in the table, and if it's occupied, it moves to the next and continues until it finds an empty slot.
   - When searching for a key, you might need to examine multiple slots in a sequence to find the desired key or determine that the key is not present.

3. **Quadratic Probing (Closed Hashing)**:
   - Quadratic probing is similar to linear probing, but it uses a quadratic function to search for the next available slot.
   - This can help reduce clustering that can occur with linear probing.

4. **Double Hashing (Closed Hashing)**:
   - Double hashing is another collision resolution technique where a second hash function is used to determine the steps to move when a collision occurs.
   - It provides a more uniform distribution of keys and helps avoid clustering.

5. **Cuckoo Hashing**:
   - Cuckoo hashing uses multiple hash functions and two hash tables.
   - When a collision occurs, it relocates the colliding key to an alternative hash table.
   - This process continues until there are no more collisions.

6. **Robin Hood Hashing**:
   - Robin Hood hashing is a variation of linear probing where the algorithm reorganizes the table to minimize the variance in the number of probes needed to access elements.
   - Collisions are resolved by moving items around within the table to reduce the difference in probe lengths.

The choice of collision resolution method depends on factors such as the expected data distribution, the hash function, and the specific requirements of the application. Each method has its advantages and disadvantages, and some may be more suitable for certain scenarios than others. It's important to select a collision resolution strategy that provides good performance and maintains a low average search time while considering the specific use case.

### What are the advantages and drawbacks of using hash tables?
Hash tables are widely used in computer science and have several advantages and drawbacks:

**Advantages:**

1. **Fast Data Retrieval:** Hash tables offer constant-time (O(1)) average and best-case time complexity for key-based data retrieval. This means that you can quickly retrieve values associated with keys without regard to the size of the dataset.

2. **Flexible Key Types:** Hash tables can use various types of keys, such as strings, integers, or custom objects, making them versatile for different data storage needs.

3. **Efficient Insertions and Deletions:** On average, insertions and deletions in hash tables are also O(1), assuming a good hash function and a low collision rate.

4. **Dynamic Sizing:** Many modern hash table implementations automatically resize when the number of stored items reaches a certain threshold, ensuring efficient space usage.

5. **Simple Interface:** Hash tables provide a straightforward interface for basic operations like inserting, deleting, and looking up values.

**Drawbacks:**

1. **Hashing Collisions:** Hash tables can experience collisions, where two different keys produce the same hash value. This can lead to performance degradation, especially if not handled properly.

2. **Hash Function Dependency:** The efficiency of a hash table is heavily dependent on the quality of the hash function used. A poor hash function can lead to a higher collision rate.

3. **Memory Usage:** Hash tables can consume more memory than other data structures. They need to allocate memory for the table's buckets and potentially linked lists.

4. **Unordered:** Hash tables are inherently unordered data structures. If you need to maintain a specific order (e.g., sorting by keys), you'll need additional data structures.

5. **Space-Time Tradeoff:** Resolving collisions, such as using separate chaining, can lead to increased memory usage, while methods like linear probing might result in performance tradeoffs.

6. **Deterministic Key Ordering:** In many cases, keys are stored and retrieved in an unpredictable order. This is typically fine for data retrieval but not suitable for applications requiring sorted data.

7. **Hash Table Initialization Overhead:** Depending on the implementation, hash tables can have initialization overhead, especially during resizing.

In summary, hash tables are powerful and efficient data structures for many use cases. However, they require careful consideration of the choice of hash function and the handling of collisions. By addressing these issues, many of the drawbacks can be mitigated. When used appropriately, hash tables are invaluable for fast data retrieval, data organization, and quick lookups in various computer science and software engineering applications.

### What are the most common use cases of hash tables ?
Hash tables are versatile data structures and find applications in a wide range of scenarios. Some of the most common use cases for hash tables include:

1. **Dictionaries:** Hash tables are often used to implement dictionaries, where keys map to values. This is a fundamental use case for storing and retrieving data efficiently.

2. **Caching:** Hash tables are suitable for caching frequently accessed data. By storing frequently used results in a hash table, you can avoid expensive calculations or database queries.

3. **Symbol Tables:** Compilers and interpreters use hash tables to manage variable and function names. They store the symbol (variable or function) names as keys and their corresponding attributes or memory locations as values.

4. **Data Deduplication:** Hash tables are used to identify and remove duplicate elements in a dataset. By hashing elements, you can quickly compare them to find duplicates.

5. **Database Indexing:** Databases use hash indexes to speed up data retrieval. This enables quick lookup of data based on key values.

6. **Cryptography:** Cryptographic hash functions are used to ensure data integrity. Hash tables can verify whether data has been tampered with.

7. **Counting Frequencies:** Hash tables can count the frequency of items in a dataset. They are useful for tasks like finding the most common words in a text document.

8. **Caching in Web Servers:** Web servers often use hash tables to store recently requested web pages, images, or database query results. This caching reduces server load and improves response times.

9. **Implementing Sets:** Hash tables can be used to implement sets, where you store a collection of unique items. This is useful for tasks like maintaining unique user IDs.

10. **Storing Configuration Settings:** Configuration settings for applications and systems can be stored in hash tables for efficient access.

11. **Implementing Object-Oriented Language Features:** Some object-oriented programming languages use hash tables to implement features like attribute lookup and method invocation.

12. **Routing Tables:** In networking, hash tables can be used to store routing information, enabling efficient packet forwarding decisions.

13. **Password Storage:** Hash tables store password hashes for authentication. This provides an additional layer of security, as plaintext passwords are not stored.

14. **Memoization:** Hash tables can be used to implement memoization in algorithms, which stores the results of expensive function calls for later reuse.

15. **Sparse Arrays:** Hash tables can be used to implement sparse arrays where elements are mostly empty or undefined. This saves memory compared to dense arrays.

16. **Frequency Analysis:** Hash tables can be used for frequency analysis in various applications, such as text processing, image processing, and signal analysis.

These are just a few examples of the many use cases for hash tables. Hash tables provide efficient data storage and retrieval, making them a fundamental data structure in computer science and software engineering. They are chosen for their fast lookup times and versatility in various problem domains.
