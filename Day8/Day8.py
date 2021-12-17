#!/usr/bin/env python3

'''
Requirements:
~none~

My solutions:
Part 1: ?
Part 2: ?
'''
import pprint
import copy
pp = pprint.PrettyPrinter(indent = 2)

DIGIT_DATA_PATH = './Day8ExampleData.txt'

# == General-use ==

def read_file_text(data_path):
    with open(data_path, 'r') as f:
        return f.read()

# == Program-specific ==

def import_digit_data(data_path):
    raw_text = read_file_text(data_path)
    digit_data = []

    for line in raw_text.split('\n'):
        if not line.strip(): continue
        digit_data.append({
            'example_digits': [x for x in line.split('|')[0].split(' ') if x],
            'display_digits': [x for x in line.split('|')[1].split(' ') if x],
        })

    return digit_data

def parse_example_digits(example_digits):
    parsed = {x: '' for x in range(0, 9+1)}

    return parsed

# == Main ==

def main ():
    digit_data = import_digit_data(DIGIT_DATA_PATH)
    # parsed = parse_digits(digit_data)
    # print(parsed)

if __name__ == '__main__':
    main()
