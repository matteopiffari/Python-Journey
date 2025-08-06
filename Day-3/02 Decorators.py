# -----------------------------------
#             Decorators:
# -----------------------------------

# Decorators are a way to modify or enhance functions or methods without changing their code.

def log(func):
    def wrapper(*args):
        print(f'Calling function: {func.__name__} with arguments: {args}')
        return func(*args)
    return wrapper

@log                        # This is equivalent to add = log(add)
def add(x, y):
    return x + y


print(add(5, 3))  # Calling the decorated function will log the call details


# More useful example: repeat a function multiple times

def repeat(n):
    def decorator(func):
        def wrapper():
            for _ in range(n):
                func()
        return wrapper
    return decorator

@repeat(5)
def printHi():
    print('Hi')

printHi()


# Even more useful example: auth required

from functools import wraps

user = {
    "username": "matteo", 
    "auth":True
}

def isAuth():
    return user["auth"]

def authReq(func):
    @wraps(func)                                    # This preserves the metadata of the original function (like its name and docstring, in this case `deleteAccount`)
    def wrapper(*args, **kwargs):                   # *args and **kwargs can be used to pass any number of arguments to the function (not necessary here, but useful in general)
        if isAuth():
            return func(*args, **kwargs)
        else:
            print("User not authenticated!")
    return wrapper


@authReq
def deleteAccount():
    print("Account deleted!")


deleteAccount()