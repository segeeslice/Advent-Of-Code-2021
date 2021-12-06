#!/usr/bin/env python3

'''
Requirements:
pip install pyyaml

My solutions:
Part 1: 1,693,300
Part 2: 1,857,508,050
'''

import yaml
import sys

DIRECTION_DATA_PATH = './Day2Data.yaml'

def load_yaml_data(data_path):
    with open(data_path, 'r') as f:
        return yaml.safe_load(f)

def get_direction_name(direction_string):
    return direction_string.split()[0]

def get_direction_amount(direction_string):
    return int(direction_string.split()[1])

def parse_directions_to_dict(direction_strings):
    return [
        {"direction": get_direction_name(d), "amount": get_direction_amount(d)}
        for d in direction_strings
    ]

def get_distance_and_depth(direction_data):
    distance = 0
    depth = 0

    # TODO: Extend with lambdas :)
    for d in direction_data:
        if d["direction"] == "forward": distance += d["amount"]
        if d["direction"] == "up": depth -= d["amount"]
        if d["direction"] == "down": depth += d["amount"]

    return (distance, depth)

def get_distance_depth_aim(direction_data):
    distance = 0
    depth = 0
    aim = 0

    for d in direction_data:
        if d["direction"] == "forward":
            distance += d["amount"]
            depth += aim * d["amount"]
        if d["direction"] == "up":
            aim -= d["amount"]
        if d["direction"] == "down":
            aim += d["amount"]

    return (distance, depth, aim)

def main():
    raw_direction_data = load_yaml_data(DIRECTION_DATA_PATH)
    direction_data = parse_directions_to_dict(raw_direction_data)

    horizontal_position, depth = get_distance_and_depth(direction_data)

    print("Part 1 (no aim):")
    print("Horizontal position: " + str(horizontal_position))
    print("Depth: " + str(depth))
    print("Multiplied: " + str(depth * horizontal_position))

    horizontal_position, depth, aim = get_distance_depth_aim(direction_data)

    print("Part 2 (with aim):")
    print("Horizontal position: " + str(horizontal_position))
    print("Depth: " + str(depth))
    print("Multiplied: " + str(depth * horizontal_position))


if __name__ == '__main__':
    main()
