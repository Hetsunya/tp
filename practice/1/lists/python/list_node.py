class ListNode:
    def __init__(self, value, next_node=None):
        if not isinstance(value, (int, float)):
            raise TypeError("Value must be an integer or float")
        if next_node is not None and not isinstance(next_node, ListNode):
            raise TypeError("Next node must be a ListNode or None")
        self.value = value
        self.next = next_node

    def __str__(self):
        return f"({self.value}) -> {self.next}"

    def __eq__(self, other):
        if not isinstance(other, ListNode):
            return False
        return self.value == other.value and self.next == other.next
