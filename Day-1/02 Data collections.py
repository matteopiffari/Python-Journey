# -----------------------------------
#               List:
# -----------------------------------

#   A list is a collection of items that can be of different types and is mutable (can be changed).


myList = [1, 2, 3, "Hello", True]       # Example of a list

myList.append("New Item")               # Adding an item to the list
myList.insert(1, "Inserted Item")       # Inserting an item at a specific position
myList.remove(2)                        # Removing an item from the list

secondList = [4, 5, 6]                  # Another list
myList.extend(secondList)               # Extending the first list with the second list

print(myList)

myList.pop()                            # Removing the last item from the list
print(myList)

myList.reverse()                        # Reversing the order of the list
print(myList)

[print(item) for item in myList]        # Printing each item in the list using a list comprehension
print("\n")                             # Adding a newline for better readability
[print(item) for item in myList if isinstance(item, int)]  # Printing only integer items in the list

myList.clear()                          # Clearing the list
print(myList)



numList = [1, 4, 3, 2, 5]               # Example of a list of integers

numList.sort()                          # Sorting the list in ascending order
print(numList)

numList.sort(reverse=True)              # Sorting the list in descending order
print(numList)


numList2 = numList                      # Creating a second list that REFERENCES the first one DOES NOT create a copy
numList2[0] = 100                       # Changing the first item in the second list
print(numList)                          # This will also change the first item in the first list

numList3 = numList.copy()               # Creating a second list that is a COPY of the first one
numList3[0] = 200                       # Changing the first item in the second list
print(numList)                          # This will NOT change the first item in the first list



# -----------------------------------
#               Tuple:
# -----------------------------------

#   A tuple is similar to a list, but it is immutable (cannot be changed).

myTuple = (1, 2, 3, "Hello", True)  # Example of a tuple
myTuple2 = ("World", 5)

if ("Hello" in myTuple):            # Checking if an item is in the tuple
    print("Hello is in the tuple")

(x, *y) = myTuple                   # Unpacking the tuple into variables, y will contain the rest of the items
print(x)                            # Printing the first item
print(y)                            # Printing the rest of the items

print(myTuple + myTuple2)           # Concatenating two tuples

print(myTuple.count("Hello"))       # Counting the occurrences of "Hello" in the tuple
print(myTuple.index("Hello"))       # Finding the index of "Hello" in the tuple



# -----------------------------------
#               Set:
# -----------------------------------

#   A set is a collection of unique items and is unordered.

mySet = {1, 2, 3, "Hello", True}    # Example of a set
mySet2 = {3, 4, 5, 6}

mySet3 = mySet.union(mySet2)        # Creating a new set that is the union of two sets
mySet4 = mySet.intersection(mySet2) # Creating a new set that is the intersection of two sets
mySet5 = mySet.difference(mySet2)   # Creating a new set that is the difference of two sets
mySet6 = mySet.symmetric_difference(mySet2)  # Creating a new set that is the symmetric difference of two sets

mySet.add("New Item")               # Adding an item to the set
mySet.remove(2)                     # Removing an item from the set

mySet.update(mySet2)                # Adding items from another set to the first set
mySet.discard("Hello")              # Removing an item from the set, does not raise an error if the item is not found

mySet.intersection_update(mySet2)   # Keeping only items that are in both sets

mySet2.symmetric_difference_update(mySet)  # Keeping items that are in either set, but not both

print(mySet)                        # Printing the set, every item will be unique
print("Hello" in mySet)             # Checking if "Hello" is in the set



# -----------------------------------
#           Dictionary:
# -----------------------------------

#   A dictionary is a collection of key-value pairs, where each key is unique and maps to a value.

myDict = {
    "name": "John",
    "age": 30,
    "is_student": False
}

myDict2 = myDict.copy()             # Creating a copy of the original dictionary

myDict["city"] = "New York"         # Adding a new key-value pair to the dictionary
myDict["name"] = "Jane"             # Updating an existing key-value pair in the dictionary

myDict.update({"height": 175})      # Adding multiple key-value pairs
myDict.update({"age": 31})          # Updating the dictionary with another dictionary

myDict.pop("is_student")            # Removing a key-value pair from the dictionary
myDict.popitem()                    # Removing the last inserted key-value pair from the dictionary

print(myDict)                       # Printing the entire dictionary
print(myDict["name"])               # Accessing a value by its key, raises an error if the key does not exist
print(myDict.get("age"))            # Accessing a value using the get method, returns None if the key does not exist
print(myDict.get("country", "Not Found"))  # Accessing a value with a default value if the key does not exist

print(myDict.keys())                # Getting all keys in the dictionary
print(myDict.values())              # Getting all values in the dictionary
print(myDict.items())               # Getting all key-value pairs in the dictionary

print("name" in myDict)             # Checking if a key exists in the dictionary

for key, value in myDict.items():   # Iterating over key-value pairs in the dictionary
    print(key, value)