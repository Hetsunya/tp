#ifndef BLACK_HOLE_LIST_H
#define BLACK_HOLE_LIST_H

typedef struct black_hole {
    char *name;
    long mass;
    struct black_hole *prev;
    struct black_hole *next;
} black_hole_t;

typedef struct {
    black_hole_t *head;
    black_hole_t *tail;
} black_hole_list_t;

char *my_strdup(const char *s);
black_hole_t *black_hole_create(const char *name, long mass);
void black_hole_destroy(black_hole_t *black_hole);
black_hole_list_t *black_hole_list_create(void);
void black_hole_list_destroy(black_hole_list_t *list);
int black_hole_list_empty(const black_hole_list_t *list);
void black_hole_list_insert(black_hole_list_t *list, black_hole_t *black_hole);
void black_hole_list_remove(black_hole_list_t *list, black_hole_t *black_hole);
black_hole_t *black_hole_list_find(const black_hole_list_t *list, const char *name);
black_hole_t *black_hole_list_front(const black_hole_list_t *list);
black_hole_t *black_hole_list_back(const black_hole_list_t *list);
black_hole_t *black_hole_list_pop(black_hole_list_t *list);
int black_hole_list_length(const black_hole_list_t *list);
int black_hole_list_contains(const black_hole_list_t *list, const char *name);
void black_hole_list_print(const black_hole_list_t *list);
int black_hole_list_index_of(const black_hole_list_t *list, const char *name);
#endif /* BLACK_HOLE_LIST_H */
