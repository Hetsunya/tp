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


static void run_all_tests(void) {
  // Run tests for the 'Create' test group
  RUN_TEST_GROUP(Create);

  // Run tests for the 'Operations' test group
  RUN_TEST_GROUP(Operations);
}


int main(int argc, const char *argv[]) {
  srand((unsigned int)time(NULL));
  return UnityMain(argc, argv, run_all_tests);
}
