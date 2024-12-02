"""
Set has several methods to delete an item
"""
soon_to_be_gone = {"Do", "It", "Shoot", "Me"}

print(f"This is the set at the start: {soon_to_be_gone}")

print()

print("First method is to use the discard() method or the remove() method. They both take one argument, the element to remove. The only difference is that remove() throws and exception if the element is not in the set.")
soon_to_be_gone.discard("Do")
print(f"This is the set now: {soon_to_be_gone}")

print()

print("Second method is using the pop() method, which removes a random item from the set")
soon_to_be_gone.pop()
print(f"This is the set now: {soon_to_be_gone}")

print()

print("Last method is to use the clear() method. It simply clears the whole set")
soon_to_be_gone.clear()
print(f"This is the set now: {soon_to_be_gone}")
