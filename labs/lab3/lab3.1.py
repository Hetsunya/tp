class BubbleSort:
    def __init__(self):
        self._steps = []

    def custom_sort(self, item):
        if isinstance(item, int) or (isinstance(item, str) and item.isdigit()):
            return (0, int(item)) if isinstance(item, int) else (1, int(item))
        else:
            return (2, item, item)


    def sort(self, arr):
        self._steps = []
        n = len(arr)
        for i in range(n):
            for j in range(0, n - i - 1):
                if arr[j] > arr[j + 1]:
                    arr[j], arr[j + 1] = arr[j + 1], arr[j]
            self._steps.append(arr.copy())  # Сохраняем текущий этап сортировки
        return arr

    def get_steps(self):
        return self._steps  # Метод для доступа к этапам сортировки

class BubbleSortWithSteps(BubbleSort):
    def __init__(self):
        super().__init__()

    def get_steps(self):
        return super().get_steps()  # Метод для получения этапов сортировки из родительского класса


class SortVisualizer:
    def __init__(self, bubble_sort, output_file=None):
        self.bubble_sort = bubble_sort
        self.output_file = output_file

    def visualize_sorting(self):
        steps = self.bubble_sort.get_steps()  # Получаем этапы сортировки из объекта BubbleSort
        for i, step in enumerate(steps, start=1):
            print(f"Шаг {i}: {','.join(map(str, step))}")  # Выводим этап сортировки в консоль
            if self.output_file:
                self.write_step_to_file(step, i)

    def write_step_to_file(self, step, step_number):
        with open(self.output_file, 'a') as file:
            file.write(f"Шаг {step_number}: {','.join(map(str, step))}\n")

def read_data_from_file(file_path):
    with open(file_path, 'r') as file:
        data = file.readlines()
        # Удаляем символ переноса строки для каждой строки и преобразуем в список
        data = [line.strip() for line in data]
    return data


def clear_file(output_file_path):
    with open(output_file_path, 'w') as file:
        pass

clear_file("lab3.1_log.txt")


# Пример использования:
bubble_sort = BubbleSort()
# bubble_sort.sort(["3", "1", "4", "1", "5", "9", '2', "6", "5", "3"])
data = read_data_from_file("list.txt")
sorted_data = bubble_sort.sort(data)

visualizer = SortVisualizer(bubble_sort, output_file="lab3.1_log.txt")
visualizer.visualize_sorting()


print(f"sort by me: \n{sorted_data}")
print(f"sort by python: \n{sorted(data)}")
