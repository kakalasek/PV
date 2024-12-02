"""
You can update an item inside a dictionary in about two ways. Of course you can only upate the value, not the key
"""
needs_update = {"a": 1, "b": 2}

print(f"This is the original dictionary: {needs_update}")

print()

print("We can update it using the 'key'='value' method")
needs_update["a"] = 32
print(f"The dict now looks like this: {needs_update}")

print()

print("The second way is using the update() method. It takes exactly one arguments, that is an iterable")
needs_update.update({"b": 75})
print(f"The dict now looks like this: {needs_update}")