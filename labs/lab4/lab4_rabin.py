import binascii
import mmap
import time

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

def calculate_probability(dev_random_path, patterns):
    with open(dev_random_path, 'rb') as file:
        mmapped_file = mmap.mmap(file.fileno(), 0, access=mmap.ACCESS_READ)
        total_bytes = len(mmapped_file)

        for pattern in patterns:
            pattern_bytes = binascii.unhexlify(pattern)
            count = rabin_karp_search(mmapped_file, pattern_bytes)
            probability = count / (total_bytes - len(pattern_bytes) + 1)
            print(f"Последовательность {pattern} встречается {count} раз, Вероятность: {probability:.10f}")

if __name__ == "__main__":
    dev_random_path = '/dev/random'  # Укажите путь к /dev/random на вашей системе
    patterns_to_search = ['F00D', 'FACE', 'DEADBEEF', 'CAFEBABE']

    start_time = time.time()
    calculate_probability(dev_random_path, patterns_to_search)
    end_time = time.time()

    print(f"Время выполнения: {end_time - start_time} секунд")
