#!/usr/bin/env python3

'''
Requirements:
pip install pyyaml

My solutions:
Part 1: 3958484
Part 2: ?
'''

import yaml
import sys
from collections import Counter

BINARY_DATA_PATH = './Day3Data.yaml'

def load_yaml_data(data_path):
    with open(data_path, 'r') as f:
        return yaml.safe_load(f)

def get_binary_bits_at_position(binary_data, position):
    return [b[position] for b in binary_data]

def get_binary_bits_at_all_positions(binary_data):
    if len(binary_data) == 0:
        return []

    # Assume all binary data lengths are the same
    size = len(binary_data[0])

    return [get_binary_bits_at_position(binary_data, p) for p in range(0, size)]

def get_most_common_element(lst):
    occurence = Counter(lst)
    return occurence.most_common()[0][0]

def get_least_common_element(lst):
    occurence = Counter(lst)
    return occurence.most_common()[-1][0]

def get_gamma_binary(binary_data):
    collected_bits = get_binary_bits_at_all_positions(binary_data)
    most_common_bits = [get_most_common_element(bits) for bits in collected_bits]
    return ''.join(most_common_bits)

def get_epsilon_binary(binary_data):
    collected_bits = get_binary_bits_at_all_positions(binary_data)
    least_common_bits = [get_least_common_element(bits) for bits in collected_bits]
    return ''.join(least_common_bits)

def convert_binary_to_decimal(binary):
    return int(binary, 2)

def main():
    binary_data = load_yaml_data(BINARY_DATA_PATH)

    gamma_binary = get_gamma_binary(binary_data)
    epsilon_binary = get_epsilon_binary(binary_data)

    gamma = convert_binary_to_decimal(gamma_binary)
    epsilon = convert_binary_to_decimal(epsilon_binary)
    power_consumption = epsilon * gamma

    print("Part 1:")
    print("Gamma: " + str(gamma))
    print("Epsilon: " + str(epsilon))
    print("Power Consumption: " + str(power_consumption))

if __name__ == '__main__':
    main()
