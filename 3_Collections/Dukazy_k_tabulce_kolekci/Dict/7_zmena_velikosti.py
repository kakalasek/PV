"""
Dictionary in python, unlike a physical dictionary, can expand. Ducktaping new pages does not count
"""
big_dictionary = {"a": 12}
print(f"The size of the dict before: {len(big_dictionary)}")
big_dictionary["b"] = 32
print(f"The size of the dict after: {len(big_dictionary)}")