#!/usr/bin/env python3

import unittest
import Day4

TEST_DATA = '''
38 94 65
79 81 80
17  2 23
'''

EXPECTED = [
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

class TestBingoBoards (unittest.TestCase):
    # TODO: Write test for single bingo board?

    def test_parse_bingo_boards_should_parse_multiple(self):
        test_data = TEST_DATA + "\n\n" + TEST_DATA
        expected = [EXPECTED, EXPECTED]

        result = Day4.parse_bingo_boards(test_data, line_start=0)
        self.assertEqual(expected, result)

    def test_parse_bingo_boards_should_parse_multiple_regardless_of_spaces_between(self):
        test_data = TEST_DATA + "\n\n\n\n\n" + TEST_DATA
        expected_length = 2

        result = Day4.parse_bingo_boards(test_data, line_start=0)
        self.assertEqual(expected_length, len(result))

if __name__ == '__main__':
    unittest.main()
