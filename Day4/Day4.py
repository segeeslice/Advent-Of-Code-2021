#!/usr/bin/env python3

import pprint
pp = pprint.PrettyPrinter(indent = 2)

# Formatted weirdly, can't be a YAML...
BINGO_DATA_PATH = './Day4Data.txt'
LINES_BETWEEN_SECTIONS = 1
BINGO_BOARD_START = 2

def read_file_text(data_path):
    with open(data_path, 'r') as f:
        return f.read()

def parse_calling_order (raw_bingo_text):
    num_text = raw_bingo_text.split('\n')[0].split(',')
    numbers = [int(num) for num in num_text]
    return numbers

def parse_bingo_boards (raw_bingo_text, line_start = BINGO_BOARD_START):
    lines = raw_bingo_text.split('\n')[line_start:]

    bingo_boards = [[]]

    for line in lines:
        if not line.strip():
            bingo_boards.append([])
            continue

        line_text = line.split(' ')
        line_nums = [int(num) for num in line_text if len(num) > 0]
        bingo_board_line = [{"number": num, "called": False} for num in line_nums]
        bingo_boards[-1].append(bingo_board_line)

    bingo_boards = [b for b in bingo_boards if len(b) > 0]
    return bingo_boards

def main ():
    raw_bingo_text = read_file_text(BINGO_DATA_PATH)
    calling_order = parse_calling_order(raw_bingo_text)
    bingo_boards = parse_bingo_boards(raw_bingo_text)
    pp.pprint(bingo_boards)

if __name__ == '__main__':
    main()
