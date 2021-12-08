#!/usr/bin/env python3

'''
Requirements:
pip install numpy

My solutions:
Part 1: 5373
Part 2: 21514
'''
import pprint
import copy
import numpy as np
import sys

pp = pprint.PrettyPrinter(indent = 2)

# Formatted weirdly, can't be a YAML...
VENT_DATA_PATH = './Day5Data.txt'
LINES_BETWEEN_SECTIONS = 1
BINGO_BOARD_START = 2

# == General-use ==

def read_file_text(data_path):
    with open(data_path, 'r') as f:
        return f.read()

# Pretty wild solution, retrieved from here:
# https://stackoverflow.com/questions/8421337/rotating-a-two-dimensional-array-in-python
def rotate_2d_array(arr):
    return list(zip(*arr[::-1]))

# == Program-specific ==

def parse_vent_data(vent_text):
    ret = []
    for line in vent_text.split('\n'):
        split_line = line.split(' -> ')
        if len(split_line) != 2: continue

        from_list = split_line[0].split(',')
        to_list = split_line[1].split(',')

        val = {
            'from': [int(x) for x in from_list],
            'to': [int(x) for x in to_list]
        }

        ret.append(val)

    return ret

def get_non_diagonal_vent_data(vent_data):
    return [v for v in vent_data if is_horizontal(v) or is_vertical(v)]

def get_max_x_y_sizes(vent_data):
    x_from_size = max(v["from"][0] for v in vent_data)
    x_to_size = max(v["to"][0] for v in vent_data)
    x_size = max(x_from_size, x_to_size) + 1

    y_from_size = max(v["from"][1] for v in vent_data)
    y_to_size = max(v["to"][1] for v in vent_data)
    y_size = max(y_from_size, y_to_size) + 1

    return (x_size, y_size)

def is_horizontal(vent_entry):
    return vent_entry["from"][1] == vent_entry["to"][1]

def is_vertical(vent_entry):
    return vent_entry["from"][0] == vent_entry["to"][0]

def is_diagonal(vent_entry):
    x_diff = vent_entry["from"][0] - vent_entry["to"][0]
    y_diff = vent_entry["from"][1] - vent_entry["to"][1]
    return abs(x_diff) == abs(y_diff)

def get_occurrence_matrix(vent_data):
    x_size, y_size = get_max_x_y_sizes(vent_data)
    arr = np.zeros((x_size, y_size))

    for v in vent_data:
        start_y = min(v["from"][1], v["to"][1])
        end_y = max(v["from"][1], v["to"][1])

        if is_horizontal(v):
            y = v["from"][1]
            start_x = min(v["from"][0], v["to"][0])
            end_x = max(v["from"][0], v["to"][0])
            for x in range(start_x, end_x+1):
                arr[x][y] = arr[x][y] + 1

        elif is_vertical(v):
            x = v["from"][0]
            start_y = min(v["from"][1], v["to"][1])
            end_y = max(v["from"][1], v["to"][1])
            for y in range(start_y, end_y+1):
                arr[x][y] += 1

        elif is_diagonal(v):
            start_x = min(v["from"][0], v["to"][0])
            end_x = max(v["from"][0], v["to"][0])

            start_y = v["from"][1] if v["from"][0] == start_x else v["to"][1]
            end_y = v["from"][1] if v["from"][0] == end_x else v["to"][1]

            x_range = range(start_x, end_x+1)
            y_range = range(start_y, end_y+1) if (end_y - start_y) > 0 else range(start_y, end_y-1, -1)

            for x, y in zip(x_range, y_range):
                arr[x][y] += 1

    return arr

def get_num_overlapping_lines(occurrence_matrix):
    return (occurrence_matrix >= 2).sum()

# == Main ==

def main ():
    raw_vent_text = read_file_text(VENT_DATA_PATH)
    vent_data = parse_vent_data(raw_vent_text)

    non_diagonal_vent_data = get_non_diagonal_vent_data(vent_data)
    non_diagonal_occurrence_matrix = get_occurrence_matrix(non_diagonal_vent_data)
    num_overlapping_lines = get_num_overlapping_lines(non_diagonal_occurrence_matrix)

    print("Part 1:")
    print("Number of overlapping lines: " + str(num_overlapping_lines))

    occurrence_matrix = get_occurrence_matrix(vent_data)
    num_overlapping_lines = get_num_overlapping_lines(occurrence_matrix)

    print("\nPart 2:")
    print("Number of overlapping lines: " + str(num_overlapping_lines))

if __name__ == '__main__':
    main()
