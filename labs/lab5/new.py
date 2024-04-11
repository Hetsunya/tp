import os

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
            result.append(Vitter._elias_gamma_encode(dictionary[buffer]))
            if buffer_plus_char in dictionary:
                buffer = buffer_plus_char
            else:
                result.append(dictionary[buffer])
                dictionary[buffer_plus_char] = start_idx
                start_idx += 1
                buffer = char

        if buffer:
            result.append(Vitter._elias_gamma_encode(dictionary[buffer]))

        return result, dictionary

    @staticmethod
    def _elias_gamma_encode(value):
        binary_value = bin(value)[2:]  # Convert to binary string (without '0b' prefix)
        unary_code = '0' * (len(binary_value) - 1)  # Unary code for the length
        return unary_code + binary_value



    @staticmethod
    def decompress(compressed, dictionary):
        reverse_dict = {v: k for k, v in dictionary.items()}
        result = ""
        previous_code = None

        buffer = ""
        for bit in ''.join(compressed):  # Join compressed codes into a bit string
            buffer += bit
            if buffer.endswith('1'):  # Check for the end of a code
                code_length = len(buffer) - 1  # Length of the binary part
                value = int(buffer[code_length:], 2)  # Decode binary part

        for code in compressed:
            if code in reverse_dict:
                result += reverse_dict[code]
                if previous_code is not None:
                    dictionary[len(dictionary)] = reverse_dict[previous_code] + reverse_dict[previous_code][0]
            else:
                result += reverse_dict[previous_code] + reverse_dict[previous_code][0]
                dictionary[len(dictionary)] = reverse_dict[previous_code] + reverse_dict[previous_code][0]
            previous_code = code

        buffer = ""


        return result

def archive(input_filename, output_filename, chunk_size=1024):
    idx, dictionary = None, None
    with open(input_filename, 'rb') as f_in, open(output_filename, 'wb') as f_out:
        while True:
            chunk = f_in.read(chunk_size)
            if not chunk:
                break
            text = chunk.decode('latin1')  # Assuming Latin-1 encoding
            compressed_chunk, idx, dictionary = simple_archive(text)
# Write compressed data to file (using variable-length encoding)
            for code in compressed_chunk:
                f_out.write(bytes(code, 'utf-8'))  # Write each encoded code as bytes


            compressed_chunk_bytes = bytes(compressed_chunk)
            f_out.write(len(compressed_chunk_bytes).to_bytes(4, byteorder='big'))  # Запись длины сжатого блока в 4 байта
            f_out.write(compressed_chunk_bytes)  # Запись сжатого блока данных

    return idx, dictionary

def dearchive(input_filename, output_filename, idx, dictionary, chunk_size=1024):
    with open(input_filename, 'rb') as f_in, open(output_filename, 'wb') as f_out:
        while True:
            compressed_chunk = []
            while True:
                char = f_in.read(1)
                if not char:
                    break
                compressed_chunk.append(char.decode('utf-8'))  # Read and decode each byte

            compressed_chunk_len_bytes = f_in.read(4)  # Чтение 4 байт длины сжатого блока
            if not compressed_chunk_len_bytes:
                break  # Если достигнут конец файла, выходим из цикла
            compressed_chunk_len = int.from_bytes(compressed_chunk_len_bytes, byteorder='big')  # Преобразование байт в число
            compressed_chunk = f_in.read(compressed_chunk_len)  # Чтение сжатого блока
            decompressed_chunk = simple_dearchive(compressed_chunk, idx, dictionary)
            f_out.write(bytes(decompressed_chunk, 'latin1'))

def simple_archive(text):
    bwt_last_column, bwt_idx = BWT.transform(text)
    compressed_bwt, vitter_dict = Vitter.compress(bwt_last_column)
    return compressed_bwt, bwt_idx, vitter_dict

def simple_dearchive(compressed_bwt, bwt_idx, vitter_dict):
    decompressed_bwt = Vitter.decompress(compressed_bwt, vitter_dict)
    original_text = BWT.inverse_transform(decompressed_bwt, bwt_idx)
    return original_text

# Example Usage
input_filename = '/dev/random'
output_filename = 'compressed_random.bin'

idx, dictionary = archive(input_filename, output_filename)
print("File compressed successfully.")

output_decompressed_filename = 'decompressed_random.bin'
dearchive(output_filename, output_decompressed_filename, idx, dictionary)
print("File decompressed successfully.")
