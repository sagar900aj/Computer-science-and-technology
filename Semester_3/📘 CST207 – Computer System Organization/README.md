# 📘 CST207 – Computer System Organization

**Exam-Ready Study Notes**

---

## Unit 1: Computer Architecture Basics

### Topics Covered
- Von Neumann Architecture
- Computer organization components
- CPU, Memory, ALU, Control Unit

### Key Concepts

**1. Von Neumann Architecture**

चार मुख्य components:
- **Input Unit**: Data और instructions लेता है
- **Memory Unit**: Data और instructions store करता है
- **Control Unit**: Program का execution control करता है
- **Arithmetic Logic Unit (ALU)**: Calculations करता है
- **Output Unit**: Results दिखाता है

**2. CPU Components**

- **Registers**: Very fast memory (accumulator, program counter, instruction register)
- **Control Unit**: Instructions को decode करके execute करता है
- **ALU**: Arithmetic और logical operations करता है

**3. Memory Hierarchy**

```
Fastest and Most Expensive:
    - Registers (few bytes)
    - Cache L1 (KB)
    - Cache L2-L3 (MB)
    - RAM (GB)
    - Hard Disk (TB)
Slowest and Cheapest
```

---

## Unit 2: Control Unit और Micro-programming

### Topics Covered
- Instruction execution cycle (Fetch-Decode-Execute)
- Micro-instructions
- Control signals

### Key Concepts

**1. Fetch-Decode-Execute Cycle**

```
1. Fetch: Program Counter से instruction fetch करो memory से
2. Decode: Instruction को decode करो control unit में
3. Execute: ALU में operation perform करो
4. Store Result: Result को memory या register में store करो
```

**2. Micro-instructions**

Micro-programming एक तरीका है जहां complex instructions को simple micro-steps में divide किया जाता है।

---

## Unit 3: Computer Arithmetic

### Topics Covered
- Integer representation (signed, unsigned)
- Addition, subtraction, multiplication
- Floating-point representation (IEEE 754)

### Key Concepts

**1. Integer Addition and Subtraction**

```
8-bit unsigned: 0 to 255
8-bit signed: -128 to 127 (2's complement)

Example: -5 का 2's complement
5 = 00000101
Invert: 11111010
Add 1: 11111011 (-5)
```

**2. Floating-Point Representation (IEEE 754)**

```
32-bit format: Sign (1) | Exponent (8) | Mantissa (23)

Example: 5.5
5 = 101
0.5 = 0.1 (binary)
5.5 = 101.1 = 1.011 × 2²
```

---

## Unit 4: Pipelining

### Topics Covered
- Pipeline concept
- Pipeline stages
- Pipeline hazards

### Key Concepts

**1. Pipelining Concept**

Pipelining में multiple instructions एक साथ execute होते हैं अलग-अलग stages में।

```
Without Pipeline:
I1: Fetch Decode Execute Store
                    I2: Fetch Decode Execute Store

With Pipeline (4 stages):
I1: Fetch Decode Execute Store
      I2: Fetch Decode Execute Store
          I3: Fetch Decode Execute Store
```

**2. Pipeline Hazards**

- **Data Hazard**: एक instruction दूसरे के data पर depend करता है
- **Control Hazard**: Branch instruction के कारण होता है
- **Structural Hazard**: Resource sharing के कारण होता है

---

## Unit 5: 8086 Microprocessor

### Topics Covered
- 8086 pin diagram
- 8086 register set
- Addressing modes
- Instruction set

### Key Concepts

**1. 8086 Registers**

```
General Purpose:
- AX, BX, CX, DX (16-bit)
- Can be divided: AH, AL, BH, BL, etc.

Segment Registers:
- CS (Code Segment)
- DS (Data Segment)
- SS (Stack Segment)
- ES (Extra Segment)

Pointers:
- IP (Instruction Pointer)
- SP (Stack Pointer)
- BP (Base Pointer)
```

**2. Addressing Modes**

```
1. Immediate: MOV AX, 1000H
2. Direct: MOV AX, [1000H]
3. Register: MOV AX, BX
4. Register Indirect: MOV AX, [BX]
5. Indexed: MOV AX, [BX + 5]
6. Based Indexed: MOV AX, [BP + BX]
```

**3. Basic 8086 Programs**

```assembly
; Program to add two numbers
MOV AX, 0005H    ; Load 5 into AX
MOV BX, 0003H    ; Load 3 into BX
ADD AX, BX       ; Add AX and BX, result in AX
                 ; Result: AX = 0008H

; Program to move data
MOV AX, [0050H]  ; Load from memory address 0050H
MOV [0060H], AX  ; Store to memory address 0060H

; Program with loop
MOV CX, 0005H    ; Counter = 5
LOOP_START: ADD AX, 0001H
LOOP LOOP_START  ; Loop 5 times
```

---

## Unit 6: Memory Organization

### Topics Covered
- Cache memory (types, levels)
- Virtual memory
- Memory management

### Key Concepts

**1. Cache Memory**

```
L1 Cache: 32KB (fastest, on processor)
L2 Cache: 256KB (fast, on processor)
L3 Cache: 8MB (slower, shared)
RAM: GB (much slower)
```

**2. Virtual Memory**

Virtual memory logical memory को physical memory से larger size देता है disk का उपयोग करके।

```
Advantages:
- Larger addressable memory
- Better memory utilization
- Process isolation

Disadvantages:
- Slower access time
- Overhead of page replacement
```

**3. Memory Mapping**

```
Logical Address → Paging/Segmentation → Physical Address

Page Size: 4KB (common)
Virtual Address Space: 2^32 (32-bit system)
```

---

## Unit 7: I/O Organization

### Topics Covered
- I/O data transfer
- Interrupt-driven I/O
- DMA (Direct Memory Access)

### Key Concepts

**1. I/O Data Transfer Methods**

```
1. Programmed I/O: CPU actively involved
2. Interrupt-driven I/O: Device interrupts CPU
3. DMA: Device transfers data directly to memory
```

---

## Practice Questions

1. 8086 में 5 + 3 add करने के लिए assembly program लिखो
2. Von Neumann Architecture के components समझाओ
3. Pipelining के फायदे और नुकसान बताओ
4. Cache memory क्या है? L1, L2, L3 में अंतर
5. Virtual memory कैसे काम करती है?
6. Interrupt handling की प्रक्रिया समझाओ
7. Different addressing modes के साथ 8086 program लिखो
8. Memory hierarchy को describe करो
9. Pipeline hazards के प्रकार बताओ
10. 8086 register set के बारे में विस्तार से बताओ

---

**Last Updated:** December 2024
