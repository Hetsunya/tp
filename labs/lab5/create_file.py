import random

def create_large_file(file_path, num_lines, line_length):
    with open(file_path, 'w') as file:
        for _ in range(num_lines):
            random_line = ''.join(random.choice('abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!@#$%^&*()_+-=[]{}|;:,.<>?') for _ in range(line_length))
            file.write(random_line + '\n')

# Размер файла в мегабайтах
file_size_mb = 100
# Количество строк в файле
num_lines = 100000
# Длина каждой строки
line_length = 1024  # 1 КБ

# Пример использования
file_path = 'large_file.txt'

create_large_file(file_path, num_lines, line_length)

# Проверка размера файла
import os
file_size = os.path.getsize(file_path) / (1024 * 1024)  # в мегабайтах
print(f"File size: {file_size} MB")
