"""
There are a few methos you can use to append an element to a set. I only list those methods which do not create a new object
"""
s = {1, 2, 3}

print(f"This is the original set: {s}")

print()

print(f"First options is to use add(). Add() takes one argument, which is the element we want to add")
s.add((1, 2))
print(id(s))
print(f"This is how the set looks now: {s}")

print()

print(f"Second options is to use update(). Update() takes a list of iterables as an argument")
s.update([6, 3, 8], [1,2,4])
print(f"This is how the set looks now: {s}")