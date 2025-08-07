def power(n,p):
    return n ** p

n=int(input("Enter a number: "))
p=int(input("Enter the power:"))

try:
    x=power(n,p)
    print(f"The result of {n} raised to the power of {p} is: {x}")

except ValueError:
    print("Please enter valid integers for both the number and the power.")