import 'dart:io';
import 'dart:math' as math;

// program to print out my name
void printName() => print("Cayenne Pham");

// print even number between an inter val
void printEvenNumber(int min, int max) {
  print("Even number between $min and $max are ");
  for (int i = min; i <= max; i++) {
    if (i % 2 == 0) {
      stdout.write("$i ");
    }
  }
  print("");
}

// greeting
void greet(String? name) => print("Hello, $name");

// generate random password
void randomPassword() {
  int len = 12;

  const String chars =
      'abcdefghijklmnopqrstuvwxyz'
      'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
      '0123456789'
      '@#%&*!-?';

  math.Random random = math.Random.secure();
  String password = '';

  for (int i = 0; i < len; i++) {
    password += chars[random.nextInt(chars.length)];
  }

  print("Generated password: $password");
}

// find are of a circle
void circleArea(double r) {
  double area = math.pi * r * r;
  print("The area of the circle is ${area.toStringAsFixed(2)} unit squared");
}

// reversed a String - 1
void reverseString1(String s) {
  String rev = s.split('').reversed.join('');
  print(rev);
}

void reverseString2(String s) {
  String rev = '';

  for (int i = s.length-1; i >= 0; i--) {
    rev += s[i];
  }
  print(rev);
}

// calculate power
void power(int n, int m) => print("$n to the power of $m is ${math.pow(n, m)}");

// add
double add(double a, double b) {
  return a + b;
}

// max number
int maxNumber(int a, int b, int c) {
  return math.max(a, math.max(b, c));
}

// check if number is even or not
bool isEven(int a) {
  return (a % 2 == 0) ? true : false;
}

// create an user
void createUser(String? name, int age, {bool isActive = true}) {
  print("Create user success");
  print("Name: $name");
  print("Age: $age");
  print("Active status: $isActive");
}

// area of rectangle
void calculateArea({double l = 1, double w = 1}) {
  double area = l * w;
  print("Area of rectangle is ${area.toStringAsFixed(2)} unit square");
}

void main() {
  printName();

  print("Enter a min number: ");
  int? min = int.parse(stdin.readLineSync()!);
  print("Enter a max number: ");
  int? max = int.parse(stdin.readLineSync()!);
  printEvenNumber(min, max);

  print("Enter a name: ");
  String? name = stdin.readLineSync();
  greet(name);

  randomPassword();

  print("Enter radius : ");
  double? radius = double.parse(stdin.readLineSync()!);
  circleArea(radius);

  print("Enter string: ");
  String revStr = stdin.readLineSync()!;
  reverseString1(revStr);
  reverseString2(revStr);

  print("Enter a number: ");
  int? x = int.parse(stdin.readLineSync()!);
  print("Enter its power: ");
  int? ex = int.parse(stdin.readLineSync()!);
  power(x, ex);

  print("Enter a number: ");
  double? arg1 = double.parse(stdin.readLineSync()!);
  print("Enter a number: ");
  double? arg2 = double.parse(stdin.readLineSync()!);
  print("the sum of $arg1 and $arg2 is ${add(arg1, arg2)}");

  print("Enter a number: ");
  int? a = int.parse(stdin.readLineSync()!);
  print("Enter a number: ");
  int? b = int.parse(stdin.readLineSync()!);
  print("Enter a number: ");
  int? c = int.parse(stdin.readLineSync()!);
  print("the max number between $a $b and $c is ${maxNumber(a, b, c)}");

  print("Enter a number: ");
  int? num = int.parse(stdin.readLineSync()!);
  print("is the number even? ${isEven(num)}");

  print("Enter you name: ");
  String? accName = stdin.readLineSync();
  print("Enter your age: ");
  int? age = int.parse(stdin.readLineSync()!);
  print("Enter active status: ");
  bool? isActive = bool.parse(stdin.readLineSync()!);
  createUser(accName, age, isActive: isActive);

  print("Enter length: ");
  double? l = double.parse(stdin.readLineSync()!);
  print("Enter width: ");
  double? w = double.parse(stdin.readLineSync()!);
  calculateArea(l: l, w: w);
}
