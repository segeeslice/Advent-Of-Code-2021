#!/usr/bin/env python3

'''
Requirements:
pip install pyyaml

My solutions:
Part 1: 3958484
Part 2: 1613181
'''

import yaml
import sys
from collections import Counter

BINARY_DATA_PATH = './Day3Data.yaml'

# == Generic Methods ==

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

def get_most_common_element(lst, default=None):
    occurence = Counter(lst)
    most_common = occurence.most_common()

    if default is not None and len(most_common) > 1:
        first_count = most_common[0][1]
        second_count = most_common[1][1]
        if first_count == second_count: return default

    return most_common[0][0]

def get_least_common_element(lst, default=None):
    occurence = Counter(lst)
    most_common = occurence.most_common()

    if default is not None and len(most_common) > 1:
        last_count = most_common[-1][1]
        second_to_last_count = most_common[-2][1]
        if last_count == second_to_last_count: return default

    return most_common[-1][0]

def convert_binary_to_decimal(binary):
    return int(binary, 2)

# == Challenge-Specific Methods ==

def get_gamma_binary(binary_data):
    collected_bits = get_binary_bits_at_all_positions(binary_data)
    most_common_bits = [get_most_common_element(bits) for bits in collected_bits]
    return ''.join(most_common_bits)

def get_epsilon_binary(binary_data):
    collected_bits = get_binary_bits_at_all_positions(binary_data)
    least_common_bits = [get_least_common_element(bits) for bits in collected_bits]
    return ''.join(least_common_bits)

def get_oxygen_generator_rating_binary(binary_data):
    get_relevant_bit_method = lambda bits, pos: get_most_common_element(bits, default = 1)
    return aggregate_and_filter_by_bit(binary_data, get_relevant_bit_method)

def get_co2_scrubber_rating_binary(binary_data):
    get_relevant_bit_method = lambda bits, pos: get_least_common_element(bits, default = 0)
    return aggregate_and_filter_by_bit(binary_data, get_relevant_bit_method)

def aggregate_and_filter_by_bit(binary_data, get_relevant_bit_method):
    if len(binary_data) == 0:
        return []

    # Assume all binary data lengths are the same
    size = len(binary_data[0])

    binary_data_filtered = binary_data.copy()
    for i in range(0, size):
        if len(binary_data_filtered) == 1: break

        bits = get_binary_bits_at_position(binary_data_filtered, i)
        relevant_bit = get_relevant_bit_method(bits, i)

        binary_data_filtered = [b for b in binary_data_filtered if b[i] == str(relevant_bit)]

    return ''.join(binary_data_filtered[0])

# == Main ==

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

    oxygen_generator_rating_binary = get_oxygen_generator_rating_binary(binary_data)
    co2_scrubber_rating_binary = get_co2_scrubber_rating_binary(binary_data)

    oxygen_generator_rating = convert_binary_to_decimal(oxygen_generator_rating_binary)
    co2_scrubber_rating = convert_binary_to_decimal(co2_scrubber_rating_binary)
    life_support_rating = oxygen_generator_rating * co2_scrubber_rating

    print("\nPart 2:")
    print("Oxygen Generator Rating: " + str(oxygen_generator_rating))
    print("CO2 Scrubber Rating: " + str(co2_scrubber_rating))
    print("Life Support Rating: " + str(life_support_rating))

if __name__ == '__main__':
    main()
