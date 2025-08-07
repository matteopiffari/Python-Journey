# -----------------------------------
#       Generator Expressions:
# -----------------------------------

# To pause a function midway and resume from where the function was paused, you use the 'yield' statement.
# When a function contains at least one yield statement, it’s a generator function.

def message():
    print("Hello")
    yield 1
    print("World")
    yield 2
    print("Goodbye")
    yield 3


message_gen = message()
print(next(message_gen))  # Output: Hello
print(next(message_gen))  # Output: World
print(next(message_gen))  # Output: Goodbye

# -----------------------------------------------------------

def squares(num):
    for i in range(num):
        yield i * i

squares_gen = squares(5)

s = [next(squares_gen) for _ in range(5)]
print(s)  # Output: [0, 1, 4, 9, 16]

# We can also write the s list comprehension as a generator expression:

squares_gen_exp = (i * i for i in range(5))
for square in squares_gen_exp:
    print(square)  # Output: 0, 1, 4, 9, 16
