#include "black_hole_list.h"  // Assuming your header file
#include "test-framework/unity.h"

// ... (Helper functions for creating and comparing black holes)

void test_create_empty_list(void) {
    bh_list_t *list = bh_list_create();
    TEST_ASSERT_NOT_NULL(list);
    TEST_ASSERT_NULL(list->head);
    TEST_ASSERT_NULL(list->tail);
    TEST_ASSERT_EQUAL_UINT(0, bh_list_size(list));
    bh_list_destroy(list);
}

void test_insert_and_sort(void) {
    bh_list_t *list = bh_list_create();
    // ... (Create black holes with different masses and types)
    bh_list_insert(list, bh1);
    bh_list_insert(list, bh2);
    bh_list_insert(list, bh3);
    // ... (Verify the list is sorted by mass)
    bh_list_destroy(list);
}

void test_split_list(void) {
    bh_list_t *list = bh_list_create();
    // ... (Insert black holes of different types)
    bh_list_t *quasars, *blazars, *unknown;
    bh_list_split(list, &quasars, &blazars, &unknown);
    // ... (Verify each list contains the correct black holes and is sorted)
    bh_list_destroy(list);
    bh_list_destroy(quasars);
    bh_list_destroy(blazars);
    bh_list_destroy(unknown);
}

// ... (More test cases for other operations)