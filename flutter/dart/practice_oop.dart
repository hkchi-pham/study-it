import "dart:io";

// laptop class with properties
class Laptop {
  int id;
  String name;
  int ram;

  Laptop(this.id, this.name, this.ram);

  void printDetails() {
    print("Laptop ID: $id, Name: $name, RAM: ${ram}GB");
  }
}

// house class with constructor
class House {
  int id;
  String name;
  double price;

  House(this.id, this.name, this.price);

  void printDetails() {
    print("House ID: $id, Name: $name, Price: $price");
  }
}

// Gender enum
enum Gender { male, female, others }

// animal and cat(inheritance) classes
class Animal {
  int id;
  String name;
  String color;

  Animal(this.id, this.name, this.color);

  void printDetails() {
    print("Animal ID: $id, Name: $name, Color: $color");
  }
}

class Cat extends Animal {
  String sound;

  Cat(int id, String name, String color, this.sound) : super(id, name, color);

  @override
  void printDetails() {
    print("Cat ID: $id, Name: $name, Color: $color, Sound: $sound");
  }
}

// camera class with private properties and getters/setters
class Camera {
  int _id;
  String _brand;
  String _color;
  double _price;

  Camera(this._id, this._brand, this._color, this._price);

  int get id => _id;
  String get brand => _brand;
  String get color => _color;
  double get price => _price;

  set id(int value) => _id = value;
  set brand(String value) => _brand = value;
  set color(String value) => _color = value;
  set price(double value) => _price = value;

  void printDetails() {
    print("Camera ID: $_id, Brand: $_brand, Color: $_color, Price: $_price");
  }
}

// bottle interface and cokebottle implementation
abstract class Bottle {
  void open();

  factory Bottle.createCoke() {
    return CokeBottle();
  }
}

class CokeBottle implements Bottle {
  @override
  void open() {
    print("Coke bottle is opened");
  }
}

//Quiz application
class Question {
  String question;
  List<String> options;
  int correctAnswer;

  Question(this.question, this.options, this.correctAnswer);
}

class Quiz {
  List<Question> questions = [];
  int score = 0;

  Quiz() {
    _loadQuestions();
  }

  void _loadQuestions() {
    questions.add(
      Question("What is the capital of France?", [
        "London",
        "Paris",
        "Berlin",
        "Madrid",
      ], 1),
    );
    questions.add(Question("What is 2 + 2?", ["3", "4", "5", "6"], 1));
    questions.add(
      Question("Which programming language is this?", [
        "Java",
        "Python",
        "Dart",
        "C++",
      ], 2),
    );
  }

  void play() {
    print("Welcome to play the Quiz");

    for (int i = 0; i < questions.length; i++) {
      print("Question ${i + 1}: ${questions[i].question}");
      for (int j = 0; j < questions[i].options.length; j++) {
        print("${j + 1}. ${questions[i].options[j]}");
      }

      print("Your answer (1-${questions[i].options.length}): ");

      int userAnswer = questions[i].correctAnswer;
      int displayAnswer = userAnswer + 1;
      print('$displayAnswer');

      if (userAnswer == questions[i].correctAnswer) {
        print("Correct\n");
        score++;
      } else {
        print(
          "Wrong! The correct answer was: ${questions[i].options[questions[i].correctAnswer]}\n",
        );
      }
    }
    _viewScore();
  }

  void _viewScore() {
    print("Thank you for completing the quiz!");

    print("Your Score: $score/${questions.length}");
    double percentage = (score / questions.length) * 100;
    print("Percentage: ${percentage.toStringAsFixed(1)}%");

    if (percentage >= 80) {
      print("Grade: Excellent!");
    } else if (percentage >= 60) {
      print("Grade: Good!");
    } else {
      print("Grade: Keep practicing!");
    }
  }
}

void main() {
  print("1. Laptop Class");
  Laptop laptop1 = Laptop(1, "Dell XPS", 16);
  Laptop laptop2 = Laptop(2, "MacBook Pro", 32);
  Laptop laptop3 = Laptop(3, "HP Pavilion", 8);

  laptop1.printDetails();
  laptop2.printDetails();
  laptop3.printDetails();

  print("2. House Class");
  List<House> houses = [];
  houses.add(House(1, "Villa Sunrise", 450000.00));
  houses.add(House(2, "Ocean View Apartment", 280000.00));
  houses.add(House(3, "Downtown Condo", 350000.00));

  for (var house in houses) {
    house.printDetails();
  }

  print("3. Gender Enum");
  print("Gender values:");
  for (var gender in Gender.values) {
    print("- ${gender.name}");
  }

  print("4. Animal and Cat(inheritance) class");
  Cat cat = Cat(1, "Whiskers", "Orange", "Meow");
  cat.printDetails();

  print("5. Camera Class(Private Properties)");
  Camera camera1 = Camera(1, "Canon", "Black", 1200.00);
  Camera camera2 = Camera(2, "Nikon", "Silver", 1500.00);
  Camera camera3 = Camera(3, "Sony", "Black", 1800.00);

  camera1.printDetails();
  camera2.printDetails();
  camera3.printDetails();

  // Using setter
  camera1.price = 1100.00;
  print("Updated camera1 price: ${camera1.price}");

  print("6. Bottle Interface & Factory");
  Bottle bottle = Bottle.createCoke();
  bottle.open();

  print("7. Quiz Application");
  Quiz quiz = Quiz();
  quiz.play();
}
