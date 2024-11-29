import unittest
import time
import random

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
    
    def __len__(self):
        """
        This method return the number of items in this Queue 
        """
        return self._size
    
    def __getitem__(self, key):
        if not isinstance(key, int):
            raise IndexError("Index must be int")
        if key >= self._size:
            raise IndexError("This index does not exist in this Queue")

        current = self._front
        for i in range(0, key):
            current = current.previous

        return current
    
    def __setitem__(self, key, value):
        if not isinstance(key, int):
            raise IndexError("Index must be int")
        if key >= self._size:
            raise IndexError("This index does not exist in this Queue")
        
        current = self._front
        for i in range(0, key):
            current = current.previous

        current.value = value

    def __contains__(self, item):
        current = self._front
        while current is not None:
            if current.value == item:
                return True
            
            current = current.previous

        return False
    
    
class testKolekce(unittest.TestCase):
    def test_items(self):
        collection = Queue()

        collection.enqueue("item")
        
        self.assertIn("item", collection, "Item is in the collection")

        collection.dequeue()

        self.assertNotIn("item", collection, "Item is not in the collection")

    def test_speed(self):
        collection = Queue()
        num_of_186 = 0

        for i in range(0,1_000_000):
            collection.enqueue(random.randint(1, 999))

        start = time.time()

        for item in collection:
            if item == 186:
                num_of_186 += 1
        
        end = time.time()

        overall_time = end - start

        self.assertLessEqual(overall_time*10e3, 500, "Program run under 500 milis")

if __name__ == '__main__':
    unittest.main()