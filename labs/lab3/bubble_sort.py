class BubbleSorter:
    def __init__(self, data):
        self.data = data

    def sort(self):
        n = len(self.data)
        for i in range(n):
            for j in range(0, n-i-1):
                if self.data[j] > self.data[j+1]:
                    self.data[j], self.data[j+1] = self.data[j+1], self.data[j]

# Пример использования:
if __name__ == "__main__":
    with open("list.txt", "r") as file:
        data = [line.strip() for line in file]

    bubble_sorter = BubbleSorter(data)
    bubble_sorter.sort()
    print("Отсортированный список:", bubble_sorter.data)
