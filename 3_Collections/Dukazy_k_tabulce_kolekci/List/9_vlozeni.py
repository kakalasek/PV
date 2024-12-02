"""
List is a lot more welcoming than tuples. You even have several methods to add an element.
"""
lst = [1]

print(f"This is how the list looks at the beginning: {lst}")

print()

print(f"First method is to use append(). Append() accepts one argument, which is the object to add to the list")
lst.append("1")
print(f"The list now looks like this: {lst}")

print()

print(f"Second method is to use extend(). Extend() accepts one argument, which is an iterable. The elements from the iterable will be appended to the list")
lst.extend("Hello")
print(f"The list now looks like this: {lst}")

print()

print(f"Third way is to use insert. Insert() takes two arguments. An index, before which to add an object, and the object to be inserted")
lst.insert(0, "No way")
print(f"The list now looks like this: {lst}")

print()

print(f"The last way is to use +=. The object on the right needs to be an iterable")
lst += ["N", "o", "n", "e"]
print(f"The list now looks like this: {lst}")