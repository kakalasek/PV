"""
You can remove an item from a dict pretty easily with several methods
"""
original_dict = {"a": 12, "b": "a", 123.44: 'No', (1,2):(1,1)}

print(f"This is the original dict: {original_dict}")

print()

print(f"You can remove an element using the pop() method. It accepts the key of the element and optionally a defaultvalue which to return, if the specified item was not found. If not specified, it throws an exception.")
original_dict.pop("a", "Item not found")
print(f"This is the dict now: {original_dict}")

print()

print(f"Another option is to use popitem(). It simply removes the last inserted element and returns it")
original_dict.popitem()
print(f"This is the dict now: {original_dict}")

print()

print(f"You can also use the 'del' keyword like this")
del original_dict["b"]
print(f"This is the dict now: {original_dict}")

print()

print(f"Lastly we can use the clear() method, which clears the whole dict")
original_dict.clear()
print(f"This is the dict now: {original_dict}")