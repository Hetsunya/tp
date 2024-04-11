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
        dictionary = {chr(i): i for i in range(256)}
        result = []
        start_idx = 256

        buffer = ""
        for char in text:
            buffer_plus_char = buffer + char
            if buffer_plus_char in dictionary:
                buffer = buffer_plus_char
            else:
                result.append(dictionary[buffer])
                dictionary[buffer_plus_char] = start_idx
                start_idx += 1
                buffer = char

        if buffer:
            result.append(dictionary[buffer])

        return result, dictionary

    @staticmethod
    def decompress(compressed, dictionary):
        reverse_dict = {v: k for k, v in dictionary.items()}
        result = ""
        previous_code = None

        for code in compressed:
            if code in reverse_dict:
                result += reverse_dict[code]
                if previous_code is not None:
                    dictionary[len(dictionary)] = reverse_dict[previous_code] + reverse_dict[previous_code][0]
            else:
                result += reverse_dict[previous_code] + reverse_dict[previous_code][0]
                dictionary[len(dictionary)] = reverse_dict[previous_code] + reverse_dict[previous_code][0]
            previous_code = code

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
