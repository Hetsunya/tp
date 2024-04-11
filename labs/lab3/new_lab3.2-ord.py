class RadixSort:
    def __init__(self):
        self._steps = []

    def hash_char(self, char):
        return ord(char)  # Просто используем ASCII-код символа в качестве хэша

    def sort(self, data):
        max_length = max(len(item) for item in data)
        for i in range(max_length - 1, -1, -1):
            buckets = [[] for _ in range(256)]  # Buckets for ASCII characters (0-255)
            for item in data:
                key = self.hash_char(item[i]) if i < len(item) else 0
                buckets[key].append(item)

            data = []
            for bucket in buckets:
                data.extend(bucket)

            self._steps.append(data.copy())  # Save the current step of sorting

        return data

    def get_steps(self):
        return self._steps  # Method to access the sorting steps


class RadixSortWithSteps(RadixSort):
    def __init__(self):
        super().__init__()

    def get_steps(self):
        return super().get_steps()  # Метод для получения этапов сортировки из родительского класса



class SortVisualizer:
    def __init__(self, radix_sort_with_steps, output_file=None):
        self.radix_sort_with_steps = radix_sort_with_steps
        self.output_file = output_file

    def visualize_sorting(self):
        steps = self.radix_sort_with_steps.get_steps()  # Получаем этапы сортировки из объекта RadixSortWithSteps
        for i, step in enumerate(steps, start=1):
            print(f"Step {i}: {','.join(map(str, step))}")  # Выводим этап сортировки в консоль
            if self.output_file:
                self.write_step_to_file(step, i)

    def write_step_to_file(self, step, step_number):
        with open(self.output_file, 'a') as file:
            file.write(f"Step {step_number}: {','.join(map(str, step))}\n")



def read_data_from_file(file_path):
    with open(file_path, 'r') as file:
        data = file.readlines()
        # Remove the newline character for each line and convert to a list
        data = [line.strip() for line in data]
    return data


def clear_file(output_file_path):
    with open(output_file_path, 'w') as file:
        pass

clear_file("lab3.2_log-ord.txt")

radix_sort = RadixSort()
data = read_data_from_file("list.txt")
sorted_data = radix_sort.sort(data)

visualizer = SortVisualizer(radix_sort, output_file="lab3.2_log-ord.txt")
visualizer.visualize_sorting()

