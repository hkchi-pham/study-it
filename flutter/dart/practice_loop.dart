import 'dart:io';

void main() {
  // print your name 100 times

  print("Enter your name: ");
  String? name = stdin.readLineSync();

  for (var i = 1; i <= 100; i++) {
    print(name);
  }

  // print sum of n natural number

  print("Enter a positive number: ");
  int? n = int.parse(stdin.readLineSync()!);

  int sum = 0;
  for (int i = 1; i <= n; i++) {
    sum += i;
  }
  print("the sum of $n number is $sum");

  // generate multiplication table of 5
  int i = 10;

  while (i > 0) {
    int prod = i * 5;
    print("5 * $i = $prod");
    i--;
  }

  // generate multiplication tables of 1-9
  int a = 1;
  while (a <= 9) {
    for (int j = 1; j <= 10; j++) {
      print("$a x $j = ${a * j}");
    }
    a++;
    print("\n");
  }


  // print 1-100 but not 41

  for (int i = 1; i <= 100; i++) {
    if (i != 41) {
      print(i);
    }
  }
}
