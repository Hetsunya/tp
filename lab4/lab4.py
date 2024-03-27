import re
import time

def naive_search(text, pattern):
    occurrences = []
    n = len(text)
    m = len(pattern)
    for i in range(n - m + 1):
        if text[i:i+m] == pattern and (i == 0 or not text[i-1].isalpha()) and (i+m == n or not text[i+m].isalpha()):
            occurrences.append(i)
    return occurrences

def rabin_karp_search(text, pattern):
    occurrences = []
    n = len(text)
    m = len(pattern)
    prime = 101  # Простое число для вычисления хэша
    pattern_hash = sum(ord(pattern[i]) * (prime ** i) for i in range(m))
    text_hash = sum(ord(text[i]) * (prime ** i) for i in range(m))
    for i in range(n - m + 1):
        if text_hash == pattern_hash and text[i:i+m] == pattern and (i == 0 or not text[i-1].isalpha()) and (i+m == n or not text[i+m].isalpha()):
            occurrences.append(i)
        if i < n - m:
            text_hash = (text_hash - ord(text[i])) // prime + ord(text[i+m]) * (prime ** (m - 1))
    return occurrences

# Считывание словаря Ожегова
with open("ojegov.txt", "r", encoding="utf-8") as file:
    dictionary = file.read()

# Замер времени выполнения для наивного алгоритма
start_time = time.time()
naive_occurrences = naive_search(dictionary, "все")
naive_time = time.time() - start_time
print("Наивный алгоритм:")
print("Количество вхождений слова 'все' как отдельного слова:", len(naive_occurrences))
print("Время выполнения:", naive_time)

# Замер времени выполнения для алгоритма Рабина-Карпа
start_time = time.time()
rk_occurrences = rabin_karp_search(dictionary, "все")
rk_time = time.time() - start_time
print("\nАлгоритм Рабина-Карпа:")
print("Количество вхождений слова 'все' как отдельного слова:", len(rk_occurrences))
print("Время выполнения:", rk_time)

with open("output_lab4.txt", "w", encoding="utf-8") as output_file:
    output_file.write("Наивный алгоритм:\n")
    output_file.write(f"Количество вхождений слова 'все' как отдельного слова: {len(naive_occurrences)}\n")
    output_file.write("Найденные вхождения:\n")
    for index, word in enumerate(naive_occurrences):
        output_file.write(f"Позиция {index}: {word}\n")
    output_file.write(f"Время выполнения: {naive_time} сек\n\n")
    output_file.write("Алгоритм Рабина-Карпа:\n")
    output_file.write(f"Количество вхождений слова 'все' как отдельного слова: {len(rk_occurrences)}\n")
    output_file.write("Найденные вхождения:\n")
    for index, word in enumerate(rk_occurrences):
        output_file.write(f"Позиция {index}: {word}\n")
    output_file.write(f"Время выполнения: {rk_time} сек\n")
