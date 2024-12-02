"""
Set is a bit special. It cannot contain certain collections. According to the error message, it is because of some hashing problem or smt. Yeah, I dont really care.
I am okay knowing just the fact, that it does not work.
"""
perfectly_fine_set = {("A tuple",),"A string"}
print(f"You can easily put a tuple or a string into a set: {perfectly_fine_set}")

print()

try:
    print("Now we will try to add a list .. see what happens")
    unperfectly_fine_set = {["A am a list"]}
except:
    print("Oopsie, an Exception has occured")

try:
    print("Now we will try to add a set .. see what happens")
    unperfectly_fine_set = {{"A am a set"}}
except:
    print("Oopsie, an Exception has occured again")

try:
    print("Now we will try to add a dict .. see what happens")
    unperfectly_fine_set = {{"a":"b"}}
except:
    print("Oopsie, an Exception has occured once more")