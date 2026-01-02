# Dart

## What is Dart?
Dart is a **programming language** developed by **Google**.  
It is designed for building **fast, scalable, and modern applications**, and it is the **primary language used by Flutter**.

---

### What is Dart usually used for?
Dart is commonly used for:
- Flutter mobile applications
- Web applications
- Backend services (e.g. Dart Frog, Shelf)
- Command-line (CLI) tools

---

### Advantages Compared to Similar Languages

| Language | Difference |
|--------|------------|
| **Dart** | Optimized for UI & async programming |
| JavaScript | Weak typing |
| Java | More verbose syntax |
| Kotlin | Mainly Android-focused |

**Key Advantages of Dart:**
- Ahead-of-Time (AOT) compilation → fast performance
- Strong typing with **null safety**
- Built-in async & await support
- Simple and readable syntax
- Hot Reload support when used with Flutter

---

### Dart Installation (Windows)

- Dart is **automatically installed when you install Flutter**.

Optional standalone installation using Chocolatey:
```bash
choco install dart-sdk
```

---

### Basic Dart Command

```dart run```	Run a Dart program

```dart format```	Format Dart code

```dart analyze```	Analyze code for errors

```dart pub get```	Install dependencies

---

### Basic Dart Features (with Examples)
1. **Variables & Data Types**
```dart
int age = 16;
double score = 9.5;
String name = "Dart";
bool isStudent = true;
```
2. **Data Structure**
```dart
List<String> names = ["Cayenne", "Olivia", "Julianne"]; // List

Set<String> weekday = {"Sun", "Mon", "Tue", "Wed", "Thu", "Fri", "Sat"}; // Set

Map<String, String> myDetails = {
   'name': 'Chi Pham',
   'address': 'Vietnam',
   'fathername': 'Pham'
}; // Map

```
3. **Functions**
```dart
int add(int a, int b) {
  return a + b;
}
```
4. **Classes & Objects**
```dart
class User {
  String name;
  int age;

  User(this.name, this.age);
}

void main() {
  User user = User("Cayenne", 16);
}
```
5. **Conditional Statements**
```dart
if (age >= 18) {
  print("Adult");
} else {
  print("Minor");
}
```
6. **Loops**
```dart
// For lopp
for (int i = 0; i < 5; i++) {
  print(i);
}

// For Each Loop
list.forEach((n) => print(n);

// For In Loop
for(names in Family){
  print(names);
}

// While Loop
int i = 1;
  while (i <= 10) {
    print(i);
    i++;
  }

// Do While Loop
int i = 1;
  do {
    print(i);
    i++;
  } while (i <= 10);
```

8. **Async & Await**
```dart
Future<void> loadData() async {
  await Future.delayed(Duration(seconds: 2));
  print("Data loaded");
}
```
9. **Null Safety**
```dart
String? optionalName;
optionalName = "Flutter";
```
