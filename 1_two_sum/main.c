/*
Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

You can return the answer in any order.
*/

#include <stdbool.h>
#include <stdint.h>
#include <stdio.h>
#include <stdlib.h>

typedef struct newNode {
  int key;
  int value;
  struct newNode *next;
} newNode;

static uint64_t hash_key(const int key) {
  const uint64_t FNV_OFFSET = 14695981039346656037UL;
  const uint64_t FNV_PRIME = 1099511628211UL;
  uint64_t hash = FNV_OFFSET;
  hash *= FNV_PRIME;
  hash ^= (uint64_t)(key);
  return hash;
}

static void destroy_set(newNode **set, size_t set_size) {
  for (int i = 0; i < set_size; i++) {
    newNode *current_ll = set[i];
    while (current_ll != NULL) {
      newNode *temp = current_ll;
      current_ll = current_ll->next;
      free(temp);
    }
  }
  free(set);
}

int key_in_hashmap(int val, newNode **arr, size_t arr_size) {
  for (int i = 0; i < sizeof(arr_size); i++) {
    uint64_t hash = hash_key(val);
    int index = (hash % arr_size);
    newNode *current = arr[index];
    while (current != NULL) {
      if (current->key == val) {
        return current->value;
      }
      current = current->next;
    }
  }
  return -1;
}

int *twoSum(int *nums, int numsSize, int target, int *returnSize) {
  newNode **linkedLists = calloc(numsSize, sizeof(newNode *));
  int *ret = malloc(*returnSize * sizeof(int));
  for (int i = 0; i < numsSize; i++) {
    int diff = target - nums[i];
    int found = key_in_hashmap(diff, linkedLists, numsSize);
    if (found != -1) {
      ret[0] = i;
      ret[1] = found;
      return ret;
    } else {
      uint64_t hash = hash_key(nums[i]);
      int index = (hash % numsSize);
      newNode *current = linkedLists[index];
      while (current != NULL) {
        current = current->next;
      }
      newNode *node = malloc(sizeof(newNode));
      node->key = nums[i];
      node->value = i;
      node->next = linkedLists[index];
      linkedLists[index] = node;
    }
  }
  return ret;
}

int main(void) {
  int test[] = {2, 7, 11, 15};
  int size = 2;
  int* ret = twoSum(test, sizeof(test) / sizeof(int), 9, &size);
  printf("[%d, %d]\n", ret[0], ret[1]);

}
