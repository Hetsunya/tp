class ArithmeticCoder:
    def __init__(self, precision=32):
        self.precision = precision
        self.one = 1 << precision
        self.quarter = self.one >> 2
        self.half = self.one >> 1
        self.threequarters = self.quarter + self.half
        self.low = 0
        self.high = self.one
        self.symbols = {}

    def encode_symbol(self, symbol, f):
        # Получение диапазона символа
        total = sum(self.symbols.values())
        symlow = sum(self.symbols[s] for s in self.symbols if s < symbol)
        symhigh = symlow + self.symbols[symbol]

        # Обновление диапазона
        newlow = self.low + (self.high - self.low) * symlow // total
        newhigh = self.low + (self.high - self.low) * symhigh // total
        self.low = newlow
        self.high = newhigh

        # Перенос битов
        while ((self.low ^ self.high) & self.half) == 0:
            bit = self.low >> (self.precision - 1)
            f.write(bit.to_bytes(1, byteorder='big'))
            for _ in range(self.precision - 1):
                f.write((bit ^ 1).to_bytes(1, byteorder='big'))
            self.low = (self.low << 1) & (self.one - 1)
            self.high = ((self.high << 1) & (self.one - 1)) | 1

        while self.low >= self.quarter and self.high < self.threequarters:
            self.low = (self.low - self.quarter) << 1
            self.high = ((self.high - self.quarter) << 1) | 1

    def finish_encoding(self, f):
        # Запись оставшихся битов
        f.write((self.low >> (self.precision - 2)).to_bytes(1, byteorder='big'))
        for _ in range(self.precision - 2):
            f.write((self.low >> (self.precision - 3)).to_bytes(1, byteorder='big'))

    def decode_symbol(self, f):
        # Чтение битов для получения значения
        value = 0
        for i in range(self.precision):
            value = 2 * value + int.from_bytes(f.read(1), byteorder='big')

        # Поиск символа
        total = sum(self.symbols.values())
        symlow = 0
        symhigh = 0
        for symbol, count in self.symbols.items():
            symhigh = symlow + count
            if symlow <= value * total < symhigh:
                break
            symlow = symhigh

        # Обновление диапазона
        newlow = self.low + (self.high - self.low) * symlow // total
        newhigh = self.low + (self.high - self.low) * symhigh // total
        self.low = newlow
        self.high = newhigh

        # Перенос битов
        while ((self.low ^ self.high) & self.half) == 0:
            self.low = (self.low << 1) & (self.one - 1)
            self.high = ((self.high << 1) & (self.one - 1)) | 1
            value = 2 * (value & self.half) + int.from_bytes(f.read(1), byteorder='big')

        while self.low >= self.quarter and self.high < self.threequarters:
            self.low = (self.low - self.quarter) << 1
            self.high = ((self.high - self.quarter) << 1) | 1
            value = 2 * (value - self.quarter) + int.from_bytes(f.read(1), byteorder='big')

        return symbol
