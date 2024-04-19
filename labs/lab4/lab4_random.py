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
    prime = 101  # Простое число для хеширования
    h_power = pow(256, m - 1, prime)
    def calculate_hash(string, length, prime):
        hash_value = 0
        for i in range(length):
            hash_value = (hash_value * 256 + string[i]) % prime
        return hash_value

    def rehash(old_hash, old_char, new_char, length, prime, h_power):
        new_hash = (old_hash - old_char * (256 ** (length - 1))) * 256 + new_char
        return new_hash % prime


    pattern_hash = calculate_hash(pattern, m, prime)
    text_hash = calculate_hash(data, m, prime)

    count = 0
    for i in range(n - m + 1):
        if text_hash == pattern_hash and data[i:i + m] == pattern:
            count += 1
        if i < n - m:
            text_hash = rehash(text_hash, data[i], data[i + m], m, prime, h_power)
    return count


def calculate_probability(dev_urandom_path, output_file_path, patterns):
    with open(dev_urandom_path, 'rb') as file:
        data = file.read(45 * 1024 * 1024)# 63 * 1024 * 1024
        hex_data = ''.join([format(byte, 'x') for byte in data])
        # print(hex_data)
        total_bytes = len(hex_data)


    # with open(output_file_random_path, "w") as out_file:
    #     out_file.write(str(data))

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

            if count_naive == count_rabin_karp:
                probability = count_rabin_karp / total_bytes

            output_file.write(f"Последовательность {pattern} встречается {count_naive} раз (наивный поиск), Время: {time_naive:.6f} секунд\n")
            output_file.write(f"Последовательность {pattern} встречается {count_rabin_karp} раз (алгоритм Рабина-Карпа), Время: {time_rabin_karp:.6f} секунд\n")
            output_file.write(f"Вероятность для последовательности {pattern}: {probability:.10f}\n\n")

if __name__ == "__main__":
    dev_urandom_path = '/dev/random'
    output_file_path = 'output_random.txt'
    # output_file_random_path = 'hexdump.txt'
    patterns_to_search = ['F00D', 'FACE', 'CAFE', "DEAD", "BABE","DEADBE", "CAFEBA"]
    # , "DEADBEEF", "CAFEBABE"

    start_time = time.time()
    calculate_probability(dev_urandom_path, output_file_path, patterns_to_search)
    end_time = time.time()

    print(f"Время выполнения: {end_time - start_time} секунд")
