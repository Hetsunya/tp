# list_node.py
class ListNode:
    def __init__(self, value, next_node=None):
        self.value = value
        self.next = next_node

    def __eq__(self, other):
        if not isinstance(other, ListNode):
            return False
        return self.value == other.value and self.next == other.next

    def __repr__(self):
        next_repr = f" -> {self.next.__repr__()}" if self.next else " -> None"
        return f"({self.value}){next_repr}"
