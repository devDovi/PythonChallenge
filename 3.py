import re

f = open('equality.txt', 'r')
data = f.read()

pattern = re.compile('''
    [^A-Z]    # any character except a capital letter
    [A-Z]{3}  # three capital letters
    (         # the beginning of a capturing group
    [a-z]     # one lowercase letter 
    )         # the end of the group
    [A-Z]{3}  # three capital letters
    [^A-Z]    # any character except a capital letter
    ''', re.VERBOSE)

print(re.findall(pattern, data))
#linkedlist