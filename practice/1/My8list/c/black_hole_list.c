#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <time.h> // Добавьте эту строку для использования srand и time

#include "black_hole_list.h"


char *my_strdup(const char *s) {
    size_t len = strlen(s) + 1;
    char *result = malloc(len);
    if (result == NULL) return NULL;
    return memcpy(result, s, len);
}

black_hole_t *black_hole_create(const char *name, long mass) {
    black_hole_t *new_black_hole = malloc(sizeof(black_hole_t));
    if (new_black_hole != NULL) {
        new_black_hole->name = my_strdup(name);
        new_black_hole->mass = mass;
        new_black_hole->prev = NULL;
        new_black_hole->next = NULL;
    }
    return new_black_hole;
}



void black_hole_destroy(black_hole_t *black_hole) {
    if (black_hole != NULL) {
        free(black_hole->name);
        free(black_hole);
    }
}

black_hole_list_t *black_hole_list_create(void) {
    black_hole_list_t *new_list = (black_hole_list_t *)malloc(sizeof(black_hole_list_t));
    if (new_list != NULL) {
        new_list->head = NULL;
        new_list->tail = NULL;
    }
    return new_list;
}

void black_hole_list_destroy(black_hole_list_t *list) {
    if (list != NULL) {
        while (list->head != NULL) {
            black_hole_t *next = list->head->next;
            black_hole_destroy(list->head);
            list->head = next;
        }
        free(list);
    }
}

int black_hole_list_empty(const black_hole_list_t *list) {
    return (list == NULL || list->head == NULL);
}

void black_hole_list_insert(black_hole_list_t *list, black_hole_t *black_hole) {
    if (list == NULL || black_hole == NULL) {
        return;
    }
    if (list->head == NULL) {
        list->head = black_hole;
        list->tail = black_hole;
    } else {
        list->tail->next = black_hole;
        black_hole->prev = list->tail;
        list->tail = black_hole;
    }
}

void black_hole_list_remove(black_hole_list_t *list, black_hole_t *black_hole) {
    if (list == NULL || black_hole == NULL) {
        return;
    }
    if (black_hole->prev != NULL) {
        black_hole->prev->next = black_hole->next;
    } else {
        list->head = black_hole->next;
    }
    if (black_hole->next != NULL) {
        black_hole->next->prev = black_hole->prev;
    } else {
        list->tail = black_hole->prev;
    }
    black_hole_destroy(black_hole);
}

black_hole_t *black_hole_list_find(const black_hole_list_t *list, const char *name) {
    if (list == NULL) {
        return NULL;
    }
    black_hole_t *current = list->head;
    while (current != NULL) {
        if (strcmp(current->name, name) == 0) {
            return current;
        }
        current = current->next;
    }
    return NULL;
}

black_hole_t *black_hole_list_front(const black_hole_list_t *list) {
    if (list == NULL) {
        return NULL;
    }
    return list->head;
}

black_hole_t *black_hole_list_back(const black_hole_list_t *list) {
    if (list == NULL) {
        return NULL;
    }
    return list->tail;
}
