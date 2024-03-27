import binascii
import os
import time

def naive_search(data, pattern):
    n = len(data)
    m = len(pattern)

    count = 0
    for i in range(n - m + 1):
        if data[i:i+m] == pattern:
            count += 1

    return count

def rabin_karp_search(data, pattern):
    n = len(data)
    m = len(pattern)
    pattern_hash = hash(pattern)

    count = 0
    for i in range(n - m + 1):
        if hash(data[i:i+m]) == pattern_hash:
            if data[i:i+m] == pattern:
                count += 1

    return count

def calculate_probability(dev_urandom_path, output_file_path, patterns):
    with open(dev_urandom_path, 'rb') as file:
        data = file.read(100000000)  # Читаем первые 100 миллионов байт из /dev/urandom
        total_bytes = len(data)

        with open(output_file_path, 'w') as output_file:
            for pattern in patterns:
                pattern_bytes = binascii.unhexlify(pattern)

                start_time_naive = time.time()
                count_naive = naive_search(data, pattern_bytes)
                end_time_naive = time.time()
                time_naive = end_time_naive - start_time_naive

                start_time_rabin_karp = time.time()
                count_rabin_karp = rabin_karp_search(data, pattern_bytes)
                end_time_rabin_karp = time.time()
                time_rabin_karp = end_time_rabin_karp - start_time_rabin_karp

                probability = count_rabin_karp / (total_bytes - len(pattern_bytes) + 1)

                output_file.write(f"Последовательность {pattern} встречается {count_naive} раз (наивный поиск), Время: {time_naive:.6f} секунд\n")
                output_file.write(f"Последовательность {pattern} встречается {count_rabin_karp} раз (алгоритм Рабина-Карпа), Время: {time_rabin_karp:.6f} секунд\n")
                output_file.write(f"Вероятность для последовательности {pattern}: {probability:.10f}\n\n")

if __name__ == "__main__":
    dev_urandom_path = '/dev/random'  # Укажите путь к /dev/urandom на вашей системе
    output_file_path = 'output_random.txt'  # Укажите путь к файлу, в который будет записан вывод
    patterns_to_search = ['F00D', 'FACE', 'CAFE']

    start_time = time.time()
    calculate_probability(dev_urandom_path, output_file_path, patterns_to_search)
    end_time = time.time()

    print(f"Время выполнения: {end_time - start_time} секунд")
