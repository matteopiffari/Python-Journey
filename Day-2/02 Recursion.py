# -----------------------------------
#             Recursion:
# -----------------------------------

from sys import getrecursionlimit
from sys import setrecursionlimit

setrecursionlimit(500)                  # Set the recursion limit
print(getrecursionlimit())              # Get the recursion limit

def recursiveFunction(x):
    print(x)
    if x == 0:
        return 'End'
    return recursiveFunction(x-1)       #cWithout the "return", the return value ("End") does not propagate to the previous functions


print(recursiveFunction(10))