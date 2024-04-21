import bwt
import struct

def bwt_stream(input_file, output_file, block_size=4096):
    with open(input_file, 'rb') as infile, open(output_file, 'wb') as outfile:
        while True:
            block = infile.read(block_size)
            if not block:
                break

            # Декодирование байтовой строки (используя utf-8)
            block_string = block.decode('utf-8')

            transformed = bwt.bijective_bwt(block_string)

            # Кодирование результата BWT
            transformed_bytes = transformed.encode('utf-8')

            # Запись длины преобразованной строки и преобразованной строки
            outfile.write(struct.pack('>I', len(transformed_bytes)))
            outfile.write(transformed_bytes)

import struct

def dec(input_file, output_file, block_size=4096):
    with open(input_file, 'rb') as infile, open(output_file, 'w', encoding='utf-8') as outfile:
        while True:
            # Чтение длины преобразованной строки из входного файла
            length_bytes = infile.read(4)
            if not length_bytes:
                break
            # Распаковка длины преобразованной строки из байтов в целое число
            length = struct.unpack('>I', length_bytes)[0]
            # Чтение преобразованной строки из входного файла
            transformed_bytes = infile.read(length)
            # Применение обратного преобразования Барроуза-Уилера и декодирование из байтов в строку
            transformed = bwt.bijective_bwt_inv(transformed_bytes.decode())
            # Запись результата в выходной файл
            outfile.write(transformed)


# Пример использования
bwt_stream("input.txt", "comp.bin")
dec("comp.bin", "output_file.txt")
