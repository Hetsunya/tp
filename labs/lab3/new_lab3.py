 import logging

class RadixSort:
    def __init__(self):
        self.logger = logging.getLogger("RadixSort")
        self.logger.setLevel(logging.INFO)
        self.handler = logging.FileHandler("lab3.2_log.txt")
        self.handler.setFormatter(logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s'))
        self.logger.addHandler(self.handler)
        self.clear_log_file()

    def clear_log_file(self):
        with open("lab3.2_log.txt", "w"):
            pass

    def radix_sort(self, arr):
        self.logger.info(f"Original array: {arr}")
        max_length = len(max(arr, key=len))  # Находим максимальную длину строки в списке
        print(f'max = {max_length} = {max(arr, key=len)}')

        for digit_index in range(max_length - 1, -1, -1):
            buckets = [[] for _ in range(2000)]  # Создаем n корзин, по одной на каждый символ ASCII

            for string in arr:
                char = ord(string[digit_index]) if digit_index < len(string) else 0  # Получаем ASCII-код символа
                buckets[char].append(string)

            arr = [string for bucket in buckets for string in bucket]

            self.logger.info(f"After digit {max_length - digit_index}: {arr}")

        return arr


def read_data_from_file(file_path):
    with open(file_path, 'r') as file:
        data = file.readlines()
        # Удаляем символ переноса строки для каждой строки и преобразуем в список
        data = [line.strip() for line in data]
    return data


# Настройка логирования
logging.basicConfig(level=logging.INFO)

# Пример использования:

if __name__ == "__main__":
    file_path = "list_old.txt"
    unsorted_data = read_data_from_file(file_path)

    # Сортировка строковых данных радикс-сортировкой
    radix_sorter = RadixSort()
    sorted_strings = radix_sorter.radix_sort(unsorted_data)
    print("Отсортированные строки:", sorted_strings)

    max_length = len(max(unsorted_data, key=len))  # Находим максимальную длину строки в списке
    print(f'max = {max_length} = {max(unsorted_data, key=len)}')
