"""
Tuple does not really care which datatype his elements have, so naturally we can nest in it any collection we want
"""
t = ((1, 2), [1, ["hell", 23]], {"hell", 14, (23, 1)}, {"a": 12, "jecna": "hell"}, "hell")
print(t)