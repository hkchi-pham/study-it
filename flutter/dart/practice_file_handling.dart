import 'dart:io';

void main() {
  // add your name to 'hello.txt' file
  File file = File('hello.txt');

  stdout.write("Enter your name: ");
  file.writeAsStringSync(stdin.readLineSync()!);
  

  // add friends name
  stdout.write("Enter friend name: ");
  file.writeAsStringSync("\n${stdin.readLineSync()!}", mode: FileMode.append);

  // get the current working directory
  print("current working directory : ${file.absolute.path}");

  // copy 'hello.txt' to 'hellocopy.txt'
  File newFile = File('hellocopy.txt');

  file.copySync(newFile.path);
  print("File copy successfully");

  // create 100 file using loop
  for (int i = 1; i <= 100; i++) {
    File file = File('file_$i.txt');
    file.writeAsStringSync('This is file number $i');
  }

  print("100 files created successfully");

  // delete 'hellocopy.txt'
  newFile.deleteSync();
  print("File deleted successfully");

  // create csv to store + view student's name, age, address
  File studentFile = File('students.csv');

  List<List<String>> students = [
    ['Name', 'Age', 'Address'],
    ['Cayenne', '16', 'str_abc'],
    ['Julianne', '16', 'str_xyz'],
  ];

  String csvData = students.map((row) => row.join(",")).join("\n");
  studentFile.writeAsStringSync(csvData);
  print("Data written successfully");
}
