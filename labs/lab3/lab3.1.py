class BubbleSort:
    def __init__(self):
        pass

    def custom_sort(self, item):
        if item.isdigit():  # Если элемент является числом
            return (len(item), int(item))  # Сначала сортируем по длине, затем по числовому значению
        else:
            return (len(item), item)  # Сначала сортируем по длине, затем лексикографически

    def sort(self, arr):
        n = len(arr)
        for i in range(n):
            for j in range(0, n - i - 1):
                if self.custom_sort(arr[j]) > self.custom_sort(arr[j + 1]):  # Используем кастомную функцию сортировки
                    arr[j], arr[j + 1] = arr[j + 1], arr[j]
        return arr

class BubbleSortWithSteps(BubbleSort):
    def __init__(self, output_file):
        super().__init__()
        self.steps = []
        self.output_file = output_file
        self.step_counter = 1

    def sort(self, arr):
        sorted_arr = super().sort(arr)  # Вызываем метод sort из родительского класса
        n = len(sorted_arr)
        for i in range(n):
            self.steps.append(sorted_arr[:i + 1].copy())
            self.write_step_to_file(sorted_arr[:i + 1].copy())
            self.step_counter += 1
        return sorted_arr

    def write_step_to_file(self, step):
        with open(self.output_file, 'a') as file:
            file.write(f"Шаг {self.step_counter}: {','.join(map(str, step))}\n")


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
    output_file_path = "lab3.1_log.txt"
    clear_file(output_file_path)
    data = read_data_from_file(file_path)
    # data = [9, 3,4,6,2,1,8,7,5]

    # Сортировка пузырьком с сохранением шагов
    sorter_with_steps = BubbleSortWithSteps(output_file_path)
    sorted_arr_with_steps = sorter_with_steps.sort(data)
    print (f"Оригинальный массив {data}")
    print (f"Отсортированный массив {sorted_arr_with_steps}")
    print("Шаги сотрировки массива сохранен в файл:", output_file_path)
