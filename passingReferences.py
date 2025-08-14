def eggs(someParameter):
    someParameter.append('Hello')

spam = [1, 2, 3]
eggs(spam)
print(spam)

# Output: [1, 2, 3, 'Hello']
# This shows that the list 'spam' was modified by the function 'eggs' because
# lists are mutable and passed by reference in Python.

