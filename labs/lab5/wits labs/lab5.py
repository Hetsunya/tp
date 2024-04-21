import bwt
from collections import Counter
from vitter import ArithmeticCoder
import os

def compress(input_file, output_file, block_size=4096):
    with open(input_file, 'rb') as f_in:
        with open(output_file, 'wb') as f_out:
            # Чтение данных блоками
            while True:
                block = f_in.read(block_size)
                if not block:
                    break

                # Преобразование данных в строку
                block_str = block.decode()

                # Применение BWT к текущему блоку
                transformed, primary_index = bwt.bwt(block_str)

                # Подсчет частот символов в текущем блоке
                frequencies = Counter(transformed)

                # Запись индекса первичной строки и частот символов в файл
                f_out.write(primary_index.to_bytes(4, byteorder='little'))
                for symbol, count in frequencies.items():
                    f_out.write(symbol.to_bytes(1, byteorder='big'))
                    f_out.write(count.to_bytes(4, byteorder='little'))

                # Кодирование с использованием ArithmeticCoder
                encoder = ArithmeticCoder()
                encoder.symbols = frequencies
                for symbol in transformed:
                    encoder.encode_symbol(symbol, f_out)
                encoder.finish_encoding(f_out)

def decompress(input_file, output_file, block_size=4096):
    with open(input_file, 'rb') as f_in:
        with open(output_file, 'wb') as f_out:
            # Чтение данных блоками
            while True:
                # Чтение индекса первичной строки текущего блока
                primary_index = int.from_bytes(f_in.read(4), byteorder='little')
                if not primary_index:
                    break

                # Чтение частот символов текущего блока
                frequencies = {}
                while True:
                    try:
                        symbol = f_in.read(1)
                        count = int.from_bytes(f_in.read(4), byteorder='little')
                        frequencies[symbol] = count
                    except:
                        break

                # Декодирование с использованием ArithmeticCoder
                decoder = ArithmeticCoder()
                decoder.symbols = frequencies
                decoded = []
                while True:
                    try:
                        symbol = decoder.decode_symbol(f_in)
                        decoded.append(symbol)
                    except EOFError:
                        break

                # Обратное BWT преобразование текущего блока
                restored = bwt.ibwt(bytes(decoded), primary_index)

                # Запись восстановленных данных в файл
                f_out.write(restored.encode())

# Пример использования
compress("input.txt", "compressed.bin")
decompress("compressed.bin", "restored.txt")
