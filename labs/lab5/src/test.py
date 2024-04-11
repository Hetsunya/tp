import heapq
import struct

class BWT:
    def __init__(self, input_string):
        self.input_string = input_string + '\0'  # Добавляем символ конца строки
        self.bwt_result, self.original_index = self._transform()

    def _transform(self):
        table = sorted(self.input_string[i:] + self.input_string[:i] for i in range(len(self.input_string)))
        last_column = ''.join(row[-1] for row in table)
        original_index = table.index(self.input_string)
        return last_column, original_index

class VitterEncoder:
    def __init__(self):
        self.symbol_count = {}
        self.codewords = {}
        self.next_codeword = 0
        self.current_codeword_length = 1

    def encode(self, symbol):
        if symbol not in self.symbol_count:
            self.symbol_count[symbol] = 0
            self.codewords[symbol] = ()
        self.symbol_count[symbol] += 1

        if len(self.codewords) == 2 ** self.current_codeword_length:
            self._update_codewords()

        return self.codewords[symbol]

    def _update_codewords(self):
        heap = [(count, symbol) for symbol, count in self.symbol_count.items()]
        heapq.heapify(heap)

        while len(heap) > 1:
            count1, symbol1 = heapq.heappop(heap)
            count2, symbol2 = heapq.heappop(heap)
            for symbol in symbol1:
                self.codewords[symbol] = (0,) + self.codewords[symbol]
            for symbol in symbol2:
                self.codewords[symbol] = (1,) + self.codewords[symbol]
            heapq.heappush(heap, (count1 + count2, symbol1 + symbol2))

        self.current_codeword_length += 1

def encode(input_string):
    bwt = BWT(input_string)
    encoder = VitterEncoder()

    encoded_bits = ''
    for symbol in bwt.bwt_result:
        encoded_bits += ''.join(str(bit) for bit in encoder.encode(symbol))

    return struct.pack('I', bwt.original_index) + bytes(int(encoded_bits[i:i+8], 2) for i in range(0, len(encoded_bits), 8))

def decode(encoded_bytes):
    original_index = struct.unpack('I', encoded_bytes[:4])[0]
    encoded_bits = ''.join('{:08b}'.format(byte) for byte in encoded_bytes[4:])

    # Декодирование с использованием алгоритма Виттера
    result = ''
    symbol_count = {}
    current_codeword_length = 1

    for bit in encoded_bits:
        if len(symbol_count) == 2 ** current_codeword_length:
            current_codeword_length += 1

        result += bit
        symbol = ''.join(result)
        if symbol not in symbol_count:
            symbol_count[symbol] = 0
        symbol_count[symbol] += 1

    symbol_table = sorted(symbol_count.keys(), key=lambda s: [symbol_count[s], s])
    bites = symbol_table[original_index].rstrip('\0')
    original_string = bits_to_string(bites)
    return original_string

def bits_to_string(bits):
    # Добавляем нули слева, чтобы дополнить последовательность до кратного 8
    while len(bits) % 8 != 0:
        bits = '0' + bits

    # Разбиваем последовательность на байты (по 8 битов в каждом)
    bytes_list = [bits[i:i+8] for i in range(0, len(bits), 8)]

    # Преобразуем каждый байт в символ ASCII и объединяем в строку
    result = ''.join(chr(int(byte, 2)) for byte in bytes_list)

    return result

# Пример использования
input_string = "hello world"
encoded_bytes = encode(input_string)
decoded_string = decode(encoded_bytes)

print("Original:", input_string)
print("Encoded Bytes:", encoded_bytes)
print("Decoded:", decoded_string)
