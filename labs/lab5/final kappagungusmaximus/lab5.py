class VitterCompression:
    def __init__(self):
        self.compressed_sequence = []
        self.current_value = None
        self.bit_length = 0

    def compress(self, data):
        for byte in data:
            if byte == self.current_value:
                self.bit_length += 1
            else:
                if self.bit_length > 0:
                    self.compressed_sequence.append((self.current_value, self.bit_length))
                self.current_value = byte
                self.bit_length = 1
        # Добавляем последний символ в последовательность
        self.compressed_sequence.append((self.current_value, self.bit_length))

    def decompress(self):
        decompressed_data = bytearray()
        for value, length in self.compressed_sequence:
            decompressed_data.extend([value] * length)
        return decompressed_data

# Сжатие файла
def compress_file(input_file, output_file):
    with open(input_file, "rb") as f:
        data = f.read()
    compressor = VitterCompression()
    compressor.compress(data)
    with open(output_file, "wb") as f:
        for value, length in compressor.compressed_sequence:
            f.write(bytes([value]) + b":" + str(length).encode() + b"\n")

# Распаковка файла
def decompress_file(input_file, output_file):
    with open(input_file, "rb") as f:
        compressed_data = f.read().splitlines()
    decompressed_data = bytearray()
    for line in compressed_data:
        value, length = line.split(b":")
        decompressed_data.extend(bytes([int(value)]) * int(length))
    with open(output_file, "wb") as f:
        f.write(decompressed_data)

# Пример использования сжатия файла
if __name__ == "__main__":
    input_file = "input.txt"
    compressed_file = "compressed.bin"
    decompressed_file = "decompressed.txt"

    # Сжимаем файл
    compress_file(input_file, compressed_file)
    print("Файл успешно сжат.")

    # Распаковываем файл
    decompress_file(compressed_file, decompressed_file)
    print("Файл успешно распакован.")
