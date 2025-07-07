#This program greets the user and asks for their name.
print("Hello")
print("What is your name?")
myName=input()
print("Nice to meet you, " + myName)

#It then tell the user the length of their name based on the user input.
print("Your name has " + str(len(myName))+ " characters")

#It then asks for the user's age and tell them how old they are going to be in a year.
print("What is your age?")
myAge=input()
print("You will be "+ str(int(myAge)+1) + " in a year")