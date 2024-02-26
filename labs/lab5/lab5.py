import gzip
import os

def compress_file(input_filename, output_filename):
    with open(input_filename, 'rb') as f_in:
        with gzip.open(output_filename, 'wb') as f_out:
            f_out.writelines(f_in)

def decompress_file(input_filename, output_filename):
    with gzip.open(input_filename, 'rb') as f_in:
        with open(output_filename, 'wb') as f_out:
            f_out.write(f_in.read())

def calculate_compression_ratio(original_size, compressed_size):
    compression_ratio = (1 - compressed_size / original_size) * 100
    return compression_ratio

# Пример использования
input_file = 'large_file.txt'
compressed_file = 'compressed_file.gz'
decompressed_file = 'decompressed_file.txt'

# Сжатие файла
compress_file(input_file, compressed_file)

# Распаковка файла
decompress_file(compressed_file, decompressed_file)

# Сравнение файлов с использованием diff
os.system(f'diff {input_file} {decompressed_file}')

# Расчет степени сжатия
original_size = os.path.getsize(input_file)
compressed_size = os.path.getsize(compressed_file)
compression_ratio = calculate_compression_ratio(original_size, compressed_size)

print(f'Compression Ratio: {compression_ratio}%')
