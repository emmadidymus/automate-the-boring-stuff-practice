def collatz(number):
    if number % 2 == 0:
        result = number // 2
    elif number % 2 == 1:
        result = 3 * number + 1
    print(result)
    return result

while True:
    try:
      collatz_number = int(input("Enter a number: "))
      break
    except ValueError:
      print("Please enter a valid integer.")

while collatz_number != 1:
    collatz_number = collatz(collatz_number)