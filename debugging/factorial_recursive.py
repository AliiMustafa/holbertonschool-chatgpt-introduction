#!/usr/bin/python3
import sys

def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)

if len(sys.argv) != 2:
    print("Usage: python script.py <number>")
    sys.exit(1)

try:
    num = int(sys.argv[1])
    if num < 0:
        print("Factorial is not defined for negative numbers")
        sys.exit(1)
    f = factorial(num)
    print(f)
except ValueError:
    print("Please provide a valid integer")
    sys.exit(1)

