class BWT:
    @staticmethod
    def transform(text):
        n = len(text)
        table = sorted(text[i:] + text[:i] for i in range(n))
        last_column = ''.join(row[-1] for row in table)
        index = table.index(text) - 1
        if index < 0 or index >= n:
            raise ValueError("Invalid index obtained from BWT transformation")
        return last_column, index

    @staticmethod
    def inverse_transform(last_column, idx):
        n = len(last_column)
        table = [''] * n
        for i in range(n):
            table = sorted(last_column[j] + table[j] for j in range(n))
        if idx < 0 or idx >= n:
            raise ValueError("Invalid index provided for inverse BWT transformation")
        return table[idx + 1]

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
                if start_idx < 256:  # Ограничиваем индекс до 255
                    dictionary[buffer_plus_char] = start_idx % 256
                    start_idx += 1
                buffer = char

        if buffer:
            result.append(dictionary[buffer])

        return result, dictionary

    @staticmethod
    def decompress(compressed, dictionary):
        max_code = max(compressed)
        reverse_dict = {v: k for k, v in dictionary.items()}
        result = []

        for code in compressed:
            if code < 256:
                result.append(chr(code))
                if len(result) > max_code:
                    break
            else:
                sequence = result[-1] + result[-1][0]
                sequence += reverse_dict.get(code, sequence[0])
                result.append(sequence)

        return ''.join(result)

def simple_archive(text):
    bwt_last_column, bwt_idx = BWT.transform(text)
    compressed_bwt, vitter_dict = Vitter.compress(bwt_last_column)
    return compressed_bwt, bwt_idx, vitter_dict

def simple_dearchive(compressed_bwt, bwt_idx, vitter_dict):
    decompressed_bwt = Vitter.decompress(compressed_bwt, vitter_dict)
    original_text = BWT.inverse_transform(decompressed_bwt, bwt_idx)
    return original_text

def simple_archive_file(input_file, output_file, chunk_size=1024):
    idx, dictionary = None, None
    with open(input_file, 'r', encoding='utf-8') as f_in:
        with open(output_file, 'w', encoding='utf-8') as f_out:
            while True:
                chunk = f_in.read(chunk_size)
                if not chunk:
                    break
                text = chunk.decode('latin1').encode('utf-8', 'replace')
                compressed_chunk, idx, dictionary = simple_archive(text)
                bytes_compressed_chunk = bytes(compressed_chunk)
                f_out.write(bytes_compressed_chunk)
    return idx, dictionary

def simple_archive_file(input_file, output_file, chunk_size=1024):
    idx, dictionary = None, None
    with open(input_file, 'rb') as f_in:
        with open(output_file, 'wb') as f_out:
            while True:
                chunk = f_in.read(chunk_size)
                if not chunk:
                    break
                compressed_chunk, idx, dictionary = simple_archive(chunk)
                f_out.write(bytes(compressed_chunk))
    return idx, dictionary


input_filename = 'random_data.bin'
output_filename = 'compressed_large_file.bin'
idx, dictionary = simple_archive_file(input_filename, output_filename)
print("Файл успешно сжат.")

output_decompressed_filename = 'decompressed_large_file.bin'
simple_dearchive_file(output_filename, output_decompressed_filename, idx, dictionary)
print("Файл успешно распакован.")
