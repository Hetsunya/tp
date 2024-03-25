import logging

class BubbleSort:
    def __init__(self):
        self.logger = logging.getLogger("BubbleSort")
        self.logger.setLevel(logging.INFO)
        self.handler = logging.FileHandler("lab3.1_log.txt")
        self.handler.setFormatter(logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s'))
        self.logger.addHandler(self.handler)
        self.clear_log_file()

    def clear_log_file(self):
        with open("lab3.1_log.txt", "w"):
            pass

    def sort(self, collection):
        n = len(collection)
        for i in range(n):
            for j in range(0, n - i - 1):
                if collection[j] > collection[j + 1]:
                    collection[j], collection[j + 1] = collection[j + 1], collection[j]
                    self.logger.info(f"Swapped {collection[j]} and {collection[j + 1]}")
                    yield collection


class BubbleSortVisualization(BubbleSort):
    def __init__(self):
        super().__init__()

    def sort_with_steps(self, collection):
        sorted_collection = list(collection)
        steps = []
        n = len(sorted_collection)
        for i in range(n):
            for j in range(0, n - i - 1):
                if sorted_collection[j] > sorted_collection[j + 1]:
                    sorted_collection[j], sorted_collection[j + 1] = sorted_collection[j + 1], sorted_collection[j]
                    steps.append(list(sorted_collection))
                    self.logger.info(f"Step {len(steps)}: {sorted_collection}")
        return steps


class BubbleSortVisualizer:
    def __init__(self):
        self.bubble_sort = BubbleSortVisualization()

    def visualize_sort(self, collection):
        import matplotlib.pyplot as plt
        from matplotlib.animation import FuncAnimation

        # Используем функцию max() для определения максимального значения в списке
        max_value = max(collection, key=lambda x: (isinstance(x, int), x))

        steps = self.bubble_sort.sort_with_steps(collection)
        fig, ax = plt.subplots()
        bar_rects = ax.bar(range(len(collection)), collection, align="edge")

        ax.set_xlim(0, len(collection))
        # Используем максимальное значение, найденное ранее
        ax.set_ylim(0, int(max_value) + 1 if isinstance(max_value, int) else 10)

        def update_fig(step):
            for rect, val in zip(bar_rects, steps[step]):
                rect.set_height(val)

        anim = FuncAnimation(
            fig, update_fig, frames=range(len(steps)), repeat=False, interval=500
        )
        plt.show()


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
    file_path = "list.txt"
    unsorted_data = read_data_from_file(file_path)

    # Простая сортировка пузырьком
    bubble_sort = BubbleSort()
    sorted_data = bubble_sort.sort(list(unsorted_data))
    print("Отсортированный список:", list(sorted_data)[-1])

    # Сортировка пузырьком с сохранением промежуточных состояний
    # bubble_sort_visualization = BubbleSortVisualization()
    # steps = bubble_sort_visualization.sort_with_steps(unsorted_data)
    # print("Промежуточные шаги сортировки:", steps)

    # Визуализация сортировки пузырьком
    # bubble_sort_visualizer = BubbleSortVisualizer()
    # bubble_sort_visualizer.visualize_sort(unsorted_data)


# Вот тут радикс
# https://github.com/navdeep-G/radix-sort-string?ysclid=lty86kkb3h505310552