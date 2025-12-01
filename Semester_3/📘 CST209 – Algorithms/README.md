# 📘 CST209 – Algorithms

**Exam-Ready Study Notes with Working Code Examples**

---

## Unit 1: Algorithm Basics

### Topics Covered
- Algorithm definition and properties
- Time and space complexity
- Big-O notation (O, Ω, Θ)
- Asymptotic analysis

### Key Concepts

**1. Big-O Complexity Analysis**

```
O(1): Constant - Array access, Hash lookup
O(log n): Logarithmic - Binary search
O(n): Linear - Simple loop
O(n log n): Linearithmic - Merge sort, Quick sort
O(n²): Quadratic - Bubble sort, Nested loops
O(n³): Cubic - Triple nested loops
O(2ⁿ): Exponential - Recursive fibonacci
O(n!): Factorial - Permutations
```

**2. Big-O, Big-Omega, Big-Theta**

```
O (Big-O): Upper bound (worst case)
Ω (Big-Omega): Lower bound (best case)
Θ (Theta): Tight bound (average case)

Example: Linear search
- Best case Ω(1): Element at first position
- Worst case O(n): Element at last position
- Average case Θ(n): Element somewhere in middle
```

---

## Unit 2: Sorting Algorithms

### Topics Covered
- Bubble sort, Selection sort, Insertion sort
- Merge sort, Quick sort
- Heap sort, Counting sort, Radix sort

### Key Concepts

**1. Bubble Sort**
```c
#include <stdio.h>

void bubbleSort(int arr[], int n) {
    for (int i = 0; i < n - 1; i++) {
        for (int j = 0; j < n - i - 1; j++) {
            if (arr[j] > arr[j + 1]) {
                int temp = arr[j];
                arr[j] = arr[j + 1];
                arr[j + 1] = temp;
            }
        }
    }
}

// Complexity: Best O(n), Average O(n²), Worst O(n²)
```

**2. Selection Sort**
```c
void selectionSort(int arr[], int n) {
    for (int i = 0; i < n - 1; i++) {
        int minIdx = i;
        for (int j = i + 1; j < n; j++) {
            if (arr[j] < arr[minIdx]) {
                minIdx = j;
            }
        }
        int temp = arr[i];
        arr[i] = arr[minIdx];
        arr[minIdx] = temp;
    }
}

// Complexity: All cases O(n²)
```

**3. Insertion Sort**
```c
void insertionSort(int arr[], int n) {
    for (int i = 1; i < n; i++) {
        int key = arr[i];
        int j = i - 1;
        
        while (j >= 0 && arr[j] > key) {
            arr[j + 1] = arr[j];
            j--;
        }
        arr[j + 1] = key;
    }
}

// Complexity: Best O(n), Average O(n²), Worst O(n²)
```

**4. Merge Sort**
```c
void merge(int arr[], int left, int mid, int right) {
    int n1 = mid - left + 1;
    int n2 = right - mid;
    
    int L[n1], R[n2];
    
    for (int i = 0; i < n1; i++)
        L[i] = arr[left + i];
    for (int j = 0; j < n2; j++)
        R[j] = arr[mid + 1 + j];
    
    int i = 0, j = 0, k = left;
    
    while (i < n1 && j < n2) {
        if (L[i] <= R[j]) {
            arr[k++] = L[i++];
        } else {
            arr[k++] = R[j++];
        }
    }
    
    while (i < n1) arr[k++] = L[i++];
    while (j < n2) arr[k++] = R[j++];
}

void mergeSort(int arr[], int left, int right) {
    if (left < right) {
        int mid = left + (right - left) / 2;
        mergeSort(arr, left, mid);
        mergeSort(arr, mid + 1, right);
        merge(arr, left, mid, right);
    }
}

// Complexity: All cases O(n log n)
```

**5. Quick Sort**
```c
int partition(int arr[], int low, int high) {
    int pivot = arr[high];
    int i = low - 1;
    
    for (int j = low; j < high; j++) {
        if (arr[j] < pivot) {
            i++;
            int temp = arr[i];
            arr[i] = arr[j];
            arr[j] = temp;
        }
    }
    
    int temp = arr[i + 1];
    arr[i + 1] = arr[high];
    arr[high] = temp;
    
    return i + 1;
}

void quickSort(int arr[], int low, int high) {
    if (low < high) {
        int pi = partition(arr, low, high);
        quickSort(arr, low, pi - 1);
        quickSort(arr, pi + 1, high);
    }
}

// Complexity: Best O(n log n), Average O(n log n), Worst O(n²)
```

**6. Heap Sort**
```c
void heapify(int arr[], int n, int i) {
    int largest = i;
    int left = 2 * i + 1;
    int right = 2 * i + 2;
    
    if (left < n && arr[left] > arr[largest])
        largest = left;
    
    if (right < n && arr[right] > arr[largest])
        largest = right;
    
    if (largest != i) {
        int temp = arr[i];
        arr[i] = arr[largest];
        arr[largest] = temp;
        heapify(arr, n, largest);
    }
}

void heapSort(int arr[], int n) {
    for (int i = n / 2 - 1; i >= 0; i--)
        heapify(arr, n, i);
    
    for (int i = n - 1; i > 0; i--) {
        int temp = arr[0];
        arr[0] = arr[i];
        arr[i] = temp;
        heapify(arr, i, 0);
    }
}

// Complexity: All cases O(n log n)
```

**7. Counting Sort**
```c
void countingSort(int arr[], int n) {
    int max = arr[0];
    for (int i = 1; i < n; i++)
        if (arr[i] > max) max = arr[i];
    
    int count[max + 1];
    for (int i = 0; i <= max; i++)
        count[i] = 0;
    
    for (int i = 0; i < n; i++)
        count[arr[i]]++;
    
    for (int i = 1; i <= max; i++)
        count[i] += count[i - 1];
    
    int output[n];
    for (int i = n - 1; i >= 0; i--) {
        output[count[arr[i]] - 1] = arr[i];
        count[arr[i]]--;
    }
    
    for (int i = 0; i < n; i++)
        arr[i] = output[i];
}

// Complexity: O(n + k) where k is range
```

---

## Unit 3: Searching Algorithms

### Topics Covered
- Linear search
- Binary search
- Hashing

### Key Concepts

**1. Linear Search**
```c
int linearSearch(int arr[], int n, int x) {
    for (int i = 0; i < n; i++) {
        if (arr[i] == x)
            return i;
    }
    return -1;
}

// Complexity: O(n)
```

**2. Binary Search**
```c
int binarySearch(int arr[], int left, int right, int x) {
    while (left <= right) {
        int mid = left + (right - left) / 2;
        
        if (arr[mid] == x)
            return mid;
        else if (arr[mid] < x)
            left = mid + 1;
        else
            right = mid - 1;
    }
    return -1;
}

// Complexity: O(log n)
// Precondition: Array must be sorted
```

**3. Binary Search (Recursive)**
```c
int binarySearchRecursive(int arr[], int left, int right, int x) {
    if (left > right)
        return -1;
    
    int mid = left + (right - left) / 2;
    
    if (arr[mid] == x)
        return mid;
    else if (arr[mid] < x)
        return binarySearchRecursive(arr, mid + 1, right, x);
    else
        return binarySearchRecursive(arr, left, mid - 1, x);
}
```

---

## Unit 4: Graph Algorithms

### Topics Covered
- Graph representation
- BFS and DFS
- Shortest path (Dijkstra, Bellman-Ford)
- Minimum spanning tree (Kruskal, Prim)

### Key Concepts

**1. Breadth-First Search (BFS)**
```c
#include <stdio.h>
#include <stdlib.h>

void bfs(int adj[][10], int n, int start) {
    int visited[n];
    for (int i = 0; i < n; i++) visited[i] = 0;
    
    int queue[n], front = 0, rear = 0;
    visited[start] = 1;
    queue[rear++] = start;
    
    printf("BFS: ");
    while (front < rear) {
        int node = queue[front++];
        printf("%d ", node);
        
        for (int i = 0; i < n; i++) {
            if (adj[node][i] && !visited[i]) {
                visited[i] = 1;
                queue[rear++] = i;
            }
        }
    }
    printf("\n");
}

// Complexity: O(V + E)
```

**2. Depth-First Search (DFS)**
```c
void dfs(int adj[][10], int n, int node, int visited[]) {
    visited[node] = 1;
    printf("%d ", node);
    
    for (int i = 0; i < n; i++) {
        if (adj[node][i] && !visited[i]) {
            dfs(adj, n, i, visited);
        }
    }
}

// Complexity: O(V + E)
```

**3. Dijkstra's Algorithm**
```c
#include <limits.h>

void dijkstra(int graph[][10], int n, int src) {
    int dist[n];
    int visited[n];
    
    for (int i = 0; i < n; i++) {
        dist[i] = INT_MAX;
        visited[i] = 0;
    }
    
    dist[src] = 0;
    
    for (int i = 0; i < n - 1; i++) {
        int u = -1;
        for (int j = 0; j < n; j++) {
            if (!visited[j] && (u == -1 || dist[j] < dist[u]))
                u = j;
        }
        
        visited[u] = 1;
        
        for (int v = 0; v < n; v++) {
            if (graph[u][v] && dist[u] != INT_MAX)
                dist[v] = (dist[u] + graph[u][v] < dist[v]) ? 
                         dist[u] + graph[u][v] : dist[v];
        }
    }
    
    printf("Shortest distances from vertex %d:\n", src);
    for (int i = 0; i < n; i++) {
        printf("To %d: %d\n", i, dist[i]);
    }
}

// Complexity: O(V²)
```

**4. Kruskal's Algorithm (MST)**
```c
struct Edge {
    int u, v, weight;
};

int find(int parent[], int x) {
    if (parent[x] != x)
        parent[x] = find(parent, parent[x]);
    return parent[x];
}

void kruskal(struct Edge edges[], int n, int e) {
    // Sort edges by weight (implementation not shown)
    
    int parent[n];
    for (int i = 0; i < n; i++)
        parent[i] = i;
    
    int mstWeight = 0;
    printf("MST edges:\n");
    
    for (int i = 0; i < e && mstWeight < n - 1; i++) {
        int u = find(parent, edges[i].u);
        int v = find(parent, edges[i].v);
        
        if (u != v) {
            printf("(%d, %d): %d\n", edges[i].u, edges[i].v, edges[i].weight);
            parent[u] = v;
            mstWeight += edges[i].weight;
        }
    }
}

// Complexity: O(E log E)
```

---

## Sorting Comparison Table

| Algorithm | Best | Average | Worst | Space | Stable |
|-----------|------|---------|-------|-------|--------|
| Bubble Sort | O(n) | O(n²) | O(n²) | O(1) | Yes |
| Selection Sort | O(n²) | O(n²) | O(n²) | O(1) | No |
| Insertion Sort | O(n) | O(n²) | O(n²) | O(1) | Yes |
| Merge Sort | O(n log n) | O(n log n) | O(n log n) | O(n) | Yes |
| Quick Sort | O(n log n) | O(n log n) | O(n²) | O(log n) | No |
| Heap Sort | O(n log n) | O(n log n) | O(n log n) | O(1) | No |
| Counting Sort | O(n+k) | O(n+k) | O(n+k) | O(k) | Yes |

---

## Practice Questions

### Sorting
1. Implement all 7 sorting algorithms
2. Compare time complexity of different sorts
3. When to use each sorting algorithm
4. Prove stability of insertion sort

### Searching
5. Binary search implementation and complexity
6. When binary search is better than linear search
7. Hash table implementation

### Graphs
8. Implement BFS and DFS
9. Find shortest path using Dijkstra
10. Find MST using Kruskal/Prim
11. Detect cycle in undirected graph
12. Topological sort for directed acyclic graph

### General
13. Solve recurrence relations
14. Calculate Big-O complexity
15. Space and time tradeoffs

---

**Last Updated:** December 2024
