#include <stdio.h>
#include <stdlib.h>

struct Node {
  int key;
  struct Node *left;
  struct Node *right;
  int height;
};

int height(struct Node *node) {
  if (node == NULL) {
    return 0;
  }
  return node->height;
}

int max(int a, int b) { return (a > b) ? a : b; }

struct Node *new_node(int key) {
  struct Node *node = (struct Node *)malloc(sizeof(struct Node));
  node->key = key;
  node->left = NULL;
  node->right = NULL;
  node->height = 1;
  return node;
}

struct Node *right_rotate(struct Node *y) {
  struct Node *x = y->left;
  struct Node *temp = x->right;

  // perform rotation
  x->right = y;
  y->left = temp;

  // update heights
  y->height = max(height(y->left), height(y->right)) + 1;
  x->height = max(height(x->left), height(x->right)) + 1;

  return x; // new root
}

// left rotation (mirrors right_rotate)
struct Node *left_rotate(struct Node *x) {
  struct Node *y = x->right;
  struct Node *temp = y->left;

  y->left = x;
  x->right = temp;

  x->height = max(height(x->left), height(x->right)) + 1;
  y->height = max(height(y->left), height(y->right)) + 1;

  return y;
}

int get_balance_factor(struct Node *node) {
  if (node == NULL) {
    return 0;
  }
  return height(node->left) - height(node->right);
}

struct Node *insert(struct Node *node, int key) {
  if (node == NULL) {
    return new_node(key);
  }

  if (key < node->key) {
    node->left = insert(node->left, key);
  } else if (key > node->key) {
    node->right = insert(node->right, key);
  } else {
    // oh no its dup!
    return node;
  }

  // update height of ancestor node
  node->height = 1 + max(height(node->left), height(node->right));

  // check balance of the ancestor
  int balance = get_balance_factor(node);

  // left-left case
  if (balance > 1 && key < node->left->key) {
    return right_rotate(node);
  }

  // right-right case
  if (balance < -1 && key > node->right->key) {
    return left_rotate(node);
  }

  // left-right case
  if (balance > 1 && key > node->left->key) {
    node->left = left_rotate(node->left);
    return right_rotate(node);
  }

  // right-left case
  if (balance < -1 && key < node->right->key) {
    node->right = right_rotate(node->right);
    return left_rotate(node);
  }

  // no rotations needed
  return node;
}

void level_order(struct Node *root) {
  if (root == NULL) {
    return;
  }

  struct Node *queue[100];
  int front = 0, rear = 0;
  queue[rear++] = root;

  while (front != rear) {
    struct Node *node = queue[front++];
    printf("%d ", node->key);

    if (node->left != NULL) {
      queue[rear++] = node->left;
    }

    if (node->right != NULL) {
      queue[rear++] = node->right;
    }
  }
}

int main() {
  struct Node *root = NULL;

  root = insert(root, 5);
  root = insert(root, 3);
  root = insert(root, 4);
  root = insert(root, 1);
  root = insert(root, 500);
  root = insert(root, -123);

  level_order(root);

  printf("\n");

  return 0;
}
