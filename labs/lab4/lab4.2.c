#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <ctype.h>
#include <time.h>

#define PRIME_BASE 31
#define MODULUS 2147483647

// Function to calculate hash using Horner's scheme
unsigned long gorners_scheme(const char *text) {
    unsigned long result = 0;
    for (int i = 0; text[i] != '\0'; i++) {
        result = (result * PRIME_BASE + text[i]) % MODULUS;
    }
    return result;
}

// Function to perform naive search
int naive_search(const char *text, const char *pattern) {
    int occurrences = 0;
    int n = strlen(text);
    int m = strlen(pattern);

    for (int i = 0; i <= n - m; i++) {
        if (strncmp(text + i, pattern, m) == 0 &&
            (i == 0 || !isalpha(text[i - 1])) &&
            (i + m == n || !isalpha(text[i + m]))) {
            occurrences++;
        }
    }

    return occurrences;
}

// Function to perform Rabin-Karp search
int rabin_karp_search(const char *text, const char *pattern) {
    int occurrences = 0;
    int n = strlen(text);
    int m = strlen(pattern);
    unsigned long pattern_hash = gorners_scheme(pattern);
    unsigned long text_hash = gorners_scheme(text);

    for (int i = 0; i <= n - m; i++) {
        if (text_hash == pattern_hash &&
            (i == 0 || !isalpha(text[i - 1])) &&
            (i + m == n || !isalpha(text[i + m]))) {
            occurrences++;
        }

        if (i < n - m) {
            text_hash = ((text_hash - text[i] * (unsigned long)pow(PRIME_BASE, m - 1)) * PRIME_BASE + text[i + m]) % MODULUS;
        }
    }

    return occurrences;
}

int main() {
    FILE *file = fopen("ojegov.txt", "r");
    if (file == NULL) {
        perror("Error opening file");
        return 1;
    }

    // Read the file into a string (assuming it's not too large)
    fseek(file, 0, SEEK_END);
    long file_size = ftell(file);
    rewind(file);
    char *dictionary = malloc(file_size + 1);
    fread(dictionary, 1, file_size, file);
    dictionary[file_size] = '\0';
    fclose(file);

    clock_t start, end;
    double cpu_time_used;

    start = clock();
    int naive_occurrences = naive_search(dictionary, "все");
    end = clock();
    cpu_time_used = ((double) (end - start)) / CLOCKS_PER_SEC;
    printf("Наивный алгоритм:\n");
    printf("Количество вхождений слова 'все' как отдельного слова: %d\n", naive_occurrences);
    printf("Время выполнения: %f\n", cpu_time_used);

    start = clock();
    int rk_occurrences = rabin_karp_search(dictionary, "все");
    end = clock();
    cpu_time_used = ((double) (end - start)) / CLOCKS_PER_SEC;
    printf("\nАлгоритм Рабина-Карпа:\n");
    printf("Количество вхождений слова 'все' как отдельного слова: %d\n", rk_occurrences);
    printf("Время выполнения: %f\n", cpu_time_used);

    // ... (Code to write results to output_lab4.txt)

    free(dictionary);
    return 0;
}
