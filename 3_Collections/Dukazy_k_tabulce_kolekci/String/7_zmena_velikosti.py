"""
String is a bit different. On first glance, it can be expanded .. but if you look closer, you'll find something terriffying. It is not the same object anymore ..
"""
obese_string = "I am obese"
print(f"This is the length of the string before: {len(obese_string)}")
print(f"This is the id of that string: {id(obese_string)}")
print()

obese_string += ". Now I am even more thicc"

print(f"This is the lenth of the string after: {len(obese_string)}")
print(f"But this is the new id: {id(obese_string)}")
