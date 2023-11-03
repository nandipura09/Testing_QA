# Fibonacci Calculator

This repository contains a Python script, `Pyhthon_Fibonacci.py`, for calculating the Fibonacci sequence and obtaining a list of Fibonacci numbers within a specified range.

## Usage

### Calculate the Nth Fibonacci Number
To find the Nth Fibonacci number, use the `fibonacci(n)` function. Provide a positive integer `n` as input, and it will return the Nth Fibonacci number. For example:

```python
from fibonacci import fibonacci

n = 10
result = fibonacci(n)
print(f"The {n}th Fibonacci number is: {result}")
```

### Calculate a Range of Fibonacci Numbers
You can also calculate a range of Fibonacci numbers between a starting and ending position using the `fibonacci_array(start, end)` function. It requires two positive integers, `start` and `end`, and provides a list of Fibonacci numbers within that range. For instance:

```python
from fibonacci import fibonacci_array

start = 5
end = 15
result = fibonacci_array(start, end)
print(f"Fibonacci numbers from {start} to {end}: {result}")
```

### Command Line Usage
The script can be executed from the command line, with the `start` and `end` values as arguments. For example:

```bash
python Pyhthon_Fibonacci.py 5 15
```

## Error Handling
The script includes error handling to ensure valid input. It raises a `TypeError` if the input is not an integer, a `ValueError` if the input is not a positive integer, or if the `start` value is greater than the `end` value when calculating a range.
