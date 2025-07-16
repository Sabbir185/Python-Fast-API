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


# list and tuple are ordered
# set is unordered

# list and set are mutable
# tuple is immutable, can not be changed after creation, not assignable

# set does not allow duplicates
# list allows duplicates
# tuple allows duplicates

# list and tuple are accessable by index
# set is not accessable by index, because it is unordered

# list -> append, remove, insert, pop
# tuple -> count, index
# set -> add, remove, discard, pop, clear -> no ending index, no duplicates