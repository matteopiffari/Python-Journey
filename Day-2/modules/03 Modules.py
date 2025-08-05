import myModule                         # Importing the custom module
# import math                           # Importing the math module
import math as m                        # Importing the math module with an alias
# from math import sqrt                 # Importing only the sqrt function from math module

def main():
    result = myModule.add(5, 10)
    print("The sum is:", result)
    print("The square root of 16 is:", m.sqrt(16))

if __name__ == "__main__":
    main()