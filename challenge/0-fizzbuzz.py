#!/usr/bin/python3
"""
FizzBuzz solution
"""
import sys


def fizzbuzz(n):
    """
    FizzBuzz function prints numbers from 1 to n separated by a space.
    """
    if n < 1:
        return

    tmp_result = []
    for i in range(1, n + 1):
        if i % 15 == 0:
            tmp_result.append("FizzBuzz")
        elif i % 3 == 0:
            tmp_result.append("Fizz")
        elif i % 5 == 0:
            tmp_result.append("Buzz")
        else:
            tmp_result.append(str(i))
    print(" ".join(tmp_result))


if __name__ == "__main__":
    if len(sys.argv) <= 1:
        print("Missing number")
        print("Usage: ./0-fizzbuzz.py <number>")
        print("Example: ./0-fizzbuzz.py 15")
    else:
        fizzbuzz(int(sys.argv[1]))
