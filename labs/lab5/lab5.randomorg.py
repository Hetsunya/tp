import random
import string
import requests

def generate_unique_strings(num_strings, string_length):
    # Генерируем уникальные случайные числа через random.org
    random_numbers = set()
    while len(random_numbers) < num_strings:
        response = requests.get('https://www.random.org/integers/?num=1&min=0&max=1000000000&col=1&base=10&format=plain&rnd=new')
        number = int(response.text.strip())
        random_numbers.add(number)

    # Генерируем строки на основе уникальных чисел
    result_strings = []
    for number in random_numbers:
        random.seed(number)
        new_string = ''.join(random.choice(string.ascii_letters + string.digits + string.punctuation) for _ in range(string_length))
        result_strings.append(new_string)

    return result_strings

# Пример использования
num_strings = 10000
string_length = 32

generated_strings = generate_unique_strings(num_strings, string_length)

# Записываем строки в файл
file_path = 'unique_strings_file.txt'
with open(file_path, 'w') as file:
    for string in generated_strings:
        file.write(string + '\n')

print(f"File with unique strings generated and saved at {file_path}")
