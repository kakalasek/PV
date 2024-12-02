"""
So basically .. dictionary is a very bad parent and does not really care, what its values are doing. So they naturally be whatever they want, including any of the collections.
But it puts some restrictions on its keys. They can be a list, set or another dict. Let me prove you that
"""
a_completely_valid_dictionary = {("I am a tuple key",):("I am a tuple value",),
                                 "I cannot be a list key":["I am a list value"], 
                                 "I cannost be a set key":{"I am a set value"},
                                 "I cannot be dict key":{"I am": "A dict value"},
                                 "I am a string key":"I am a string value"}

print("This is a completely valid dictionary. It literally speaks for itself:")

for key, value in a_completely_valid_dictionary.items():
    print(key, value)

print()

print("Now comes the fun part, breaking stuff.")

try:
    print("Trying to put a list as a key")
    not_a_valid_dictionary = {["I am list key"]: "This wont work"}
except:
    print("An exception was thrown .. which means, it did not work")

print()

try:
    print("Trying to put a set as a key")
    not_a_valid_dictionary_vol_2 = {{"I am a set key"}: "This wont work either"}
except:
    print("An exception was thrown .. which means, this did not work either")

print()

try:
    print("Trying to put a dict as a key")
    not_a_valid_dictionary_vol_3 = {{"I am": "A dict key"}: "Still not working"}
except:

    print("An exception was thrown .. which means, its still not working")
