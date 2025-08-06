# -----------------------------------
#              Lambdas:
# -----------------------------------

# Lambdas are anonymous functions defined with the `lambda` keyword.
# They can take any number of arguments but can only have one expression.

def add(x, y):
    return x + y

addLambda = lambda x, y: x + y                      # Equivalent to the add function above

addResult = add(5, 3)                               # Call the regular function  
addLambdaResult = addLambda(5, 3)                   # Call the lambda function

print(f"Function result: {addResult}")              # Output: Function result: 8
print(f"Lambda result: {addLambdaResult}")          # Output: Lambda result: 8




printFullName = lambda firstName, lastName: f"{firstName} {lastName}"  # Lambda to concatenate first and last name
print(f"Full name: {printFullName('John', 'Doe')}")  # Output: Full name: John Doe




listOfNumbers = [1, 2, 3, 4, 5]
squaredNumbers = list(map(lambda x: x ** 2, listOfNumbers))             # Using lambda with map to square each number
print(f"Squared numbers: {squaredNumbers}")