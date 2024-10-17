class Node():
    """
    This class represent a single element inside a linked list 
    """

    def __init__(self, value, next):
        """
        Creates the node object, initializes default properties

        :param value: The value this Node holds
        :param next: Must be of type Node or None. The next Node this Node points to 
        """
        if not isinstance(next, Node) and next is not None:
            raise TypeError("Argument 'next' must be of type 'Node' or None")

        self._value = value 
        self._next = next

    @property
    def value(self):
        return self._value
    
    @value.setter
    def value(self, value):
        self._value = value

    @property
    def next(self):
        return self._next
    
    @next.setter
    def next(self, next):
        """
        Setter for the next Node

        :param next: Must be of type Node or None 
        """
        if not isinstance(next, Node) and next is not None:
            raise TypeError("Argument 'next' must be of type 'Node' or None")
        self._next = next

    def __str__(self):
        return str(self.value)
    
    def __repr__(self):
        return str(self.value)

class Stack():
    """
    This class represents a stack architecture using a signle direction connected list 
    """

    def __init__(self):
        """
        This is the class constructor. It initializes the Stack top to None and the Stack size to 0 
        """
        self._size = 0
        self._top = None

    def add(self, value):
        """
        This method adds an element onto the top of the stack

        :param value: Value to add to the top 
        """
        if self._top is None:
            self._size += 1
            self._top = Node(value, None)
        else:
            self._size += 1
            new_top = Node(value, self._top)
            self._top = new_top

    def pop(self):
        """
        This method removes an element from the top of the stack and returns it

        :return: The value of the top most element inside the Stack. Or None if the Stack is empty
        """
        if self._top is None:
            return None

        temp = self._top
        self._top = self._top.next
        self._size -= 1
        return temp

    def count(self):
        """
        This method returns the current number of elements inside the Stack 
        """
        return self._size

    def clear(self):
        """
        This method clears the entire Stack
        """
        self._top = None
        self._size = 0    

    def popAll(self):
        """
        This method returns all the elements inside the Stack

        :return: List of all elements from the Stack
        """
        output = []
        current = self.pop()
        print(current)
        while current is not None:
            output.append(current)
            current = self.pop()
        
        return output

    def __iter__(self):
        """
        This method returns the current number of elements inside the stack. It is NOT thread safe
        """
        self.current = self._top
        return self
    
    def __next__(self):
        """
        This method returns the next elementy inside an iteration 
        """
        if self.current == None:
            raise StopIteration

        temp: Node = self.current
        self.current: Node = self.current.next
        return temp

stk = Stack()
stk.add("Hello")
stk.add(11)
stk.add(21.11)
for item in stk:
    print(item)

print(stk.popAll())