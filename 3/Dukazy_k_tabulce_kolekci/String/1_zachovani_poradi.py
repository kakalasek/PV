"""
Simple answer is YES. String is immutable, so adding an object will create a new object, but as you can see, It will still be in order
"""
s = "Help me, please"
print(f"Heres is the original string: {s}\n And Id: {id(s)}")
s += "!"
print(f"Heres the new string: {s}\n And Id: {id(s)}")