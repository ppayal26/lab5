#!/usr/bin/env python3
# Author ID: ppayal1

def read_file_string(file_name):
    try:
        with open(file_name, 'r') as f:
            return f.read()
    except FileNotFoundError:
        return "error: could not read file"

def read_file_list(file_name):
    try:
        with open(file_name, 'r') as f:
            return [line.strip() for line in f.readlines()]
    except FileNotFoundError:
        return "error: could not read file"

if __name__ == '__main__':
    file_name = 'data.txt'
    print(read_file_string(file_name))
    print(read_file_list(file_name))
