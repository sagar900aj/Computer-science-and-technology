# 📘 CST205 – Data Structures

**Exam-Ready Study Notes with Working Code Examples**

---

## Unit 1: Arrays

### Topics Covered
- Array basics and declaration
- Accessing array elements
- Array operations (insert, delete, search)
- Searching (linear, binary)
- Sorting algorithms

### Key Concepts

**1. Linear Search**
```c
#include <stdio.h>

int linearSearch(int arr[], int size, int target) {
    for (int i = 0; i < size; i++) {
        if (arr[i] == target) {
            return i;  // Element found at index i
        }
    }
    return -1;  // Element not found
}

int main() {
    int arr[] = {10, 25, 30, 45, 50};
    int target = 30;
    
    int result = linearSearch(arr, 5, target);
    if (result != -1) {
        printf("Element found at index %d\n", result);
    } else {
        printf("Element not found\n");
    }
    return 0;
}
```

**2. Binary Search**
```c
#include <stdio.h>

int binarySearch(int arr[], int left, int right, int target) {
    while (left <= right) {
        int mid = left + (right - left) / 2;
        
        if (arr[mid] == target) {
            return mid;
        } else if (arr[mid] < target) {
            left = mid + 1;  // Search right half
        } else {
            right = mid - 1;  // Search left half
        }
    }
    return -1;  // Element not found
}

int main() {
    int arr[] = {10, 20, 30, 40, 50};  // Must be sorted
    int target = 30;
    
    int result = binarySearch(arr, 0, 4, target);
    if (result != -1) {
        printf("Element found at index %d\n", result);
    } else {
        printf("Element not found\n");
    }
    return 0;
}
```

**3. Bubble Sort**
```c
#include <stdio.h>

void bubbleSort(int arr[], int size) {
    for (int i = 0; i < size - 1; i++) {
        for (int j = 0; j < size - i - 1; j++) {
            if (arr[j] > arr[j + 1]) {
                // Swap
                int temp = arr[j];
                arr[j] = arr[j + 1];
                arr[j + 1] = temp;
            }
        }
    }
}

int main() {
    int arr[] = {50, 30, 20, 40, 10};
    int size = 5;
    
    printf("Before sort: ");
    for (int i = 0; i < size; i++) printf("%d ", arr[i]);
    
    bubbleSort(arr, size);
    
    printf("\nAfter sort: ");
    for (int i = 0; i < size; i++) printf("%d ", arr[i]);
    printf("\n");
    
    return 0;
}
```

**4. Insertion Sort**
```c
#include <stdio.h>

void insertionSort(int arr[], int size) {
    for (int i = 1; i < size; i++) {
        int key = arr[i];
        int j = i - 1;
        
        while (j >= 0 && arr[j] > key) {
            arr[j + 1] = arr[j];
            j--;
        }
        arr[j + 1] = key;
    }
}

int main() {
    int arr[] = {50, 30, 20, 40, 10};
    int size = 5;
    
    printf("Before: ");
    for (int i = 0; i < size; i++) printf("%d ", arr[i]);
    
    insertionSort(arr, size);
    
    printf("\nAfter: ");
    for (int i = 0; i < size; i++) printf("%d ", arr[i]);
    printf("\n");
    
    return 0;
}
```

---

## Unit 2: Stack

### Topics Covered
- Stack basics (LIFO)
- Push and pop operations
- Stack applications
- Expression evaluation (Infix to Postfix)

### Key Concepts

**1. Stack Implementation Using Array**
```c
#include <stdio.h>
#include <stdlib.h>

#define SIZE 100

struct Stack {
    int arr[SIZE];
    int top;
};

// Initialize stack
void initStack(struct Stack *s) {
    s->top = -1;
}

// Check if stack is empty
int isEmpty(struct Stack *s) {
    return s->top == -1;
}

// Check if stack is full
int isFull(struct Stack *s) {
    return s->top == SIZE - 1;
}

// Push element
void push(struct Stack *s, int value) {
    if (isFull(s)) {
        printf("Stack overflow!\n");
    } else {
        s->arr[++(s->top)] = value;
        printf("Pushed %d\n", value);
    }
}

// Pop element
int pop(struct Stack *s) {
    if (isEmpty(s)) {
        printf("Stack underflow!\n");
        return -1;
    }
    return s->arr[(s->top)--];
}

// Display stack
void display(struct Stack *s) {
    if (isEmpty(s)) {
        printf("Stack is empty!\n");
        return;
    }
    printf("Stack elements: ");
    for (int i = 0; i <= s->top; i++) {
        printf("%d ", s->arr[i]);
    }
    printf("\n");
}

int main() {
    struct Stack s;
    initStack(&s);
    
    push(&s, 10);
    push(&s, 20);
    push(&s, 30);
    display(&s);
    
    printf("Popped: %d\n", pop(&s));
    display(&s);
    
    return 0;
}
```

**2. Infix to Postfix Conversion**
```c
#include <stdio.h>
#include <string.h>
#include <ctype.h>

#define SIZE 100

struct Stack {
    char arr[SIZE];
    int top;
};

void initStack(struct Stack *s) {
    s->top = -1;
}

void push(struct Stack *s, char c) {
    s->arr[++(s->top)] = c;
}

char pop(struct Stack *s) {
    return s->arr[(s->top)--];
}

int precedence(char c) {
    if (c == '+' || c == '-') return 1;
    if (c == '*' || c == '/') return 2;
    return 0;
}

void infixToPostfix(char *infix, char *postfix) {
    struct Stack s;
    initStack(&s);
    int k = 0;
    
    for (int i = 0; infix[i]; i++) {
        char c = infix[i];
        
        if (isdigit(c)) {
            postfix[k++] = c;
        } else if (c == '(') {
            push(&s, c);
        } else if (c == ')') {
            while (s.top != -1 && s.arr[s.top] != '(') {
                postfix[k++] = pop(&s);
            }
            pop(&s);  // Remove '('
        } else {
            while (s.top != -1 && precedence(s.arr[s.top]) >= precedence(c)) {
                postfix[k++] = pop(&s);
            }
            push(&s, c);
        }
    }
    
    while (s.top != -1) {
        postfix[k++] = pop(&s);
    }
    postfix[k] = '\0';
}

int main() {
    char infix[] = "2+3*4";
    char postfix[SIZE];
    
    infixToPostfix(infix, postfix);
    printf("Infix: %s\n", infix);
    printf("Postfix: %s\n", postfix);
    
    return 0;
}
```

---

## Unit 3: Queue

### Topics Covered
- Queue basics (FIFO)
- Enqueue and dequeue
- Circular queue
- Double-ended queue (deque)

### Key Concepts

**1. Queue Implementation**
```c
#include <stdio.h>

#define SIZE 100

struct Queue {
    int arr[SIZE];
    int front, rear;
};

void initQueue(struct Queue *q) {
    q->front = -1;
    q->rear = -1;
}

int isEmpty(struct Queue *q) {
    return q->front == -1;
}

int isFull(struct Queue *q) {
    return q->rear == SIZE - 1;
}

void enqueue(struct Queue *q, int value) {
    if (isFull(q)) {
        printf("Queue overflow!\n");
    } else {
        if (q->front == -1) q->front = 0;
        q->arr[++(q->rear)] = value;
        printf("Enqueued %d\n", value);
    }
}

int dequeue(struct Queue *q) {
    if (isEmpty(q)) {
        printf("Queue underflow!\n");
        return -1;
    }
    return q->arr[(q->front)++];
}

void display(struct Queue *q) {
    if (isEmpty(q)) {
        printf("Queue is empty!\n");
        return;
    }
    printf("Queue: ");
    for (int i = q->front; i <= q->rear; i++) {
        printf("%d ", q->arr[i]);
    }
    printf("\n");
}

int main() {
    struct Queue q;
    initQueue(&q);
    
    enqueue(&q, 10);
    enqueue(&q, 20);
    enqueue(&q, 30);
    display(&q);
    
    printf("Dequeued: %d\n", dequeue(&q));
    display(&q);
    
    return 0;
}
```

**2. Circular Queue**
```c
#include <stdio.h>

#define SIZE 5

struct CircularQueue {
    int arr[SIZE];
    int front, rear;
};

void initQueue(struct CircularQueue *q) {
    q->front = -1;
    q->rear = -1;
}

int isFull(struct CircularQueue *q) {
    return (q->rear + 1) % SIZE == q->front;
}

int isEmpty(struct CircularQueue *q) {
    return q->front == -1;
}

void enqueue(struct CircularQueue *q, int value) {
    if (q->front == -1) q->front = 0;
    
    if (isFull(q)) {
        printf("Circular Queue is full!\n");
    } else {
        q->rear = (q->rear + 1) % SIZE;
        q->arr[q->rear] = value;
        printf("Enqueued %d\n", value);
    }
}

int dequeue(struct CircularQueue *q) {
    if (isEmpty(q)) {
        printf("Queue is empty!\n");
        return -1;
    }
    
    int value = q->arr[q->front];
    
    if (q->front == q->rear) {
        q->front = -1;
        q->rear = -1;
    } else {
        q->front = (q->front + 1) % SIZE;
    }
    
    return value;
}

int main() {
    struct CircularQueue q;
    initQueue(&q);
    
    enqueue(&q, 10);
    enqueue(&q, 20);
    enqueue(&q, 30);
    enqueue(&q, 40);
    
    printf("Dequeued: %d\n", dequeue(&q));
    enqueue(&q, 50);
    
    return 0;
}
```

---

## Unit 4: Linked List

### Topics Covered
- Singly linked list (insert, delete, search)
- Doubly linked list
- Circular linked list
- Linked list operations

### Key Concepts

**1. Singly Linked List**
```c
#include <stdio.h>
#include <stdlib.h>

struct Node {
    int data;
    struct Node *next;
};

typedef struct Node Node;

// Create new node
Node* createNode(int data) {
    Node *newNode = (Node*)malloc(sizeof(Node));
    newNode->data = data;
    newNode->next = NULL;
    return newNode;
}

// Insert at beginning
void insertBeginning(Node **head, int data) {
    Node *newNode = createNode(data);
    newNode->next = *head;
    *head = newNode;
}

// Insert at end
void insertEnd(Node **head, int data) {
    Node *newNode = createNode(data);
    
    if (*head == NULL) {
        *head = newNode;
        return;
    }
    
    Node *current = *head;
    while (current->next != NULL) {
        current = current->next;
    }
    current->next = newNode;
}

// Display list
void display(Node *head) {
    printf("List: ");
    while (head != NULL) {
        printf("%d -> ", head->data);
        head = head->next;
    }
    printf("NULL\n");
}

// Search element
int search(Node *head, int target) {
    while (head != NULL) {
        if (head->data == target) return 1;
        head = head->next;
    }
    return 0;
}

// Delete node
void deleteNode(Node **head, int data) {
    Node *current = *head;
    
    if (current != NULL && current->data == data) {
        *head = current->next;
        free(current);
        return;
    }
    
    Node *prev = NULL;
    while (current != NULL && current->data != data) {
        prev = current;
        current = current->next;
    }
    
    if (current != NULL) {
        prev->next = current->next;
        free(current);
    }
}

int main() {
    Node *head = NULL;
    
    insertEnd(&head, 10);
    insertEnd(&head, 20);
    insertEnd(&head, 30);
    insertBeginning(&head, 5);
    
    display(head);
    
    printf("Search 20: %s\n", search(head, 20) ? "Found" : "Not Found");
    
    deleteNode(&head, 20);
    display(head);
    
    return 0;
}
```

---

## Unit 5: Trees

### Topics Covered
- Binary tree basics
- Tree traversal (inorder, preorder, postorder)
- Binary search tree (BST)
- AVL trees

### Key Concepts

**1. Binary Search Tree**
```c
#include <stdio.h>
#include <stdlib.h>

struct TreeNode {
    int data;
    struct TreeNode *left;
    struct TreeNode *right;
};

typedef struct TreeNode TreeNode;

// Create new node
TreeNode* createNode(int data) {
    TreeNode *node = (TreeNode*)malloc(sizeof(TreeNode));
    node->data = data;
    node->left = NULL;
    node->right = NULL;
    return node;
}

// Insert in BST
TreeNode* insert(TreeNode *root, int data) {
    if (root == NULL) {
        return createNode(data);
    }
    
    if (data < root->data) {
        root->left = insert(root->left, data);
    } else if (data > root->data) {
        root->right = insert(root->right, data);
    }
    
    return root;
}

// Inorder traversal (Left, Root, Right)
void inorder(TreeNode *root) {
    if (root == NULL) return;
    inorder(root->left);
    printf("%d ", root->data);
    inorder(root->right);
}

// Preorder traversal (Root, Left, Right)
void preorder(TreeNode *root) {
    if (root == NULL) return;
    printf("%d ", root->data);
    preorder(root->left);
    preorder(root->right);
}

// Search in BST
int search(TreeNode *root, int target) {
    if (root == NULL) return 0;
    
    if (target == root->data) return 1;
    else if (target < root->data) return search(root->left, target);
    else return search(root->right, target);
}

int main() {
    TreeNode *root = NULL;
    
    root = insert(root, 50);
    insert(root, 30);
    insert(root, 70);
    insert(root, 20);
    insert(root, 40);
    
    printf("Inorder: ");
    inorder(root);
    printf("\n");
    
    printf("Preorder: ");
    preorder(root);
    printf("\n");
    
    printf("Search 40: %s\n", search(root, 40) ? "Found" : "Not Found");
    
    return 0;
}
```

---

## Unit 6: Graphs

### Topics Covered
- Graph representation (adjacency list, matrix)
- Graph traversal (BFS, DFS)
- Shortest path algorithms

### Key Concepts

**1. Graph - BFS and DFS**
```c
#include <stdio.h>
#include <stdlib.h>

#define MAX_NODES 10

struct Graph {
    int adj[MAX_NODES][MAX_NODES];
    int vertices;
};

// Create graph
struct Graph* createGraph(int vertices) {
    struct Graph *graph = (struct Graph*)malloc(sizeof(struct Graph));
    graph->vertices = vertices;
    
    for (int i = 0; i < vertices; i++) {
        for (int j = 0; j < vertices; j++) {
            graph->adj[i][j] = 0;
        }
    }
    return graph;
}

// Add edge
void addEdge(struct Graph *graph, int u, int v) {
    graph->adj[u][v] = 1;
    graph->adj[v][u] = 1;  // For undirected graph
}

// DFS using recursion
void dfs(struct Graph *graph, int node, int visited[]) {
    visited[node] = 1;
    printf("%d ", node);
    
    for (int i = 0; i < graph->vertices; i++) {
        if (graph->adj[node][i] && !visited[i]) {
            dfs(graph, i, visited);
        }
    }
}

// BFS using queue
void bfs(struct Graph *graph, int start) {
    int visited[MAX_NODES] = {0};
    int queue[MAX_NODES];
    int front = 0, rear = 0;
    
    visited[start] = 1;
    queue[rear++] = start;
    
    while (front < rear) {
        int node = queue[front++];
        printf("%d ", node);
        
        for (int i = 0; i < graph->vertices; i++) {
            if (graph->adj[node][i] && !visited[i]) {
                visited[i] = 1;
                queue[rear++] = i;
            }
        }
    }
}

int main() {
    struct Graph *graph = createGraph(4);
    
    addEdge(graph, 0, 1);
    addEdge(graph, 0, 2);
    addEdge(graph, 1, 2);
    addEdge(graph, 1, 3);
    addEdge(graph, 2, 3);
    
    printf("DFS: ");
    int visited[MAX_NODES] = {0};
    dfs(graph, 0, visited);
    printf("\n");
    
    printf("BFS: ");
    bfs(graph, 0);
    printf("\n");
    
    return 0;
}
```

---

## Practice Questions

1. Implement quick sort algorithm
2. Implement merge sort algorithm
3. Implement linear and binary search
4. Implement stack and queue operations
5. Implement singly linked list with all operations
6. Implement doubly linked list
7. Implement binary search tree with insertion, deletion, search
8. Implement graph traversal (BFS, DFS)
9. Find shortest path using Dijkstra's algorithm
10. Implement infix to postfix conversion

---

## Complexity Analysis

| Operation | Best | Average | Worst |
|-----------|------|---------|-------|
| Linear Search | O(1) | O(n) | O(n) |
| Binary Search | O(1) | O(log n) | O(log n) |
| Bubble Sort | O(n) | O(n²) | O(n²) |
| Insertion Sort | O(n) | O(n²) | O(n²) |
| Merge Sort | O(n log n) | O(n log n) | O(n log n) |
| Quick Sort | O(n log n) | O(n log n) | O(n²) |

---

**Last Updated:** December 2024
