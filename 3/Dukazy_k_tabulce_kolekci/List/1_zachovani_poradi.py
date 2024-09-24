"""
If we simply add to a list using append() without doing any crazy ass stuff, elements just gets appended to the end, without breaking the order
"""
l = [{1, 2, "Hello"}, 3, "space", 123.33]
print(f"List before appending an element: {l}")
l.append("No please no")
print(f"List after appending and element: {l}")