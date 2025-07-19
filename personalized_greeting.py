def greet_user(name,age):
    print("Hello, " + name + "!")
    print("You will be " + str(age+1)+ " years old in one year.")

try:
    name=input("Please enter your name: ")
    age=int(input("Please enter your age: "))
    greet_user(name,age)
except ValueError:
    print("Error: Please enter a valid age.")