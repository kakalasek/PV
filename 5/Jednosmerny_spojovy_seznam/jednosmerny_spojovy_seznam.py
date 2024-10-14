class Node():
    def __init__(self, value, next):
        self.value = value 
        self.next = next

    def set_value(self, value) -> None:
        self.value = value

    def set_next(self, next) -> None:
        if not isinstance(next, Node):
            raise TypeError("Argument 'next' must be of type 'Node'")
        self.next = next

    def __str__(self):
        return str(self.value)

class Linked_list():
    def __init__(self):
        self.size = 0
        self.head = None

    def add(self, value):
        if self.head == None:
            self.size += 1
            self.head = Node(value, None)
        else:
            self.size += 1
            new_head = Node(value, self.head)
            self.head = new_head

    def remove(self, index):
        if index >= self.size or index < 0:
            raise IndexError("Index is out of range")
        if index == 0:
            self.head = self.head.next
        else:
            current = self.get(index-1)
            current.next = current.next.next if current.next is not None else None
        
        
    def get(self, index):
        if index >= self.size or index < 0:
            raise IndexError("Index is out of range")
        current = self.head
        for index in range(0, index):
            current = current.next
        return current

    def __iter__(self):
        self.current = self.head
        return self
    
    def __next__(self):
        if self.current == None:
            raise StopIteration

        temp: Node = self.current
        self.current: Node = self.current.next
        return temp
    
ls = Linked_list()
ls.add(1)
ls.add("Hello")
ls.add(1.1)
ls.add(True)
ls.add(["hello"])
for item in ls:
    print(item)

ls.remove(0)
print()

for item in ls:
    print(item)