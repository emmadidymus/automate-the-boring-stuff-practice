import sys

name = input("Enter your name: ")

while name != "Alice":
    name=input("Enter your name: ")
    if name == "exit":
        sys.exit()
    
password = input("Enter your password: ")

while password != "swordfish":
    password = input("Enter your password: ")
    if password == "exit":
        sys.exit()
print("Welcome, Alice!")


