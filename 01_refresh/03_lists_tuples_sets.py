l = ["a","b","c"]

t = ("x","y","z")

s = {"a", "b","c"}
# key_value = {"a": 2, "b": 4,"c": 10}

print(l)
print(t)
print(s)

l.append("d")
l.remove("a")
print(l)

print(t[2])

# t.append("d")  # This will raise an error because tuples are immutable
# t.remove("a")  # This will also raise an error for the same reason

s.add("d")
s.add("d")
s.remove("a")

print(s)
