x=int(input("How many times do you want the message to be printend? "))

y=input("What message do you want to print? ")

for i in range(x):
    print(y + '(' + str(i) + ')')

# This code takes user input for the number of times to print a message and the message itself.
# It then uses a for loop to print the message the specified number of times, appending
# the current iteration index `i` in parentheses after the message.
# The output will be the message followed by the iteration index, e.g.:
# If the user inputs 5 for the number of times and "Hello" for the message,
# the output will be:   
# Hello (0)
# Hello (1)
# Hello (2)
# Hello (3)
# Hello (4)
