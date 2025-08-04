# --------------------------
#           Types
# --------------------------

var = "Hello World"     # String
var = 10                # Integer
var = 10.5              # Float
var = True              # Boolean
var = None              # Null
var = [1, 2, 3]         # List
var = (1, 2, 3)         # Tuple
var = {1, 2, 3}         # Set
var = {"key": "value"}  # Dictionary
var = range(10)         # Range

type(var)               # Check the type of the variable

if type(var) == range:
    print("The variable is a range")

var = 10
# v-ar NO
# 2var NO

# Variables with different values
var2, var3 = 20, 30

# Variables with the same value
var4 = var5 = 40


cities = ["Milano", "Bergamo"]
city1, city2 = cities


# Casting
var = "10"          # String
var = int(var)      # Convert to Integer


# --------------------------
#          Strings
# --------------------------


string = "Hello"        # Simple String
var = """HELLO
Hello
hello"""                # Multiline String

for char in "Hello world":
    print(char)             # Print each character of the string

print("Hello " * 3)         # Print "Hello" three times

print(string[::-1])         # Print the string in reverse
print(string[:3])
print(string[2:])           # Print characters from position 2 to the end
print(string[1:4])          # Print characters from position 1 to 3
print(string[-1])           # Print the last character of the string


# String methods
string = "Hello World"
string = string.replace("World", "Python")  # Replace "World" with "Python"
string = string.upper()                     # Convert the string to uppercase
string = string.lower()                     # Convert the string to lowercase
string = string.capitalize()                # Capitalize the first letter
string = string.title()                     # Capitalize the first letter of each word
string = string.strip()                     # Remove whitespace from the beginning and end
string2 = string.split()                    # Split the string into a list of words
string = string.split(",")                  # Split the string into a list of words using the comma as a separator

# Formatting strings
name = "Mario"
surname = "Rossi"

print(f"My name is {name} and my surname is {surname}")                 # Formatting with f-string
print("My name is {} and my surname is {}".format(name, surname))
print("My name is %s and my surname is %s" % (name, surname))           # Formatting with %
print("My name is {0} and my surname is {1}".format(name, surname))     # Formatting with format



# --------------------------
#         Booleans
# --------------------------

bool_var = True         # Boolean true
bool_var = False        # Boolean false

# If I want to check if something is empty or not, I can use bool()
bool(0)                 # False
bool(None)              # False
bool([])                # False
bool("")                # False

bool(1)                 # True
bool(" ")               # True (a string with a space is not empty)
bool([1, 2, 3])         # True
bool("hello")           # True


cash = 1000

if not(cash):
    print("No money!")
else:
    print("Cash available!")


# --------------------------
#         Operators
# --------------------------

# Arithmetic Operators
a = 10
b = 5

sum_result = a + b          # Addition
sub_result = a - b          # Subtraction
mul_result = a * b          # Multiplication
div_result = a / b          # Division
mod_result = a % b          # Modulus
exp_result = a ** b         # Exponentiation
floor_div_result = a // b   # Floor Division (return the largest integer less than or equal to the division result)

# Methods

x = min(1, 2, 3)            # Minimum value
y = max(1, 2, 3)            # Maximum value
abs_value = abs(-10)        # Absolute value
round_value = round(10.5)   # Round to the nearest integer
p = pow(2, 3)               # Power (2 raised to the power of 3)


# --------------------------
#       IF Statements
# --------------------------

x = 10

if(5 <= x <= 15):                       # Check if x is between 5 and 15
    print("x is between 5 and 15")
elif (x < 5):
    print("x is less than 5")
else:
    print("x is greater than 15")


# --------------------------
#          Loops
# --------------------------

cities = ["Milano", "Bergamo", "Roma"]

for city in cities:                     # For loop
    print(city)

for i in range(len(cities)):            # For loop with range
    print(cities[i])

i = 0
while i < len(cities):                  # While loop
    print(cities[i])
    i += 1

# --------------------------
#         Exceptions
# --------------------------

try:
    print(cities[3])
except IndexError:
    print("City not found!")

try:
    print(cities[3])
except IndexError as e:
    print(f"Error: {e}")

try:
    print(cities[3])
except Exception as e:
    print(f"Error: {e}")

try:
    raise Exception("Custom error message")
except Exception as e:
    print(f"Error: {e}")
finally:
    print("This block is always executed, even if there is an error")