#include <stdio.h>
#include <stdlib.h>
#include <fcntl.h>
#include <unistd.h>

#define TARGET_SIZE (10 * 1024 * 1024) // 100 Мб

int main() {
    // Открываем /dev/random для чтения
    int random_fd = open("/dev/random", O_RDONLY);
    if (random_fd < 0) {
        perror("Ошибка открытия /dev/random");
        return 1;
    }

    // Открываем файл для записи
    FILE *output_file = fopen("random_data.bin", "wb");
    if (!output_file) {
        perror("Ошибка открытия файла для записи");
        close(random_fd);
        return 1;
    }

    // Буфер для считываемых данных
    char buffer[1024];
    size_t bytes_written = 0;

    // Считываем данные и записываем их в файл, пока не достигнем TARGET_SIZE
    while (bytes_written < TARGET_SIZE) {
        // Определяем количество байт, которое нужно прочитать
        size_t bytes_to_read = (TARGET_SIZE - bytes_written) > sizeof(buffer) ? sizeof(buffer) : (TARGET_SIZE - bytes_written);

        // Считываем данные из /dev/random
        ssize_t bytes_read = read(random_fd, buffer, bytes_to_read);
        if (bytes_read < 0) {
            perror("Ошибка чтения из /dev/random");
            break;
        }

        // Записываем считанные данные в файл
        fwrite(buffer, 1, bytes_read, output_file);
        bytes_written += bytes_read;
    }

    // Закрываем файл и устройство
    fclose(output_file);
    close(random_fd);

    printf("Файл \"random_data.bin\" создан.\n");

    return 0;
}

