# 0x13 JavaScript Objects, Scopes, and Closures

## Overview

This project explores the concepts of objects, scopes, and closures in JavaScript. These are fundamental topics for understanding how JavaScript works, especially in the context of functional and object-oriented programming.

## Topics Covered

- **Objects**: Creating and manipulating objects.
- **Prototypes**: Understanding the prototype chain and inheritance.
- **Scopes**: Variable scope and closures.
- **Closures**: Creating and using closures for data encapsulation.
- **ES6 Classes**: Using modern JavaScript classes for object-oriented programming.
- **Inheritance**: Implementing inheritance using prototypes and ES6 classes.

## Contents

1. **Objects**
    - Creating objects using object literals, constructor functions, and ES6 classes.
    - Adding and accessing properties and methods.

2. **Prototypes**
    - Understanding the prototype chain.
    - Creating objects that inherit from other objects.

3. **Scopes**
    - Understanding global, local, and block scopes.
    - Variable hoisting and the `let`, `const`, and `var` keywords.

4. **Closures**
    - Creating closures and understanding their use cases.
    - Encapsulating data using closures.

5. **ES6 Classes**
    - Defining classes and constructors.
    - Using `extends` for inheritance.
    - Using `super` to call parent class constructors and methods.

## Examples

### Creating and Using Objects

```javascript
let person = {
  name: 'John',
  age: 30,
  greet: function() {
    console.log('Hello, ' + this.name);
  }
};

person.greet(); // Outputs: Hello, John
```
## how to run
clone the repo
```sh
git clone https://github.com/yourusername/0x13-javascript_objects_scopes_closures.git
```

## navigate to the directory and run
```sh
cd 0x13-javascript_objects_scopes_closures
node filename.js
```

