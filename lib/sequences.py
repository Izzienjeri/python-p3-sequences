#!/usr/bin/env python3

def print_fibonacci(length):
    if length == 0:
        print([])
        return

    fib_sequence = [0, 1]  # Initialize the sequence with the first two Fibonacci numbers

    while len(fib_sequence) < length:
        next_fib = fib_sequence[-1] + fib_sequence[-2]
        fib_sequence.append(next_fib)

    print(fib_sequence[0:length])

print_fibonacci(9)
