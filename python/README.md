# Python

## 1. What is Python?
It is a igh-level, interpreted, dynamically typed language. It has efficient high-level data structures and a simple but effective approach to object-oriented programming.



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



# if-elif-else
if (condition):
  [code]
elif (condition):
  [code]
else:
  [code]

# for loop
for i in range(6): # 0-5
  print(i)

# while loop
i = 0
while i<6:
  print(i)
  i+=1

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
def greet(user):
    return f"Hello, {user}!"

print(greet(name))
