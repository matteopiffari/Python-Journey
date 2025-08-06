# -----------------------------------
#        Regular Expressions:
# -----------------------------------

# Code      Meaning
 
# \w        Matches any alphanumeric character (equivalent to [a-zA-Z0-9_])
# \d        Matches any digit (equivalent to [0-9])
# \s        Matches any whitespace character (spaces, tabs, newlines)
# .         Matches any character except a newline
# ^         Matches the start of a string
# $         Matches the end of a string
# *         Matches 0 or more repetitions of the preceding pattern
# +         Matches 1 or more repetitions of the preceding pattern
# ?         Matches 0 or 1 repetition of the preceding pattern
# {n}       Matches exactly n repetitions of the preceding pattern
# {n,}      Matches n or more repetitions of the preceding pattern
# {n,m}     Matches between n and m repetitions of the preceding pattern
# [abc]     Matches any single character a, b, or c
# [^abc]    Matches any single character not a, b, or c
# ()()      Groups patterns together and captures the matched text
# |         Acts as a logical OR between patterns
# \         Escapes a special character to match it literally

import re

string = "Hello world! This is a test string with some numbers: 12345 and special characters: @#$%^&*()"

# Find all words in the string
words = re.findall(r'\w+', string)
print("Words:", words)

# Find all numbers in the string
numbers = re.findall(r'\d+', string)
print("Numbers:", numbers)

# Find all special characters in the string
special_characters = re.findall(r'[^\w\s]', string)
print("Special Characters:", special_characters)

# Extract email addresses from a string
email_string = "Contact us at support@example.com for assistance."
email = re.search(r'([\w]+)@([\w]+)', email_string)

if email:
    print('Username:', email.group(1))
    print('Domain:', email.group(2))
else:
    print("No email found in the string.")