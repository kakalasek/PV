"""
The easiest way to get the third element inside tuple is to use and index
"""
t = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)

print(f"This is the third element: {t[2]}")
print(f"This is also the third element: {t[-len(t)+2]}")