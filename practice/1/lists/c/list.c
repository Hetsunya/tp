#include "list.h"
#include <stdlib.h>
#include <string.h>

list_t *list_create(size_t data_size) {
  list_t *list = (list_t *)malloc(sizeof(list_t));
  if (list != NULL) {
    list->head = NULL;
    list->data_size = data_size;
  }
  return list;
}

bool list_empty(list_t *list) {
  return list->head == NULL;
}

bool list_contains(list_t *list, void *data) {
  list_node_t *current = list->head;
  while (current != NULL) {
    if (memcmp(current->data, data, list->data_size) == 0) {
      return true;
    }
    current = current->next;
  }
  return false;
}

size_t list_length(list_t *list) {
  size_t length = 0;
  list_node_t *current = list->head;
  while (current != NULL) {
    length++;
    current = current->next;
  }
  return length;
}

size_t list_index(list_t *list, void *data) {
  size_t index = 0;
  list_node_t *current = list->head;
  while (current != NULL) {
    if (memcmp(current->data, data, list->data_size) == 0) {
      return index;
    }
    index++;
    current = current->next;
  }
  return SIZE_MAX;
}

void *list_pop(list_t *list) {
    if (list == NULL || list->head == NULL) {
        return NULL;
    }

    // Find the second-to-last node
    list_node_t *current = list->head;
    list_node_t *previous = NULL;
    while (current->next != NULL) {
        previous = current;
        current = current->next;
    }

    // Handle the case of a single-element list
    if (previous == NULL) {
        list->head = NULL;
    } else {
        previous->next = NULL;
    }

    // Extract data and free the node
    void *data_copy = malloc(list->data_size);
    if (data_copy == NULL) {
        // Handle allocation failure
        return NULL; // Or handle the error appropriately
    }
    memcpy(data_copy, current->data, list->data_size);

    free(current->data);
    free(current);
    return data_copy;
}


void list_append(list_t *list, void *data) {
  list_node_t *new_node = (list_node_t *)malloc(sizeof(list_node_t));
  if (new_node != NULL) {
    new_node->data = malloc(list->data_size);
    if (new_node->data != NULL) {
      memcpy(new_node->data, data, list->data_size);
      new_node->next = NULL;
      if (list_empty(list)) {
        list->head = new_node;
      } else {
        list_node_t *current = list->head;
        while (current->next != NULL) {
          current = current->next;
        }
        current->next = new_node;
      }
    } else {
      free(new_node);
    }
  }
}

void list_remove(list_t *list, void *data) {
  list_node_t *current = list->head;
  list_node_t *previous = NULL;
  while (current != NULL) {
    if (memcmp(current->data, data, list->data_size) == 0) {
      if (previous != NULL) {
        previous->next = current->next;
      } else {
        list->head = current->next;
      }
      free(current->data);
      free(current);
      return;
    }
    previous = current;
    current = current->next;
  }
}

void list_insert(list_t *list, size_t index, void *data) {
    if (!list) {
        printf("Error: Invalid list\n");
        return;
    }

    list_node_t *new_node = (list_node_t *)malloc(sizeof(list_node_t));
    if (!new_node) {
        printf("Error: Memory allocation failed\n");
        return;
    }

    new_node->data = malloc(list->data_size);
    if (!new_node->data) {
        printf("Error: Memory allocation failed\n");
        free(new_node);
        return;
    }

    memcpy(new_node->data, data, list->data_size);
    new_node->next = NULL;

    if (index == 0 || !list->head) {
        new_node->next = list->head;
        list->head = new_node;
        return;
    }

    list_node_t *current = list->head;
    for (size_t i = 0; i < index - 1 && current->next; i++) {
        current = current->next;
    }

    new_node->next = current->next;
    current->next = new_node;
}


void list_destroy(list_t *list) {
  while (list->head != NULL) {
    list_node_t *temp = list->head;
    list->head = list->head->next;
    free(temp->data);
    free(temp);
  }
  free(list);
}

void list_print_int(list_t *list, FILE *file) {
  list_node_t *current = list->head;
  if (current == NULL) {
    fprintf(file, "NULL");
    return;
  }
  fprintf(file, "(");
  while (current != NULL) {
    fprintf(file, "%d", *(int *)(current->data));
    if (current->next != NULL) {
      fprintf(file, ") -> (");
    }
    current = current->next;
  }
  if (current != NULL) {
    free(current);
  }
  fprintf(file, ") -> NULL");
}
