/*
Given an integer array nums, return true if any value appears at least twice in
the array, and return false if every element is distinct.
*/

#include <stdbool.h>
#include <stdint.h>
#include <stdio.h>
#include <stdlib.h>

typedef struct newNode {
  int data;
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
bool containsDuplicate(int *nums, int numsSize) {
  newNode **linkedLists = calloc(numsSize, sizeof(newNode *));
  for (int i = 0; i < numsSize; i++) {
    uint64_t hash = hash_key(nums[i]);
    int index = (hash % numsSize);
    newNode *current = linkedLists[index];
    while (current != NULL) {
      if (current->data == nums[i]) {
        free(linkedLists);
        return true;
      }
      current = current->next;
    }
    newNode *node = malloc(sizeof(newNode));
    node->data = nums[i];
    node->next = linkedLists[index];
    linkedLists[index] = node;
  }
  free(linkedLists);
  return false;
}

int main(void) {
  int test[] = {925,  467,  318,  353,  -250, -707, -481, 809,  -718, 982,
                -42,  -550, 530,  951,  -807, -184, 813,  -2,   -666, 368,
                705,  -541, -669, 447,  -116, 56,   -172, -305, -137, -599,
                -269, -347, -811, 479,  -250, -960, -307, 135,  -60,  -97,
                441,  -962, -212, -321, 60,   278,  -394, 50,   968,  -868,
                -768, 882,  615,  -531, 991,  795};
  printf("Contains duplicates?: %d\n",
         containsDuplicate(test, sizeof(test) / sizeof(int)));
}
