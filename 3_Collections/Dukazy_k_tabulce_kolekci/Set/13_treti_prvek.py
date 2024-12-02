"""
The set is unindexed, so we will use method to iterate over the set and find the third value. It will also most probably be always different
"""
sst = {"hello", "there", 3.12, (3, 1), "no way", 4}

print("We need to write ourselves a simple loop to get the current third element")

count = 0

for element in sst:
    count += 1
    if count == 3:
        print(f"The third element: {element}")
        break