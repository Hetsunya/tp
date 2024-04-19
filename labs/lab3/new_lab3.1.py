class BubbleSort:
    def __init__(self):
        self._steps = []


    def sort(self, data):
        n = len(data)
        for i in range(n):
            for j in range(0, n - i - 1):
                if data[j] > data[j + 1]:
                    data[j], data[j + 1] = data[j + 1], data[j]
            self._steps.append(data.copy())  # Сохраняем текущий этап сортировки
        return data


class BubbleSortWithSteps(BubbleSort):
    def __init__(self):
        super().__init__()

    def get_steps(self):
        return self._steps


class SortVisualizer:
    def __init__(self, bubble_sort, output_file=None):
        self.bubble_sort = bubble_sort
        self.output_file = output_file

    def visualize_sorting(self):
        steps = self.bubble_sort.get_steps()
        for i, step in enumerate(steps, start=1):
            print(f"Шаг {i}: {','.join(map(str, step))}")
            if self.output_file:
                self.write_step_to_file(step, i)

    def write_step_to_file(self, step, step_number):
        with open(self.output_file, 'a') as file:
            file.write(f"Шаг {step_number}: {','.join(map(str, step))}\n")

def read_data_from_file(file_path):
    with open(file_path, 'r') as file:
        data = file.readlines()
        data = [line.strip() for line in data]
    return data


def clear_file(output_file_path):
    with open(output_file_path, 'w') as file:
        pass

clear_file("lab3.1_log.txt")


bubble_sort = BubbleSortWithSteps()
# data = ["3", "1", "4", "1", "5", "9", '2', "6", "5", "3"]
data = read_data_from_file("list.txt")
sorted_data = bubble_sort.sort(data)

visualizer = SortVisualizer(bubble_sort, output_file="lab3.1_log.txt")
visualizer.visualize_sorting()


print(f"sort by me: \n{sorted_data}")
print(f"sort by python: \n{sorted(data)}")
