class BlackHoleNode:
    def __init__(self, value, prev_node=None, next_node=None):
        if not isinstance(value, (int, float)):
            raise TypeError("Value must be an integer or float")
        self.value = value  # Mass of the black hole
        self.type = None  # Type: "quasar", "blazar", or None (unknown)
        self.prev = prev_node
        self.next = next_node

    def __str__(self):
        return f"({self.value}, {self.type})"

    def __eq__(self, other):
        if not isinstance(other, BlackHoleNode):
            return False
        return self.value == other.value and self.type == other.type and self.next == other.next
