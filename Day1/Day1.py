#!/usr/bin/env python3

'''
Requirements:
pip install pyyaml
'''

import yaml
import sys

HEIGHT_DATA_PATH = './Day1Data.yaml'

def load_yaml_data(data_path):
    with open(HEIGHT_DATA_PATH, 'r') as f:
        return yaml.safe_load(f)

def get_increases_and_decreases(height_data):
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

def main():
    height_data = load_yaml_data(HEIGHT_DATA_PATH)

    # Oops, default is 1000
    # Let it slide this time....
    sys.setrecursionlimit(len(height_data) + 100)
    increases, decreases = get_increases_and_decreases(height_data)
    print("Increases: " + str(increases))
    print("Decreases: " + str(decreases))

if __name__ == '__main__':
    main()
