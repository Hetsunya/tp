import struct

# Функция для выполнения BWT на заданных байтовых данных
def bwt(input_bytes):
    rotations = [input_bytes[i:] + input_bytes[:i] for i in range(len(input_bytes))]
    sorted_rotations = sorted(rotations)
    bwt_transform = bytes(rotation[-1] for rotation in sorted_rotations)
    return bwt_transform, sorted_rotations.index(input_bytes)


# Функция для обратного преобразования BWT
def reverse_bwt(bwt_bytes, index):
    table = [b''] * len(bwt_bytes)  # Создаем список байтовых строк
    for i in range(len(bwt_bytes)):
        # Преобразуем строку в байтовую строку перед объединением
        table = sorted(b'%s%s' % (bytes([bwt_bytes[i]]), table[i]) for i in range(len(bwt_bytes)))
    original_data = table[index]
    return original_data



# Функция для сжатия данных с использованием BWT
def compress_file(input_file, output_file):
    with open(input_file, "rb") as f_in:
        with open(output_file, "wb") as f_out:
            block_size = 1024  # Размер блока данных для обработки BWT (можно настроить)
            while True:
                data_block = f_in.read(block_size)
                if not data_block:
                    break

                bwt_transform, index = bwt(data_block)
                f_out.write(struct.pack('I', index))
                f_out.write(bwt_transform)


# Функция для распаковки сжатых данных
def decompress_file(input_file, output_file):
    with open(input_file, "rb") as f_in:
        with open(output_file, "wb") as f_out:
            while True:
                index_bytes = f_in.read(4)
                if not index_bytes:
                    break

                index = struct.unpack('I', index_bytes)[0]
                bwt_transform = f_in.read()
                original_data = reverse_bwt(bwt_transform, index)
                f_out.write(original_data)


# Пример использования:
input_filename = 'diff.txt'  # Путь к вашему файлу с данными из /dev/random
compressed_filename = 'compressed_random.txt'
decompressed_filename = 'decompressed_random.txt'

# Сжатие данных из файла
compress_file(input_filename, compressed_filename)

# Распаковка сжатых данных
decompress_file(compressed_filename, decompressed_filename)
