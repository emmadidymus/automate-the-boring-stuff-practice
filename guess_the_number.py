import random

random_number = random.randint(1, 100)
attempts = 0

while True:
    guess = int(input("Guess a number between 1 and 100: "))
    attempts += 1
    if guess == random_number:
        print(f"Congratulations! You've guessed the number {random_number} in {attempts} attempts.")
        break
    elif guess < random_number:
        print("Too low! Try again.")
    else:
        print("Too high! Try again.")