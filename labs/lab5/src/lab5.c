#include <stdio.h>
#include <stdlib.h>
#include <string.h>

#define BUFFER_SIZE 4096
#define ALPHABET_SIZE 1024

// Функция для применения преобразования BWT
void apply_bwt(char *input, int length) {
    char *bwt_matrix[length];

    // Создание матрицы сдвигов
    for (int i = 0; i < length; i++) {
        bwt_matrix[i] = input + i;
    }

    // Сортировка матрицы по сдвигам
    qsort(bwt_matrix, length, sizeof(char *),
          [](const void *a, const void *b) -> int {
              return strcmp(*(const char **)a, *(const char **)b);
          });

    // Получение последнего столбца матрицы
    for (int i = 0; i < length; i++) {
        input[i] = *(bwt_matrix[i] + length - 1);
    }
}

// Функция для применения преобразования MTF
void apply_mtf(char *input, int length) {
    char alphabet[ALPHABET_SIZE];
    for (int i = 0; i < ALPHABET_SIZE; i++) {
        alphabet[i] = i;
    }

    for (int i = 0; i < length; i++) {
        char current = input[i];
        int j;
        for (j = 0; j < ALPHABET_SIZE; j++) {
            if (alphabet[j] == current) {
                input[i] = j;
                break;
            }
        }
        // Перемещение символа вперед в алфавите
        for (int k = j; k > 0; k--) {
            alphabet[k] = alphabet[k - 1];
        }
        alphabet[0] = current;
    }
}

// Функция для обратного преобразования MTF
void reverse_mtf(char *input, int length) {
    char alphabet[ALPHABET_SIZE];
    for (int i = 0; i < ALPHABET_SIZE; i++) {
        alphabet[i] = i;
    }

    for (int i = 0; i < length; i++) {
        int index = input[i];
        char current = alphabet[index];
        input[i] = current;

        // Перемещение символа вперед в алфавите
        for (int j = index; j > 0; j--) {
            alphabet[j] = alphabet[j - 1];
        }
        alphabet[0] = current;
    }
}

// Функция для обратного преобразования BWT
void reverse_bwt(char *input, int length) {
    int count[length][2];

    // Инициализация счетчика
    for (int i = 0; i < length; i++) {
        count[i][0] = count[i][1] = 0;
    }

    // Подсчет количества каждого символа
    for (int i = 0; i < length; i++) {
        count[i][0] = input[i];
        count[i][1] = i;
    }

    // Сортировка счетчика по символам
    qsort(count, length, sizeof(count[0]),
          [](const void *a, const void *b) -> int {
              return (*(const int (*)[2])a)[0] - (*(const int (*)[2])b)[0];
          });

    // Восстановление исходной строки из последнего столбца и счетчика
    for (int i = 0, j = 0; i < length; i++) {
        j = count[j][1];
        input[i] = count[j][0];
    }
}

// Функция для сжатия файла с использованием BWT и MTF
void compress_file(const char *input_filename, const char *output_filename) {
    FILE *input_file = fopen(input_filename, "r");
    FILE *output_file = fopen(output_filename, "wb");
    if (!input_file || !output_file) {
        printf("Ошибка открытия файлов\n");
        return;
    }

    // Чтение содержимого файла в память
    char buffer[BUFFER_SIZE];
    size_t bytes_read;
    while ((bytes_read = fread(buffer, 1, BUFFER_SIZE, input_file)) > 0) {
        // Применение BWT к содержимому файла
        apply_bwt(buffer, bytes_read);
        // Применение MTF к результату BWT
        apply_mtf(buffer, bytes_read);
        // Запись сжатых данных в файл
        fwrite(buffer, 1, bytes_read, output_file);
    }

    fclose(input_file);
    fclose(output_file);
}

// Функция для декомпрессии файла с использованием BWT и MTF
void decompress_file(const char *input_filename, const char *output_filename) {
    FILE *input_file = fopen(input_filename, "rb");
    FILE *output_file = fopen(output_filename, "w");
    if (!input_file || !output_file) {
        printf("Ошибка открытия файлов\n");
        return;
    }

    // Чтение сжатых данных из файла в память
    char buffer[BUFFER_SIZE];
    size_t bytes_read;
    while ((bytes_read = fread(buffer, 1, BUFFER_SIZE, input_file)) > 0) {
        // Применение обратного MTF к сжатым данным
        reverse_mtf(buffer, bytes_read);
        // Применение обратного BWT к результату MTF
        reverse_bwt(buffer, bytes_read);
        // Запись восстановленного содержимого файла
        fwrite(buffer, 1, bytes_read, output_file);
    }

    fclose(input_file);
    fclose(output_file);
}

int main(int argc, char *argv[]) {
    if (argc != 4) {
        printf("Использование: %s <команда> <входной файл> <выходной файл>\n", argv[0]);
        printf("Команды:\n");
        printf("  compress   - для сжатия файла\n");
        printf("  decompress - для декомпрессии файла\n");
        return 1;
    }

    if (strcmp(argv[1], "compress") == 0) {
        compress_file(argv[2], argv[3]);
    } else if (strcmp(argv[1], "decompress") == 0) {
        decompress_file(argv[2], argv[3]);
    } else {
        printf("Неверная команда: %s\n", argv[1]);
        return 1;
    }

    return 0;
}
