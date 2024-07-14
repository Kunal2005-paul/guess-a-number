import random
from art import logo

print(logo)
print("Welcome to the number guessing game!\nI'am thinking of a number between 1 to 100.")


mode = input("Choose a difficulty. Type 'easy' or 'hard': ")

# getting a random whole number between 1 to 100
answer = random.randint(1,100)
# print(answer)

# according to difficulty level initiating attempts
if mode.lower() == "easy":
    chance = 10
else:
    chance = 5


#   initiating i for iterate attempts
i = 0
while i < chance:
    print(f"You have {chance-i} attempts remaining to guess the number.")
    guess = int(input("Enter your guess: "))
    if guess == answer:
        print(f"You got it! The answer is {answer}.")
        break
    elif chance-i == 1:
        print("You loose.")
    elif guess > answer:
        print("Too high.\nGuess again.")
    elif guess < answer:
        print("Too low.\nGuess again.")
    i += 1