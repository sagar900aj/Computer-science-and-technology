# OOPs JAVA

---

<p align="center">
  <img src="https://github.com/sagar900aj/Computer-science-and-technology/blob/Study/Semester_4/OOPs%20Using%20Java/java%20book%20cover.png" alt="OPPs Java book cover" width="100%">
</p>

---

## Full Index

### UNIT 1: Introduction to Java

1. Basics and History of Java
2. Java and Internet
3. Advantages of Java
4. Java Virtual Machine (JVM) & Bytecode
5. Java Environment Setup
6. Java Program Structure
7. Procedure-Oriented vs Object-Oriented Programming
8. OOP Concepts: Abstraction, Encapsulation, Inheritance, Polymorphism
9. Compiling and Running Java Program
10. Common Compilation & Runtime Errors

### UNIT 2: Building Blocks of the Language

1. Primitive Data Types
2. User Defined Data Types
3. Identifiers and Literals
4. Constants and Variables
5. Type Conversion and Casting
6. Scope and Default Values
7. Wrapper Classes
8. Garbage Collection
9. Arrays and Types of Arrays
10. String and String Buffer
11. Operators
12. Decision & Control Statements
13. Loops and Jump Statements

### UNIT 3: Object Oriented Programming Concepts

1. Classes and Objects
2. Fields and Methods
3. Access Rules
4. this Keyword
5. static Keyword
6. final Keyword
7. Method Overloading
8. Constructors
9. Constructor Overloading
10. Passing Objects as Parameters

### UNIT 4: Inheritance, Packages & Interfaces

1. Types of Inheritance
2. Method Overriding
3. Dynamic Method Dispatch
4. Object Class
5. Packages (Creating & Using)
6. Access Rules for Packages
7. Interfaces
8. Multiple Inheritance using Interfaces

### UNIT 5: Exception Handling & Multithreading

1. Types of Errors and Exceptions
2. try-catch Blocks
3. throw and throws
4. finally Block
5. User Defined Exceptions
6. Thread Creation
7. Thread Life Cycle
8. Thread Priority
9. Thread Synchronization
10. Exception Handling in Threads

### UNIT 6: File Handling

1. Stream Classes
2. Class Hierarchy
3. File Input and Output
4. Reading and Writing Text Files

---

## UNIT 1: Introduction to Java

### UNIT 1 – Topic 1: Basics & History of Java

#### Basics of Java

- Java is a **high-level, object-oriented programming language**
- Developed for **platform independence** → “Write Once, Run Anywhere”
- Uses **JVM (Java Virtual Machine)** to run programs

Key Features:

- Simple
- Object-Oriented
- Platform Independent
- Secure
- Robust

#### History of Java

- Developed by **James Gosling** at Sun Microsystems (1991)
- Original name: **Oak** → later changed to **Java**
- Official release: **1995**
- Now maintained by **Oracle Corporation**

#### Why Java was created?

- To create **portable programs** (run on any device)
- Mainly for **Internet-based applications**

---

### UNIT 1 – Topic 2: Java and Internet

#### What is Java’s role in Internet?

- Java is widely used for **web-based applications**
- It helps in creating **dynamic and interactive web pages**

#### How Java works on Internet

- Java programs are compiled into **bytecode**
- This bytecode runs on **JVM inside web browser or server**
- So, Java programs can run on **any system with JVM**

#### Java Technologies for Internet

- **Applets** → Small Java programs that run in browser *(now mostly outdated but important for exam)*
- **Servlets** → Used for server-side programming
- **JSP (Java Server Pages)** → Used to create dynamic web pages

#### Advantages in Internet use

- Platform independent → works on any OS
- Secure → suitable for online applications
- Robust → handles errors properly

---

### UNIT 1 – Topic 3: Advantages of Java

#### Main Advantages of Java

1. **Platform Independent**
    - Java program runs on any system with JVM
    - No need to rewrite code for different OS
2. **Object-Oriented**
    - Based on OOP concepts (class, object, inheritance, etc.)
    - Helps in code reusability and better structure
3. **Simple**
    - Easy to learn compared to C++
    - Removes complex features like pointers
4. **Secure**
    - No direct memory access
    - Bytecode runs inside JVM → safer execution
5. **Robust**
    - Strong memory management
    - Handles errors using exception handling
6. **Multithreading**
    - Can run multiple tasks at the same time
7. **Portable**
    - Same program works on different platforms
8. **High Performance**
    - Uses Just-In-Time (JIT) compiler for faster execution

---

### UNIT 1 – Topic 4: Java Virtual Machine (JVM) & Bytecode

#### What is JVM?

- JVM = **Java Virtual Machine**
- It is a **virtual environment** that runs Java programs
- JVM converts **bytecode → machine code**

Simple idea:

Java program does NOT run directly on OS, it runs inside JVM

#### What is Bytecode?

- When Java program is compiled → it generates **.class file**
- This file contains **bytecode (not machine code)**
- Bytecode is **platform independent**

#### Working Process

1. Write program → .java file
2. Compile using javac → generates .class file (bytecode)
3. JVM executes bytecode → converts into machine code

#### Why JVM is Important?

- Makes Java **platform independent**
- Provides **security**
- Handles **memory management**

---

### UNIT 1 – Topic 5: Java Environment Setup

#### What is Java Environment Setup?

- It means preparing your system to **write, compile, and run Java programs**

#### Steps to Setup Java

1. **Install JDK (Java Development Kit)**
    - JDK contains:
        - Compiler (javac)
        - JVM
        - Libraries
2. **Set Environment Variable (PATH)**
    - Add JDK bin folder to system PATH
    - Example path:C:\Program Files\Java\jdk\bin
3. **Check Installation**
    - Open terminal / command prompt
    - Type:
        - java -version
        - javac -version
    - If version shows → setup successful

#### Tools Required

- JDK (mandatory)
- Text Editor / IDE (VS Code, Notepad, etc.)

---

### UNIT 1 – Topic 6: Java Program Structure

#### Basic Structure of a Java Program

```java
class Hello {
public static void main(String[] args) {
System.out.println("Hello World");
}
}
```

#### Explanation

1. **class Hello**
    - Defines a class named Hello
    - Every Java program must have at least one class
2. **main() Method**
    - Entry point of program
    - Execution starts from here
3. **public static void main(String[] args)**
    - public → accessible from anywhere
    - static → no need to create object
    - void → no return value
    - String[] args → command line arguments
4. **System.out.println()**
    - Used to print output on screen

#### Important Rules

- File name must match class name → [Hello.java](http://Hello.java)
- Java is **case-sensitive**
- Every statement ends with ;

---

### UNIT 1 – Topic 7: Procedure-Oriented vs Object-Oriented Programming

#### Procedure-Oriented Programming (POP)

- Program is divided into **functions (procedures)**
- Focus is on **data + functions separately**

Example: C language

Features:

- Top-down approach
- Functions operate on data
- Less security (data is global)
- Difficult to manage large programs

#### Object-Oriented Programming (OOP)

- Program is divided into **objects (real-world entities)**
- Combines **data + methods in one unit (class)**

Example: Java

Features:

- Bottom-up approach
- Data hiding (security)
- Code reusability
- Easy to manage large programs

#### Key Differences (Exam Ready)

| **POP** | **OOP** |
| --- | --- |
| Based on functions | Based on objects |
| Top-down approach | Bottom-up approach |
| Less secure | More secure (data hiding) |
| No reusability | Supports reusability |
| Example: C | Example: Java |

---

### UNIT 1 – Topic 8: OOP Concepts

#### 1. Abstraction

- Hiding **internal details** and showing only **essential features**

Example:

- ATM machine → you use it, but don’t know internal working

Purpose: Reduce complexity

#### 2. Encapsulation

- Wrapping **data + methods** into a single unit (class)

Example:

```java
class Student {
int id;
void show() { }
}
```

Purpose: Data protection (data hiding)

#### 3. Inheritance

- One class **inherits properties** of another class

Example:

- Parent → Child class

Purpose: Code reusability

#### 4. Polymorphism

- Same method behaves **differently in different situations**

Types:

- Compile-time (Method Overloading)
- Runtime (Method Overriding)

Purpose: Flexibility in code

---

### UNIT 1 – Topic 9: Compiling and Running Java Program

#### Steps to Compile and Run

1. **Write Program**
    - Save file with .java extension
    - Example: [Hello.java](http://Hello.java)
2. **Compile the Program**
    - Use command:
        - javac [Hello.java](http://Hello.java)
    - Output → creates Hello.class (bytecode)
3. **Run the Program**
    - Use command:
        - java Hello
    - Output will be displayed on screen

#### Flow (Important)

Hello.java → (javac) → Hello.class → (JVM) → Output

#### Common Points

- Compilation checks **syntax errors**
- JVM executes the compiled program

#### Exam Points (Important)

- javac = compiler
- java = run program
- .java → .class → output

---

### UNIT 1 – Topic 10: Common Compilation & Runtime Errors

#### 1. Compilation Errors (Syntax Errors)

- Occur during **compilation (javac)**
- Due to **wrong syntax**

Examples:

- Missing ;
- Wrong spelling of keywords
- Missing brackets { }

Example:

int a = 10   // ❌ missing semicolon

#### 2. Runtime Errors

- Occur during **program execution (java)**
- Program compiles but crashes while running

Examples:

- Division by zero
- Null pointer
- Array index out of bounds

Example:

int a = 10 / 0;  // ❌ runtime error

#### 3. Logical Errors

- Program runs but gives **wrong output**
- Hard to detect

Example:

int sum = a - b; // ❌ should be a + b

---

## UNIT 2: Building Blocks of the Language

### UNIT 2 – Topic 1: Primitive Data Types

#### What are Primitive Data Types?

- Basic built-in data types in Java
- Used to store **simple values (not objects)**

#### Types of Primitive Data Types

| **Data Type** | **Size** | **Example** |
| --- | --- | --- |
| byte | 1 byte | 10 |
| short | 2 bytes | 1000 |
| int | 4 bytes | 100000 |
| long | 8 bytes | 100000L |
| float | 4 bytes | 10.5f |
| double | 8 bytes | 10.5 |
| char | 2 bytes | 'A' |
| boolean | 1 bit | true / false |

#### Explanation (Simple)

- **int** → integer numbers
- **float/double** → decimal numbers
- **char** → single character
- **boolean** → true/false

#### Example

int a = 10;

float b = 5.5f;

char c = 'A';

boolean d = true;

---

### UNIT 2 – Topic 2: User Defined Data Types

#### What are User Defined Data Types?

- Data types **created by the programmer**
- Used to store **complex data (objects)**

#### Examples in Java

- **Class**
- **Interface**
- **Array**

#### Class (Most Important)

- A class is a **blueprint of objects**

Example:

```java
class Student {
int id;
String name;
}
```

#### Object

- Object is an **instance of a class**

Example:

Student s1 = new Student();

#### Array (also user defined type)

- Used to store **multiple values of same type**

Example:

int arr[] = {1, 2, 3};

---

### UNIT 2 – Topic 3: Identifiers and Literals

#### Identifiers

- Identifiers are **names given to variables, classes, methods, etc.**

Examples:

int age;

class Student { }

void show() { }

#### Rules for Identifiers

- Must start with **letter, _ (underscore), or $**
- Cannot start with number
- Cannot use **keywords** (like int, class)
- Case-sensitive

Valid:

- age, _num, $value

Invalid:

- 1age, int, class

#### Literals

- Literals are **fixed values (constants)** used in program

Examples:

int a = 10;      // 10 is integer literal

char c = 'A';    // 'A' is character literal

float f = 5.5f;  // 5.5f is float literal

#### Types of Literals

- Integer literals → 10, 20
- Floating literals → 3.14, 5.5f
- Character literals → 'A'
- String literals → "Hello"
- Boolean literals → true, false

---

### UNIT 2 – Topic 4: Constants and Variables

#### Variables

- Variable = **named memory location** used to store data
- Value can **change during program execution**

Example:

int a = 10;

a = 20;   // value changed

#### Types of Variables (Basic idea)

- Local variable → inside method
- Instance variable → inside class, outside method
- Static variable → declared with static keyword

#### Constants

- Constant = value that **cannot be changed**
- Declared using final keyword

Example:

final int MAX = 100;

#### Difference (Exam Ready)

| **Variable** | **Constant** |
| --- | --- |
| Value can change | Value cannot change |
| Normal declaration | Uses final keyword |
| Example: int a = 10 | Example: final int MAX = 100 |

---

### UNIT 2 – Topic 5: Type Conversion and Casting

#### What is Type Conversion?

- Changing one data type to another

#### Types of Conversion

1. **Implicit Conversion (Automatic)**
- Done automatically by Java
- Converts **smaller type → larger type**

Example:

int a = 10;

double b = a;   // int → double

No data loss

1. **Explicit Conversion (Casting)**
- Done manually by programmer
- Converts **larger type → smaller type**

Example:

double x = 10.5;

int y = (int)x;   // double → int

Data loss possible (decimal removed)

#### Key Points

- Implicit → safe conversion
- Explicit → needs casting (type)
- Use casting when types are not compatible

---

### UNIT 2 – Topic 6: Scope and Default Values of Variables

#### Scope of Variables

- Scope = **where a variable can be used in program**

#### Types of Scope

1. **Local Variable**
- Declared **inside method/block**
- Accessible **only inside that method**

Example:

void show() {

int a = 10;   // local variable

}

1. **Instance Variable**
- Declared **inside class, outside method**
- Accessed using **object**

Example:

class Test {

int x = 5;   // instance variable

}

1. **Static Variable**
- Declared with **static keyword**
- Shared by all objects

Example:

class Test {

static int count = 0;

}

#### Default Values of Variables

Only for **instance & static variables** (not local)

| **Data Type** | **Default Value** |
| --- | --- |
| int | 0 |
| float | 0.0 |
| double | 0.0 |
| char | '' |
| boolean | false |
| object | null |

#### Important Point

- **Local variables have NO default value**
- Must initialize before use

---

### UNIT 2 – Topic 7: Wrapper Classes

#### What are Wrapper Classes?

- Wrapper classes convert **primitive data types → objects**

Example:

- `int` → `Integer`
- `float` → `Float`
- `char` → `Character`

#### Why Wrapper Classes are used?

- Java works with **objects (OOP concept)**
- Sometimes we need primitive values as **objects**

#### Common Wrapper Classes

| Primitive | Wrapper Class |
| --- | --- |
| int | Integer |
| float | Float |
| double | Double |
| char | Character |
| boolean | Boolean |

#### Example

```
inta=10;
Integerobj=Integer.valueOf(a);// primitive → object
```

#### Autoboxing & Unboxing

- **Autoboxing** → primitive → object automatically
- **Unboxing** → object → primitive

Example:

```
Integerobj=10;// autoboxing
intx=obj;// unboxing
```

---

### UNIT 2 – Topic 8: Garbage Collection

#### What is Garbage Collection?

- Process of **removing unused objects from memory**
- Done automatically by Java

Purpose: **Free memory & improve performance**

#### Why needed?

- In Java, memory is allocated using `new`
- Some objects become **unused (no reference)**
- Garbage Collector deletes them

#### Example

```
Strings=newString("Hello");
s=null;// object becomes unused
```

Now this object is eligible for garbage collection

#### How Garbage Collector Works

- JVM automatically checks **unused objects**
- Deletes them from memory

#### Important Points

- No need to manually free memory (unlike C/C++)
- Java provides method:

```
System.gc();
```

It requests JVM to run garbage collector (not guaranteed)

---

### UNIT 2 – Topic 9: Arrays and Types of Arrays

#### What is an Array?

- Array = collection of **same type of elements**
- Stored in **continuous memory locations**

#### Declaration of Array

```
intarr[]=newint[5];
```

#### Initialization

```
intarr[]= {1,2,3,4,5};
```

#### Accessing Elements

```
System.out.println(arr[0]);// first element
```

#### Types of Arrays

#### 1. One-Dimensional Array

- Single list of elements

Example:

```
inta[]= {10,20,30};
```

#### 2. Two-Dimensional Array

- Array of arrays (matrix form)

Example:

```
inta[][]= {
    {1,2},
    {3,4}
};
```

#### 3. Multidimensional Array

- More than 2 dimensions

Example:

```
inta[][][]=newint[2][2][2];
```

#### Important Points

- Index starts from **0**
- Size is fixed after creation

---

### UNIT 2 – Topic 10: String and String Buffer

#### What is String?

- String = **sequence of characters**
- In Java, String is an **object (class)**

Example:

```
Strings="Hello";
```

#### Important String Operations

1. **Concatenation (joining strings)**

```
Strings1="Hello";
Strings2="World";
Strings3=s1+s2;// HelloWorld
```

1. **Length**

```
s.length();
```

1. **Change Case**

```
s.toUpperCase();
s.toLowerCase();
```

1. **Character Extraction**

```
s.charAt(0);
```

1. **String Comparison**

```
s1.equals(s2);
```

#### What is String Buffer?

- Used for **mutable strings (can change)**
- More efficient for frequent modifications

Example:

```
StringBuffersb=newStringBuffer("Hello");
sb.append(" World");
```

#### Difference (Exam Ready)

| String | StringBuffer |
| --- | --- |
| Immutable | Mutable |
| Cannot change | Can change |
| Slower for modification | Faster |

---

### UNIT 2 – Topic 11: Operators

#### What are Operators?

- Operators are **symbols used to perform operations** on variables/values

#### Types of Operators

#### 1. Arithmetic Operators

- Used for **mathematical operations**

| Operator | Meaning |
| --- | --- |
| + | Addition |
| - | Subtraction |
| * | Multiplication |
| / | Division |
| % | Modulus |

Example:

```
intc=a+b;
```

#### 2. Relational Operators

- Used for **comparison**

| Operator | Meaning |
| --- | --- |
| == | Equal |
| != | Not equal |
| > | Greater |
| < | Less |
| >= | Greater or equal |
| <= | Less or equal |

Output is always **true/false**

#### 3. Logical Operators

- Used with **boolean values**

| Operator | Meaning |
| --- | --- |
| && | AND |
| || | OR |
| ! | NOT |

#### 4. Assignment Operators

- Used to assign values

| Operator | Example |
| --- | --- |
| = | a = 10 |
| += | a += 5 |
| -= | a -= 5 |

#### 5. Increment & Decrement

- Increase/decrease value by 1

```
a++;// increment
a--;// decrement
```

#### 6. Conditional (Ternary) Operator

- Short form of if-else

```
intmax= (a>b)?a :b;
```

---

### UNIT 2 – Topic 12: Decision & Control Statements

#### What are Decision Statements?

- Used to **make decisions in program flow**
- Execute code based on **condition (true/false)**

#### Types of Decision Statements

#### 1. if Statement

```
if(condition) {
// code
}
```

#### 2. if-else Statement

```
if(condition) {
// true block
}else {
// false block
}
```

#### 3. else-if Ladder

```
if(cond1) {
// code
}elseif(cond2) {
// code
}else {
// default
}
```

#### 4. switch Statement

- Used for **multiple choices**

```
switch(value) {
case1:
// code
break;
case2:
// code
break;
default:
// code
}
```

#### Control Statements

- Control the **flow of execution**

Includes:

- Decision statements
- Loop statements (next topic)
- Jump statements (break, continue, return)

---

### UNIT 2 – Topic 13: Loops and Jump Statements

#### What are Loops?

- Loops are used to **repeat a block of code multiple times**

#### Types of Loops

#### 1. while Loop

- Checks condition **before execution**

```
inti=1;
while(i<=5) {
System.out.println(i);
i++;
}
```

#### 2. do-while Loop

- Executes **at least once**, then checks condition

```
inti=1;
do {
System.out.println(i);
i++;
}while(i<=5);
```

#### 3. for Loop

- Used when number of iterations is known

```
for(inti=1;i<=5;i++) {
System.out.println(i);
}
```

#### Jump Statements

#### 1. break

- Stops the loop

```
break;
```

#### 2. continue

- Skips current iteration

```
continue;
```

#### 3. return

- Exits from method

```
return;
```

---

## UNIT 3 – Topic 1: Classes and Objects

### What is a Class?

- Class = **blueprint/template** to create objects
- It contains **variables (fields) + methods (functions)**

Example:

```
classStudent {
intid;
Stringname;

voidshow() {
System.out.println(id+" "+name);
    }
}
```

### What is an Object?

- Object = **instance of a class**
- Used to access class properties

Example:

```
Students1=newStudent();
s1.id=1;
s1.name="Sagar";
s1.show();
```

### Key Points

- Class defines structure
- Object uses that structure
- Multiple objects can be created from one class

---

## UNIT 3 – Topic 2: Fields and Methods

### What are Fields?

- Fields = **variables inside a class**
- Used to store **data of an object**

Example:

```
classStudent {
intid;// field
Stringname;// field
}
```

### What are Methods?

- Methods = **functions inside a class**
- Used to **perform operations**

Example:

```
classStudent {
voidshow() {// method
System.out.println("Hello");
    }
}
```

### Types of Methods (Basic)

- With return type
- Without return type (`void`)

Example:

```
intadd(inta,intb) {
returna+b;
}
```

### Key Points

- Fields store data
- Methods perform actions
- Both are part of a class

---

## UNIT 3 – Topic 3: Access Rules (Access Modifiers)

### What are Access Modifiers?

- Define **who can access variables, methods, and classes**

### Types of Access Modifiers

| Modifier | Access Level |
| --- | --- |
| public | Accessible from anywhere |
| private | Accessible only within same class |
| protected | Accessible within package + subclasses |
| default (no keyword) | Accessible within same package |

### Example

```
classTest {
publicinta=10;
privateintb=20;
}
```

### Explanation

- `public` → can be used anywhere
- `private` → only inside class
- `protected` → package + inheritance
- `default` → only same package

### Key Points

- Used for **data security and control**
- Important in **encapsulation**

---

## UNIT 3 – Topic 4: `this` Keyword

### What is `this`?

- `this` is a **reference variable** that refers to the **current object**

### Why use `this`?

- To **distinguish between instance variables and parameters**
- To **refer current object**

### Example

```
classStudent {
intid;

voidsetId(intid) {
this.id=id;// this.id = instance variable
    }
}
```

Here:

- `id` → parameter
- `this.id` → instance variable

### Other Uses of `this`

1. Call current class method
2. Pass current object as argument
3. Call constructor

### Key Points

- `this` always refers to **current object**
- Mostly used when variable names are same

---

## UNIT 3 – Topic 5: `static` Keyword

### What is `static`?

- `static` means **belongs to class, not to objects**

### Why use `static`?

- To **share data among all objects**
- Memory efficient (only one copy exists)

### Example

```
classTest {
staticintcount=0;
}
```

All objects share same `count`

### Static Method

```
classDemo {
staticvoidshow() {
System.out.println("Hello");
    }
}
```

Can be called without object:

```
Demo.show();
```

### Important Points

- Static variable → shared
- Static method → called using class name
- Cannot directly use non-static variables inside static method

---

## UNIT 3 – Topic 6: `final` Keyword

### What is `final`?

- `final` means **value cannot be changed**

### Uses of `final`

### 1. Final Variable

- Value becomes **constant**

```
finalintMAX=100;
```

Cannot change value later

### 2. Final Method

- Cannot be **overridden** by subclass

```
finalvoidshow() {
System.out.println("Hello");
}
```

### 3. Final Class

- Cannot be **inherited (extended)**

```
finalclassTest { }
```

### Key Points

- final variable → constant
- final method → no overriding
- final class → no inheritance

---

## UNIT 3 – Topic 7: Method Overloading

### What is Method Overloading?

- Same method name, but **different parameters**
- Occurs in **same class**

### How to Overload?

Method must differ in:

- Number of parameters
- Type of parameters
- Order of parameters

### Example

```
classDemo {
intadd(inta,intb) {
returna+b;
    }

intadd(inta,intb,intc) {
returna+b+c;
    }
}
```

### Key Points

- Same method name
- Different parameter list
- Return type alone is **not enough**

### Why use it?

- Improves **code readability**
- Provides **flexibility**

---

## UNIT 3 – Topic 8: Constructors

### What is a Constructor?

- Special method used to **initialize objects**
- Has **same name as class**
- No return type (not even `void`)

### Types of Constructors

### 1. Default Constructor

- No parameters

```
classDemo {
Demo() {
System.out.println("Default Constructor");
    }
}
```

### 2. Parameterized Constructor

- Takes parameters

```
classDemo {
intx;
Demo(inta) {
x=a;
    }
}
```

### Key Points

- Called automatically when object is created
- Used to initialize values

### Example

```
Demod1=newDemo();// default
Demod2=newDemo(10);// parameterized
```

---

## UNIT 3 – Topic 9: Constructor Overloading

### What is Constructor Overloading?

- Multiple constructors in the **same class**
- Same name (class name) but **different parameters**

### Why use it?

- To **initialize objects in different ways**

### Example

```
classDemo {
intx;

Demo() {
x=0;
    }

Demo(inta) {
x=a;
    }
}
```

### Object Creation

```
Demod1=newDemo();// calls default constructor
Demod2=newDemo(10);// calls parameterized constructor
```

### Key Points

- Same constructor name
- Different parameter list
- Improves flexibility

---

## UNIT 3 – Topic 10: Passing Objects as Parameters

### What does it mean?

- Passing an **object to a method as argument**
- Method can **access and modify object data**

### Example

```
classTest {
intx;

voidsetValue(Testt) {
t.x=100;
    }
}

classMain {
publicstaticvoidmain(String[]args) {
Testobj=newTest();
obj.setValue(obj);
System.out.println(obj.x);// 100
    }
}
```

### Explanation

- `obj` is passed to method `setValue()`
- Method modifies `t.x` → affects original object

### Key Points

- Objects are passed by **reference (address)**
- Changes inside method affect original object

---

## UNIT 4 – Topic 1: Types of Inheritance

### What is Inheritance?

- Inheritance = **one class acquires properties of another class**
- Parent class → **Superclass**
- Child class → **Subclass**

### Types of Inheritance in Java

### 1. Single Inheritance

- One parent → one child

```
classA { }
classBextendsA { }
```

### 2. Multilevel Inheritance

- Chain of inheritance

```
classA { }
classBextendsA { }
classCextendsB { }
```

### 3. Hierarchical Inheritance

- One parent → multiple children

```
classA { }
classBextendsA { }
classCextendsA { }
```

### 4. Multiple Inheritance

- One class inherits from multiple classes

❌ Not supported in Java using classes

✅ Supported using **interfaces**

### 5. Hybrid Inheritance

- Combination of different types

❌ Not directly supported using classes

### Key Points

- Use `extends` keyword
- Promotes **code reuse**
- Java does not support multiple inheritance via classes

---

## UNIT 4 – Topic 2: Method Overriding

### What is Method Overriding?

- Same method name + same parameters
- Defined in **parent class** and **redefined in child class**

### Purpose

- To provide **different implementation** in subclass

### Example

```
classA {
voidshow() {
System.out.println("Parent class");
    }
}

classBextendsA {
voidshow() {
System.out.println("Child class");
    }
}
```

### Key Points

- Method name must be same
- Parameters must be same
- Happens between **parent & child class**

### Important Rules

- Cannot override **final method**
- Access level should not be more restrictive

---

## UNIT 4 – Topic 3: Dynamic Method Dispatch

### What is Dynamic Method Dispatch?

- Mechanism by which a **call to an overridden method is resolved at runtime**
- Depends on **object type (not reference type)**

### Simple Idea

- Parent reference → Child object
- Method call decided at **runtime**

### Example

```
classA {
voidshow() {
System.out.println("Parent");
    }
}

classBextendsA {
voidshow() {
System.out.println("Child");
    }
}

classMain {
publicstaticvoidmain(String[]args) {
Aobj=newB();// parent reference, child object
obj.show();// calls child method
    }
}
```

### Explanation

- Reference type = A
- Object type = B
- Output → **Child method is called**

### Key Points

- Happens only in **method overriding**
- Decided at **runtime**
- Supports **runtime polymorphism**

---

## UNIT 4 – Topic 4: Object Class

### What is Object Class?

- `Object` is the **root (super) class of all classes in Java**
- Every class **automatically inherits** from `Object`

### Why it is Important?

- Provides **common methods** for all objects

### Common Methods of Object Class

1. **toString()**
- Converts object to string

```
System.out.println(obj.toString());
```

1. **equals()**
- Compares two objects

```
obj1.equals(obj2);
```

1. **hashCode()**
- Returns unique hash value of object

```
obj.hashCode();
```

### Key Points

- All classes inherit `Object` class
- Methods can be **overridden**

---

## UNIT 4 – Topic 5: Creating and Using Packages

### What is a Package?

- Package = **collection of related classes**
- Used to **organize code**

### Why use Packages?

- Avoid naming conflict
- Provide access control
- Improve code management

### Creating a Package

```
packagemypack;

classTest {
voidshow() {
System.out.println("Hello");
    }
}
```

### Compiling Package

```
javac -d . Test.java
```

### Using a Package

### 1. Using import keyword

```
importmypack.Test;
```

### 2. Using full name

```
mypack.Testobj=newmypack.Test();
```

### Key Points

- `package` keyword → define package
- `import` keyword → use package
- Helps in code organization

---

## UNIT 4 – Topic 6: Access Rules for Packages

### What are Access Rules in Packages?

- Define **how classes and members are accessed** from different packages
- Controlled using **access modifiers**

### Access Modifiers and Package Access

| Modifier | Same Class | Same Package | Different Package |
| --- | --- | --- | --- |
| public | ✔ | ✔ | ✔ |
| protected | ✔ | ✔ | ✔ (via inheritance) |
| default | ✔ | ✔ | ❌ |
| private | ✔ | ❌ | ❌ |

### Explanation

- **public** → accessible everywhere
- **protected** → same package + subclasses
- **default** → only inside same package
- **private** → only inside same class

### Example

```
packagep1;

publicclassA {
protectedintx=10;
}
```

### Key Points

- Access depends on **modifier + package**
- Important for **security and control**

---

## UNIT 4 – Topic 7: Interfaces

### What is an Interface?

- Interface = **collection of abstract methods**
- Used to achieve **100% abstraction**

### Syntax

```
interfaceShape {
voiddraw();// abstract method
}
```

### Implementing Interface

```
classCircleimplementsShape {
publicvoiddraw() {
System.out.println("Drawing Circle");
    }
}
```

### Key Points

- Use `interface` keyword
- Methods are **public and abstract by default**
- Cannot create object of interface
- Class uses `implements` keyword

### Why Interfaces?

- Provide **abstraction**
- Support **multiple inheritance**

---

## UNIT 4 – Topic 8: Multiple Inheritance using Interfaces

### What is Multiple Inheritance?

- One class inherits from **more than one parent**

In Java:

- ❌ Not possible using classes
- ✅ Possible using **interfaces**

### How it works?

- A class can **implement multiple interfaces**

### Example

```
interfaceA {
voidshow();
}

interfaceB {
voiddisplay();
}

classTestimplementsA,B {
publicvoidshow() {
System.out.println("From A");
    }

publicvoiddisplay() {
System.out.println("From B");
    }
}
```

### Key Points

- Use `implements` keyword
- Can implement multiple interfaces
- Must define all methods

---

## UNIT 5 – Topic 1: Types of Errors and Exceptions

### What is an Error?

- Error = **problem in program execution**
- Causes program to **stop or behave incorrectly**

### Types of Errors

### 1. Compile-Time Error

- Occurs during **compilation**
- Due to **syntax mistakes**

Example:

```
inta=10// missing semicolon
```

### 2. Runtime Error

- Occurs during **execution**
- Program compiles but crashes

Example:

```
inta=10/0;// divide by zero
```

### 3. Logical Error

- Program runs but gives **wrong output**

Example:

```
intsum=a-b;// wrong logic
```

### What is an Exception?

- Exception = **runtime error that can be handled**
- Java provides mechanism to **handle exceptions**

### Key Difference

| Error | Exception |
| --- | --- |
| Cannot be handled easily | Can be handled using code |
| Causes program crash | Can continue program |

---

## UNIT 5 – Topic 2: try-catch Blocks

### What is try-catch?

- Used to **handle exceptions (runtime errors)**
- Prevents program from crashing

### Syntax

```
try {
// risky code
}catch(Exceptione) {
// handling code
}
```

### Example

```
try {
inta=10/0;
}catch(ArithmeticExceptione) {
System.out.println("Cannot divide by zero");
}
```

### Multiple catch Blocks

- Handle different exceptions separately

```
try {
inta[]=newint[5];
a[10]=50;
}catch(ArrayIndexOutOfBoundsExceptione) {
System.out.println("Array error");
}catch(Exceptione) {
System.out.println("General error");
}
```

### Key Points

- `try` → contains risky code
- `catch` → handles exception
- Program continues after handling

---

## UNIT 5 – Topic 3: `throw` and `throws` Keywords

### `throw` Keyword

- Used to **explicitly throw an exception**

Example:

```
thrownewArithmeticException("Error occurred");
```

### `throws` Keyword

- Used to **declare exceptions** in method signature
- Tells that method **may cause exception**

Example:

```
voidshow()throws ArithmeticException {
inta=10/0;
}
```

### Difference (Exam Ready)

| throw | throws |
| --- | --- |
| Used inside method | Used in method declaration |
| Throws single exception | Can declare multiple exceptions |
| Used to create exception | Used to inform about exception |

### Key Points

- `throw` → actual throwing
- `throws` → declaration

---

## UNIT 5 – Topic 4: finally Block

### What is `finally` Block?

- `finally` block is used to execute **important code always**
- Runs **whether exception occurs or not**

### Syntax

```
try {
// risky code
}catch(Exceptione) {
// handle exception
}finally {
// always executes
}
```

### Example

```
try {
inta=10/2;
}catch(Exceptione) {
System.out.println("Error");
}finally {
System.out.println("Always executed");
}
```

### Key Points

- Executes in **all cases** (exception or no exception)
- Used for **cleanup tasks** (closing files, releasing resources)

### Important Note

- Even if `try` or `catch` has `return`, `finally` still executes

---

## UNIT 5 – Topic 5: User Defined Exceptions

### What are User Defined Exceptions?

- Custom exceptions **created by programmer**
- Used when built-in exceptions are not enough

### How to Create?

- Create a class that **extends Exception**

### Example

```
classMyExceptionextendsException {
MyException(Stringmsg) {
super(msg);
    }
}
```

### Using User Defined Exception

```
classTest {
voidcheck(intage)throwsMyException {
if(age<18) {
thrownewMyException("Not eligible");
        }
    }
}
```

### Key Points

- Must extend `Exception` class
- Use `throw` to throw exception
- Use `throws` in method

---

## UNIT 5 – Topic 6: Thread Creation

### What is a Thread?

- Thread = **smallest unit of execution**
- Used to perform **multiple tasks simultaneously**

### Ways to Create Thread

### 1. Extending Thread Class

```
classMyThreadextendsThread {
publicvoidrun() {
System.out.println("Thread running");
    }
}

MyThreadt=newMyThread();
t.start();
```

### 2. Implementing Runnable Interface

```
classMyThreadimplementsRunnable {
publicvoidrun() {
System.out.println("Thread running");
    }
}

Threadt=newThread(MyThread);
t.start();
```

### Key Points

- `run()` method contains code to execute
- `start()` method starts the thread
- Do not call `run()` directly

---

## UNIT 5 – Topic 7: Thread Life Cycle

### What is Thread Life Cycle?

- It shows **different states of a thread** from creation to termination

### States of Thread

1. **New**
- Thread is created but not started
1. **Runnable**
- Thread is ready to run (waiting for CPU)
1. **Running**
- Thread is executing
1. **Blocked / Waiting**
- Thread is waiting for resource or event
1. **Terminated (Dead)**
- Thread execution finished

### Flow (Important)

```
New → Runnable → Running → Waiting → Running → Terminated
```

### Key Points

- Thread moves between states
- Controlled by JVM and scheduler

---

## UNIT 5 – Topic 8: Thread Priority

### What is Thread Priority?

- Thread priority defines **which thread gets CPU first**
- Higher priority → more chance to execute

### Priority Values

- Range: **1 to 10**

| Constant | Value |
| --- | --- |
| MIN_PRIORITY | 1 |
| NORM_PRIORITY | 5 (default) |
| MAX_PRIORITY | 10 |

### Example

```
Threadt1=newThread();
t1.setPriority(10);// highest priority
```

### Get Priority

```
t1.getPriority();
```

### Key Points

- Default priority = 5
- Scheduler decides execution (not guaranteed)

---

## UNIT 5 – Topic 9: Thread Synchronization

### What is Thread Synchronization?

- Process of **controlling access of multiple threads** to shared resources
- Ensures **data consistency**

### Why needed?

- When multiple threads access same data → **data inconsistency problem**

### Example Problem

- Two threads updating same variable → wrong result

### Solution: Synchronization

### 1. Synchronized Method

```
synchronizedvoidshow() {
// critical section
}
```

### 2. Synchronized Block

```
synchronized(this) {
// critical section
}
```

### Key Points

- Only one thread can access synchronized block at a time
- Prevents data inconsistency

---

## UNIT 5 – Topic 10: Exception Handling in Threads

### What is it?

- Handling **exceptions inside threads**
- Prevents thread from crashing unexpectedly

### How to Handle?

- Use **try-catch inside run() method**

### Example

```
classMyThreadextendsThread {
publicvoidrun() {
try {
inta=10/0;
        }catch(ArithmeticExceptione) {
System.out.println("Error in thread");
        }
    }
}
```

### Key Points

- Exception must be handled **inside thread**
- Each thread handles its own exception

---

## UNIT 6 – Topic 1: Stream Classes

### What is a Stream?

- Stream = **flow of data** between program and file/device
- Used for **input and output (I/O)** operations

### Types of Streams

### 1. Input Stream

- Used to **read data**

Example:

- `FileInputStream`

### 2. Output Stream

- Used to **write data**

Example:

- `FileOutputStream`

### Byte Stream vs Character Stream

| Type | Description |
| --- | --- |
| Byte Stream | Handles binary data (bytes) |
| Character Stream | Handles text data (characters) |

### Examples of Stream Classes

- `InputStream`, `OutputStream`
- `FileInputStream`, `FileOutputStream`
- `FileReader`, `FileWriter`

### Key Points

- Used for file handling
- Two main types → Input & Output

---

## UNIT 6 – Topic 2: Class Hierarchy (Stream Classes)

### What is Class Hierarchy?

- Shows **parent-child relationship of classes**
- In Java I/O, stream classes follow a **hierarchical structure**

### Basic Hierarchy

```
          Object
            |
    -------------------
    |                 |
InputStream     OutputStream
    |                 |
FileInputStream  FileOutputStream
```

### Character Stream Hierarchy

```
   Object
     |
   Reader
     |
FileReader

   Object
     |
   Writer
     |
FileWriter
```

### Explanation

- `InputStream` / `OutputStream` → base classes (byte stream)
- `Reader` / `Writer` → base classes (character stream)
- File classes are derived from these

### Key Points

- Hierarchy helps in **code reuse**
- All classes ultimately come from **Object class**

---

## UNIT 6 – Topic 3: File Input and Output

### What is File I/O?

- File I/O = **reading from and writing to files**
- Uses **stream classes**

### Writing to a File (Output)

Using FileOutputStream:

```
importjava.io.*;

classTest {
publicstaticvoidmain(String[]args)throwsException {
FileOutputStreamfout=newFileOutputStream("test.txt");
fout.write(65);// writes 'A'
fout.close();
    }
}
```

### Reading from a File (Input)

Using FileInputStream:

```java
importjava.io.*;

classTest {
publicstaticvoidmain(String[]args)throwsException {
FileInputStreamfin=newFileInputStream("test.txt");
inti=fin.read();
System.out.println((char)i);
fin.close();
    }
}
```

### Key Points

- `FileInputStream` → read file
- `FileOutputStream` → write file
- Always **close the stream**

---

## UNIT 6 – Topic 4: Reading and Writing Text Files

### What is Text File Handling?

- Used to **store and process text data**
- Uses **character streams**

### Writing Text File

Using FileWriter:

```
importjava.io.*;

classTest {
publicstaticvoidmain(String[]args)throwsException {
FileWriterfw=newFileWriter("test.txt");
fw.write("Hello World");
fw.close();
    }
}
```

### Reading Text File

Using FileReader:

```
importjava.io.*;

classTest {
publicstaticvoidmain(String[]args)throwsException {
FileReaderfr=newFileReader("test.txt");
inti;
while((i=fr.read())!=-1) {
System.out.print((char)i);
        }
fr.close();
    }
}
```

### Key Points

- `FileWriter` → write text
- `FileReader` → read text
- Loop used to read full file
