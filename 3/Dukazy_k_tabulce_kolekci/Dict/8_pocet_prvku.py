"""
The dictionary is a little different .. len() still works for the number of elements in the main dict, but if you also want to count the number of elements in
nested dicts, like in a json for example, you will need to create your own method. But in most cases, just use len()
"""
dct = {"a": "hello", "b": {"c": 1, "d": 2}}
print(f"This is the length of the dict .. it will be 2, because len() wont count the nested elements: {len(dct)}")