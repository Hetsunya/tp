#include <stdio.h>
#include <string.h>
#include <ctype.h>
#include <math.h>
#include <stdlib.h>
#include <time.h>


// Функция наивного поиска
int naive_search(char *text, char *pattern, char **occurrences) {
  int n = strlen(text);
  int m = strlen(pattern);
  int count = 0;
  for (int i = 0; i <= n - m; i++) {
    if (strncmp(text + i, pattern, m) == 0) {
      if ((i == 0 || !isalpha(text[i-1])) && (i + m == n || !isalpha(text[i+m]))) {
        occurrences[count] = text + i - m;
        count++;
      }
    }
  }
  return count;
}

// Функция хеширования по схеме Горнера
long long gorners_scheme(char *text) {
  long long base = 31;
  long long result = text[0];
  for (int i = 1; text[i] != '\0'; i++) {
    result = result * base + text[i];
  }
  return result;
}

// Функция вычисления хеша
long long calculate_hash(char *text) {
  long long q = 2147483647;
  return gorners_scheme(text) % q;
}

// Функция поиска Рабина-Карпа
int rabin_karp_search(char *text, char *pattern, char **occurrences) {
  long long base = 31;
  long long q = 2147483647;
  int m = strlen(pattern);
  int n = strlen(text);
  long long pattern_hash = calculate_hash(pattern);
  long long text_hash = calculate_hash(text);
  int count = 0;

  for (int i = 0; i <= n - m; i++) {
    if (text_hash == pattern_hash) {
      if (strncmp(text + i, pattern, m) == 0) {
        if ((i == 0 || !isalpha(text[i-1])) && (i + m == n || !isalpha(text[i+m]))) {
          occurrences[count] = text + i - m;
          count++;
        }
      }
    }
    if (i < n - m) {
                  text_hash = ((text_hash - text[i] * (long long int)pow(base, m-1)) * base + text[i + m]) % q;
    }
  }
  return count;
}

int main() {
  // Чтение словаря из файла
  FILE *file = fopen("ojegov.txt", "r");
  if (file == NULL) {
    printf("Ошибка открытия файла.\n");
    return 1;
  }
  fseek(file, 0, SEEK_END);
  long fsize = ftell(file);
  fseek(file, 0, SEEK_SET);
  char *dictionary = malloc(fsize + 1);
  fread(dictionary, fsize, 1, file);
  fclose(file);
  dictionary[fsize] = '\0';

  // Подсчет символов
  int count = 0;
  for (int i = 0; dictionary[i] != '\0'; i++) {
    count++;
  }
  printf("Количество символов: %d\n", count);

  char *pattern = "все";

  // Наивный алгоритм
  char *naive_occurrences[1000];
  clock_t start_time = clock();
  int naive_count = naive_search(dictionary, pattern, naive_occurrences);
  clock_t end_time = clock();
  double naive_time = (double)(end_time - start_time) / CLOCKS_PER_SEC;
  printf("\nНаивный алгоритм:\n");
  printf("Количество вхождений: %d\n", naive_count);
  printf("Время выполнения: %f\n", naive_time);

  // Алгоритм Рабина-Карпа
  char *rk_occurrences[1000];
  start_time = clock();
  int rk_count = rabin_karp_search(dictionary, pattern, rk_occurrences);
  end_time = clock();
  double rk_time = (double)(end_time - start_time) / CLOCKS_PER_SEC;
  printf("\nАлгоритм Рабина-Карпа:\n");
  printf("Количество вхождений: %d\n", rk_count);
  printf("Время выполнения: %f\n", rk_time);

  // Запись результатов в файл
  FILE *output_file = fopen("output_lab4.txt", "w");
  if (output_file == NULL) {
    printf("Ошибка открытия файла.\n");
    return 1;
  }
  fprintf(output_file, "Наивный алгоритм:\n");
  fprintf(output_file, "Количество вхождений: %d\n", naive_count);
  fprintf(output_file, "Найденные вхождения:\n");
  for (int i = 0; i < naive_count; i++) {
    fprintf(output_file, "Позиция %d: %s\n", i, naive_occurrences[i]);
  }
  fprintf(output_file, "Время выполнения: %f сек\n\n", naive_time);
  fprintf(output_file, "Алгоритм Рабина-Карпа:\n");
  fprintf(output_file, "Количество вхождений: %d\n", rk_count);
  fprintf(output_file, "Найденные вхождения:\n");
  for (int i = 0; i < rk_count; i++) {
    fprintf(output_file, "Позиция %d: %s\n", i, rk_occurrences[i]);
  }
  fprintf(output_file, "Время выполнения: %f сек\n", rk_time);
  fclose(output_file);

  free(dictionary);
  return 0;
}
