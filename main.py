import random

print("Welcome to the number guessing game")

number = random.randint(1, 10)

tries = 0
max_attempts = 3

while tries < max_attempts:
    
    guess = input("eter your guess between 1 to 10: \n")
    
    if guess == number:
        print("you guess correctly")
        break
    else:
        tries += 1
        remaining_tries = max_attempts - tries
        print(f"you have {remaining_tries} tries remaining")
        
        if tries == max_attempts:
            print(f"game over, the number was {number}")

