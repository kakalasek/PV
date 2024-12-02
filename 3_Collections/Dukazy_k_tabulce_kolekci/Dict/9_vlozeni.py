"""
You can add an element to dict no problem
"""
d = {}

print(f"This is an empty dict: {d}")

print()

print("First method is to use 'key'='value'")
d['a'] = 1
print(f'This is the dict now: {d}')

print()

print("Second method is to use update(). It takes one argument, which should be a dict")
d.update({1:2})
print(f'This is the dict now: {d}')