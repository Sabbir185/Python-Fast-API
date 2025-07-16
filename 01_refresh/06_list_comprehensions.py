numbers = [1,2,3,4,5]
doubled = []

for num in numbers:
    doubled.append(num * 2)

# Using list comprehension to achieve the same result
list_doubled = [num * 2 for num in numbers]

print(doubled)
print(list_doubled)


# Another example with conditions
friends = ["Alice", "Bob", "Charlie", "Boshir", "Dina"]
b_friends = []

for friend in friends:
    if friend.startswith("B"):
        b_friends.append(friend)

# Using list comprehension with a condition
b_friends_list = [friend for friend in friends if friend.startswith("B")]

print(b_friends)
print(b_friends_list)


# Note:
# List comprehensions are a concise way to create lists in Python.
# They can replace the need for a for loop in many cases, making the code cleaner and more readable.
# The syntax is: [expression for item in iterable if condition]
# where 'expression' is what you want to do with each item.
# list comprehensions create a new memory address for the new list.
