#include <stdio.h>
#include "black_hole_list.c"

int main() {
    // Create a list of black holes
    black_hole_list_t *list = black_hole_list_create();

    // Create and insert some black holes
    black_hole_t *bh1 = black_hole_create("Sagittarius A*", 4.3e6);
    black_hole_list_insert(list, bh1);

    black_hole_t *bh2 = black_hole_create("M87*", 6.5e9);
    black_hole_list_insert(list, bh2);

    // Print information about the black holes in the list
    printf("Black Holes in the List:\n");
    black_hole_t *current = list->head;
    while (current != NULL) {
        printf("Name: %s, Mass (solar masses): %ld\n", current->name, current->mass);
        current = current->next;
    }

    // Find a specific black hole
    black_hole_t *target = black_hole_list_find(list, "M87*");
    if (target != NULL) {
        printf("\nFound black hole: %s\n", target->name);
    } else {
        printf("\nBlack hole not found.\n");
    }

    // Remove a black hole
    black_hole_list_remove(list, bh1);

    // Destroy the list and free memory
    black_hole_list_destroy(list);

    return 0;
}
