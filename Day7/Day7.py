#!/usr/bin/env python3

'''
Requirements:
~none~

My solutions:
Part 1: 328187
Part 2: 91257582
'''
import pprint
import copy
pp = pprint.PrettyPrinter(indent = 2)

CRAB_POSITIONS_PATH = './Day7Data.txt'

# == General-use ==

def read_file_text(data_path):
    with open(data_path, 'r') as f:
        return f.read()

# https://en.wikipedia.org/wiki/1_%2B_2_%2B_3_%2B_4_%2B_%E2%8B%AF
def triangular_func(n):
    return (n*(n+1)) / 2

# == Program-specific ==

def import_crab_positions(data_path):
    raw_text = read_file_text(data_path)
    return [int(i) for i in raw_text.split(',')]

def calculate_constant_fuel_use(current, destination):
    return abs(current - destination)

def calculate_triangular_fuel_use(current, destination):
    dist = abs(current - destination)
    return triangular_func(dist)

def calculate_fuel_uses(crab_positions, destination, fuel_use_method):
    return sum(fuel_use_method(c, destination) for c in crab_positions)

def calculate_constant_fuel_uses(crab_positions, destination):
    return calculate_fuel_uses(crab_positions, destination, calculate_constant_fuel_use)

def calculate_triangular_fuel_uses(crab_positions, destination):
    return calculate_fuel_uses(crab_positions, destination, calculate_triangular_fuel_use)

def find_lowest_fuel_use_destination(crab_positions, calculate_method):
    min_pos = min(crab_positions)
    max_pos = max(crab_positions)

    results = {d: calculate_method(crab_positions, d)
               for d in range(min_pos, max_pos+1)}

    min_dest = min(results, key=results.get)
    fuel_usage = results[min_dest]
    return {
        'dest': min_dest,
        'fuel_usage': fuel_usage
    }

# == Main ==

def main ():
    crab_positions = import_crab_positions(CRAB_POSITIONS_PATH)
    lowest_constant = find_lowest_fuel_use_destination(crab_positions, calculate_constant_fuel_uses)

    print("Part 1 (Constant fuel use):")
    print("Best destination: " + str(lowest_constant["dest"]))
    print("Fuel usage: " + str(lowest_constant["fuel_usage"]))

    lowest_triangular = find_lowest_fuel_use_destination(crab_positions, calculate_triangular_fuel_uses)

    print("Part 2 (Increasing/Triangular fuel use):")
    print("Best destination: " + str(lowest_triangular["dest"]))
    print("Fuel usage: " + str(lowest_triangular["fuel_usage"]))

if __name__ == '__main__':
    main()
