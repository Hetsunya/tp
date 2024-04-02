#include <ctype.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <time.h>

#define PRIME_BASE 31 // Prime base for hash calculations
#define MODULUS 32768 // подели вот это на 2 в случае чего

int naive_search(const char *text, const char *pattern) {
  int occurrences = 0;
  int n = strlen(text);
  int m = strlen(pattern);

  for (int i = 0; i <= n - m; i++)
    if (strncmp(text + i, pattern, m) == 0)
      if ((i == 0 || !isalpha(text[i - 1])) && (i + m == n || !isalpha(text[i + m])))
        occurrences++;

  return occurrences;
}

int rabin_karp_search(const char *text, const char *pattern) {
  int occurrences = 0;
  int n = strlen(text);
  int m = strlen(pattern);

  // Precompute the pattern hash
  unsigned long pattern_hash = 0;
  for (int i = 0; i < m; i++) {
    pattern_hash =
        (pattern_hash * PRIME_BASE + (unsigned char)pattern[i]) % MODULUS;
  }

  // Initialize the rolling hash for the first window
  unsigned long text_hash = 0;
  for (int i = 0; i < m; i++) {
    text_hash = (text_hash * PRIME_BASE + (unsigned char)text[i]) % MODULUS;
  }

  // Iterate through the text, updating the rolling hash efficiently
  for (int i = 0; i <= n - m; i++) {
    // Check for hash match and word boundaries
    if (text_hash == pattern_hash && (i == 0 || !isalpha(text[i - 1])) &&
        (i + m == n || !isalpha(text[i + m]))) {
      occurrences++;
    }

    // Update the rolling hash for the next window (if not at the end)
    if (i < n - m) {
      text_hash = ((text_hash * PRIME_BASE -
                    (unsigned char)text[i] * (PRIME_BASE ^ (m - 1))) +
                   (unsigned char)text[i + m]) %
                  MODULUS;
    }
  }

  return occurrences;
}

int main() {
  // Read the dictionary from the file (replace "ojegov.txt" with your actual
  // file path)
  FILE *file = fopen("ojegov.txt", "r");
  if (file == NULL) {
    printf("Error opening file.\n");
    return 1;
  }

  fseek(file, 0, SEEK_END);
  long file_size = ftell(file);
  rewind(file);

  char *dictionary = malloc(file_size + 1);
  if (dictionary == NULL) {
    printf("Error allocating memory.\n");
    fclose(file);
    return 1;
  }

  fread(dictionary, 1, file_size, file);
  dictionary[file_size] = '\0';
  fclose(file);

  // Measure execution time for naive search
  clock_t start_time = clock();
  int naive_occurrences = naive_search(dictionary, "все");
  double naive_time = (double)(clock() - start_time) / CLOCKS_PER_SEC;
  printf("Наивный алгоритм:\n");
  printf("Количество вхождений слова 'все' как отдельного слова: %d\n",
         naive_occurrences);
  printf("Время выполнения: %f сек\n\n", naive_time);

  // Measure execution time for Rabin-Karp search
  start_time = clock();
  int rk_occurrences = rabin_karp_search(dictionary, "все");
  double rk_time = (double)(clock() - start_time) / CLOCKS_PER_SEC;
  printf("Алгоритм Рабина-Карпа:\n");
  printf("Количество вхождений слова 'все' как отдельного слова: %d\n",
         rk_occurrences);
  printf("Время выполнения: %f сек\n", rk_time);

  // Write results to output file (replace "output_lab4.txt" with your desired
  // file path)
  FILE *output_file = fopen("output_lab4.txt", "w");
  if (output_file == NULL) {
    printf("Error opening output file.\n");
    free(dictionary);
    return 1;
  }

  fprintf(output_file, "Наивный алгоритм:\n");
  fprintf(output_file,
          "Количество вхождений слова 'все' как отдельного слова: %d\n",
          naive_occurrences);
  fprintf(output_file, "Время выполнения: %f сек\n\n", naive_time);

  fprintf(output_file, "Алгоритм Рабина-Карпа:\n");
  fprintf(output_file,
          "Количество вхождений слова 'все' как отдельного слова: %d\n",
          rk_occurrences);
  fprintf(output_file, "Время выполнения: %f сек\n", rk_time);

  fclose(output_file);

  free(dictionary);
  return 0;
}
