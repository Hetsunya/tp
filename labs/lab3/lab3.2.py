class RadixSort:
    def __init__(self):
        pass

    def sort(self, arr):
        max_length = max(len(str(x)) for x in arr)

        # Проходимся по каждому символу в строках, начиная с последнего
        for char_place in range(max_length - 1, -1, -1):
            # Создаем 256 корзин для каждого символа (ASCII код от 0 до 255)
            buckets = [[] for _ in range(2000)]

            # Распределяем элементы по корзинам в соответствии с текущим символом
            for string in arr:
                if char_place < len(string):
                    char = ord(string[char_place])  # Получаем ASCII код символа
                else:
                    char = 0  # Если длина строки меньше, чем текущий символ, используем 0
                buckets[char].append(string)

            # Собираем элементы обратно в исходный массив
            arr = [string for bucket in buckets for string in bucket]

        return arr


class RadixSortWithSteps(RadixSort):
    def __init__(self, output_file):
        self.steps = []
        self.output_file = output_file
        self.step_counter = 1  # Счетчик шагов

    def sort(self, arr):
        max_length = max(len(str(x)) for x in arr)
        for char_place in range(max_length - 1, -1, -1):
            buckets = [[] for _ in range(2000)]
            for string in arr:
                if char_place < len(string):
                    char = ord(string[char_place])
                else:
                    char = 0
                buckets[char].append(string)
            arr = [string for bucket in buckets for string in bucket]
            self.steps.append(arr.copy())
            self.write_step_to_file(arr.copy())
            self.step_counter += 1
        return arr

    def write_step_to_file(self, step):
        with open(self.output_file, 'a') as file:
            file.write(f"Шаг {self.step_counter}: {','.join(step)}\n")


class RadixSortVisualizer(RadixSortWithSteps):
    def __init__(self):
        super().__init__()

    def visualize(self):
        for step, arr in enumerate(self.steps):
            print(f"Шаг {step + 1}: {arr}")


def read_data_from_file(file_path):
    with open(file_path, 'r') as file:
        data = file.readlines()
        data = [line.strip() for line in data]
    return data


def clear_file(output_file_path):
    with open(output_file_path, 'w') as file:
        pass


if __name__ == "__main__":
    file_path = "list.txt"
    output_file_path = "lab3.2_log.txt"
    clear_file(output_file_path)
    # arr = read_data_from_file(file_path)
    arr = ["37", '101', "2", "199" ,"198", "20", "18", "a"]

    # Сортировка поразрядной сортировкой с сохранением шагов
    sorter_with_steps = RadixSortWithSteps(output_file_path)
    sorted_arr_with_steps = sorter_with_steps.sort(arr)

    print("Отсортированный массив сохранен в файл:", output_file_path)




