# -----------------------------------
#               Arrays:
# -----------------------------------

import array as arr

# arr.array(type, list)
#   Types:  Code    Type            Bytes       
#
#       -   i       int             2/4         Signed      --> int
#       -   I       int             2/4         Unsigned    --> int
#       -   u       unicode char    2
#       -   h       int             2           Signed      --> Short int
#       -   H       int             2           Unsigned    --> Short int
#       -   l       int             4           Signed
#       -   L       int             4           Unsigned
#       -   f       float           4
#       -   d       float           8

myArray = arr.array('i', [1,2,3,4,5])
myArray.append(6)                           # Insert an element at the end
myArray.insert(6,7)                         # Insert an element at the given index (index, element)
myArray.pop()                               # Remove the last element
myArray.pop(0)                              # Remove the element at the given index
myArray.remove(2)                           # Remove the given element

myArray2 = arr.array('i', [8,9,10])
mergedArray = myArray + myArray2            # Merge two or more arrays

print(myArray)
print(myArray[0])
print(mergedArray)


# -----------------------------------
#            Linked List:
# -----------------------------------

from collections import deque

linkedList = deque([1,2,3,4,5])
linkedList.append(6)                    # Insert an element at the end
linkedList.appendleft(0)                # Insert an element at the begin

print(linkedList)

linkedList.pop()                        # Remove an element at the end
linkedList.popleft()                    # Remove an element at the begin

linkedList2 = deque('hello')
linkedList.extend(linkedList2)          # Extend the list (there is also extendleft)

print(linkedList)
print(linkedList[0])


# -----------------------------------
#            Binary tree:
# -----------------------------------

#        1
#       / \
#      2   3
#     / \ / \
#    4  5 6  7
#

# Each element is an object (leaf) with a left ands right child that points to another leaf


# -----------------------------------
#            Hash tables:
# -----------------------------------

# A hash table is a data structure that implements an associative array abstract data type, a structure that can map keys to values.
# In Python, dictionaries are implemented as hash tables.

cityMap = {
    'New York': 'USA',
    'Tokyo': 'Japan',
    'London': 'UK',
    'Milan': 'Italy'
}

# The complexity of a dictionary is O(1) for search, insert and delete operations on average.
# When you search for a key, Python computes a hash value for the key and uses it to find the corresponding value in the hash table.

print(cityMap['New York'])  # Accessing a value by key
print(cityMap.get('Tokyo'))  # Accessing a value by key with get() method

# Adding a new key-value pair
cityMap['Berlin'] = 'Germany'

# Removing a key-value pair
del cityMap['London']

print(cityMap)