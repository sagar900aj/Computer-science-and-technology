# 📘 CST203 – Scripting Languages (Python)

**Exam-Ready Study Notes with Working Code Examples**

---

## Unit 1: Python Basics

### Topics Covered
- Python syntax and structure
- Data types (int, float, string, list, tuple, dict)
- Variables and naming conventions
- Comments and docstrings
- Input/output operations
- String operations

### Key Concepts

**1. Data Types and Variables**
```python
# Integer
age = 25
print(f"Age: {age}, Type: {type(age)}")

# Float
gpa = 3.75
height = 5.9
print(f"GPA: {gpa}, Height: {height}")

# String
name = "Ravi Kumar"
grade = 'A'
print(f"Name: {name}, Grade: {grade}")

# Boolean
is_student = True
is_working = False
print(f"Student: {is_student}, Working: {is_working}")
```

**2. Input/Output Operations**
```python
# Taking input
name = input("Enter your name: ")
age = int(input("Enter your age: "))
salary = float(input("Enter salary: "))

# Display output
print("Name:", name)
print("Age:", age)
print("Salary:", salary)

# Formatted strings
print(f"Welcome {name}! You are {age} years old.")
print("Name: %s, Age: %d" % (name, age))
```

**3. Arithmetic Operators**
```python
a = 10
b = 3

print(f"Addition: {a} + {b} = {a + b}")
print(f"Subtraction: {a} - {b} = {a - b}")
print(f"Multiplication: {a} * {b} = {a * b}")
print(f"Division: {a} / {b} = {a / b}")
print(f"Integer Division: {a} // {b} = {a // b}")
print(f"Modulo: {a} % {b} = {a % b}")
print(f"Power: {a} ** {b} = {a ** b}")
```

**4. String Operations**
```python
text = "Python Programming"

print(f"Length: {len(text)}")
print(f"Uppercase: {text.upper()}")
print(f"Lowercase: {text.lower()}")
print(f"Replace: {text.replace('Programming', 'Language')}")
print(f"Split: {text.split()}")

# String slicing
print(f"First 6 chars: {text[:6]}")
print(f"Last 11 chars: {text[-11:]}")
print(f"Reverse: {text[::-1]}")
```

---

## Unit 2: Control Structures

### Topics Covered
- Conditional statements (if, elif, else)
- Comparison and logical operators
- Loops (for, while)
- Loop control (break, continue, pass)
- List comprehension

### Key Concepts

**1. if-elif-else Statement**
```python
age = int(input("Enter age: "))

if age >= 18:
    print("You are an adult")
elif age >= 13:
    print("You are a teenager")
else:
    print("You are a child")
```

**2. while Loop - Sum of Numbers**
```python
n = int(input("Enter n: "))
sum = 0
i = 1

while i <= n:
    sum += i
    i += 1

print(f"Sum of first {n} numbers: {sum}")
```

**3. for Loop - Factorial Calculation**
```python
n = int(input("Enter a number: "))
factorial = 1

for i in range(1, n + 1):
    factorial *= i

print(f"Factorial of {n} = {factorial}")
```

**4. Prime Number Checker**
```python
num = int(input("Enter a number: "))
is_prime = True

if num <= 1:
    is_prime = False
else:
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            is_prime = False
            break

print(f"{num} is {'prime' if is_prime else 'not prime'}")
```

**5. Fibonacci Series**
```python
n = int(input("Enter number of terms: "))
fib = []
a, b = 0, 1

for _ in range(n):
    fib.append(a)
    a, b = b, a + b

print(f"Fibonacci series: {fib}")
```

**6. List Comprehension**
```python
# Square numbers
squares = [x**2 for x in range(1, 6)]
print(f"Squares: {squares}")

# Even numbers
evens = [x for x in range(1, 11) if x % 2 == 0]
print(f"Even numbers: {evens}")

# Nested list
matrix = [[i*j for j in range(1, 4)] for i in range(1, 4)]
print("Matrix:", matrix)
```

---

## Unit 3: Data Structures

### Topics Covered
- Lists and list methods
- Tuples
- Dictionaries
- Sets
- Operations on collections

### Key Concepts

**1. Lists - Creation and Operations**
```python
# Create list
numbers = [10, 20, 30, 40, 50]
print(f"Original list: {numbers}")

# Add elements
numbers.append(60)
numbers.insert(2, 25)
print(f"After insertion: {numbers}")

# Remove elements
numbers.remove(25)
numbers.pop()
print(f"After removal: {numbers}")

# Find and sort
print(f"Length: {len(numbers)}")
print(f"Index of 30: {numbers.index(30)}")
numbers.sort()
print(f"Sorted: {numbers}")
```

**2. List - Sum, Max, Min, Average**
```python
marks = [85, 92, 78, 95, 88]

print(f"Marks: {marks}")
print(f"Sum: {sum(marks)}")
print(f"Max: {max(marks)}")
print(f"Min: {min(marks)}")
print(f"Average: {sum(marks) / len(marks):.2f}")
```

**3. Tuples - Immutable Collections**
```python
# Create tuple
colors = ("red", "green", "blue")
coordinates = (10, 20, 30)

print(f"Colors: {colors}")
print(f"First color: {colors[0]}")
print(f"Color count: {len(colors)}")

# Unpacking
r, g, b = colors
print(f"RGB values: {r}, {g}, {b}")
```

**4. Dictionary - Key-Value Pairs**
```python
# Create dictionary
student = {
    "name": "Ravi",
    "roll": 101,
    "gpa": 3.8,
    "subjects": ["Math", "Python", "Database"]
}

print(f"Student: {student}")
print(f"Name: {student['name']}")
print(f"Roll: {student.get('roll')}")

# Update and add
student["city"] = "Delhi"
student["gpa"] = 3.9

# Display all keys and values
print(f"Keys: {student.keys()}")
for key, value in student.items():
    print(f"{key}: {value}")
```

**5. Sets - Unique Elements**
```python
# Create set
fruits1 = {"apple", "banana", "orange"}
fruits2 = {"apple", "mango", "orange"}

print(f"Set 1: {fruits1}")
print(f"Set 2: {fruits2}")

# Set operations
print(f"Union: {fruits1 | fruits2}")
print(f"Intersection: {fruits1 & fruits2}")
print(f"Difference: {fruits1 - fruits2}")

# Add and remove
fruits1.add("grape")
fruits1.remove("banana")
print(f"Updated: {fruits1}")
```

---

## Unit 4: Functions and Modules

### Topics Covered
- Function definition and calling
- Parameters and return values
- Default parameters and keyword arguments
- *args and **kwargs
- Lambda functions
- Built-in modules (math, random)

### Key Concepts

**1. Basic Functions**
```python
def greet(name):
    print(f"Hello, {name}!")

def add(a, b):
    return a + b

greet("Ravi")
result = add(10, 20)
print(f"Sum: {result}")
```

**2. Function with Default Parameters**
```python
def power(base, exp=2):
    return base ** exp

print(f"2^2 = {power(2)}")
print(f"2^3 = {power(2, 3)}")
print(f"5^2 = {power(5)}")
```

**3. Factorial Using Recursion**
```python
def factorial(n):
    if n <= 1:
        return 1
    return n * factorial(n - 1)

num = int(input("Enter number: "))
print(f"Factorial of {num} = {factorial(num)}")
```

**4. Lambda Functions**
```python
# Square numbers
square = lambda x: x ** 2
print(f"Square of 5: {square(5)}")

# Add two numbers
add = lambda x, y: x + y
print(f"5 + 3 = {add(5, 3)}")

# Using with map
numbers = [1, 2, 3, 4, 5]
squared = list(map(lambda x: x**2, numbers))
print(f"Squared numbers: {squared}")
```

**5. Using math and random Modules**
```python
import math
import random

# Math operations
print(f"Square root of 25: {math.sqrt(25)}")
print(f"3.7 rounded up: {math.ceil(3.7)}")
print(f"3.2 rounded down: {math.floor(3.2)}")
print(f"sin(π/2): {math.sin(math.pi/2)}")

# Random numbers
print(f"Random number (0-1): {random.random()}")
print(f"Random int (1-10): {random.randint(1, 10)}")

random_list = [1, 2, 3, 4, 5]
print(f"Random choice: {random.choice(random_list)}")
```

---

## Unit 5: File Handling

### Topics Covered
- Opening, reading, writing, closing files
- File modes (r, w, a, rb, wb)
- Reading files (read, readline, readlines)
- Writing and appending
- Working with CSV and JSON files

### Key Concepts

**1. Basic File Operations**
```python
# Write to file
with open("data.txt", "w") as file:
    file.write("Hello World!\n")
    file.write("This is a test file.\n")

print("File written successfully!")

# Read from file
with open("data.txt", "r") as file:
    content = file.read()
    print("File content:")
    print(content)

# Read line by line
with open("data.txt", "r") as file:
    lines = file.readlines()
    for i, line in enumerate(lines, 1):
        print(f"Line {i}: {line.strip()}")
```

**2. Append to File**
```python
# Append new content
with open("data.txt", "a") as file:
    file.write("New line appended.\n")

# Display updated content
with open("data.txt", "r") as file:
    print(file.read())
```

**3. Working with CSV Files**
```python
import csv

# Write CSV
with open("students.csv", "w", newline="") as file:
    writer = csv.writer(file)
    writer.writerow(["Roll", "Name", "GPA"])
    writer.writerow([101, "Ravi", 3.8])
    writer.writerow([102, "Priya", 3.9])

# Read CSV
with open("students.csv", "r") as file:
    reader = csv.reader(file)
    for row in reader:
        print(row)
```

**4. Working with JSON Files**
```python
import json

# Write JSON
student = {
    "roll": 101,
    "name": "Ravi",
    "gpa": 3.8,
    "subjects": ["Math", "Python"]
}

with open("student.json", "w") as file:
    json.dump(student, file, indent=4)

# Read JSON
with open("student.json", "r") as file:
    data = json.load(file)
    print(f"Name: {data['name']}")
    print(f"GPA: {data['gpa']}")
```

---

## Unit 6: Django Basics

### Topics Covered
- Django project and app creation
- Models, Views, URLs
- Templates and static files
- Forms and admin panel

### Key Concepts

**1. Django Project Setup**
```bash
# Create virtual environment
python -m venv myenv
myenv\Scripts\activate

# Install Django
pip install django

# Create project and app
django-admin startproject myproject
cd myproject
python manage.py startapp blog
```

**2. Models (models.py)**
```python
from django.db import models

class Post(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    author = models.CharField(max_length=50)
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.title
```

**3. Views (views.py)**
```python
from django.shortcuts import render
from django.http import HttpResponse
from .models import Post

def blog_list(request):
    posts = Post.objects.all()
    return render(request, 'blog/post_list.html', {'posts': posts})

def blog_detail(request, pk):
    post = Post.objects.get(pk=pk)
    return render(request, 'blog/post_detail.html', {'post': post})
```

**4. URLs (urls.py)**
```python
from django.urls import path
from . import views

urlpatterns = [
    path('posts/', views.blog_list, name='post_list'),
    path('posts/<int:pk>/', views.blog_detail, name='post_detail'),
]
```

**5. Templates (HTML)**
```html
<!-- post_list.html -->
<h1>Blog Posts</h1>
{% for post in posts %}
    <div>
        <h2>{{ post.title }}</h2>
        <p>{{ post.content }}</p>
        <small>By {{ post.author }} on {{ post.created_at }}</small>
    </div>
{% endfor %}
```

---

## Practice Questions

### Unit 1 & 2
1. Calculate area and perimeter of circle
2. Check if year is leap year
3. Print multiplication table using loop

### Unit 3
4. Find sum, max, min in a list
5. Merge two lists and remove duplicates
6. Count frequency of elements in list

### Unit 4
7. Calculate power using recursion
8. Filter even numbers using lambda
9. Create a simple calculator function

### Unit 5
10. Read student marks from file and calculate average
11. Write employee records to CSV
12. Read and parse JSON file

### Unit 6
13. Create Django blog app with posts
14. Create student registration form
15. Display data from database in template

---

## Exam Tips

1. **Use meaningful variable names**
2. **Practice list comprehension**
3. **Understand try-except for error handling**
4. **Master dictionary and list operations**
5. **Know built-in functions: len(), range(), enumerate(), zip()**

---

**Last Updated:** December 2024
