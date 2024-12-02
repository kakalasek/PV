"""
You can get the third element inside a list using several methods
"""
some_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

print("Using the index")
print(f"Third element: {some_list[2]}")
print(f"Also the third element: {some_list[-len(some_list) + 2]}")