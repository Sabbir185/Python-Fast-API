number = 7

while True:
    user_input = input("Would you like to play? (Y/n): ").lower().strip()

    if user_input == 'n':
        print("Thank you!")
        break

    guess = int(input("Please enter your guess: "))
    if guess == number:
        print("Congratulations! You guessed the number correctly.")
        break
    elif (number - guess) in (1,-1):
        print("Your were off by one")
    elif abs(number - guess) == 2:
        print("You were off by two")
    else:
        print("Sorry, you guessed wrong.")



nums = [1, 2, 3, 4, 5]
total = 0
count = len(nums)

for num in nums:
    total += num

# alternative way to calculate total
for i in range(len(nums)):
    total += nums[i]

print(f"The total is: {total}")
print(f"The average is: {total / count if count > 0 else 0}")
print("The total is: {}".format(sum(nums)))