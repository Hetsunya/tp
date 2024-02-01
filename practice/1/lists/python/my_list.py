# my_list.py
from list_node import ListNode

class MyList:
    def __init__(self, head=None):
        self.head = head

    def append(self, value):
        if not self.head:
            self.head = ListNode(value)
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = ListNode(value)

    def __eq__(self, other):
        if isinstance(other, MyList):
            return self.head == other.head
        elif other is None:
            return False
        return NotImplemented

    def __str__(self):
        return str(self.head)

    def __len__(self):
        count = 0
        current = self.head
        while current:
            count += 1
            current = current.next
        return count

    def insert(self, index, value):
        if index < 0:
            raise IndexError("List index out of range")
        new_node = ListNode(value)
        if index == 0:
            new_node.next = self.head
            self.head = new_node
        else:
            current = self.head
            for _ in range(index - 1):
                if current is None:
                    raise IndexError("List index out of range")
                current = current.next
            new_node.next = current.next
            current.next = new_node

    def reverse(self):
        prev = None
        current = self.head
        while current:
            next_node = current.next
            current.next = prev
            prev = current
            current = next_node
        self.head = prev

    def index(self, value):
        current = self.head
        index = 0
        while current:
            if current.value == value:
                return index
            index += 1
            current = current.next
        raise ValueError(f"{value} not in list")

    def count(self, value):
        count = 0
        current = self.head
        while current:
            if current.value == value:
                count += 1
            current = current.next
        return count

    def pop(self):
        if not self.head:
            raise IndexError("pop from empty list")
        value = self.head.value
        self.head = self.head.next
        return value

    def remove(self, value):
        if not self.head:
            raise ValueError(f"{value} not in list")
        if self.head.value == value:
            self.head = self.head.next
            return
        current = self.head
        while current.next:
            if current.next.value == value:
                current.next = current.next.next
                return
            current = current.next
        raise ValueError(f"{value} not in list")

    def clear(self):
        self.head = None

    def extend(self, iterable):
        for value in iterable:
            self.append(value)

    def copy(self):
        new_list = MyList()
        current = self.head
        while current:
            new_list.append(current.value)
            current = current.next
        return new_list