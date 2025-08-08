import random

secretNumber=random.randint(1,50)
print("I am thinking of a number between 1 and 50.")

for guessTaken in range(1,7):
    guess=int(input("Guess the number: "))

    if guess < secretNumber:
        print("Your guess is too low.")
    elif guess > secretNumber:
        print("Your guess is too high.")
    else:
        break

if guess == secretNumber:
    print(f"Congratulations! You guessed the number righ in {guessTaken} tries!")
else:
    print(f"Sorry, the number I was thinking of was {secretNumber}.")
