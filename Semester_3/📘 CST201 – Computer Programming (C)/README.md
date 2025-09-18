# 🎯 C Programming Course Notes 📘

> 🚀 A comprehensive guide to C Programming fundamentals and advanced concepts

## 📚 Table of Contents

### 📌 Unit 1: Basics of C
- [🏛️ History of C](#%EF%B8%8F-history-of-c)
- [🏗️ Structured Programming](#-history-of-c)
- [📁 Files in C](#-files-in-c)
- [🔤 Language Basics](#-language-basics)
- [🎮 Operators & Types](#-operators)
- [💻 Input/Output](#-inputoutput-examples)

### 📌 Unit 2: Control Flow
- [🔄 Decision Making](#-decision-making-statements)
  - [⚡ if Statements](#-if-statement)
  - [🔀 switch Statement](#-switch-statement)
  - [↪️ goto Statement](#-goto-statement)
- [🔁 Loops](#-loops)
  - [📍 while Loop](#-while-loop)
  - [🔄 do-while Loop](#-do-while-loop)
  - [📈 for Loop](#-for-loop)
  - [🎮 Control Statements](#-control-statements)

### 📌 Unit 3: Arrays & Strings
- [📊 Arrays](#-arrays)
  - [📈 One-Dimensional Arrays](#-one-dimensional-arrays)
  - [🔳 Multi-Dimensional Arrays](#-multi-dimensional-arrays)
- [📝 Strings](#-strings)
  - [🔤 String Basics](#-string-basics)
  - [🛠️ String Functions](#-string-functions)
  - [✂️ String Manipulation](#-string-manipulation-examples)

### 📌 Unit 4: Functions
- [🎯 Function Basics](#-function-basics)
- [🌐 Variable Scope](#-variable-scope)
- [💾 Storage Classes](#-storage-classes)
- [📤 Parameter Passing](#-parameter-passing)
- [🔄 Recursion](#-recursion)

### 📌 Unit 5: Pointers
- [🎯 Pointer Fundamentals](#-pointer-fundamentals)
- [🔢 Types of Pointers](#-types-of-pointers)
- [🎮 Pointer Operations](#-pointer-operations)
- [💾 Memory Management](#-dynamic-memory-management)
- [🎯 Advanced Concepts](#-advanced-pointer-concepts)

### 📌 Unit 6: Advanced Topics
- [📚 Structures and Unions](#-structures-and-unions)
- [📂 File Handling](#-file-handling)
- [🔄 Dynamic Memory Allocation](#-dynamic-memory-allocation)
- [📚 Advanced Data Types](#-advanced-data-types)
- [📜 Preprocessor Directives](#-preprocessor-directives)

### 📌 Unit 7: Projects and Resources
- [📂 Mini Projects](#-mini-projects)
- [📚 Resources](#-resources)
- [💡 Best Practices](#-best-practices)

## 🌟 Unit 1: Basics of C

### 🏛️ History of C
- 👨‍💻 Developed by Dennis Ritchie (1972) at Bell Labs
- 🔄 Based on B and BCPL languages
- 💻 Used for UNIX Operating System development
- 🌱 Foundation for modern languages (C++, Java, Python)

### 🏗️ Advantages of Structured Programming
- 📦 Modular program design
- ♻️ Code reusability
- 🐞 Easy debugging
- 👥 Team collaboration
- 📈 Systematic approach

### 📁 Files in C
1. **📝 Source files** (.c)
   ```c
   // Example: program.c
   #include <stdio.h>
   int main() {
       printf("Hello World!");
       return 0;
   }
   ```

2. **📚 Header files** (.h)
   ```c
   // Example: myheader.h
   void sayHello(void);
   int add(int a, int b);
   ```

### 💻 Language Basics

#### 🔤 Character Set
- 📝 Letters (A-Z, a-z)
- 🔢 Digits (0-9)
- ⚡ Special symbols (+, -, *, /, etc.)
- ⌨️ White space characters

#### 🎯 Data Types
```c
int     // 🔢 2 or 4 bytes
float   // 📊 4 bytes
double  // 📈 8 bytes
char    // 📝 1 byte
void    // ⭕ empty
```

### ⚙️ Operators
1. ➕ Arithmetic: `+`, `-`, `*`, `/`, `%`
2. ⚖️ Relational: `<`, `>`, `<=`, `>=`, `==`, `!=`
3. 🔄 Logical: `&&`, `||`, `!`
4. 📝 Assignment: `=`, `+=`, `-=`, `*=`, `/=`

### 🖥️ Input/Output Examples
```c
// 📤 Output Example
printf("Hello, %s! You are %d years old.\n", name, age);

// 📥 Input Example
scanf("%d %s", &age, name);
```

## 🚀 Getting Started
1. 📥 Clone this repository
2. 📂 Navigate to specific units
3. 📝 Follow the examples
4. ✏️ Try practice problems
5. ▶️ Run sample programs


## 🤝 Contributing
🌟 Pull requests are welcome. For major changes, please open an issue first.

---

⭐ Star this repository if you find it helpful! ⭐

[⬅️ Previous Unit](#-unit-1-basics-of-c-1) | [Next Unit ➡️](#-unit-2-control-flow-1)

## 🔄 Unit 2: Control Flow

### ⚡ Decision Making Statements

#### 📝 if Statement
```c
// Simple if
if (condition) {
    // code block
}

// if-else
if (condition) {
    // code if true
} else {
    // code if false
}

// if-else-if ladder
if (condition1) {
    // code block 1
} else if (condition2) {
    // code block 2
} else {
    // default code block
}
```

#### 🔀 switch Statement
```c
switch (expression) {
    case constant1:
        // code block 1
        break;
    case constant2:
        // code block 2
        break;
    default:
        // default code block
}
```

#### 🎯 Example: Grade Calculator
```c
char calculateGrade(int score) {
    switch (score / 10) {
        case 10:
        case 9:
            return 'A';
        case 8:
            return 'B';
        case 7:
            return 'C';
        case 6:
            return 'D';
        default:
            return 'F';
    }
}
```

### 🔁 Loops

#### 📍 while Loop
```c
// Entry-controlled loop
while (condition) {
    // code block
    // update condition
}
```

#### 🔄 do-while Loop
```c
// Exit-controlled loop
do {
    // code block
    // update condition
} while (condition);
```

#### 📈 for Loop
```c
for (initialization; condition; update) {
    // code block
}

// Example: Print numbers 1 to 5
for (int i = 1; i <= 5; i++) {
    printf("%d ", i);
}
```

### 🎮 Control Statements

#### 🚪 break Statement
```c
// Exit from loop or switch
for (int i = 1; i <= 10; i++) {
    if (i == 5) break;
    printf("%d ", i);
} // Output: 1 2 3 4
```

#### ⏭️ continue Statement
```c
// Skip rest of loop body
for (int i = 1; i <= 5; i++) {
    if (i == 3) continue;
    printf("%d ", i);
} // Output: 1 2 4 5
```

#### ↪️ goto Statement
```c
// Not recommended but available
start:
    printf("Enter a positive number: ");
    if (num <= 0) {
        goto start;
    }
```

### 🎯 Practice Examples

#### 📝 Number Pattern
```c
/*
Output:
1
1 2
1 2 3
1 2 3 4
*/

void printPattern(int n) {
    for (int i = 1; i <= n; i++) {
        for (int j = 1; j <= i; j++) {
            printf("%d ", j);
        }
        printf("\n");
    }
}
```

#### 🔢 Prime Number Checker
```c
bool isPrime(int num) {
    if (num <= 1) return false;
    for (int i = 2; i <= sqrt(num); i++) {
        if (num % i == 0) return false;
    }
    return true;
}
```

### 💡 Key Points
- ⚠️ Avoid deep nesting of control structures
- 🔍 Always use braces {} for clarity
- 🎯 Choose the right loop for your need
- ⚡ Optimize loop conditions for performance
- 🚫 Minimize use of goto statements

### 🎯 Practice Problems
1. 📊 Create a simple calculator using switch
2. 🔢 Print Fibonacci series using loops
3. 🎲 Generate multiplication table
4. ⭐ Check for palindrome number
5. 📈 Find factorial using loops

[⬅️ Previous Unit](#-unit-2-control-flow-1) | [Next Unit ➡️](#-unit-3-arrays--strings-1)

## 📊 Unit 3: Arrays & Strings

### 📈 Arrays

#### 🔰 One-Dimensional Arrays
```c
// Array declaration
int numbers[5];         // Uninitialized array
int scores[5] = {90, 85, 88, 92, 76};  // Initialized array
float prices[] = {19.99, 24.50, 9.99}; // Size determined automatically
```

#### 🎲 Array Operations
```c
// Array traversal
for(int i = 0; i < 5; i++) {
    printf("%d ", scores[i]);
}

// Finding maximum element
int max = numbers[0];
for(int i = 1; i < size; i++) {
    if(numbers[i] > max) {
        max = numbers[i];
    }
}
```

#### 🔳 Multi-Dimensional Arrays
```c
// 2D Array declaration
int matrix[3][4];

// 2D Array initialization
int grid[3][3] = {
    {1, 2, 3},
    {4, 5, 6},
    {7, 8, 9}
};

// Accessing elements
for(int i = 0; i < 3; i++) {
    for(int j = 0; j < 3; j++) {
        printf("%d ", grid[i][j]);
    }
    printf("\n");
}
```

### 📝 Strings

#### 🔤 String Basics
```c
// String declaration
char greeting[20] = "Hello";
char name[] = "John";

// String input
char str[50];
scanf("%s", str);              // Single word
fgets(str, 50, stdin);        // With spaces
```

#### 🛠️ String Functions
```c
#include <string.h>

// Common string operations
strlen(str);          // String length
strcpy(dest, src);    // String copy
strcat(dest, src);    // String concatenation
strcmp(str1, str2);   // String comparison
```

#### ✂️ String Manipulation Examples
```c
// Reverse a string
void reverseString(char str[]) {
    int len = strlen(str);
    for(int i = 0; i < len/2; i++) {
        char temp = str[i];
        str[i] = str[len-1-i];
        str[len-1-i] = temp;
    }
}

// Convert to uppercase
void toUpper(char str[]) {
    for(int i = 0; str[i] != '\0'; i++) {
        if(str[i] >= 'a' && str[i] <= 'z') {
            str[i] = str[i] - 32;
        }
    }
}
```

### 🎯 Practice Examples

#### 📊 Matrix Operations
```c
// Matrix Addition
void addMatrices(int A[][3], int B[][3], int C[][3], int rows, int cols) {
    for(int i = 0; i < rows; i++) {
        for(int j = 0; j < cols; j++) {
            C[i][j] = A[i][j] + B[i][j];
        }
    }
}
```

#### 🔍 String Search
```c
// Find character frequency
int charFrequency(char str[], char ch) {
    int count = 0;
    for(int i = 0; str[i] != '\0'; i++) {
        if(str[i] == ch) count++;
    }
    return count;
}
```

### 💡 Key Points
- 📌 Arrays are zero-indexed
- 🔒 Array size is fixed once declared
- 📝 Strings are character arrays
- ⚠️ Always check array bounds
- 🔍 String functions require string.h
- 🔚 Strings end with null character '\0'

### 🎯 Practice Problems
1. 📊 Implement bubble sort for an array
2. 🎲 Create a matrix transpose function
3. 🔤 Build a palindrome checker
4. 📝 Create a string tokenizer
5. 🔍 Find common elements in two arrays

### 🔨 Advanced Topics
- 📊 Dynamic arrays
- 🎲 Sparse matrices
- 🔤 Pattern matching algorithms
- 📝 String manipulation techniques
- 🔍 Array sorting algorithms

[⬅️ Previous Unit](#-unit-3-arrays--strings-1) | [Next Unit ➡️](#%EF%B8%8F-unit-4-functions)

## ⚙️ Unit 4: Functions

### 🎯 Function Basics

#### 📝 Function Declaration & Definition
```c
// Function declaration (prototype)
return_type function_name(parameter_list);

// Function definition
return_type function_name(parameter_list) {
    // function body
    return value;
}

// Example
int add(int a, int b) {
    return a + b;
}
```

#### 🎨 Types of Functions
```c
// 1. No arguments, no return
void greet(void) {
    printf("Hello!\n");
}

// 2. Arguments, no return
void printSum(int a, int b) {
    printf("Sum: %d\n", a + b);
}

// 3. No arguments, with return
int getInput(void) {
    int n;
    scanf("%d", &n);
    return n;
}

// 4. Arguments with return
float average(int arr[], int size) {
    int sum = 0;
    for(int i = 0; i < size; i++) {
        sum += arr[i];
    }
    return (float)sum/size;
}
```

### 🌐 Variable Scope

#### 🏠 Local Variables
```c
void function() {
    int localVar = 10;  // Scope limited to this function
}
```

#### 🌍 Global Variables
```c
int globalVar = 20;  // Accessible throughout the program

void function() {
    printf("%d", globalVar);  // Can access global variable
}
```

### 💾 Storage Classes

#### 🔄 auto
```c
void function() {
    auto int x = 10;  // Default storage class for local variables
}
```

#### 📌 static
```c
void counter() {
    static int count = 0;  // Retains value between function calls
    count++;
    printf("%d\n", count);
}
```

#### 🌐 extern
```c
// In header file
extern int globalVar;  // Declaration of variable defined elsewhere
```

#### 🔒 register
```c
void function() {
    register int counter;  // Suggestion to store in CPU register
}
```

### 📤 Parameter Passing

#### 📥 Call by Value
```c
void swap(int a, int b) {
    int temp = a;
    a = b;
    b = temp;
}  // Original values remain unchanged
```

#### 🔄 Call by Reference
```c
void swap(int *a, int *b) {
    int temp = *a;
    *a = *b;
    *b = temp;
}  // Original values are modified
```

### 🔄 Recursion

#### 📝 Basic Recursion Example
```c
// Factorial calculation
int factorial(int n) {
    if (n <= 1) return 1;  // Base case
    return n * factorial(n-1);  // Recursive case
}
```

#### 🎯 Advanced Recursion Example
```c
// Fibonacci sequence
int fibonacci(int n) {
    if (n <= 1) return n;
    return fibonacci(n-1) + fibonacci(n-2);
}
```

### 💡 Best Practices
- ✨ Use meaningful function names
- 📝 Always declare function prototypes
- 🎯 Keep functions small and focused
- 📊 Limit parameters (max 4-5)
- 🔍 Document function purpose and parameters
- ⚠️ Avoid global variables when possible

### 🎯 Practice Problems
1. ⚙️ Create a function library for basic math operations
2. 🔄 Implement Tower of Hanoi using recursion
3. 📊 Create a function to calculate power using recursion
4. 🎲 Implement binary search function
5. 📝 Create a menu-driven program using functions

[⬅️ Previous Unit](#%EF%B8%8F-unit-4-functions) | [Next Unit ➡️](#-unit-5-pointers-1)

## 📌 Unit 5: Pointers

### 🎯 Pointer Fundamentals

#### 🔍 Basic Pointer Concepts
```c
// Declaration and initialization
int num = 10;
int *ptr = &num;    // ptr stores address of num

// Accessing values
printf("Value: %d\n", *ptr);     // Dereferencing
printf("Address: %p\n", (void*)ptr); // Printing address
```

### 🔢 Types of Pointers

#### 📍 Basic Pointers
```c
// Integer pointer
int *intPtr;

// Character pointer
char *charPtr;

// Float pointer
float *floatPtr;
```

#### 🎯 Special Pointers
```c
// Void pointer
void *voidPtr;     // Generic pointer type

// NULL pointer
int *nullPtr = NULL;

// Constant pointer
const int* constPtr;    // Value cannot be changed through pointer
int* const ptrConst;    // Pointer cannot point to different address
```

### 🎮 Pointer Operations

#### 📝 Basic Operations
```c
// Pointer arithmetic
int arr[] = {1, 2, 3, 4, 5};
int *p = arr;

p++;        // Move to next element
p--;        // Move to previous element
p += 2;     // Skip two elements
```

#### 🔄 Array and Pointer Relationship
```c
// Arrays and pointers
int arr[5] = {1, 2, 3, 4, 5};
int *ptr = arr;  // arr decays to pointer

// Accessing elements
printf("%d %d\n", arr[2], *(ptr + 2));  // Both print 3
```

### 💾 Dynamic Memory Management

#### 📦 Memory Allocation
```c
// malloc() - Memory allocation
int *ptr = (int*)malloc(sizeof(int));
*ptr = 10;

// calloc() - Cleared memory allocation
int *arr = (int*)calloc(5, sizeof(int));

// realloc() - Resize memory
arr = (int*)realloc(arr, 10 * sizeof(int));

// Always free allocated memory
free(ptr);
free(arr);
```

#### ⚠️ Common Mistakes
```c
// Memory leak
int *ptr = (int*)malloc(sizeof(int));
ptr = NULL;  // Memory leak! Original allocation lost

// Dangling pointer
int *ptr = (int*)malloc(sizeof(int));
free(ptr);
*ptr = 10;  // Dangling pointer! Memory already freed
```

### 🎯 Advanced Pointer Concepts

#### 📚 Pointer to Pointer
```c
int num = 10;
int *ptr1 = &num;
int **ptr2 = &ptr1;  // Pointer to pointer

printf("Value: %d\n", **ptr2);  // Access value through double pointer
```

#### 🔄 Function Pointers
```c
// Function pointer declaration
int (*operation)(int, int);

// Function definition
int add(int a, int b) { return a + b; }
int subtract(int a, int b) { return a - b; }

// Using function pointers
operation = add;
printf("Sum: %d\n", operation(5, 3));

operation = subtract;
printf("Difference: %d\n", operation(5, 3));
```

### 💡 Best Practices
- ✅ Always initialize pointers
- 🔍 Check for NULL before dereferencing
- 🔒 Free dynamically allocated memory
- ⚠️ Avoid dangling pointers
- 📝 Use const when pointer shouldn't modify data

### 🎯 Practice Problems
1. 📊 Implement array operations using pointers
2. 🔄 Create a dynamic array implementation
3. 📝 Build a simple memory allocator
4. 🎲 Implement string functions using pointers
5. 🔍 Create a pointer-based linked list

[⬅️ Previous Unit](#-unit-5-pointers-1) | [Next Unit ➡️](#-unit-6-advanced-topics-1)

## 🔨 Unit 6: Advanced Topics

### 📚 Structures and Unions

#### 🏗️ Structures
- A structure is a user-defined data type that groups related variables of different data types.
- Accessed using the dot `.` operator.
```c
struct Person {
    char name[50];
    int age;
};

struct Person p1;
strcpy(p1.name, "John");
p1.age = 30;
```

#### 🛠️ Unions
- A union is a user-defined data type that allows storing different data types in the same memory location.
- Only one member can contain a value at any given time.
```c
union Data {
    int intValue;
    float floatValue;
    char charValue;
};

union Data data;
data.intValue = 10;
```

### 📂 File Handling

#### 📁 File Operations
- **Open**: `fopen("filename", "mode")`
- **Close**: `fclose(filePointer)`
- **Read**: `fscanf()`, `fgets()`, `fread()`
- **Write**: `fprintf()`, `fputs()`, `fwrite()`
```c
FILE *fp;
fp = fopen("file.txt", "r");
fclose(fp);
```

#### 📊 Binary vs Text Files
- Text files store data in a human-readable format.
- Binary files store data in a machine-readable format (more compact, faster I/O).

### 🔄 Dynamic Memory Allocation

#### 📦 Memory Management Functions
- `malloc(size)`: Allocates `size` bytes and returns a pointer to the allocated memory.
- `calloc(n, size)`: Allocates memory for an array of `n` elements of `size` bytes each and initializes all bits to zero.
- `realloc(ptr, size)`: Resizes the memory block pointed to by `ptr` to `size` bytes.
- `free(ptr)`: Deallocates the memory previously allocated by `malloc`, `calloc`, or `realloc`.
```c
int *arr = (int*)malloc(5 * sizeof(int));  // Allocate memory for 5 integers
free(arr);  // Deallocate memory
```

### 📚 Advanced Data Types

#### 📊 Enumerations
- A user-defined data type that consists of integral constants.
- Enhances code readability by giving meaningful names to integral values.
```c
enum boolean { NO, YES };
enum boolean flag;
flag = YES;
```

#### 🔄 Typedef
- A keyword used to create an alias for a data type.
- Improves code readability and portability.
```c
typedef unsigned long ulong;
ulong fileSize;
```

### 📜 Preprocessor Directives

#### 📌 Common Directives
- `#define`: Defines macros or constants.
- `#include`: Includes header files.
- `#ifdef`, `#ifndef`, `#endif`: Conditional compilation.
```c
#define PI 3.14159
#include <stdio.h>
```

#### 🔄 Macros vs Functions
- Macros are replaced by the preprocessor before compilation, functions are compiled as part of the program.
- Macros do not have type checking, functions do.

### 💡 Best Practices
- Use structures to group related data.
- Prefer `fopen`/`fclose` for file handling.
- Use dynamic memory allocation for flexible data structures.
- Clean up allocated memory using `free`.
- Use enumerations and typedefs for better code readability.

### 🎯 Practice Problems
1. 📚 Create a library management system using structures
2. 🎲 Implement a stack using linked list and perform basic operations
3. 🌳 Build a binary search tree and implement search, insert, delete operations
4. 📁 Create a program to copy contents from one file to another
5. 🔄 Implement a memory pool for dynamic memory allocation

[⬅️ Previous Unit](#-unit-6-advanced-topics-1) | [Next Unit ➡️](#-unit-7-projects-and-resources-1)

## 🚀 Unit 7: Projects and Resources

### 📂 Mini Projects

#### 📚 Library Management System
- Features: Add, remove, search books; register and manage users; issue and return books.
- Technologies: C, file handling for data storage.

#### 🎲 Tic-Tac-Toe Game
- Features: Play against another player or AI; X and O markers; win/lose/draw detection.
- Technologies: C, basic algorithms for AI.

#### 🌳 Personal Diary Application
- Features: Add, view, edit, delete diary entries; search by date or keywords.
- Technologies: C, file handling for data storage.

### 📚 Resources

#### 📖 Books
- "The C Programming Language" by Brian W. Kernighan and Dennis M. Ritchie
- "C Programming: A Modern Approach" by K. N. King

#### 🌐 Online Tutorials
- [Learn-C.org](https://www.learn-c.org/)
- [CProgramming.com](https://www.cprogramming.com/)

#### 🎥 Video Lectures
- [Harvard's CS50: Introduction to Computer Science](https://cs50.harvard.edu/college/2021/fall/courses/cs50/)

### 💡 Best Practices
- Break projects into smaller, manageable tasks.
- Use version control (e.g., Git) for code management.
- Write clean, modular, and well-documented code.
- Test code thoroughly to identify and fix bugs.
- Continuously learn and explore new C programming concepts and techniques.

### 🎯 Practice Problems
1. 📚 Implement a complete library management system
2. 🎲 Create a multiplayer tic-tac-toe game with advanced AI
3. 🌳 Develop a personal diary application with encryption
4. 📁 Build a file compression and decompression tool
5. 🔄 Create a memory management library

[⬅️ Previous Unit](#-unit-7-projects-and-resources-1)
