
secret_number = 7
guess = 0

print("=== GUESS THE NUMBER ===")

while guess != secret_number:
    guess = int(input("Guess a number between 1 and 10: "))
    
    if guess > secret_number:
        print("Too high! Try again.")
    elif guess < secret_number:
        print("Too low! Try again.")
    else:
        print("🎉 Boom! You got it right.")