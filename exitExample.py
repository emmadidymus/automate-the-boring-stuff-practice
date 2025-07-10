import sys

while True:
    print("Type exit to exit the program.")
    response = input()

    if response == "exit":
        sys.exit()
    print('You typed '  + response + '.')

# This code will run until the user types "exit", at which point it will terminate the program.
# The sys.exit() function is used to exit the program gracefully.
