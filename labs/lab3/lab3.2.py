class RadixSort:
    def __init__(self, data):
        self.data = data
        self.max_length = max(len(str(item)) for item in data)

    def sort(self):
        for i in range(self.max_length - 1, -1, -1):  # Iterate from the least significant digit/character
            buckets = [[] for _ in range(256)]  # Buckets for ASCII characters (0-255)
            for item in self.data:
                # Extract the character at the current position (handling different data types)
                key = ord(str(item)[i]) if i < len(str(item)) else 0
                buckets[key].append(item)

            self.data = []
            for bucket in buckets:
                self.data.extend(bucket)

        return self.data


class RadixSortWithSteps(RadixSort):
    def __init__(self, data):
        super().__init__(data)
        self.steps = []  # To store the intermediate states

    def _sort(self):
        for i in range(self.max_length - 1, -1, -1):
            buckets = [[] for _ in range(257)]  # 257 buckets (0-256)
            for item in self.data:
                item_str = str(item)
                key = ord(item_str[i]) if i < len(item_str) else 0  # Use 0 for shorter items
                buckets[key].append(item)

            # Reconstruct the data using sorted() on each bucket
            self.data = []
            for bucket in buckets:
                self.data.extend(sorted(bucket))  # Sort each bucket before extending

class RadixSortWithOutput:
    def __init__(self, data, output_file):
        self.sorter = RadixSortWithSteps(data)
        self.output_file = output_file

    def sort_and_output(self):
        self.sorter.sort()

        with open(self.output_file, 'w') as f:
            for i, step in enumerate(self.sorter.steps):
                f.write(f"Pass {i+1}: {step}\n")

def read_data_from_file(file_path):
    with open(file_path, 'r') as file:
        data = file.readlines()
        data = [line.strip() for line in data]
    return data


def clear_file(output_file_path):
    with open(output_file_path, 'w') as file:
        pass


if __name__ == "__main__":
    file_path = "list_old.txt"
    output_file_path = "lab3.2_log.txt"
    clear_file(output_file_path)
    # data = read_data_from_file(file_path)
    data = ["apple", "cherry", "banana", "123", "45", "kiwi", "10"]

    # Сортировка поразрядной сортировкой с сохранением шагов
    sorter = RadixSortWithOutput(data, "lab3.2_log.txt")
    sorter.sort_and_output()

    print("Отсортированный массив сохранен в файл:", output_file_path)




