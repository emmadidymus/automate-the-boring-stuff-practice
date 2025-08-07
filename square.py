def double(n):
    return n ** 2
try:
    x=double(int(input("Enter a number: ")))
    print(f"The square of the number is: {x}")

except ValueError:
    print("Please enter a valid integer.")



