while True:
    print("Who are you?")
    name=input()
    
    if name != 'Joe':
        continue
    print("Hello, Joe! What is the password? (It is a fish)")
    password=input()
    if password == 'swordfish':
        break
print("Access granted.")
# This code will keep asking for the name until 'Joe' is entered, then it will ask for the password.
# If the password is 'Swordfish', it will print "Access granted." and exit the loop.
# If the name is not 'Joe', it will continue to ask for the name.   
# If the password is incorrect, it will not break the loop and will continue to ask for the password.
# This is a simple authentication loop that demonstrates the use of `continue` and `break`
# statements in Python.
# The loop will run indefinitely until the correct name and password are provided.
