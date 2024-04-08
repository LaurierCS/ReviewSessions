#include <stdio.h>
#include <stdlib.h>

typedef struct node {
    int val;
    struct node *left;
    struct node *right;
} TNODE;

typedef struct QueueNode {
    TNODE *data;
    struct QueueNode *next;
} QueueNode;

typedef struct Queue {
    QueueNode *front, *rear;
} Queue;

TNODE *new_node(int value) {
    TNODE *node = (TNODE *)malloc(sizeof(TNODE));
    node->val = value;
    node->left = NULL;
    node->right = NULL;
    return node;
}

//Create queue
Queue* createQueue() {
    Queue* q = (Queue*)malloc(sizeof(Queue));
    q->front = q->rear = NULL;
    return q;
}


//add node to the queue
void enqueue(Queue* q, TNODE* node) {
    QueueNode* newNode = (QueueNode*)malloc(sizeof(QueueNode));
    newNode->data = node;
    newNode->next = NULL;
    if (q->rear == NULL) {
        q->front = q->rear = newNode;
        return;
    }
    q->rear->next = newNode;
    q->rear = newNode;
}

//remove node from queue
TNODE* dequeue(Queue* q) {
    if (q->front == NULL)
        return NULL;
    QueueNode* temp = q->front;
    TNODE* node = temp->data;
    q->front = q->front->next;
    if (q->front == NULL)
        q->rear = NULL;
    free(temp);
    return node;
}

int isEmpty(Queue* q) {
    return q->front == NULL;
}

void bfs(TNODE *root) {
    if (root == NULL)
        return;
    
    Queue* queue = createQueue();
    enqueue(queue, root);

    //While there is still values in the queue, remove the front and add its children to the queue
    while (!isEmpty(queue)) {
        TNODE* node = dequeue(queue);
        printf("%d ", node->val);

        if (node->left != NULL)
            enqueue(queue, node->left);
        if (node->right != NULL)
            enqueue(queue, node->right);
    }
}

int main() {
    //create tree
    TNODE *root = NULL;
    root = new_node(24);
    root->left = new_node(18);
    root->right = new_node(33);
    root->left->left = new_node(4);
    root->left->right = new_node(50);
    root->right->left = new_node(6);
    root->right->right = new_node(37);

    
    printf("Visual of tree created:\n");
    printf("        24\n");
    printf("      /    \\\n");
    printf("     18    33\n");
    printf("    / \\    / \\\n");
    printf("   4  50  6   37\n");

    printf("Breadth-First Search (BFS) traversal of the tree: ");
    bfs(root);

    return 0;
}