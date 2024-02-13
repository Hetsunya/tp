class Sorter:
    def __init__(self, data):
        self.data = data

    def sort(self):
        pass  # Здесь будет реализация сортировки

class IntermediateDataSorter(Sorter):
    def __init__(self, data):
        super().__init__(data)
        self.intermediate_data = []

    def sort(self):
        # Реализация сортировки пузырьком с записью промежуточных данных
        n = len(self.data)
        for i in range(n):
            for j in range(0, n-i-1):
                if self.data[j] > self.data[j+1]:
                    self.data[j], self.data[j+1] = self.data[j+1], self.data[j]
                    # Записываем текущее состояние массива после обмена
                    self.intermediate_data.append(self.data.copy())

class VisualizerSorter(IntermediateDataSorter):
    def visualize_sort(self):
        # Реализация визуализации сортировки с использованием промежуточных данных
        for step, data_snapshot in enumerate(self.intermediate_data):
            print(f"Шаг {step + 1}: {data_snapshot}")

# Пример использования:
# with open("list.txt", "r") as file:
#     data = [line.strip() for line in file]
data = ["123456", "12345", "123456789", "password", "iloveyou", "princess", "1234567", "rockyou", "12345678", "abc123", "nicole", "daniel", "babygirl", "monkey", "lovely", "jessica", "654321", "michael", "ashley", "qwerty", "111111", "iloveu", "000000"]

visualizer_sorter = VisualizerSorter(data)
visualizer_sorter.sort()
visualizer_sorter.visualize_sort()
