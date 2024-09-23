"""
Since we cannot add any new elements into a tuple, we are the ones who decide, wheter they will be in order or not
"""
t_ordered_numbers = (1, 2, 3, 4, 5)
t_ordered_strings = ("apple", "banana")
print(f"Ordered tuple with numbers: {t_ordered_numbers}")
print(f"Ordered tuple (kind of) with strings: {t_ordered_strings}")
t_unordered = (12, "hello", 3)
print(f"Unordered tuple: {t_unordered}")
