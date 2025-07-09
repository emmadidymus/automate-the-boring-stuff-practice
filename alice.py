name=input("Waht is your name?")
age=int(input("What is your age?"))

if name == "Alice":
    print("Hello Alice, welcome back!")
elif age < 12:
    print("You are not Alice Kiddo, go away!")
elif age > 2000:
    print("Sorry, you are not Alice, you are either a time traveller or a ghost!")
elif age > 100:
    print("Sorry, you are too old to be Alice!")
else:
    print("You are neither Alice nor a kid, you are just a normal person.")