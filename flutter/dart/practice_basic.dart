import 'dart:io';

void main() {
  // print my name
  var name = "Chi";
  print("My name is $name");
  
  // print with single + double quote
  print("Hello I am \"John Doe\"");
  
  print('Hello I\'am "John Doe"');
  
  // declare constant int value
  const num = 7;
  print(num);
  
  // calculating simple interest
  int price = 10000; // original price
  int time = 2; // years
  int rate = 5; // increase by 5% per t
  
  double interest = (price * time * rate)/100;
  
  print(interest.toStringAsFixed(2));
  
  // square a number that user input
  print("Enter a number: ");
  int? number = int.parse(stdin.readLineSync()!);
  int square = number * number;
  print("The square of your number is $square");
  
  // print full name from user input
  print("Enter your first name: ");
  String? firstName = stdin.readLineSync();
  print("ENter your last name: ");
  String? lastName = stdin.readLineSync();
  print("Your full name is $firstName $lastName");
  
  // find the quotient and remainder
  int num1 = 10;
  int num2 = 4;
  
  int quotient = num1 ~/ num2;
  int remainder = num1 % num2;
  
  print("Quotient is $quotient, remainder is $remainder");
  
  // swap two numbers
  int numA = 10;
  int numB = 3;
  print("numA before swapping: $numA");
  print("numB before swapping: $numB");
  
  int b = numA;
  numA = numB;
  numB = b;
  print("numA after swapping: $numA");
  print("numB after swapping: $numB");
  
  // remove all whitespaces from String
  String A = "  Forever  ";
  String B = "  cup";
  String C = "hello world";
  print("String a: ${A.trim()}");
  print("String b: ${B.trimLeft()}");
  print("String a: ${C.trim()}");
  
  // convert String to int
  String s = "1";
  print("Type of s is ${s.runtimeType}");   
  int n = int.parse(s);
  print("Value of n is $n");
  print("Type of n is ${n.runtimeType}");

  
  // calculate split amount of bill
  print("Enter the total bill amount: ");
  int? totalBill = int.parse(stdin.readLineSync()!);
  print("Enter total amount of people: ");
  int? people = int.parse(stdin.readLineSync()!);
  
  double splitBill = totalBill / people;
  print("The split bill amount for each person is $splitBill");
  
  //calculate time taken to reach office in minutes
  int d = 25;
  int v = 40;
  
  double t = d / v; // hour
  t = t * 60;
  
  print("The time taken to reach the office is ${t.toStringAsFixed(1)} minutes");
}
