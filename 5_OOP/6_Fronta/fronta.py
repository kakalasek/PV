class Node():    
    """
    This class represent a single element inside a linked list 
    """

    def __init__(self, value, next, previous):
        """
        Creates the node object, initializes default properties

        :param value: The value this Node holds
        :param next: Must be of type Node or None. The next Node this Node points to 
        """
        if not isinstance(next, Node) and next is not None:
            raise TypeError("Argument 'next' must be of type 'Node' or None")

        if not isinstance(previous, Node) and previous is not None:
            raise TypeError("Argument 'next' must be of type 'Node' or None")

        self._value = value 
        self._next = next
        self._previous = previous

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

    @property
    def previous(self):
        return self._previous
    
    @previous.setter
    def previous(self, previous):
        """
        Setter for the previous Node

        :param previous: Must be of type Node or None 
        """
        if not isinstance(previous, Node) and previous is not None:
            raise TypeError("Argument 'previous' must be of type 'Node' or None")

        self._previous = previous

    def __str__(self):
        return str(self.value)
    
    def __repr__(self):
        return str(self.value)

class Queue():
    """
    This class represents a queue architecture using a signle direction connected list 
    """

    def __init__(self):
        """
        This is the class constructor. It initializes the Queue front and back to None and the Queue size to 0 
        """
        self._size = 0
        self._front = None
        self._back = None

    def enqueue(self, value):
        """
        This method adds an element onto the back of the Queue

        :param value: Value to add to the back
        """
        if self._size == 0:
            self._size += 1
            new_node = Node(value, None, None)
            self._front = new_node
            self._back = new_node
        else:
            self._size += 1
            new_back = Node(value, self._back, None)
            self._back.previous = new_back
            self._back = new_back

    def dequeue(self):
        """
        This method removes an element from the front of the Queue and returns it

        :return: The value of the front most element inside the Queue. Or None if the Queue is empty
        """
        if self._front is None:
            return None

        temp = self._front
        self._front = self._front.previous
        self._size -= 1
        return temp

    def count(self):
        """
        This method returns the current number of elements inside the Queue
        """
        return self._size

    def clear(self):
        """
        This method clears the entire Queue
        """
        self._front = None
        self._back = None
        self._size = 0    

    def dequeueAll(self):
        """
        This method returns all the elements inside the Queue

        :return: List of all elements from the Queue
        """

        output = []
        current = self.dequeue()
        while current is not None:
            output.append(current)
            current = self.dequeue()
        
        return output

    def __iter__(self):
        """
        This method returns the current number of elements inside the Queue. It is NOT thread safe
        """
        self.current = self._front
        return self
    
    def __next__(self):
        """
        This method returns the next elementy inside an iteration 
        """
        if self.current == None:
            raise StopIteration

        temp = self.current
        self.current = self.current.previous
        return temp

que = Queue()
que.enqueue(11)
que.enqueue(20)
print(que.dequeueAll())
