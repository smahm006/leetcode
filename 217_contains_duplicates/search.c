#include <stdio.h>
#include <stdlib.h>
#include <string.h>

typedef struct {
    char* key;
    int value;
} item;

item* linear_search(item* items, size_t size, const char* key) {
    for (size_t i=0; i<size; i++) {
        if (strcmp(items[i].key, key) == 0) {
            return &items[i];
        }
    }
    return NULL;
}

item* binary_search(item* items, size_t size, const char* key) {
  if (size + size < size) {
    return NULL; // size too big; avoid overflow
  }
  while(size != 0) {
    int mid_index = size/2;
    item mid_val = items[mid_index];
    item *half_array = malloc(mid_index * sizeof(item));
    if(strcmp(mid_val.key,key) > 0) {
      memcpy(half_array, items, mid_index * sizeof(item));
    } else if (strcmp(mid_val.key, key) < 0){
      memcpy(half_array, &items[mid_index + 1], mid_index * sizeof(item));
    } else {
      return &items[mid_index];
    }
    items = half_array;
    size = mid_index;
    }
  return NULL;
}

int main(int argc, char* argv[]) {
    item items[] = {
    {"alice", 1}, {"bar", 42}, {"bazz", 36}, {"bob", 11}, {"buzz", 7},
    {"charlie", 2}, {"david", 3}, {"emma", 4}, {"fred", 5}, {"george", 6},
    {"harry", 8}, {"irene", 9}, {"jane", 100}, {"kate", 12}, {"lucy", 13},
    {"mike", 14}, {"nancy", 15}, {"oliver", 16}, {"peter", 17}, {"quinn", 18}
    };
    size_t num_items = sizeof(items) / sizeof(item);

    item* found_linear = linear_search(items, num_items, "bob");
    if (!found_linear) {
        return 1;
    }
    printf("linear_search: value of 'bob' is %d\n", found_linear->value);
    item* found_binary = binary_search(items, num_items, "bob");
    if (!found_binary) {
        return 1;
    }
    printf("binary_search: value of 'bob' is %d\n", found_binary->value);
    return 0;
}
