"""
So, you should not be able to add anything to a tuple. This little restriction can be bypassed .. kind of. Two tuples can be added together, but the resulting tuple will be a new object
"""
t1 = (1, 2)

print(f"This is t1 now: {t1}")
print(f"And its id: {id(t1)}")

t1 += (3,)

print(f"This is t1 after: {t1}")
print(f"And its new id: {id(t1)}")

print()

print("A tuple does not even have a method to add an element")
tuple_methods = []
for method in dir(tuple):
    if "__" not in method:
        tuple_methods.append(method)

print(f"Tuple methods: {tuple_methods}")

print()

try:
    print("If we try, to add an element using lets say +=, we get an exception")

    t1 += 2
except:
    print("See, we cant add an element to a tuple without changing it")