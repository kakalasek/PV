"""
You cannot expand string without creating a new object, since it is unmutable. But if we dont consider that into account, you can use join() or +=
"""
unmutable_string = "YoYo"

print(f"This is the original string: {unmutable_string}")
print(f"This is the id of the string now: {id(unmutable_string)}")
print(f"We will now use += to append something to the string")
unmutable_string += "Nono"
print(f"This is the id after: {id(unmutable_string)}")
print(f"An this is the string: {unmutable_string}")