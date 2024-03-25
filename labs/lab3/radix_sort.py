class RadixSorter:
    def __init__(self, data):
        self.data = data

    def radix_sort(self):
        max_length = len(str(max(map(int, self.data))))
        for i in range(max_length):
            self._counting_sort(i)

    def _counting_sort(self, exp):
        n = len(self.data)
        output = [0] * n
        count = [0] * 10

        for i in range(n):
            index = self._get_digit(int(self.data[i]), exp)
            count[index] += 1

        for i in range(1, 10):
            count[i] += count[i - 1]

        i = n - 1
        while i >= 0:
            index = self._get_digit(int(self.data[i]), exp)
            output[count[index] - 1] = self.data[i]
            count[index] -= 1
            i -= 1

        for i in range(n):
            self.data[i] = output[i]

    def _get_digit(self, num, exp):
        return (num // 10 ** exp) % 10

# Пример использования:
if __name__ == "__main__":
    with open("list_old.txt", "r") as file:
        data = [line.strip() for line in file]

    radix_sorter = RadixSorter(data)
    radix_sorter.radix_sort()
    print("Отсортированный список:", radix_sorter.data)
