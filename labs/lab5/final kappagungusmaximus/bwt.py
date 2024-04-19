class BurrowsWheelerTransform:

    def __init__(self, data):
        self.data = data

    def transform(self):
        # get data size
        size = len(self.data)
        # get doubled string
        self.data *= 2
        # get order (by index) of rotations
        order = sorted(range(size), key=lambda i: self.data[i:])
        # get index of original rotation
        index = order.index(0)
        # return index appended with last column of (imaginary) rotation table
        return chr(255) * (index // 255) + chr(index % 255) + ''.join(self.data[(i - 1 + size) % size] for i in order)

    def restore(self):
        # get index of end of index
        eoi = next(i for i in range(len(self.data)) if ord(self.data[i]) < 255)
        # get index
        index = 255 * eoi + ord(self.data[eoi])
        # get tranformed content
        content = self.data[eoi + 1:]
        size = len(content)
        # get lshift array
        lshift = [i for symbol in sorted(set(content)) for i, x in enumerate(content) if x == symbol]
        # restore
        restored = ''
        for i in range(size):
            index = lshift[index]
            if index >= size: break
            restored += content[index]
        # return restored
        return restored

bwt = BurrowsWheelerTransform("banana")
comp = bwt.transform()
print(comp)
decomp = bwt.restore()
print(decomp)
