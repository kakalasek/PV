"""
We will need to write our little method to acces the third element. Since dict is not indexed, but uses keys 
"""
r2_d2 = {"I": "A", "A":"I", "Chat": "Sucks"}

count = 0

for key,value in r2_d2.items():
    count += 1
    if count == 3:
        print(f"This is the third element: {key}:{value}")