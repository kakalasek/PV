"""
You can use the 'in' keyword to see if tuple contains a certain value. Second option is to use the 'count' function
"""
t = ((1,2), 'hello', 3.21)

if (1,2) in t:
    print("This tuple contains the value (1,2)")

print()

print("Now with the count() function")
if t.count('hello') > 0:
    print("This tuple contains the value 'hello'")