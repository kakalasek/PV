class LockedDoorsException(Exception):
    pass

class Doors():
    

d = Doors(locked=True)
try:
    d.open()
    print("I have .. come")
except LockedDoorsException as e:
    print("Doors are locked, you cant open them")