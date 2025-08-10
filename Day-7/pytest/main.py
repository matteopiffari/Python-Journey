def func(something):
    if type(something) is str:
        return "String"
    elif type(something) is int:
        return "Integer"
    elif type(something) is float:
        return "Float"
    else:
        return "Unknown"

def divide(a, b):
    if b == 0:
        raise ZeroDivisionError("Division by zero error")
    return a / b


users = {}

def addUser(email, password):
    if email in users:
        raise ValueError("User already exists")
    users[email] = password
    return "User added successfully"