Python - Control flow and functions

# Notes
## `print()`
1. `print` *automatically displays text followed by a new line, how can that new line be escaped ?*
  
In Python, you can use the `end` parameter of the `print()` function to specify what character(s) should be printed at the end of the printed string instead of the default newline character (`"\n"`). By default, `print()` ends with `"\n"`, which adds a newline, but you can change it to any character or an empty string to suppress the newline.

Here's how you can use the `end` parameter to print without a newline:

```python
print("Hello, ", end="")
print("world!")
```

In this example, the `end=""` argument in the first `print()` statement ensures that there is no newline character added after "Hello, ", so the output will be "Hello, world!" on the same line.

You can use any character or string you like as the value of the `end` parameter to specify what separates the printed content. For example:

```python
print("This is", end=" custom ")
print("output.", end="\n")  # You can also explicitly add a newline if needed
```

This code will produce the output "This is custom output." with a space between "This is" and "custom," and a newline after "output."

## `.format()` method in python
The `.format()` method is a versatile and powerful way to perform string formatting in Python. It allows you to create strings with placeholders and then replace those placeholders with values. Here's a more detailed explanation of how to use the `.format()` method:

### Basic Usage:
You can use curly braces `{}` as placeholders inside a string. These placeholders are positions where values will be inserted. Then, you use the `.format()` method to replace the placeholders with actual values.

```python
name = "Alice"
age = 30
message = "My name is {} and I am {} years old.".format(name, age)
print(message)
```

In this example, `{}` are placeholders, and `.format(name, age)` inserts the values of `name` and `age` into those positions in the string.

### Positional Arguments:
You can specify the order of insertion by using positional arguments. The numbers inside the curly braces indicate the index of the arguments to use.

```python
message = "My name is {0} and I am {1} years old.".format(name, age)
```

### Named Arguments:
You can also use named arguments, which can make the code more readable, especially when dealing with a large number of placeholders.

```python
message = "My name is {name} and I am {age} years old.".format(name=name, age=age)
```

### Formatting Specifiers:
You can specify how values should be formatted within the placeholders by adding a colon and formatting specifier inside the curly braces.

```python
pi = 3.14159265359
formatted_pi = "The value of pi is {:.2f}".format(pi)
```

In this example, `:.2f` specifies that the floating-point value `pi` should be formatted with two decimal places.

### Reusing Values:
You can reuse the same value multiple times by referring to its index within the `.format()` method.

```python
message = "{0} is my name. I am {1} years old. Yes, {0}.".format(name, age)
```

### Mixing Positional and Named Arguments:
You can mix positional and named arguments.

```python
message = "My name is {0} and I am {age} years old.".format(name, age=age)
```

### Padding and Alignment:
You can control the alignment and width of values within placeholders using formatting specifiers.

```python
number = 42
formatted_number = "Number: {:>5}".format(number)
```

In this example, `:>` specifies right alignment, and `5` specifies a minimum width of 5 characters.

The `.format()` method offers great flexibility for creating and formatting strings in Python. It's widely used in Python 2.7+ and Python 3.x for various string formatting tasks.

## Format specifiers Python supports
Python supports a wide range of format specifiers for different data types when using string formatting. Here's a comprehensive list of commonly used format specifiers:

- **String Formatting**:
  - `%s`: String
  - `%r`: String (repr)
  - `%c`: Character (a single character)
  
- **Integer Formatting**:
  - `%d`: Decimal Integer
  - `%o`: Octal Integer
  - `%x`: Hexadecimal Integer (lowercase)
  - `%X`: Hexadecimal Integer (uppercase)
  - `%b`: Binary Integer

- **Floating-Point Formatting**:
  - `%f`: Floating-Point
  - `%e`: Exponential Notation (lowercase)
  - `%E`: Exponential Notation (uppercase)
  - `%g`: General Format (default precision)
  - `%G`: General Format (default precision, uppercase)
  
- **Width and Precision**:
  - `%n.mf`: Width and Precision (n characters wide, m decimal places)

- **Special Formatting**:
  - `%%`: Literal `%` character

These format specifiers are typically used with string formatting methods like `%` operator (in Python 2), `.format()` method (in Python 2.7+ and Python 3.x), and f-strings (in Python 3.6+).

Here are some examples:

```python
name = "Alice"
age = 30
pi = 3.14159

# String formatting
print("Name: %s" % name)
print("Age: %d" % age)

# Floating-point formatting
print("Pi: %.2f" % pi)
print("Pi in exponential notation: %e" % pi)

# Width and precision
number = 42
print("Padded number: %5d" % number)
print("Formatted number: %0.2f" % pi)

# Special formatting
print("A literal percent sign: %%")
```

In Python 3.6 and later, you can use f-strings, which provide a more concise and readable way to format strings:

```python
name = "Alice"
age = 30
pi = 3.14159

print(f"Name: {name}")
print(f"Age: {age}")
print(f"Pi: {pi:.2f}")
```

These format specifiers give you fine-grained control over how data is displayed when formatting strings in Python.
