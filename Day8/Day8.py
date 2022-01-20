#!/usr/bin/env python3

'''
Requirements:
~none~

My solutions:
Part 1: 409
Part 2: ?
'''
import pprint
import copy
pp = pprint.PrettyPrinter(indent = 2)

DIGIT_DATA_PATH = './Day8Data.txt'

# == General-use ==

def read_file_text(data_path):
    with open(data_path, 'r') as f:
        return f.read()

def first(iterator, condition, default=None):
    return next((x for x in iterator if condition(x)), default)

def reverse_dict(dct):
    return {v: k for k, v in dct.items()}

def count(iterator, condition):
    count_result = 0
    for x in iterator:
        if is_iterable(x)
            count_result += count(x, condition)
        elif condition(x):
            count_result += 1

    return count_result

def is_iterable(x):
    return hasattr(x, '__iter__')

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

def get_number_to_digit_key(example_digits):
    key = {}
    key[1] = first(example_digits, lambda x: len(x) == 2)
    key[4] = first(example_digits, lambda x: len(x) == 4)
    key[7] = first(example_digits, lambda x: len(x) == 3)
    key[8] = first(example_digits, lambda x: len(x) == 7)

    return key

def get_digit_to_number_key(example_digits):
    return reverse_dict(get_number_to_digit_key(example_digits))

def parse_digit(digit, digit_to_number_key):
    for key in digit_to_number_key:
        if len(key) == len(digit) and all(digit_letter in key for digit_letter in digit):
            return digit_to_number_key[key]

    return None

def parse_digits(digits, digit_to_number_key):
    return [parse_digit(d, digit_to_number_key) for d in digits]

def count_parsed_digits(parsed_digits):
    return {x: count(parsed_digits, lambda y: y == x) for x in range(0, 9+1)}

# == Main ==

def main ():
    digit_data = import_digit_data(DIGIT_DATA_PATH)
    all_data = []
    for digit_line in digit_data:
        digit_to_number_key = get_digit_to_number_key(digit_line['example_digits'])
        parsed_digits = parse_digits(digit_line['display_digits'], digit_to_number_key)
        all_data.append(parsed_digits)

    counted = count_parsed_digits(all_data)

    print("Number of 1's, 4's, 7's, or 8's: ")
    print(sum(counted[k] for k in counted))

if __name__ == '__main__':
    main()
