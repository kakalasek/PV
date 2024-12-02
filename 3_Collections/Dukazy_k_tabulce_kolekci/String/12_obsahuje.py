"""
We can either simply use the "in" keyword. But you can also use find and count if you desire
"""
very_nice_string = "I am extraordinary nice"

print("First method is to use the 'in' keyword")
if "I am" in very_nice_string:
    print("'I am' is present in the string")

print()

print("Second method is to use the find() method. It can either take one argument, that is the substring to find, or you can specify start and end index to search")
if very_nice_string.find("extraordinary", 5, len(very_nice_string)-1):
    print("'extraordinary' is present in the string")

print()

print("The last method is to use the count() method. It works pretty much the same as the find() method. It just returns the number of occurences")
if very_nice_string.count("nice") > 0:
    print("'nice' is present in the string")