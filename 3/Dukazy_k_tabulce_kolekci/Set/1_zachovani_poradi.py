"""
Set is unordered, unindexed. Which means it does not really care when you put what in it, it just does its own thing
"""
s = {"hello", (1,2,3), 3, 12.34}
print(f"Set before adding an element: {s}")
s.add(("no problem", 342.11, None))
print(f"Set after adding an element: {s}")
print("\nIf the output is ordered as expected, it is just a coincidence, RUN IT AGAIN")