# Python Basics Overview

This repository contains a collection of Python code snippets demonstrating fundamental programming concepts. It is designed for beginners to understand basic Python syntax, operations, and constructs.

## Table of Contents

1. [Variables](#variables)
2. [Input](#input)
3. [Type Conversion](#type-conversion)
4. [Arithmetic Operators](#arithmetic-operators)
5. [Comparison Operators](#comparison-operators)
6. [Logical Operators](#logical-operators)
7. [Conditional Statements](#conditional-statements)
8. [Loops](#loops)
9. [Lists](#lists)
10. [For Loops](#for-loops)
11. [Range Function](#range-function)
12. [Tuples](#tuples)

## Variables

Variables in Python are used to store data values. Here are some examples:

```python
# Declaring and Using a Variable
age = 20  # first value of the variable
age = 30  # second value of the variable
print(age)  # prints the second value of the variable

# Declaring variables and assigning a string value
price = 19.95
first_name = "Mosh"
is_online = True
```

## Input

You can use the `input()` function to get user input:

```python
name = input("What is your name? ")
print("Hello " + name)  # string concatenation
```

## Type Conversion

Convert data types using built-in functions:

```python
birth_year = input("Enter your birth year: ")
age = 2024 - int(birth_year)  # convert string to int
```

Functions for conversion:
- `float()`: Converts to floating-point number
- `int()`: Converts to integer
- `bool()`: Converts to boolean
- `str()`: Converts to string

## Arithmetic Operators

Perform basic arithmetic operations:

```python
print(10 + 3)  # addition
print(10 - 3)  # subtraction
print(10 * 3)  # multiplication
print(10 / 3)  # division
print(10 // 3) # integer division
print(10 % 3)  # modulus
print(10 ** 3) # exponentiation
```

## Comparison Operators

Compare values to return boolean results:

```python
x = 3 > 2
print(x)  # prints True
```

## Logical Operators

Build complex conditions:

```python
price = 50
print(price > 25 and price < 75)  # both conditions must be true
print(price < 25 or price > 75)  # at least one condition must be true
print(not(price > 25))  # negates the condition
```

## Conditional Statements

Make decisions in your code:

```python
temperature = 37
if temperature > 30:
    print("It's a hot day")
    print("Drink plenty of water")
elif temperature > 20:
    print("It's a nice day")
else:
    print("It's not a hot day")
print("Okr")
```

## Loops

Repeat a block of code multiple times:

### While Loops

```python
i = 1
while i <= 10:
    print(i)
    i = i + 1
```

### For Loops

```python
numbers = [1, 2, 3, 4, 5]
for item in numbers:
    print

```markdown
(item)  # prints each item in the list
```

## Lists

Store multiple items in a single variable:

```python
names = ["John", "Bob", "Mosh", "Sarah", "Mary"]
print(names)  # prints the entire list
print(names[0])  # prints the first element
names[0] = "Jon"  # update an element
print(names)  # prints the updated list
print(names[0:3])  # slice the list
```

### List Methods

```python
numbers = [1, 2, 3, 4, 5]
numbers.append(6)  # add an element
numbers.insert(0, -1)  # insert an element
numbers.remove(3)  # remove an element
numbers.clear()  # clear all elements
print(1 in numbers)  # check for existence
print(len(numbers))  # length of the list
```

## Range Function

Generate sequences of numbers:

```python
numbers = range(5, 10, 2)
print(list(numbers))  # convert range object to list
for number in range(5):
    print(number)
```

## Tuples

Immutable sequences of values:

```python
numbers = (1, 2, 3)
print(numbers.count(1))  # count occurrences of an element
print(numbers.index(1))  # index of the first occurrence
```

## Contact

For any questions, please contact:

- **Email**: [kamundikevin@gmail.com](mailto:kamundikevin@gmail.com)
- **GitHub**: [KevinGitari](https://github.com/KevinGitari)

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.