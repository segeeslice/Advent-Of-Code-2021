#!/usr/bin/env python3

'''
Requirements:
~none~

My solutions:
Part 1: 328187
Part 2: ?
'''
import pprint
import copy
pp = pprint.PrettyPrinter(indent = 2)

CRAB_POSITIONS_PATH = './Day7Data.txt'

# == General-use ==

def read_file_text(data_path):
    with open(data_path, 'r') as f:
        return f.read()

# == Program-specific ==

def import_crab_positions(data_path):
    raw_text = read_file_text(data_path)
    return [int(i) for i in raw_text.split(',')]

def calculate_fuel_use_to(current, destination):
    return abs(current - destination)

def calculate_fuel_uses_to(crab_positions, destination):
    return sum(calculate_fuel_use_to(c, destination) for c in crab_positions)

def find_lowest_fuel_use_destination(crab_positions):
    min_pos = min(crab_positions)
    max_pos = max(crab_positions)
    print(min_pos, max_pos)
    results = {d: calculate_fuel_uses_to(crab_positions, d)
               for d in range(min_pos, max_pos+1)}
    # pp.pprint(results)
    min_dest = min(results, key=results.get)
    fuel_usage = results[min_dest]
    return {
        'dest': min_dest,
        'fuel_usage': fuel_usage
    }

# == Main ==

def main ():
    crab_positions = import_crab_positions(CRAB_POSITIONS_PATH)
    lowest = find_lowest_fuel_use_destination(crab_positions)

    print("Part 1:")
    print("Best destination: " + str(lowest["dest"]))
    print("Fuel usage: " + str(lowest["fuel_usage"]))

if __name__ == '__main__':
    main()
