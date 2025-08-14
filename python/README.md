# Python

## 1. What is Python?
It is a high-level, interpreted, dynamically typed language. It has efficient high-level data structures and a simple but effective approach to object-oriented programming.



## 2. What is it used for?
- Web development
- Data science & AI
- Automation
- Game development

## 3. Python Basics
```python
# input
name  = input("What is your name? ")
age = int(input("What is your age? ")) # input integer type

# output
print("Hello, World!")

# variables
name = "Alice"
age = 20
found = true
gibber = 3 * 'un' + 'ium' # ="unununium"
gibber[0] # ='u'
gibber[1:3] # ="nu"

# list
squares = [1,4,9,16,25]
squares[0] # access tp first element in the list
squares = squares + [36,49,65,81,100] # [1,4,9,16,25,36,49,65,81,100]
squares[7] = 64 # replace
squares.append(121) # add 11 squared at the end of the list
squares.append(12**2) # add 12 squared at the end of the list
len(squares) # length of the array = 12

# set
colors = {"red", "blue", "red"}  # duplicates remove automatically
colors.add("green")
print(colors)  # {'red', 'blue', 'green'}

# dictionary
student = {
    "name": "Alice",
    "age": 20,
    "grades": [85, 92, 78]
}

# stack (LIFO)
stack = []
stack.append("A")   # Push
stack.append("B")
stack.append("C")
print(stack.pop())  # Pop → 'C'
print(stack)        # ['A', 'B']

# queue (FIFO)
queue = deque()
queue.append("A")  # Enqueue
queue.append("B")
queue.append("C")
print(queue.popleft())  # Dequeue → 'A'
print(queue)            # deque(['B', 'C'])

# if-elif-else
score = 78

if score >= 90:
    grade = "A"
elif score >= 75:
    grade = "B"
elif score >= 60:
    grade = "C"
else:
    grade = "F"
print(f"your grade is {grade}")

# for loop
fruits = ["apple", "banana", "cherry"]
for index, fruit in enumerate(fruits, start=1):
    print(f"{index} {fruit.capitalize()}")

# while loop
countdown = 5
while countdown > 0:
    print(f"T-minus {countdown}")
    countdown -= 1
else:
    print("Lift off!")

# calculation
a = 7
b = 2
c = a+b # =9
d = a-b # =5
e = a/b # =3.5
f = a//b # =3
g = a%b # =1
h = a**b # =49


# Function
def factorial(n):
    if n <= 1:
        return 1
    return n * factorial(n - 1)

# error handling
try:
    num = int(input("Enter a number: "))
    result = 10 / num
except ValueError:
    print("❌ That’s not a valid integer.")
except ZeroDivisionError:
    print("❌ Cannot divide by zero.")
else:
    print(f"Result is {result}")
finally:
    print("Operation completed.")
```

## 4. Python vs Java vs Node.js vs C++

