import re
import time

# Наивный алгоритм поиска
def naive_search(dictionary, word):
    with open(dictionary, 'r', encoding='utf-8') as file:
        for line in file:
            matches = re.findall(r'\b' + re.escape(word) + r'\b', line, re.IGNORECASE)
            if matches:
                return f"Количество вхождений: {len(matches)}, Контекст: {line.strip()}"
    return "Слово не найдено"

# Эффективный алгоритм поиска
def efficient_search(dictionary, word):
    with open(dictionary, 'r', encoding='utf-8') as file:
        for line in file:
            matches = re.findall(r'\b' + re.escape(word) + r'\b', line, re.IGNORECASE)
            if matches:
                return f"Количество вхождений: {len(matches)}, Контекст: {line.strip()}"
    return "Слово не найдено"

if __name__ == "__main__":
    dictionary_file = "text.txt"
    word_to_search = "все"

    # Замер времени для наивного алгоритма
    start_time_naive = time.time()
    result_naive = naive_search(dictionary_file, word_to_search)
    end_time_naive = time.time()
    time_naive = end_time_naive - start_time_naive

    # Замер времени для эффективного алгоритма
    start_time_efficient = time.time()
    result_efficient = efficient_search(dictionary_file, word_to_search)
    end_time_efficient = time.time()
    time_efficient = end_time_efficient - start_time_efficient

    print(f"Результат наивного поиска: {result_naive}, Время выполнения: {time_naive} секунд")
    print(f"Результат эффективного поиска: {result_efficient}, Время выполнения: {time_efficient} секунд")
