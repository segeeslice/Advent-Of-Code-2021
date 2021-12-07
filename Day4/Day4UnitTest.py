#!/usr/bin/env python3

import unittest
import Day4

TEST_DATA = '''
38 94 65
79 81 80
17  2 23
'''

EXPECTED_PARSE = [
    [
        {
            "number": 38,
            "called": False,
        },
        {
            "number": 94,
            "called": False,
        },
        {
            "number": 65,
            "called": False,
        },
    ],
    [
        {
            "number": 79,
            "called": False,
        },
        {
            "number": 81,
            "called": False,
        },
        {
            "number": 80,
            "called": False,
        },
    ],
    [
        {
            "number": 17,
            "called": False,
        },
        {
            "number": 2,
            "called": False,
        },
        {
            "number": 23,
            "called": False,
        },
    ],
]

TEST_BOARD_NO_WIN = [
    [
        {
            "number": 38,
            "called": False,
        },
        {
            "number": 94,
            "called": True,
        },
        {
            "number": 65,
            "called": False,
        },
    ],
    [
        {
            "number": 79,
            "called": False,
        },
        {
            "number": 81,
            "called": True,
        },
        {
            "number": 80,
            "called": True,
        },
    ],
    [
        {
            "number": 17,
            "called": True,
        },
        {
            "number": 2,
            "called": False,
        },
        {
            "number": 23,
            "called": False,
        },
    ],
]

TEST_BOARD_WITH_WIN_HORIZONTAL = [
    [
        {
            "number": 38,
            "called": False,
        },
        {
            "number": 94,
            "called": False,
        },
        {
            "number": 65,
            "called": False,
        },
    ],
    [
        {
            "number": 79,
            "called": True,
        },
        {
            "number": 81,
            "called": True,
        },
        {
            "number": 80,
            "called": True,
        },
    ],
    [
        {
            "number": 17,
            "called": False,
        },
        {
            "number": 2,
            "called": False,
        },
        {
            "number": 23,
            "called": False,
        },
    ],
]

TEST_BOARD_WITH_WIN_VERTICAL = [
    [
        {
            "number": 38,
            "called": True,
        },
        {
            "number": 94,
            "called": False,
        },
        {
            "number": 65,
            "called": False,
        },
    ],
    [
        {
            "number": 79,
            "called": True,
        },
        {
            "number": 81,
            "called": False,
        },
        {
            "number": 80,
            "called": False,
        },
    ],
    [
        {
            "number": 17,
            "called": True,
        },
        {
            "number": 2,
            "called": False,
        },
        {
            "number": 23,
            "called": False,
        },
    ],
]

TEST_BOARD_WITH_WIN_DIAGONAL_RIGHT = [
    [
        {
            "number": 38,
            "called": True,
        },
        {
            "number": 94,
            "called": False,
        },
        {
            "number": 65,
            "called": False,
        },
    ],
    [
        {
            "number": 79,
            "called": False,
        },
        {
            "number": 81,
            "called": True,
        },
        {
            "number": 80,
            "called": False,
        },
    ],
    [
        {
            "number": 17,
            "called": False,
        },
        {
            "number": 2,
            "called": False,
        },
        {
            "number": 23,
            "called": True,
        },
    ],
]

TEST_BOARD_WITH_WIN_DIAGONAL_LEFT = [
    [
        {
            "number": 38,
            "called": False,
        },
        {
            "number": 94,
            "called": False,
        },
        {
            "number": 65,
            "called": True,
        },
    ],
    [
        {
            "number": 79,
            "called": False,
        },
        {
            "number": 81,
            "called": True,
        },
        {
            "number": 80,
            "called": False,
        },
    ],
    [
        {
            "number": 17,
            "called": True,
        },
        {
            "number": 2,
            "called": False,
        },
        {
            "number": 23,
            "called": False,
        },
    ],
]

class TestBingoBoards (unittest.TestCase):
    # TODO: Write test for single bingo board?

    def test_parse_bingo_boards_should_parse_multiple(self):
        test_data = TEST_DATA + "\n\n" + TEST_DATA
        expected = [EXPECTED_PARSE, EXPECTED_PARSE]

        result = Day4.parse_bingo_boards(test_data, line_start=0)
        self.assertEqual(expected, result)

    def test_parse_bingo_boards_should_parse_multiple_regardless_of_spaces_between(self):
        test_data = TEST_DATA + "\n\n\n\n\n" + TEST_DATA
        expected_length = 2

        result = Day4.parse_bingo_boards(test_data, line_start=0)
        self.assertEqual(expected_length, len(result))

    def test_bingo_board_has_win_should_detect_false(self):
        self.assertFalse(Day4.bingo_board_has_win(TEST_BOARD_NO_WIN))

    def test_bingo_board_has_win_should_detect_true_horizontal(self):
        self.assertTrue(Day4.bingo_board_has_win(TEST_BOARD_WITH_WIN_HORIZONTAL))

    def test_bingo_board_has_win_should_detect_true_vertical(self):
        self.assertTrue(Day4.bingo_board_has_win(TEST_BOARD_WITH_WIN_VERTICAL))

    def test_bingo_board_has_win_should_detect_true_diagonal_left(self):
        self.assertTrue(Day4.bingo_board_has_win(TEST_BOARD_WITH_WIN_DIAGONAL_LEFT))

    def test_bingo_board_has_win_should_detect_true_diagonal_right(self):
        self.assertTrue(Day4.bingo_board_has_win(TEST_BOARD_WITH_WIN_DIAGONAL_RIGHT))

if __name__ == '__main__':
    unittest.main()
