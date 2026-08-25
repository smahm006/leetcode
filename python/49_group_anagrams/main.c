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
  char* key;
  char** value;
  struct newNode *next;
} newNode;

static uint64_t hash_key(const char* key) {
  const uint64_t FNV_OFFSET = 14695981039346656037UL;
  const uint64_t FNV_PRIME = 1099511628211UL;
  uint64_t hash = FNV_OFFSET;
  for (const char *p = key; *p; p++) {
    hash *= FNV_PRIME;
    hash ^= (uint64_t)(p);
  }
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

char* bubble_sort_sting(char* word) {
  size_t lenword = strlen(word);
  char* sorted_word = (char*)malloc(lenword * sizeof(char));
  if (sorted_word == NULL) {
    return NULL;
  }
  strcpy(sorted_word, word);
  for (int i=0; i < lenword; i++) {
    for (int j=1; j < lenword-i; j++) {
      if ((unsigned char)sorted_word[j-1] > (unsigned char)sorted_word[j]) {
        char temp = sorted_word[j];
        sorted_word[j] = sorted_word[j-1];
        sorted_word[j-1] = temp;
      }
    }
  }
  return sorted_word;
}
char* sum_octals(char* word) {
  int total = 0;
  for (const char* p = word; *p; p++) {
    total += (unsigned char)*p;
  }
  char* sorted_word = bubble_sort_sting(word);
  int len_total_string = snprintf(NULL, 0,"%d", total);
  char* total_string = malloc((len_total_string+1) * sizeof(char));
  sprintf(total_string, "%d", total);
  char *result = malloc((strlen(sorted_word) + len_total_string + 1)* sizeof(char));
  strcpy(result, total_string);
  strcat(result, sorted_word);
  free(sorted_word);
  free(total_string);
  return result;
}

char ***groupAnagrams(char **strs, int strsSize, int *returnSize,
                      int **returnColumnSizes) {
  newNode **linkedLists = calloc(strsSize, sizeof(newNode *));
  char **ordstrs = malloc(strsSize * sizeof(char));
  for (int i = 0; i < strsSize; i++) {
    ordstrs[i] = sum_octals(strs[i]);
  }
  for (int i = 0; i < strsSize; i++) {
    uint64_t hash = hash_key(ordstrs[i]);
    int index = (hash % strsSize);

    newNode *current = linkedLists[index];
    while (current != NULL) {
      size_t len_value = sizeof(current->value);
      if (current->key == ordstrs[i]) {
        current->value = realloc(current->value, (len_value+1)*sizeof(char));
        current->value[len_value] = strs[i];
      }
      current = current->next;
    }
    newNode *node = malloc(sizeof(newNode));
    node->key = ordstrs[i];
    char** new_arr = malloc(1*sizeof(char));
    new_arr[0] = strs[i];
    node->value = new_arr;
    node->next = linkedLists[index];
    linkedLists[index] = node;
  }
  char ***ret = malloc(*returnSize * sizeof(char**))
}

int main(void) {
  char *test[] = {"eat", "tea", "tan", "ate", "nat", "bat"};
  int rows;
  int *columns;
  char ***ret = groupAnagrams(test, sizeof(test) / sizeof(int), &rows, &columns);
  for (int i = 0; i < rows; i++) {
    printf("Group %d:\n", i + 1);
    for (int j = 0; j < columns[i]; j++) {
      printf("  %s\n", ret[i][j]);
    }
  }
}
