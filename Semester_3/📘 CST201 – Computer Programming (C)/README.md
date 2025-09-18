# C Programming Course Notes 📘

> A comprehensive guide to C Programming fundamentals and advanced concepts.

## Table of Contents

### Unit 1: Basics of C
- [History and Evolution](#history-of-c)
- [Structured Programming](#advantages-of-structured-programming)
- [Files in C](#files-in-c)
- [Language Basics](#c-language-basics)
- [Operators & Types](#operators-and-types)
- [Input/Output](#input-and-output)

### Unit 2: Control Flow
- [Decision Making](#decision-making)
  - [if Statements](#if-statements)
  - [switch Statement](#switch-statement)
  - [goto Statement](#goto-statement)
- [Loops](#loops)
  - [while & do-while](#while-and-do-while)
  - [for Loop](#for-loop)
  - [Control Statements](#control-statements)

### Unit 3: Arrays & Strings
- [Arrays](#arrays)
  - [One-Dimensional Arrays](#one-dimensional-arrays)
  - [Multi-Dimensional Arrays](#multi-dimensional-arrays)
- [Strings](#strings)
  - [String Functions](#string-functions)
  - [String Operations](#string-operations)

### Unit 4: Functions
- [Function Basics](#function-basics)
- [Variable Scope](#scope-and-lifetime)
- [Storage Classes](#storage-classes)
- [Parameter Passing](#parameter-passing)
- [Recursion](#recursion)

### Unit 5: Pointers
- [Pointer Fundamentals](#pointer-fundamentals)
- [Types of Pointers](#types-of-pointers)
- [Pointer Operations](#pointer-operations)
- [Memory Management](#dynamic-memory-allocation)
- [Advanced Concepts](#advanced-pointer-concepts)

## Unit 1: Basics of C

### History of C
- Developed by Dennis Ritchie (1972) at Bell Labs
- Based on B and BCPL languages
- Used for UNIX Operating System development
- Foundation for modern languages (C++, Java, Python)

### Advantages of Structured Programming
- Modular program design
- Code reusability
- Easy debugging
- Team collaboration
- Systematic approach

### Files in C
1. **Source files** (.c)
   - Contains program code
   - Example: `program.c`

2. **Header files** (.h)
   - Contains function declarations
   - Example: `stdio.h`, `math.h`

3. **Object files** (.obj/.o)
   - Machine code after compilation
   - Not directly executable

4. **Executable files** (.exe/.out)
   - Final runnable program
   - Created by linker

### C Language Basics

#### Character Set
- Letters (A-Z, a-z)
- Digits (0-9)
- Special symbols (+, -, *, /, etc.)
- White space characters

#### Tokens
1. Keywords (32 reserved words)
2. Identifiers (variable/function names)
3. Constants (fixed values)
4. Strings ("text")
5. Operators (+, -, *, etc.)
6. Separators (;, {}, (), etc.)

### Operators and Types

#### Data Types
```c
int     // 2 or 4 bytes
float   // 4 bytes
double  // 8 bytes
char    // 1 byte
void    // empty
```

#### Operators
1. Arithmetic: `+`, `-`, `*`, `/`, `%`
2. Relational: `<`, `>`, `<=`, `>=`, `==`, `!=`
3. Logical: `&&`, `||`, `!`
4. Assignment: `=`, `+=`, `-=`, `*=`, `/=`
5. Increment/Decrement: `++`, `--`
6. Conditional: `?:`
7. Bitwise: `&`, `|`, `^`, `<<`, `>>`

### Input and Output

#### printf()
```c
printf("format_string", variables);
// Format specifiers: %d, %f, %c, %s
```

#### scanf()
```c
scanf("format_string", &variables);
// Always use & for variables
```

[Continue to Unit 2 →](#unit-2-control-flow)

## Unit 2: Control Flow

### Decision Making

#### if Statements
```c
if (condition) {
    // code
} else if (condition) {
    // code
} else {
    // code
}
```

[View full content and more examples...](./Unit2.md)

## Resources
- [Practice Problems](./Resources/Practice.md)
- [Sample Programs](./Resources/Samples.md)
- [Additional Reading](./Resources/Reading.md)

## Getting Started
1. Clone this repository
2. Navigate to specific units
3. Follow the examples
4. Try practice problems
5. Run sample programs

## License
MIT License - feel free to use and share

## Contributing
Pull requests are welcome. For major changes, please open an issue first.