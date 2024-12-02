"""
You cannot really remove anything from a string, because it is immutable. But if we dont consider the fact, that we are creating a new object, methods like replace() can be used
"""
hard_string = 'I am really tuff'

print("Without creating a new object, we cant remove anything from string")
print(f"This is the original string: {hard_string}")
print(f"This is its id: {id(hard_string)}")
hard_string = hard_string.replace('a', '')
print(f"This is the string after using replace(): {hard_string}")
print(f"And this is its new id: {id(hard_string)}")