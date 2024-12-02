class LockedDoorsException(Exception):
    pass

class Doors():
    def __init__(self, locked: bool):
        if not isinstance(locked, bool):
            raise TypeError("The 'locked' attribute must be a boolean")
        self.locked = locked
        self.opened = False

    def open(self) -> None:
        if self.locked:
            raise LockedDoorsException
        self.opened = True

    def is_open(self) -> bool:
        return self.opened

d = Doors(locked=True)
try:
    d.open()
    print("I have .. come")
except LockedDoorsException as e:
    print("Doors are locked, you cant open them")
except TypeError as e:
    print(e)
finally:
    print("You have successfuly arrived on the other side of the door") if d.is_open() else print("You have not been able to open the door")