# -----------------------------------
#           Context Manager:
# -----------------------------------

# When we want to manage resources like files, network connections, or database connections, we can use context managers
# to ensure that these resources are properly managed and released when they are no longer needed.


def readFileWithoutContextManager(fileName):
    file = open(fileName, 'r')
    try:
        data = file.read()
    finally:
        file.close()
    return data


def readFile(fileName):
    with open(fileName, 'r') as file:   # Using 'with' statement to ensure the file is closed automatically
        data = file.read()
    return data


print(readFileWithoutContextManager('./file.txt'))
print(readFile('./file.txt'))