#include <stdio.h>
#include <stdlib.h>

typedef struct node {
    int val;
    struct node *left;
    struct node *right;
} TNODE;

TNODE *new_node(int value) {
    TNODE *node = (TNODE *)malloc(sizeof(TNODE));
    node->val = value;
    node->left = NULL;
    node->right = NULL;
    return node;
}

typedef struct stackNode {
    TNODE *node;
    struct stackNode *next;
} StackNode;

StackNode *createStackNode(TNODE *node) {
    StackNode *stackNode = (StackNode *)malloc(sizeof(StackNode));
    stackNode->node = node;
    stackNode->next = NULL;
    return stackNode;
}

void push(StackNode **topPtr, TNODE *node) {
    StackNode *stackNode = createStackNode(node);
    stackNode->next = *topPtr;
    *topPtr = stackNode;
}

TNODE *pop(StackNode **topPtr) {
    if (*topPtr == NULL) return NULL;
    StackNode *temp = *topPtr;
    TNODE *node = temp->node;
    *topPtr = (*topPtr)->next;
    free(temp);
    return node;
}

int isEmpty(StackNode *top) {
    return top == NULL;
}

//Implement DFS using a stack and print each value when popped
void dfs(TNODE *root) {
    if (root == NULL) return;
    StackNode *stack = NULL;
    push(&stack, root);

    printf("Depth-First Search (DFS) traversal of the tree: ");
    while (!isEmpty(stack)) {
        TNODE *current = pop(&stack);
        printf("%d ", current->val);

        if (current->right != NULL) push(&stack, current->right);
        if (current->left != NULL) push(&stack, current->left);
    }
}

int main() {
    // Create tree
    TNODE *root = NULL;
    root = new_node(45);
    root->left = new_node(19);
    root->right = new_node(27);
    root->left->left = new_node(4);
    root->left->right = new_node(13);
    root->right->left = new_node(6);
    root->right->right = new_node(32);

    printf("Visual of tree created:\n");
    printf("        45\n");
    printf("      /    \\\n");
    printf("     19    27\n");
    printf("    / \\    / \\\n");
    printf("   4  13  6   32\n");

    dfs(root);

    return 0;
}