import 'dart:io';
import 'dart:math' as math;

void main() {
  // create a list of given name
  print("How many name do you wanna input? ");
  int? n = int.parse(stdin.readLineSync()!);

  List<String> listName = [];
  for (int i = 0; i < n; i++) {
    stdout.write("Enter name: ");
    String name = stdin.readLineSync()!;
    listName.add(name);
  }

  listName.forEach((n) => print(n));

  // create a set of fruits
  print("How many fruit do you wanna input? ");
  int? num = int.parse(stdin.readLineSync()!);

  Set<String> setFruit = {};
  for (int i = 0; i < n; i++) {
    stdout.write("Enter fruit: ");
    String fruit = stdin.readLineSync()!;
    setFruit.add(fruit);
  }

  for (String f in setFruit) {
    print(f);
  }

  // calculate total expenses
  List<double> expenses = [];
  double total = 0;

  print("Enter expenses with no unit (type 0 to stop): ");

  while (true) {
    double value = double.parse(stdin.readLineSync()!);
    if (value == 0) break;

    expenses.add(value);
    total += value;
  }

  print("Total expenses: $total");

  // add days
  List<String> days = [];

  days.addAll([
    "Monday",
    "Tuesday",
    "Wednesday",
    "Thursday",
    "Friday",
    "Saturday",
    "Sunday",
  ]);

  for (var day in days) {
    print(day);
  }

  // find friends name start with A
  List<String> friends = [
    "Alex",
    "Brian",
    "Anna",
    "Chris",
    "Amanda",
    "David",
    "Aaron",
  ];

  var result = friends.where((name) => name.toLowerCase().startsWith('a'));

  print("Friends that name start with 'a' are ${result.toList()}");

  // store personal info
  Map<String, dynamic> person = {
    "name": "Cayenne",
    "address": "Hanoi",
    "age": 16,
    "country": "Vietnam",
  };

  person["country"] = "England";

  person.forEach((key, value) {
    print("$key : $value");
  });

  // find contact number of person with key = 4
  Map<String, String> contacts = {
    "Cayenne": "123456",
    "Olivia": "5678",
    "Julianne": "99991",
    "Alex": "1111",
  };

  var keysLength4 = contacts.values.where((value) => value.length == 4);

  print("Phone keys with length 4 are ${keysLength4.toList()}");

  // simple to-do list
  List<String> toDos = [];

  while (true) {
    print("\n1. Add Task");
    print("2. Remove Task");
    print("3. View Tasks");
    print("4. Exit");
    stdout.write("Choose option: ");

    int choice = int.parse(stdin.readLineSync()!);

    if (choice == 1) {
      print("Enter task: ");
      toDos.add(stdin.readLineSync()!);
    } else if (choice == 2) {
      stdout.write("Enter task index: ");
      int index = int.parse(stdin.readLineSync()!);
      if (index > 0 && index <= toDos.length) {
        toDos.removeAt(index - 1);
      }
    } else if (choice == 3) {
      for (int i = 0; i < toDos.length; i++) {
        print("${i + 1}: ${toDos[i]}");
      }
    } else if (choice == 4) {
      break;
    } else {
      print("Please enter a valid number!!");
    }
  }
}
