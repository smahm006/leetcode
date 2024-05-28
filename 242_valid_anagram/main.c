/*
Given two strings t and t, return true if t is an anagram of s, and false
otherwise. An Anagram is a word or phrase formed by rearranging the letters of a
different word or phrase, typically using all the original letters exactly once.
*/

#include <stdbool.h>
#include <stdint.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

typedef struct newNode {
  char data;
  struct newNode *next;
} newNode;

static uint64_t hash_key(const char key) {
  const uint64_t FNV_OFFSET = 14695981039346656037UL;
  const uint64_t FNV_PRIME = 1099511628211UL;
  uint64_t hash = FNV_OFFSET;
  hash ^= (uint64_t)(unsigned char)(key);
  hash *= FNV_PRIME;
  return hash;
}

static newNode **convert_to_set(char *arr, size_t arr_size) {
  newNode **linkedLists = calloc(arr_size, sizeof(newNode));
  if (linkedLists == NULL) {
    return NULL;
  }
  for (int i = 0; i < arr_size; i++) {
    uint64_t hash = hash_key(arr[i]);
    int index = (hash % arr_size);
    newNode *current = linkedLists[index];
    bool is_duplicate = false;
    while (current != NULL) {
      if (current->data == arr[i]) {
        is_duplicate = true;
        break;
      }
      current = current->next;
    }
    if (!is_duplicate) {
      newNode *node = malloc(sizeof(newNode));
      if (node == NULL) {
        return NULL;
      }
      node->data = arr[i];
      node->next = linkedLists[index];
      linkedLists[index] = node;
    }
  }
  return linkedLists;
}

static int count_char(char c, char *s) {
  int count = 0;
  for (const char *p = s; *p; p++) {
    if (c == *p) {
      count += 1;
    }
  }
  return count;
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

bool isAnagram(char *s, char *t) {
  size_t lens = strlen(s);
  size_t lent = strlen(t);
  if (lens != lent) {
    return false;
  }
  newNode **set = convert_to_set(s, lens);
  for (int i = 0; i < lens; i++) {
    newNode *current_ll = set[i];
    while (current_ll != NULL) {
      char c = current_ll->data;
      if (count_char(c, s) != count_char(c, t)) {
        return false;
        destroy_set(set, lens);
      }
      current_ll = current_ll->next;
    }
  }
  destroy_set(set, lens);
  return true;
}

bool isAnagramBest(char *s, char *t) {
  int count[256] = {};
  size_t lens = strlen(s);
  size_t lent = strlen(t);
  if (lens != lent) {
    return false;
  }
  for (int i = 0; i < lens; i++) {
    count[(unsigned char)s[i]]++;
    count[(unsigned char)t[i]]--;
  }
  for (int i = 0; i < lens; i++) {
    if (count[(unsigned char)s[i]] != 0) {
      return false;
    }
  }
  return true;
}

int main(void) { printf("\n%d\n", isAnagramBest("anagram", "magaran")); }