#!/usr/bin/env python3
# Author ID: ppayal1

def add(number1, number2):
    try:
        return int(number1) + int(number2)
    except ValueError:
        return 'error: could not add numbers'

def read_file(filename):
    try:
        with open(filename, 'r') as f:
            return f.readlines()
    except FileNotFoundError:
        return 'error: could not read file'

if __name__ == '__main__':
    print(add(10, 5))                    # should work
    print(add('10', 5))                  # should work
    print(add('abc', 5))                 # should trigger exception
    print(read_file('seneca2.txt'))      # should work if file exists
    print(read_file('file10000.txt'))    # should trigger exception
