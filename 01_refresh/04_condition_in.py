number = 7
user_input = input("Please enter y, if would like to play: ").lower().strip()

if user_input == 'y':
    guess = int(input("Please enter your guess: "))
    if guess == number:
        print("Congratulations! You guessed the number correctly.")
    elif (number - guess) in (1,-1):
        print("Your were off by one")
    elif abs(number - guess) == 2:
        print("You were off by two")
    else:
        print("Sorry, you guessed wrong.")