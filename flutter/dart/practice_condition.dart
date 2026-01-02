import 'dart:io';

void main() {
  // check if number is odd or even
  print("Enter a number: ");
  int? numA = int.parse(stdin.readLineSync()!);
  print("Enter a number: ");
  int? numB = int.parse(stdin.readLineSync()!);

  print("$numA is ${(numA % 2 == 0) ? "even" : "odd"}");
  print("$numB is ${(numB % 2 == 0) ? "even" : "odd"}");

  // check if letter is vowel or consonant
  print("Enter a letter: ");
  String? s = stdin.readLineSync()!;
  s = s.toLowerCase();

  if (s.length == 1 && RegExp(r'^[a-z]$').hasMatch(s)) {
    if ('aeiou'.contains(s)) {
      print("$s is a vowel");
    } else {
      print("$s is a consonant");
    }
  } else {
    print("This is not an alphabetical letter");
  }

  // check if the number is pos, neg, or 0
  print("Enter a number: ");
  int? num = int.parse(stdin.readLineSync()!);

  if (num == 0) {
    print("num is 0");
  }

  print("$num is ${(num > 0) ? "positive" : "negative"}");

  // create a simple calculator
  print("Enter a number: ");
  int? n1 = int.parse(stdin.readLineSync()!);
  print("Enter a number: ");
  int? n2 = int.parse(stdin.readLineSync()!);
  print("What calculation do you want to perform (+,-,x,/) ? ");
  String? calc = stdin.readLineSync();

  switch (calc) {
    case "+":
      print("$n1 + $n2 = ${n1 + n2}");
      break;
    case "-":
      print("$n1 - $n2 = ${n1 - n2}");
      break;
    case "x":
      print("$n1 x $n2 = ${n1 * n2}");
      break;
    case "/":
      print("$n1 / $n2 = ${n1 / n2}");
      break;
  }

}
