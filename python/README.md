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

- Popularity & Community
   - Python: Over 2.5M repositories on GitHub, ~3M questions tagged on Stack Overflow. Dominant in AI/ML, data science, education, automation, scripting.
   - Java: Standard in enterprise backends, Android apps, and large-scale systems.
   - Node.js: Core language of the web; indispensable for frontend and often used for backend APIs, backed by npm with ~2.6M packages (largest registry in the world).
   - C++: Consistently in top 5; ~1.2M GitHub repos, ~900k Stack Overflow questions. Key in game development, embedded systems, and high-performance computing.
- Scalability
   - Python:
     - Highly modular, with thousands of PyPI packages for quick feature addition.
     - Can integrate with C/C++ for performance-critical features (Cython, ctypes).
     - Works across domains — easy to pivot from web to AI, automation, or data processing.
   - Java:
     - Enterprise-grade modularity (Java Modules, OSGi) for large-scale extensions.
     - JVM allows mixing in Kotlin, Scala, or Groovy without rewriting everything.
   - Node.js:
     - npm registry enables rapid extension with millions of packages.
     - Strong compatibility with modern APIs, frontend frameworks, and microservices.
   - C++:
     - Extremely flexible at the system level — can be embedded almost anywhere.
     - Strong interoperability with other languages via native APIs.
- Library & Ecosystem support
   - Python:
     - Web: Django, Flask, FastAPI.
     - AI/ML: TensorFlow, PyTorch, Scikit-learn.
     - Data: NumPy, Pandas, Matplotlib.
     - Automation: Selenium, BeautifulSoup, PyAutoGUI.
   - Java:
     - Backend: Spring, Spring Boot, Micronaut.
     - Android: Jetpack, AndroidX.
     - Big Data: Apache Hadoop, Apache Spark (Java APIs).
   - Node.js:
     - Web: Express, Nest.js, Koa.
     - Real-time: Socket.io.
     - Build tools: Webpack, Gulp, Vite.
   - C++:
     - GUI: Qt, wxWidgets.
     - Game engines: Unreal Engine, Cocos2d-x.
     - Scientific: Eigen, Armadillo.
- Ease of Learning & Accessibility
   - Python: Pseudocode-like syntax, indentation-based structure. Minimal boilerplate (e.g., a web server in Flask can be <10 lines).
   - Java: Verbose; requires understanding OOP principles.
   - Node.js: Moderate learning curve; async/await simplifies callbacks.
   - C++: Complex syntax, pointers, manual memory management.
-  Performance & Scalability
   - I/O-bound tasks (network APIs, file streams):
     - Node.js > Java ≈ Python (with async frameworks) > C++ (unless manually optimized).
   - CPU-bound tasks (matrix multiplication, image processing):
     - C++ > Java ≈ optimized Node.js (via native addons) > Python (unless using NumPy/Cython).
- Frameworks by Domain


   | Domain      | Python                 | Node.js          | Java           | C++                  |
  | ----------- | ---------------------- | ---------------- | -------------- | -------------------- |
  | Web Backend | Django, Flask, FastAPI | Express, Nest.js | Spring Boot    | Wt (C++ Web Toolkit) |
  | Mobile      | Kivy, BeeWare          | React Native     | Android SDK    | C++ with Qt          |
  | AI/ML       | PyTorch, TensorFlow    | Brain.js         | Deeplearning4j | dlib, Shark          |
  | Games       | Pygame                 | Phaser.js        | jMonkeyEngine  | Unreal, OGRE3D       |


- Limitations
    - Python: Slower raw execution speed; GIL limits true multithreading.
    - Java: Verbose code; slower startup time than Node/Python.
    - Node.js: Weak for CPU-heavy tasks unless offloaded.
    - C++: Steep learning curve; longer development time.

- Why I choose Python for this project:
  - Fast development — ideal for a prototype-to-product approach.
  - Broad ecosystem — strong for AI/ML integration, web APIs, automation.
  - Beginner-to-advanced accessibility — helps to learn onboard quickly.
  - Readable code — better long-term maintainability.

## 5. Django vs Flask vs FastAPI

- Django
   - Best for: Large, structured web apps with relational DBs; e-commerce, social networks, news/media sites.
   - Advantages
     - Full-stack, batteries included → built-in authentication, caching, sessions, ORM.
     - Ease of setup: minimal need for external packages.
     - Database support: Works well with relational DBs (SQLite, MySQL, PostgreSQL).
     - Security: Many protections built-in.
     - Scalability: Can horizontally scale & use async.
     - Community & docs: Very large and active.
   - Disadvantages
     - Heavyweight: May be too much for small/simple apps.
     - Learning curve: More features = more to learn.
     - Performance: Slower than Flask/FastAPI.
- Flask
   - Best for: Small-to-medium apps, MVPs, or projects needing high customization.
   - Advantage
     - Lightweight, flexible: Minimal core; choose your own libraries.
     - Scalable: Modular architecture.
     - Easy to learn: Shallow learning curve for beginners.
     - Extensible: Large ecosystem of extensions.
   - Disadvantage
     - Bring-your-own: No ORM, validation, or security by default — must add yourself.
     - Security: Minimal built-in; must ensure dependencies are safe.
     - Performance: Good, but slower than FastAPI.
- FastAPI
   - Best for: High-performance APIs, real-time systems, data-intensive or ML-driven applications.
   - Advantage
     - High performance: Async-first, faster than Django & Flask.
     - Modern: Type hints, Pydantic validation, auto-generated docs via OpenAPI.
     - Scalable: Lightweight, modular; works well with microservices.
     - Industry standards: OAuth 2.0, OpenAPI, JSON Schema support.
   - Disadvantage
     - Younger: Less mature & smaller community.
     - Fewer packages than Django/Flask.
     - Less built-in functionality — need to add components for full apps.
   





