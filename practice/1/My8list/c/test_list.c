#include "black_hole_list.h"
#include "test-framework/unity.h"
#include "test-framework/unity_fixture.h"
#include <time.h>
#include <stdlib.h> // Добавьте эту строку
#include <string.h> // Добавьте эту строку

#define TIMES_TO_RUN_RANDOM_TESTS 10ul

black_hole_list_t *quasars_list = NULL;
black_hole_list_t *blazars_list = NULL;
black_hole_list_t *no_data_list = NULL;

static void create_lists(void) {
  quasars_list = black_hole_list_create();
  blazars_list = black_hole_list_create();
  no_data_list = black_hole_list_create();
}

static void destroy_lists(void) {
  if (quasars_list) {
    black_hole_list_destroy(quasars_list);
    quasars_list = NULL;
  }
  if (blazars_list) {
    black_hole_list_destroy(blazars_list);
    blazars_list = NULL;
  }
  if (no_data_list) {
    black_hole_list_destroy(no_data_list);
    no_data_list = NULL;
  }
}

TEST_GROUP(Create);

TEST_SETUP(Create) { create_lists(); }

TEST_TEAR_DOWN(Create) { destroy_lists(); }

TEST(Create, CreateEmptyLists) {
  TEST_ASSERT_NOT_NULL(quasars_list);
  TEST_ASSERT_TRUE(black_hole_list_empty(quasars_list));

  TEST_ASSERT_NOT_NULL(blazars_list);
  TEST_ASSERT_TRUE(black_hole_list_empty(blazars_list));

  TEST_ASSERT_NOT_NULL(no_data_list);
  TEST_ASSERT_TRUE(black_hole_list_empty(no_data_list));
}

TEST_GROUP_RUNNER(Create) { RUN_TEST_CASE(Create, CreateEmptyLists); }

TEST_GROUP(Operations);

TEST_SETUP(Operations) { create_lists(); }

TEST_TEAR_DOWN(Operations) { destroy_lists(); }

TEST(Operations, InsertQuasar) {
  // Ensure quasars_list is not NULL
  TEST_ASSERT_NOT_NULL(quasars_list);

  // Insert a quasar
  black_hole_t *quasar = black_hole_create("Quasar", 1000000000);
  black_hole_list_insert(quasars_list, quasar);

  // Ensure the list is not empty after insertion
  TEST_ASSERT_FALSE(black_hole_list_empty(quasars_list));

  // Ensure front element name is correct
  if (!black_hole_list_empty(quasars_list)) {
    TEST_ASSERT_EQUAL_STRING("Quasar", black_hole_list_front(quasars_list)->name);
  }
}


TEST(Operations, RemoveBlazar) {
  // Insert a blazar
  black_hole_t *blazar = black_hole_create("Blazar", 500000000);
  black_hole_list_insert(blazars_list, blazar);

  // Remove the blazar
  black_hole_list_remove(blazars_list, blazar);

  TEST_ASSERT_TRUE(black_hole_list_empty(blazars_list));
}

TEST(Operations, FindBlackHole) {
  // Insert a black hole
  black_hole_t *black_hole = black_hole_create("Black Hole", 2000000000);
  black_hole_list_insert(no_data_list, black_hole);

  // Find the black hole
  black_hole_t *found_black_hole = black_hole_list_find(no_data_list, "Black Hole");

  TEST_ASSERT_NOT_NULL(found_black_hole);
  TEST_ASSERT_EQUAL_STRING("Black Hole", found_black_hole->name);
}

TEST_GROUP_RUNNER(Operations) {
  RUN_TEST_CASE(Operations, InsertQuasar);
  RUN_TEST_CASE(Operations, RemoveBlazar);
  RUN_TEST_CASE(Operations, FindBlackHole);
}

TEST_GROUP(Append);

TEST_SETUP(Append) { create_lists(); }

TEST_TEAR_DOWN(Append) { destroy_lists(); }

TEST(Append, AppendBlackHole) {
  // Insert a black hole
  black_hole_t *black_hole = black_hole_create("Black Hole", 2000000000);
  black_hole_list_insert(no_data_list, black_hole);

  // Ensure the list is not empty after insertion
  TEST_ASSERT_FALSE(black_hole_list_empty(no_data_list));

  // Ensure front and back elements are the same after insertion
  if (!black_hole_list_empty(no_data_list)) {
    TEST_ASSERT_EQUAL_STRING("Black Hole", black_hole_list_front(no_data_list)->name);
    TEST_ASSERT_EQUAL_STRING("Black Hole", black_hole_list_back(no_data_list)->name);
  }
}

TEST_GROUP_RUNNER(Append) { RUN_TEST_CASE(Append, AppendBlackHole); }


TEST_GROUP(Length);

TEST_SETUP(Length) { create_lists(); }

TEST_TEAR_DOWN(Length) { destroy_lists(); }

TEST(Length, ListLength) {
  // Insert some black holes
  black_hole_t *bh1 = black_hole_create("Sagittarius A*", 4.3e6);
  black_hole_list_insert(quasars_list, bh1);

  black_hole_t *bh2 = black_hole_create("M87*", 6.5e9);
  black_hole_list_insert(blazars_list, bh2);

  // Ensure the length of the lists is correct
  TEST_ASSERT_EQUAL_INT(1, black_hole_list_length(quasars_list));
  TEST_ASSERT_EQUAL_INT(1, black_hole_list_length(blazars_list));
  TEST_ASSERT_EQUAL_INT(0, black_hole_list_length(no_data_list));
}

TEST_GROUP_RUNNER(Length) { RUN_TEST_CASE(Length, ListLength); }


TEST_GROUP(Empty);

TEST_SETUP(Empty) { create_lists(); }

TEST_TEAR_DOWN(Empty) { destroy_lists(); }

TEST(Empty, ListNotEmptyAfterInsertion) {
  // Insert a black hole
  black_hole_t *black_hole = black_hole_create("Black Hole", 2000000000);
  black_hole_list_insert(no_data_list, black_hole);

  // Ensure the list is not empty after insertion
  TEST_ASSERT_FALSE(black_hole_list_empty(no_data_list));
}

TEST_GROUP_RUNNER(Empty) { RUN_TEST_CASE(Empty, ListNotEmptyAfterInsertion); }


TEST_GROUP(Contains);

TEST_SETUP(Contains) { create_lists(); }

TEST_TEAR_DOWN(Contains) { destroy_lists(); }

TEST(Contains, ListContainsBlackHole) {
  // Insert a black hole
  black_hole_t *black_hole = black_hole_create("Black Hole", 2000000000);
  black_hole_list_insert(no_data_list, black_hole);

  // Check if the list contains the black hole
  TEST_ASSERT_TRUE(black_hole_list_contains(no_data_list, "Black Hole"));
}

TEST_GROUP_RUNNER(Contains) { RUN_TEST_CASE(Contains, ListContainsBlackHole); }


TEST_GROUP(Index);

TEST_SETUP(Index) {
  create_lists();
  // Insert some black holes
  black_hole_t *bh1 = black_hole_create("Sagittarius A*", 4.3e6);
  black_hole_list_insert(quasars_list, bh1);

  black_hole_t *bh2 = black_hole_create("M87*", 6.5e9);
  black_hole_list_insert(blazars_list, bh2);
}

TEST_TEAR_DOWN(Index) { destroy_lists(); }

TEST(Index, IndexOfBlackHole) {
  // Check the index of black holes in the lists
  TEST_ASSERT_EQUAL_INT(0, black_hole_list_index_of(quasars_list, "Sagittarius A*"));
  TEST_ASSERT_EQUAL_INT(0, black_hole_list_index_of(blazars_list, "M87*"));
  TEST_ASSERT_EQUAL_INT(-1, black_hole_list_index_of(no_data_list, "Black Hole"));
}

TEST_GROUP_RUNNER(Index) { RUN_TEST_CASE(Index, IndexOfBlackHole); }


TEST_GROUP(Pop);

TEST_SETUP(Pop) { create_lists(); }

TEST_TEAR_DOWN(Pop) { destroy_lists(); }

TEST(Pop, PopBlackHole) {
  // Insert a black hole
  black_hole_t *black_hole = black_hole_create("Black Hole", 2000000000);
  black_hole_list_insert(no_data_list, black_hole);

  // Pop the black hole from the list
  black_hole_t *popped = black_hole_list_pop(no_data_list);

  // Ensure the popped black hole is not NULL
  TEST_ASSERT_NOT_NULL(popped);

  // Ensure the popped black hole name is correct
  TEST_ASSERT_EQUAL_STRING("Black Hole", popped->name);

  // Ensure the list is empty after popping
  TEST_ASSERT_TRUE(black_hole_list_empty(no_data_list));

  // Destroy the popped black hole
  black_hole_destroy(popped);
}

TEST_GROUP_RUNNER(Pop) { RUN_TEST_CASE(Pop, PopBlackHole); }


TEST_GROUP(Remove);

TEST_SETUP(Remove) {
  create_lists();
  // Insert some black holes
  black_hole_t *bh1 = black_hole_create("Sagittarius A*", 4.3e6);
  black_hole_list_insert(quasars_list, bh1);

  black_hole_t *bh2 = black_hole_create("M87*", 6.5e9);
  black_hole_list_insert(blazars_list, bh2);
}

TEST_TEAR_DOWN(Remove) { destroy_lists(); }

TEST(Remove, RemoveBlackHole) {
  // Remove black holes from the lists
  black_hole_list_remove(quasars_list, quasars_list->head);
  black_hole_list_remove(blazars_list, blazars_list->head);

  // Ensure the lists are empty after removal
  TEST_ASSERT_TRUE(black_hole_list_empty(quasars_list));
  TEST_ASSERT_TRUE(black_hole_list_empty(blazars_list));
}

TEST_GROUP_RUNNER(Remove) { RUN_TEST_CASE(Remove, RemoveBlackHole); }


TEST_GROUP(Insert);

TEST_SETUP(Insert) { create_lists(); }

TEST_TEAR_DOWN(Insert) { destroy_lists(); }

TEST(Insert, InsertMultipleBlackHoles) {
  // Insert multiple black holes into the lists
  black_hole_t *bh1 = black_hole_create("Sagittarius A*", 4.3e6);
  black_hole_list_insert(quasars_list, bh1);

  black_hole_t *bh2 = black_hole_create("M87*", 6.5e9);
  black_hole_list_insert(blazars_list, bh2);

  // Ensure the lists are not empty after insertion
  TEST_ASSERT_FALSE(black_hole_list_empty(quasars_list));
  TEST_ASSERT_FALSE(black_hole_list_empty(blazars_list));

  // Ensure the lengths of the lists are correct
  TEST_ASSERT_EQUAL_INT(1, black_hole_list_length(quasars_list));
  TEST_ASSERT_EQUAL_INT(1, black_hole_list_length(blazars_list));
}

TEST_GROUP_RUNNER(Insert) { RUN_TEST_CASE(Insert, InsertMultipleBlackHoles); }

// Определение временного файла для записи вывода
#define TMP_FILENAME "tmp_output.txt"

TEST_GROUP(Print);

// Файловый указатель и имя файла для временного файла вывода
FILE *tmp_file;
const char *tmp_filename = TMP_FILENAME;

TEST_SETUP(Print) { create_lists(); }

TEST_TEAR_DOWN(Print) {
  destroy_lists();
  remove(tmp_filename); // Удаление временного файла после завершения теста
}

// Тест для печати пустого списка
TEST(Print, PrintBlackHolesEmptyList) {
  black_hole_list_print(quasars_list); // Печать списка
}

// Тест для печати непустого списка
TEST(Print, PrintBlackHolesNonEmptyList) {
  // Добавление элементов в список
  black_hole_t *bh1 = black_hole_create("Sagittarius A*", 4.3e6);
  black_hole_list_insert(quasars_list, bh1);

  black_hole_t *bh2 = black_hole_create("M87*", 6.5e9);
  black_hole_list_insert(quasars_list, bh2);

  black_hole_list_print(quasars_list); // Печать списка
}

// Запуск тестов Print
TEST_GROUP_RUNNER(Print) {
  RUN_TEST_CASE(Print, PrintBlackHolesEmptyList);
  RUN_TEST_CASE(Print, PrintBlackHolesNonEmptyList);
}


static void run_all_tests(void) {
  // Run tests for the 'Create' test group
  RUN_TEST_GROUP(Create);

  // Run tests for the 'Operations' test group
  RUN_TEST_GROUP(Operations);

  // Run tests for the 'Append' test group
  RUN_TEST_GROUP(Append);

  // Run tests for the 'Length' test group
  RUN_TEST_GROUP(Length);

  // Run tests for the 'Empty' test group
  RUN_TEST_GROUP(Empty);

  // Run tests for the 'Contains' test group
  RUN_TEST_GROUP(Contains);

  // Run tests for the 'Index' test group
  RUN_TEST_GROUP(Index);

  // Run tests for the 'Pop' test group
  RUN_TEST_GROUP(Pop);

  // Run tests for the 'Remove' test group
  RUN_TEST_GROUP(Remove);

  // Run tests for the 'Insert' test group
  RUN_TEST_GROUP(Insert);

  // Run tests for the 'Print' test group
  RUN_TEST_GROUP(Print);
}


int main(int argc, const char *argv[]) {
  srand((unsigned int)time(NULL));
  return UnityMain(argc, argv, run_all_tests);
}
