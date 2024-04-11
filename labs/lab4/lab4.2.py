import re
import time

def naive_search(text, pattern):
    occurrences = []
    n = len(text)
    m = len(pattern)

    for i in range(n - m + 1):
        if text[i:i+m] == pattern:
            if (i == 0 or not text[i-1].isalpha()) and (i+m == n or not text[i+m].isalpha()):
                occurrences.append(text[i-m:i+m+m])
    return occurrences



def gorners_scheme(text):
    base = 31
    result = ord(text[0])
    for i in range(len(text) - 1):
        result = result * base + ord(text[i + 1])
    return result

def calculate_hash(text):
    q = 2147483647
    return gorners_scheme(text) % q

def rabin_karp_search(text, pattern):
    occurrences = []
    base = 31
    q = 2147483647
    m = len(pattern)
    n = len(text)
    pattern_hash = calculate_hash(pattern)
    text_hash = calculate_hash(text[0:m])

    for i in range(n - m + 1):
        if text_hash == pattern_hash:
            if (i == 0 or not text[i - 1].isalpha()) and (i + m == n or not text[i + m].isalpha()):
                occurrences.append(text[i:i + m])

        if i < n - m:
            text_hash = ((text_hash - ord(text[i]) * base ** (m - 1)) * base + ord(text[i + m])) % q

    return occurrences


with open("ojegov.txt", "r", encoding="utf-8") as file:
    dictionary = file.read()
    count = 0
    for word in dictionary:
        for sym in word:
            count += 1

    print(count)

pattern = "все"

start_time = time.time()
naive_occurrences = naive_search(dictionary, pattern)
naive_time = time.time() - start_time
print("Наивный алгоритм:")
print(f"Количество вхождений слова '{pattern}' как отдельного слова: {len(naive_occurrences)}")
print("Время выполнения:", naive_time)

start_time = time.time()
rk_occurrences = rabin_karp_search(dictionary, pattern)
rk_time = time.time() - start_time
print("\nАлгоритм Рабина-Карпа:")
print(f"Количество вхождений слова '{pattern}' как отдельного слова: {len(rk_occurrences)}")
print("Время выполнения:", rk_time)

with open("output_lab4.txt", "w", encoding="utf-8") as output_file:
    output_file.write("Наивный алгоритм:\n")
    output_file.write(f"Количество вхождений слова '{pattern}' как отдельного слова: {len(naive_occurrences)}")
    output_file.write("\nНайденные вхождения:\n")
    for index, word in enumerate(naive_occurrences):
        output_file.write(f"Позиция {index}: {word}\n")
    output_file.write(f"Время выполнения: {naive_time} сек\n\n")
    output_file.write("Алгоритм Рабина-Карпа:\n")
    output_file.write(f"Количество вхождений слова '{pattern}' как отдельного слова: {len(rk_occurrences)}")
    output_file.write("\nНайденные вхождения:\n")
    for index, word in enumerate(rk_occurrences):
        output_file.write(f"Позиция {index}: {word}\n")
    output_file.write(f"Время выполнения: {rk_time} сек\n")
