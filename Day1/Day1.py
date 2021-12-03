#!/usr/bin/env python3

'''
Requirements:
pip install pyyaml

My solutions:
Part 1: 1400 increases
Part 2: 1429 increases
'''

import yaml
import sys

HEIGHT_DATA_PATH = './Day1Data.yaml'

def load_yaml_data(data_path):
    with open(data_path, 'r') as f:
        return yaml.safe_load(f)

def get_increases_and_decreases(height_data):
    # Oops, default is 1000...
    sys.setrecursionlimit(len(height_data) + 100)
    return _get_increases_and_decreases(height_data, 0, 0)

def _get_increases_and_decreases(height_data, increases, decreases):
    if len(height_data) <= 1:
        return (increases, decreases)
    elif height_data[1] > height_data[0]:
        return _get_increases_and_decreases(height_data[1:], increases+1, decreases)
    elif height_data[1] < height_data[0]:
        return _get_increases_and_decreases(height_data[1:], increases, decreases+1)
    else:
        return _get_increases_and_decreases(height_data[1:], increases, decreases)

def aggregate_sliding_height_sum(height_data, num_to_compile = 3):
    result = []
    if (len(height_data) < num_to_compile):
        return result

    for index in range(0, len(height_data) - num_to_compile + 1):
        sliding_sum = sum(height_data[i] for i in range(index, index + num_to_compile))
        result.append(sliding_sum)

    return result

def main():
    height_data = load_yaml_data(HEIGHT_DATA_PATH)

    increases, decreases = get_increases_and_decreases(height_data)
    print("Part 1:")
    print("Increases: " + str(increases))
    print("Decreases: " + str(decreases))

    compiled_height_data = aggregate_sliding_height_sum(height_data)
    compiled_increases, compiled_decreases = get_increases_and_decreases(compiled_height_data)
    print("\nPart 2:")
    print("Increases: " + str(compiled_increases))
    print("Decreases: " + str(compiled_decreases))

if __name__ == '__main__':
    main()
