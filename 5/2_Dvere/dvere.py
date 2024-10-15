class LockedDoorsException(Exception):
    pass

class Doors():
    def __init__(self, locked: bool):
        if not isinstance(locked, bool):
            raise TypeError("The 'locked' attribute must be a boolean")
        self.locked = locked
        self.is_open = False

    def open(self) -> None:
        if self.locked:
            raise LockedDoorsException
        self.is_open = True

d = Doors(locked=True)
try:
    d.open()
    print("I have .. come")
except LockedDoorsException as e:
    print("Doors are locked, you cant open them")
except TypeError as e:
    print(e)