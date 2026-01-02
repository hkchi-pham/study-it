# Flutter

## What is Flutter?
Flutter is an **open-source UI software development kit (SDK)** created by **Google**.  
It allows developers to build **natively compiled applications** for **mobile, web, and desktop** from a **single codebase**.

---

### What is Flutter usually used for?
Flutter is commonly used to build:
- Mobile apps (Android & iOS)
- Web applications
- Desktop apps (Windows, macOS, Linux)
- Rapid prototypes & MVPs
- Apps with custom UI and animations

---

### Advantages compared to similar frameworks

| Framework | Key Difference |
|---------|----------------|
| **Flutter** | Uses its own rendering engine → consistent UI |
| React Native | Relies on native UI components |
| Xamarin | Heavier & slower builds |
| Ionic | Web-based, lower performance |

**Flutter Advantages:**
- Single codebase for multiple platforms
- High performance (compiled to native ARM code)
- Pixel-perfect UI with full customization
- Hot Reload for fast development
- Rich widget library

---

### Flutter Installation (Windows)

Download Flutter SDK  
   --> https://flutter.dev/docs/get-started/install/windows

---

### Basic Flutter Command
```flutter doctor```	Check environment setup

```flutter create app_name```	Create a new project

```flutter run```	Run the app

```flutter pub get```	Install dependencies

```flutter clean```	Clear build cache

```flutter build apk```	Build Android APK

---

### Basic Flutter Widget

1. **Text**

- Displays text on the screen.
```dart
Text(
  "Hello Flutter",
  style: TextStyle(fontSize: 20),
)
```
2. **Icon**

- Displays a material design icon.
```dart
Icon(
  Icons.favorite,
  color: Colors.red,
  size: 30,
)
```
3. **Container**

- A box widget used for layout, padding, and styling.
```dart
Container(
  padding: EdgeInsets.all(16),
  color: Colors.blue,
  child: Text("Inside Container"),
)
```
4. **SizedBox**

- Creates fixed space or size.

```SizedBox(height: 20)```

5. **Row**

- Arranges widgets horizontally.
```dart
Row(
  children: [
    Icon(Icons.star),
    Text("Rating"),
  ],
)
```

6. **Column**

- Arranges widgets vertically.
```dart
Column(
  children: [
    Text("Title"),
    Text("Subtitle"),
  ],
)
```

7. **Center**

- Centers its child widget.
```dart
Center(
  child: Text("Centered Text"),
)
```
8. **Scaffold**

- Provides the basic layout structure of an app.
```dart
Scaffold(
  appBar: AppBar(title: Text("Home")),
  body: Center(child: Text("Hello")),
)
```
9. **AppBar**

- Top navigation bar of the app.
```dart
AppBar(
  title: Text("My App"),
)
```
10. **Image**

- Displays an image.

```Image.asset("assets/logo.png")```

11. **ElevatedButton**

- Clickable button widget.
```dart
ElevatedButton(
  onPressed: () {},
  child: Text("Click Me"),
)
```
12. **ListView**

- Scrollable list of widgets.
```dart
ListView(
  children: [
    Text("Item 1"),
    Text("Item 2"),
  ],
)
```
