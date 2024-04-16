from black_hole_node import BlackHoleNode

class MyBlackHoleList:
    def __init__(self, value=None):
        if value is not None:
            self.head = BlackHoleNode(value)
        else:
            self.head = None

    def append(self, value):
        if self.head is None:
            self.head = BlackHoleNode(value)
        else:
            current = self.head
            while current.next is not None:
                current = current.next
            current.next = BlackHoleNode(value, prev=current)
            # current.next.prev = None  # Set prev to None for the newly appended node


    def pop(self):
        if self.head is None:
            raise IndexError("pop from empty list")
        elif self.head.next is None:
            value = self.head.value
            self.head = None
            return value
        else:
            current = self.head
            while current.next.next is not None:
                current = current.next
            value = current.next.value
            current.next = None
            return value

    def remove(self, value):
        if self.head is None:
            raise ValueError("list.remove(x): x not in list")
        elif self.head.value == value:
            self.head = self.head.next
        else:
            current = self.head
            while current.next is not None:
                if current.next.value == value:
                    current.next = current.next.next
                    return
                current = current.next
            raise ValueError("list.remove(x): x not in list")

    def extend(self, other_list):
        if isinstance(other_list, MyBlackHoleList):
            if other_list.head is not None:
                if self.head is None:
                    self.head = other_list.head
                else:
                    current = self.head
                    while current.next is not None:
                        current = current.next
                    current.next = other_list.head
        else:
            raise TypeError("MyBlackHoleList.extend() argument must be MyBlackHoleList")

    def clear(self):
        self.head = None

    def __len__(self):
        count = 0
        current = self.head
        while current is not None:
            count += 1
            current = current.next
        return count

    def __str__(self):
        if self.head is None:
            return "None"
        else:
            current = self.head
            result = ""
            while current is not None:
                result += f"({current.value}) -> "
                current = current.next
            result += "None"
            return result

    def __repr__(self):
        return f"MyBlackHoleList(head={self.head})"
