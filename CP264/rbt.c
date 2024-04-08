#include <stdio.h>
#include <stdlib.h>

typedef enum color { RED, BLACK } Color;

typedef struct node {
  int val;
  Color color;
  struct node *left;
  struct node *right;
  struct node *parent;
} Node;

Node *new_node(int val) {
  Node *node = (Node *)malloc(sizeof(Node));
  node->val = val;
  node->color = RED;
  node->left = NULL;
  node->right = NULL;
  node->parent = NULL;
  return node;
}

void left_rotate(Node **root, Node *x) {
  Node *y = x->right;
  x->right = y->left;
  if (y->left != NULL) {
    y->left->parent = x;
  }

  y->parent = x->parent;

  if (x->parent == NULL) {
    *root = y;
  } else if (x == x->parent->left) {
    x->parent->left = y;
  } else {
    x->parent->right = y;
  }

  y->left = x;
  x->parent = y;
}

void right_rotate(Node **root, Node *x) {
  Node *y = x->left;
  x->left = y->right;
  if (y->right != NULL) {
    y->right->parent = x;
  }

  y->parent = x->parent;
  if (x->parent == NULL) {
    *root = y;
  } else if (x == x->parent->right) {
    x->parent->right = y;
  } else {
    x->parent->left = y;
  }

  y->right = x;
  x->parent = y;
}

void fix_violation(Node **root, Node *z) {
  while (z != *root && z->parent->color == RED) {
    Node *y;

    // If z's parent is the left child of z's grandparent
    if (z->parent == z->parent->parent->left) {
      y = z->parent->parent->right; // uncle of z

      // Case 1: z's uncle y is red
      if (y != NULL && y->color == RED) {
        z->parent->color = BLACK;
        y->color = BLACK;
        z->parent->parent->color = RED;
        z = z->parent->parent;
      } else {
        // Case 2: z is the right child of its parent
        if (z == z->parent->right) {
          z = z->parent;
          left_rotate(root, z);
        }

        // Case 3: z is the left child of its parent
        z->parent->color = BLACK;
        z->parent->parent->color = RED;
        right_rotate(root, z->parent->parent);
      }
    } else {
      // Symmetric to the above
      y = z->parent->parent->left;

      if (y != NULL && y->color == RED) {
        z->parent->color = BLACK;
        y->color = BLACK;
        z->parent->parent->color = RED;
        z = z->parent->parent;
      } else {
        if (z == z->parent->left) {
          z = z->parent;
          right_rotate(root, z);
        }

        z->parent->color = BLACK;
        z->parent->parent->color = RED;
        left_rotate(root, z->parent->parent);
      }
    }
  }
  (*root)->color = BLACK;
}

Node *bst_insert(Node *root, Node *node) {
  if (root == NULL) {
    return node;
  }

  if (node->val < root->val) {
    root->left = bst_insert(root->left, node);
    root->left->parent = root;
  } else if (node->val > root->val) {
    root->right = bst_insert(root->right, node);
    root->right->parent = root;
  }

  return root;
}

void insert(Node **root, int val) {
  Node *node = new_node(val);
  *root = bst_insert(*root, node);
  fix_violation(root, node);
}

void level_order(Node *root) {
  if (root == NULL) {
    return;
  }

  Node *queue[100];
  int front = 0, rear = 0;
  queue[rear++] = root;

  while (front != rear) {
    Node *node = queue[front++];
    printf("%d ", node->val);

    if (node->left != NULL) {
      queue[rear++] = node->left;
    }

    if (node->right != NULL) {
      queue[rear++] = node->right;
    }
  }
}

int main() {
  Node *root = NULL;

  insert(&root, 7);
  insert(&root, 3);
  insert(&root, 8);
  insert(&root, 11);
  insert(&root, 18);
  insert(&root, 10);
  insert(&root, 26);
  insert(&root, 22);

  level_order(root);
  printf("\n");

  return 0;
}
