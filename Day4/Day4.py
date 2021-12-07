#!/usr/bin/env python3


'''
Requirements:
~none~

My solutions:
Part 1: 51776
Part 2: ?
'''
import pprint
pp = pprint.PrettyPrinter(indent = 2)

# Formatted weirdly, can't be a YAML...
BINGO_DATA_PATH = './Day4Data.txt'
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

def bingo_board_has_win(bingo_board):
    return bingo_board_has_vertical_win(bingo_board) or \
        bingo_board_has_horizontal_win(bingo_board) or \
        bingo_board_has_diagonal_win(bingo_board)

def bingo_board_has_vertical_win(bingo_board):
    rotated_board = rotate_2d_array(bingo_board)
    return bingo_board_has_horizontal_win(rotated_board)

def bingo_board_has_horizontal_win(bingo_board):
    return any(all(item["called"] for item in row) for row in bingo_board)

def bingo_board_has_diagonal_win(bingo_board):
    index = 0
    left_win = True
    right_win = True

    while index < len(bingo_board) and index < len(bingo_board[index]):
        if not bingo_board[index][index]["called"]:
            left_win = False
        if not bingo_board[index][-(index+1)]["called"]:
            right_win = False

        index += 1

    return left_win or right_win

def assign_called(num, bingo_board):
    for row in bingo_board:
        for val in row:
            if num == val["number"]:
                val["called"] = True

    return bingo_board

def get_first_winning_board_info(calling_order, bingo_boards):
    for num in calling_order:
        for bingo_board in bingo_boards:
            assign_called(num, bingo_board)
            if bingo_board_has_win(bingo_board):
                return { "board": bingo_board, "last_number_called": num }

def get_unmarked_sum(bingo_board):
    sum_val = 0

    for row in bingo_board:
        for val in row:
            if not val["called"]: sum_val += val["number"]

    return sum_val

# == Main ==

def main ():
    raw_bingo_text = read_file_text(BINGO_DATA_PATH)
    calling_order = parse_calling_order(raw_bingo_text)
    bingo_boards = parse_bingo_boards(raw_bingo_text)

    first_winning_board_info = get_first_winning_board_info(calling_order, bingo_boards)
    first_winning_board = first_winning_board_info["board"]
    last_number_called = first_winning_board_info["last_number_called"]

    unmarked_sum = get_unmarked_sum(first_winning_board)
    final_score = unmarked_sum * last_number_called

    print("Part 1:")
    print("Score: " + str(final_score))

if __name__ == '__main__':
    main()
