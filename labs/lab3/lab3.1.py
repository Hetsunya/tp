class BubbleSort:
    def __init__(self):
        pass

    def sort(self, arr):
        n = len(arr)
        for i in range(n):
            for j in range(0, n - i - 1):
                if arr[j] > arr[j + 1]:
                    arr[j], arr[j + 1] = arr[j + 1], arr[j]
        return arr


class BubbleSortWithSteps(BubbleSort):
    def __init__(self, output_file):
        self.steps = []
        self.output_file = output_file
        self.step_counter = 1

    def sort(self, arr):
        n = len(arr)
        for i in range(n):
            for j in range(0, n - i - 1):
                if arr[j] > arr[j + 1]:
                    arr[j], arr[j + 1] = arr[j + 1], arr[j]
            self.steps.append(arr.copy())
            self.write_step_to_file(arr.copy())
            self.step_counter += 1
        return arr

    def write_step_to_file(self, step):
        with open(self.output_file, 'a') as file:
            file.write(f"Шаг {self.step_counter}: {','.join(map(str, step))}\n")

class BubbleSortVisualizer(BubbleSortWithSteps):
    def __init__(self):
        super().__init__()

    def visualize(self):
        for step, arr in enumerate(self.steps):
            print(f"Шаг {step + 1}: {arr}")


def read_data_from_file(file_path):
    with open(file_path, 'r') as file:
        data = file.readlines()
        # Удаляем символ переноса строки для каждой строки и преобразуем в список
        data = [line.strip() for line in data]
    return data

def clear_file(file_path):
    with open(file_path, 'w') as file:
        pass


if __name__ == "__main__":
    file_path = "list.txt"
    clear_file(file_path)
    output_file_path = "lab3.1_log.txt"
    arr = read_data_from_file(file_path)

    # Сортировка пузырьком с сохранением шагов
    sorter_with_steps = BubbleSortWithSteps(output_file_path)
    sorted_arr_with_steps = sorter_with_steps.sort(arr)

    print("Отсортированный массив сохранен в файл:", output_file_path)