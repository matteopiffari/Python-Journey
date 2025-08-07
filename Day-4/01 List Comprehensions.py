# -----------------------------------
#       List Comprehensions:
# -----------------------------------

nums = [1, 2, 3, 4, 5]
squared = [x**2 for x in nums]          # List comprehension to square each number

fullZero = [0 for _ in range(10)]       # List comprehension to create a list of zeros

combs = [(x, y) for x in range(3) for y in range(3)]  # List comprehension for combinations

print(fullZero)
print(squared)
print(combs)