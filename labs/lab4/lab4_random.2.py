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
    q= 2147483647
    m = len(pattern)
    n = len(text)
    pattern_hash = calculate_hash(pattern)
    text_hash = calculate_hash(text[0:m])

    for i in range(n - m + 1):
        if text_hash == pattern_hash:
            if (i == 0 or not text[i - 1].isalpha()) and (i + m == n or not text[i + m].isalpha()):
                occurrences.append(text[i-m:i+m+m])


        if i < n - m:
            text_hash = ((text_hash - ord(text[i]) * base**(m-1)) * base + ord(text[i + m])) % q
    return occurrences


def calculate_probability(dev_urandom_path, output_file_path, patterns):
    with open(dev_urandom_path, 'rb') as file:
        data = file.read(32 * 1024 * 1024)# 63 * 1024 * 1024
        hex_data = ''.join([format(byte, 'x') for byte in data])  # Преобразовать байты в шестнадцатеричный формат
        # print(hex_data)
        total_bytes = len(hex_data)


    with open(output_file_random_path, "w") as out_file:
        out_file.write(str(data))

    with open(output_file_path, 'w') as output_file:
        for pattern in patterns:
            pattern_bytes = binascii.unhexlify(pattern)

            start_time_naive = time.time()
            count_naive = naive_search(data, pattern_bytes)
            end_time_naive = time.time()
            time_naive = end_time_naive - start_time_naive

            start_time_rabin_karp = time.time()
            count_rabin_karp = rabin_karp_search(data, pattern_bytes)
            print(f"начало измерения{start_time_rabin_karp}")
            end_time_rabin_karp = time.time()
            print(f"конц измерения{end_time_rabin_karp}")
            time_rabin_karp = end_time_rabin_karp - start_time_rabin_karp

            if count_naive == count_rabin_karp:
                probability = count_rabin_karp / (total_bytes - len(pattern_bytes) - 1)

            output_file.write(f"Последовательность {pattern} встречается {count_naive} раз (наивный поиск), Время: {time_naive:.6f} секунд\n")
            output_file.write(f"Последовательность {pattern} встречается {count_rabin_karp} раз (алгоритм Рабина-Карпа), Время: {time_rabin_karp:.6f} секунд\n")
            output_file.write(f"Вероятность для последовательности {pattern}: {probability:.10f}\n\n")

if __name__ == "__main__":
    dev_urandom_path = '/dev/random'
    output_file_path = 'output_random.txt'
    output_file_random_path = 'hexdump.txt'
    patterns_to_search = ['F00D', 'FACE', 'CAFE', "DEAD", "BABE","DEADBEEF", "CAFEBABE"]
    # , "DEADBEEF", "CAFEBABE"

    start_time = time.time()
    calculate_probability(dev_urandom_path, output_file_path, patterns_to_search)
    end_time = time.time()

    print(f"Время выполнения: {end_time - start_time} секунд")
