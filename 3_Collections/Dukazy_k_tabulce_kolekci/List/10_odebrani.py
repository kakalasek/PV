"""
There are several methods to remove an element from a list
"""
is_about_to_be_destroyed = ["No", "Please no", "Dont remove me", "I have kids", "Dont do it"]

print(f"This is the list at the beggining: {is_about_to_be_destroyed}")

print()

print("First option is to use the del keyword. It can also delete the entire list, if you dont specify the index")
del is_about_to_be_destroyed[-1]
print(f"This is the list now: {is_about_to_be_destroyed}")

print()


print("Second option is to use the remove() method. It takes one argument, which is the element to be removed")
is_about_to_be_destroyed.remove("I have kids")
print(f"This is the list now: {is_about_to_be_destroyed}")

print()

print("The next option is pop(). Pop() has one argument, an index of an element. If no index is specified, it removes the last item")
is_about_to_be_destroyed.pop(-1)
print(f"This is the list now: {is_about_to_be_destroyed}")

print()

print("The last option is the clear() method. It completely empites the list")
is_about_to_be_destroyed.clear()
print(f"This is the list now: {is_about_to_be_destroyed}")