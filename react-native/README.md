
# ** React Native **


## 1. What is React Native?
It is an open-source framework by Meta, uses JavaScript/TypeScript to build cross-platform mobile apps.

## 2. What is it used for?
- Build mobile apps for iOS & Android from one codebase.
- Build full-stack website on one codebase.


## 3. Basic Commands
```bash
npx react-native init MyApp
cd MyApp
npx react-native start
npx react-native run-android
npx react-native run-ios
```
## 4. Basic Code Examples
```javascript
// Output
console.log("Hello, React Native!");

// Input Example: reading from TextInput
import React, { useState } from 'react';
import { View, TextInput, Button } from 'react-native';

export default function App() {
  const [name, setName] = useState('');
  return (
    <View>
      <TextInput
        placeholder="Enter name"
        onChangeText={(text) => setName(text)}
      />
      <Button title="Say Hi" onPress={() => console.log(`Hi, ${name}`)} />
    </View>
  );
}

// String
let greeting = "Hello";
// Number
let age = 18;
// Boolean
let isStudent = true;
// Object
let person = { name: "Chi", age: 18 };

// Array
let numbers = [1, 2, 3];
numbers.push(4);
// Object
let car = { brand: "Toyota", year: 2020 };
car.color = "blue";

// Function
function add(a, b) {
  return a + b;
}
console.log(add(5, 3));
// Arrow function
const greet = (name) => `Hello, ${name}!`;
console.log(greet("Chi"));

// React-native example
import React from 'react';
import { Text, View, Button } from 'react-native';

export default function App() {
  const sayHello = () => console.log("Hello from function!");
  return (
    <View style={{ marginTop: 50 }}>
      <Text>Welcome to React Native</Text>
      <Button title="Click Me" onPress={sayHello} />
    </View>
  );
}
```
## React Native vs Flutter

- **User Accessibility:**
  - **React**: Great for developers familiar with JavaScript and React; uses native UI components; huge community support.
  - **Flutter**: Uses Dart (less common) but provides highly consistent UI; good for newcomers to UI design.

- Scalability:
  - **React**: Scales well if you manage architecture with tools like Redux or MobX; relies on a JS bridge for native calls.
  - **Flutter**: Strong for large apps; compiles to native ARM code; widget-based architecture supports maintainability.

- **Expandability**:
  - **React**: Very large npm ecosystem; can integrate native modules; some deep platform APIs may require custom native code.
  - **Flutter**: Ecosystem is growing; can use platform channels to access native APIs; fewer third-party libs than RN.

- **Performance**:
  - **React**: Near-native performance; JS bridge can cause slight lag with heavy animations; can be optimized.
  - **Flutter**: Excellent; compiles to native ARM; better suited for graphics-heavy or animation-rich apps.

- **Ease of Use**:
  - **React**: Easy if you already know JS/React; supports hot reload; excellent docs and community.
  - **Flutter**: Steeper learning curve due to Dart and widget system; great tooling; hot reload available.

- **Ease of Learning**:
  - **React**: Very quick to pick up for web devs; minimal setup; follows familiar React patterns.
  - **Flutter**: Medium difficulty; need to learn Dart plus Flutter’s widget concepts.

- **Library & Ecosystem**:
  - **React**: Mature npm library base with many integrations; long history and stability.
  - **Flutter**: Smaller than RN but growing rapidly; official packages are high-quality and well-maintained.

