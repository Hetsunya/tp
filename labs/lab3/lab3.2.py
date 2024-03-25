import logging

logging.basicConfig(filename='lab3.2_log.txt', level=logging.INFO, format='%(asctime)s - %(message)s')


class RadixSort:
    def __init__(self, data):
        self.data = data

    def radix_sort(self):
        self.data = [int(x) if x.isdigit() else x for x in self.data]

        max_length = len(str(max(self.data, key=lambda x: len(str(x)))))

        for i in range(max_length):
            buckets = [[] for _ in range(10)]
            for num in self.data:
                num_str = str(num)
                if len(num_str) <= i:
                    digit = 0
                else:
                    try:
                        digit = int(num_str[-i - 1])
                    except ValueError:
                        digit = 0
                buckets[digit].append(num)
            self.data = [num for bucket in buckets for num in bucket]
            logging.info(f"Iteration {i + 1}: {self.data}")
        return self.data


class SortingVisualization(RadixSort):
    def __init__(self, data):
        super().__init__(data)

    def visualize_sorting(self):
        logging.info("Initial data: " + str(self.data))
        sorted_data = self.radix_sort()
        logging.info("Sorted data: " + str(sorted_data))
        print("Sorted data:", sorted_data)


def main():
    try:
        with open('list_old.txt', 'r') as file:
            data = [line.strip() for line in file.readlines()]
            sorting_visualization = SortingVisualization(data)
            sorting_visualization.visualize_sorting()
    except FileNotFoundError:
        logging.error("File 'list_old.txt' not found.")


if __name__ == "__main__":
    main()
