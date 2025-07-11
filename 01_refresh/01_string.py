# f string
name = "Sabbir"
greeting = f"Hello, {name}!"  # f string

print(greeting)

# template string .format()
name2 = "Morning"
greeting2 = "Good, {}!"

with_name2 = greeting2.format(name2)
print(with_name2)

print("Thi is {}{}".format("cool", " right?"))