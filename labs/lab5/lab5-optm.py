class BWT:
    @staticmethod
    def transform(text):
        n = len(text)
        table = sorted(text[i:] + text[:i] for i in range(n))
        last_column = ''.join(row[-1] for row in table)
        return last_column, table.index(text)

    @staticmethod
    def inverse_transform(last_column, idx):
        n = len(last_column)
        table = [''] * n
        for i in range(n):
            table = sorted(last_column[j] + table[j] for j in range(n))
        return table[idx]

class Vitter:
    @staticmethod
    def compress(text):
        result = bytearray()
        dictionary = [None] * 256
        next_code = 256
        buffer = 0
        buffer_size = 0

        for char in text:
            buffer = (buffer << 8) | ord(char)
            buffer_size += 8

            while buffer_size >= 9:
                code = buffer >> (buffer_size - 9)
                if dictionary[code] is None:
                    result.extend((buffer >> (buffer_size - 8)).to_bytes(1, byteorder='big'))
                    dictionary[code] = next_code
                    next_code += 1
                    buffer_size -= 8
                else:
                    buffer_size -= 9
                buffer &= (1 << buffer_size) - 1

        if buffer_size > 0:
            result.extend((buffer << (8 - buffer_size)).to_bytes(1, byteorder='big'))

        return result


    @staticmethod
    def decompress(compressed):
        dictionary = [chr(i) for i in range(256)]
        result = ""
        buffer = chr(compressed.pop(0))

        for code in compressed:
            if code < len(dictionary):
                entry = dictionary[code]
            elif code == len(dictionary):
                entry = buffer + buffer[0]
            else:
                raise ValueError("Bad compressed code")
            result += entry
            dictionary.append(buffer + entry[0])
            buffer = entry

        return result



def simple_archive(text):
    bwt_last_column, bwt_idx = BWT.transform(text)
    compressed_bwt, vitter_dict = Vitter.compress(bwt_last_column)
    return compressed_bwt, bwt_idx, vitter_dict

def simple_dearchive(compressed_bwt, bwt_idx, vitter_dict):
    decompressed_bwt = Vitter.decompress(compressed_bwt, vitter_dict)
    original_text = BWT.inverse_transform(decompressed_bwt, bwt_idx)
    return original_text



# Считывание текстового файла
input_filename = 'ojegov.txt'
with open(input_filename, 'r') as file:
    text = file.read()

# Сжатие текста
compressed, idx, dictionary = simple_archive(text)
# print("Сжатый текст:", compressed)

# Декомпрессия сжатых данных
decompressed = simple_dearchive(compressed, idx, dictionary)
# print("Исходный текст:", decompressed)

# Запись восстановленного текста обратно в файл
output_filename = 'lab5-ojegov.txt'
with open(output_filename, 'w') as file:
    file.write(decompressed)


# Пример использования:
# text = "exampletext"  # ваш текст
# print("Ориинальный текст", text)
# compressed, idx, dictionary = simple_archive(text)
# print("Сжатый текст:", compressed)
# decompressed = simple_dearchive(compressed, idx, dictionary)
# print("Исходный текст:", decompressed)
