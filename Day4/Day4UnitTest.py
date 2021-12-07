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

LAST_WINNING_BOARD_DATA = [
    [
        [
            {
                "number": 3,
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
                "number": 4,
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
                "number": 5,
                "called": False,
            },
            {
                "number": 6,
                "called": False,
            },
            {
                "number": 7,
                "called": False,
            },
        ],
    ],
    [
        [
            {
                "number": 0,
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
                "number": 1,
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
                "number": 2,
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
    ],
]


LAST_WINNING_CALLING_ORDER = [0, 1, 2, 3, 4, 5, 6, 7]
LAST_WINNING_EXPECTED_BOARD = [
    [
        {
            "number": 3,
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
            "number": 4,
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
            "number": 5,
            "called": True,
        },
        {
            "number": 6,
            "called": False,
        },
        {
            "number": 7,
            "called": False,
        },
    ],
]
LAST_WINNING_EXPECTED_LAST_NUMBER = 5


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

    def test_bingo_board_get_last_winning_board(self):
        last_winning_info = Day4.get_last_winning_board_info(LAST_WINNING_CALLING_ORDER, LAST_WINNING_BOARD_DATA)
        self.assertEqual(LAST_WINNING_EXPECTED_LAST_NUMBER, last_winning_info["last_number_called"])
        self.assertEqual(LAST_WINNING_EXPECTED_BOARD, last_winning_info["board"])

if __name__ == '__main__':
    unittest.main()
