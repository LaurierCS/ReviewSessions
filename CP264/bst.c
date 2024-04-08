#include <stdio.h>
#include <stdlib.h>

typedef struct node {
  int val;
  struct node *left, *right;
} TNODE;

void level_order(TNODE *root) {
  if (root == NULL) {
    return;
  }

  TNODE *queue[100];
  int front = 0, rear = 0;
  queue[rear++] = root;

  while (front != rear) {
    TNODE *node = queue[front++];
    printf("%d ", node->val);

    if (node->left != NULL) {
      queue[rear++] = node->left;
    }

    if (node->right != NULL) {
      queue[rear++] = node->right;
    }
  }
}

TNODE *new_node(int value) {
  TNODE *node = (TNODE *)malloc(sizeof(TNODE));
  node->val = value;
  node->left = NULL;
  node->right = NULL;
  return node;
}

TNODE *insert(TNODE *node, int value) {
  if (node == NULL)
    return new_node(value);

  if (value < node->val) {
    node->left = insert(node->left, value);
  } else if (value > node->val) {
    node->right = insert(node->right, value);
  }

  return node;
}

int main() {
  TNODE *root = NULL;

  int values[7] = {2, 11, 24, 6, 15, 67, -244};

  for (int i = 0; i < 7; i++) {
    root = insert(root, values[i]);
  }

  level_order(root);

  printf("\n");

  return 0;
}
