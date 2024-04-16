class BlackHoleNode:
    def __init__(self, value, next=None, prev=None):
        if not isinstance(value, (int, float)):
            raise TypeError("Value must be an integer or a float")
        self.value = value
        self.next = next
        self.prev = prev
        self.is_black_hole = False


    def __str__(self):
        return f"({self.value}) -> {self.next}"

    def __repr__(self):
            if self.next is None:
                return f"BlackHoleNode(value={self.value}, next=None, prev={self.prev})"
            else:
                return f"BlackHoleNode(value={self.value}, next=({self.next.value}) -> {self.next.next}, prev={self.prev})"
