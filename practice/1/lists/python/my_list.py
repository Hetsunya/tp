from list_node import ListNode


class MyList:
    def __init__(self, value=None):
        self.head = ListNode(value) if value is not None else None

    def __len__(self):
        count = 0
        node = self.head
        while node:
            count += 1
            node = node.next
        return count

    def __str__(self):
        return str(self.head)

    def __repr__(self):
        return str(self)

    def __eq__(self, other):
        if not isinstance(other, MyList):
            return False
        node1 = self.head
        node2 = other.head
        while node1 and node2:
            if node1.value != node2.value:
                return False
            node1 = node1.next
            node2 = node2.next
        return node1 is None and node2 is None

    def append(self, value):
        new_node = ListNode(value)
        if self.head is None:
            self.head = new_node
        else:
            node = self.head
            while node.next:
                node = node.next
            node.next = new_node

    def __contains__(self, value):
        node = self.head
        while node:
            if node.value == value:
                return True
            node = node.next
        return False

    def remove(self, value):
        node = self.head
        prev = None
        while node:
            if node.value == value:
                if prev:
                    prev.next = node.next
                else:
                    self.head = node.next
                return
            prev = node
            node = node.next
        raise ValueError("Value not found in list")

    def pop(self, index=-1):
        """Удаляет и возвращает элемент по указанному индексу.
        Если индекс не указан, удаляется последний элемент.
        """
        if self.head is None:
            raise IndexError("Cannot pop from an empty list")

        if index == -1:  # Удаление последнего элемента
            if self.head.next is None:  # Список с одним элементом
                data = self.head.value
                self.head = None
                return data

            node = self.head
            while node.next.next:  # Доходим до предпоследнего узла
                node = node.next
            data = node.next.value
            node.next = None
            return data

        elif index >= 0:  # Удаление по индексу
            if index == 0:  # Удаление первого элемента
                data = self.head.value
                self.head = self.head.next
                return data

            node = self.head
            i = 0
            while node.next and i < index - 1:
                node = node.next
                i += 1

            if node.next is None:
                raise IndexError("Index out of range")

            data = node.next.value
            node.next = node.next.next
            return data

        else:
            raise IndexError("Index cannot be negative")




    def clear(self):
        self.head = None

    def extend(self, other):
        if not isinstance(other, MyList):
            raise TypeError("Can only extend with another MyList")
        if other.head is None:
            return
        if self.head is None:
            self.head = other.head
        else:
            node = self.head
            while node.next:
                node = node.next
            node.next = other.head

    def copy(self):
        new_list = MyList()
        node = self.head
        while node:
            new_list.append(node.value)
            node = node.next
        return new_list

    def insert(self, index, value):
        """Inserts an element at the specified index within the MyList."""
        if index < 0:
            # return 0

            raise IndexError('list index out of range')

            # try:
            #     self.head = ListNode(value, self.head)
            # except KeyError as err:
            #     return err

        if self.head is None:  # Check for empty list only if index is not negative
            self.head = ListNode(value)
            return

        if index == 0 or self.head is None:
            # Handle insertion at the beginning, including empty list
            self.head = ListNode(value, self.head)
            return

        prev = None
        node = self.head
        i = 0
        while node and i < index:
            prev = node
            node = node.next
            i += 1

        if i < index:
            # Handle index beyond the list's length, append to the end
            prev.next = ListNode(value)
        else:
            # Insert the new node before the found node
            prev.next = ListNode(value, node)




    def reverse(self):
        prev = None
        node = self.head
        while node:
            next_node = node.next
            node.next = prev
            prev = node
            node = next_node
        self.head = prev

    def index(self, value):
        node = self.head
        i = 0
        while node:
            if node.value == value:
                return i
            node = node.next
            i += 1
        raise ValueError("Value not found in list")

    def count(self, value):
        count = 0
        node = self.head
        while node:
            if node.value == value:
                count += 1
            node = node.next
        return count
