import hashlib
import binascii
import os

def rabin_karp(text, pattern):
    # Размер хэша для сравнения
    hash_pattern = hashlib.md5(pattern.encode()).hexdigest()
    pattern_length = len(pattern)
    text_length = len(text)
    hash_text = hashlib.md5(text[:pattern_length].encode()).hexdigest()

    occurrences = []

    for i in range(text_length - pattern_length + 1):
        if hash_text == hash_pattern:
            if text[i:i + pattern_length] == pattern:
                occurrences.append(i)
        if i < text_length - pattern_length:
            # Обновляем хэш для следующего окна
            hash_text = hashlib.md5(text[i + 1:i + pattern_length + 1].encode()).hexdigest()

    return occurrences

def naive_search(text, pattern):
    pattern_length = len(pattern)
    text_length = len(text)
    occurrences = []

    for i in range(text_length - pattern_length + 1):
        if text[i:i + pattern_length] == pattern:
            occurrences.append(i)

    return occurrences

def calculate_probability(text, pattern):
    # Вычисляем общее количество вхождений
    total_occurrences = len(naive_search(text, pattern))

    # Размер хэша для сравнения
    hash_pattern = hashlib.md5(pattern.encode()).hexdigest()

    # Подсчитываем количество вхождений с помощью алгоритма Рабина-Карпа
    rabin_occurrences = len(rabin_karp(text, pattern))

    # Вычисляем вероятность
    probability = rabin_occurrences / total_occurrences if total_occurrences > 0 else 0

    return probability

def read_hexdump(file_path):
    with open(file_path, 'rb') as f:
        content = binascii.hexlify(f.read()).decode()
    return content

def main():
    file_path = "/dev/random"  # Путь к hexdump /dev/random
    pattern = "F00D"  # Заданная последовательность байтов

    # Чтение hexdump файла
    hexdump_content = read_hexdump(file_path)

    # Вычисление вероятности появления заданной последовательности
    probability = calculate_probability(hexdump_content, pattern)

    print(f"Вероятность появления последовательности {pattern} в {file_path}: {probability}")

if __name__ == "__main__":
    main()
