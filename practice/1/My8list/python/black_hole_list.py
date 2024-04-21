from list_node import BlackHoleNode

class BlackHoleList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.quasars = None  # Initialize as None
        self.blazars = None  # Initialize as None
        self.unknown = None  # Initialize as None


    def __len__(self):
        count = 0
        node = self.head
        while node:
            count += 1
            node = node.next
        return count

        def __str__(self):
            result = "["
            node = self.head
            while node:
                result += str(node) + ", "
                print(node)
                node = node.next
                print(node)
            result = result.rstrip(", ") + "]"

        if self.quasars:
            result += "\nQuasars: " + str(self.quasars)
        if self.blazars:
            result += "\nBlazars: " + str(self.blazars)
        if self.unknown:
            result += "\nUnknown: " + str(self.unknown)

        return result


    def __repr__(self):
        return str(self)

    def __eq__(self, other):
        if not isinstance(other, BlackHoleList):
            return False
        node1 = self.head
        node2 = other.head
        while node1 and node2:
            if node1.value != node2.value or node1.type != node2.type:
                return False
            node1 = node1.next
            node2 = node2.next
        return node1 is None and node2 is None

    def _insert_node(self, new_node, sublist):
        """Inserts a node into the main list and the specified sublist in sorted order by mass."""
        if sublist is None:  # Check if the sublist is None
            sublist = BlackHoleList()  # Create a new sublist if needed


        if sublist.head is None:
            sublist.head = sublist.tail = new_node
        else:
            node = sublist.head
            while node and node.value < new_node.value:
                node = node.next
            if node is None:  # Insert at the end
                new_node.prev = sublist.tail
                sublist.tail.next = new_node
                sublist.tail = new_node
            elif node == sublist.head:  # Insert at the beginning
                new_node.next = sublist.head
                sublist.head.prev = new_node
                sublist.head = new_node
            else:  # Insert in the middle
                new_node.prev = node.prev
                new_node.next = node
                node.prev.next = new_node
                node.prev = new_node
        print("После вставки:")
        print("Новый узел:", new_node)
        print("Предыдущий узел:", new_node.prev)
        print("Следующий узел:", new_node.next)

        # Insert into the main list
        if self.head is None:
            self.head = self.tail = new_node
        else:
            node = self.head
            while node and node.value < new_node.value:
                node = node.next
            if node is None:
                new_node.prev = self.tail
                self.tail.next = new_node
                self.tail = new_node
            elif node == self.head:
                new_node.next = self.head
                self.head.prev = new_node
                self.head = new_node
            else:
                new_node.prev = node.prev
                new_node.next = node
                node.prev.next = new_node
                node.prev = new_node

    def append(self, value, type=None):
        new_node = BlackHoleNode(value)
        new_node.type = type

        if type == "quasar":
            if self.quasars is None:
                self.quasars = BlackHoleList()  # Create sublist only if needed
            self._insert_node(new_node, self.quasars)
        elif type == "blazar":
            self._insert_node(new_node, self.blazars)
        else:
            self._insert_node(new_node, self.unknown)

    def __contains__(self, value):
        node = self.head
        while node:
            if node.value == value:
                return True
            node = node.next
        return False

    def remove(self, value):
        node = self.head
        while node:
            if node.value == value:
                if node.prev:
                    node.prev.next = node.next
                else:
                    self.head = node.next
                if node.next:
                    node.next.prev = node.prev
                else:
                    self.tail = node.prev
                # Remove from sublist
                if node.type == "quasar":
                    self._remove_from_sublist(node, self.quasars)
                elif node.type == "blazar":
                    self._remove_from_sublist(node, self.blazars)
                else:
                    self._remove_from_sublist(node, self.unknown)
                return
            node = node.next
        raise ValueError("Value not found in list")

    def _remove_from_sublist(self, node, sublist):
        if node.prev:
            node.prev.next = node.next
        else:
            sublist.head = node.next
        if node.next:
            node.next.prev = node.prev
        else:
            sublist.tail = node.prev

    def pop(self, index=-1):
        if self.head is None:
            raise IndexError("Cannot pop from an empty list")

        if index == -1:  # Remove last element
            node = self.tail
            if node.prev:
                node.prev.next = None
                self.tail = node.prev
            else:  # List with one element
                self.head = self.tail = None
        elif index == 0:  # Remove first element
            node = self.head
            if node.next:
                node.next.prev = None
                self.head = node.next
            else:  # List with one element
                self.head = self.tail = None
        else:
            i = 0
            node = self.head
            while node and i < index:
                node = node.next
                i += 1
            if node is None:
                raise IndexError("Index out of range")
            node.prev.next = node.next
            if node.next:
                node.next.prev = node.prev
            else:
                self.tail = node.prev

        # Remove from sublist
        if node.type == "quasar":
            self._remove_from_sublist(node, self.quasars)
        elif node.type == "blazar":
            self._remove_from_sublist(node, self.blazars)
        else:
            self._remove_from_sublist(node, self.unknown)
        return node.value

    def clear(self):
        self.head = self.tail = None
        self.quasars.clear()
        self.blazars.clear()
        self.unknown.clear()

    def extend(self, other):
        if not isinstance(other, BlackHoleList):
            raise TypeError("Can only extend with another BlackHoleList")
        if other.head is None:
            return
        if self.head is None:
            self.head = other.head
            self.tail = other.tail
        else:
            self.tail.next = other.head
            other.head.prev = self.tail
            self.tail = other.tail

        # Merge sublists
        self.quasars.extend(other.quasars)
        self.blazars.extend(other.blazars)
        self.unknown.extend(other.unknown)

    def copy(self):
        new_list = BlackHoleList()
        node = self.head
        while node:
            new_list.append(node.value, node.type)
            node = node.next
        return new_list

    def insert(self, index, value, type=None):
        if index < 0:
            raise IndexError("list index out of range")

        new_node = BlackHoleNode(value)
        new_node.type = type

        if index == 0 or self.head is None:  # Insert at the beginning or empty list
            if self.head:
                new_node.next = self.head
                self.head.prev = new_node
            else:
                self.tail = new_node
            self.head = new_node
        else:
            i = 0
            node = self.head
            while node and i < index - 1:
                node = node.next
                i += 1
            if node is None:
                raise IndexError("list index out of range")
            new_node.next = node.next
            if node.next:
                node.next.prev = new_node
            else:
                self.tail = new_node
            node.next = new_node
            new_node.prev = node

        # Insert into sublist
        if type == "quasar":
            self._insert_node(new_node, self.quasars)
        elif type == "blazar":
            self._insert_node(new_node, self.blazars)
        else:
            self._insert_node(new_node, self.unknown)

    def reverse(self):
        node = self.head
        while node:
            node.prev, node.next = node.next, node.prev
            node = node.prev  # Move to the "next" node which is now prev
        self.head, self.tail = self.tail, self.head

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
