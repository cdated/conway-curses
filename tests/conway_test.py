#!/usr/bin/env python

import unittest
from ..conway import Conway

class Test_Conway(unittest.TestCase):

    def setUp(self):
        self.bounds = (-5,0)
        self.conway = Conway(bounds=self.bounds)

    def test_board_dimensions(self):
        board = self.conway.board

        (min, max) = self.bounds
        dimension = max - min
        self.assertEqual(len(board), dimension)

    def test_next_state_on_board_can_be_set_false(self):
        (x, y) = (-1, -1)

        state = False
        self.conway.set_next_state_on_board((x,y), state)
        board = self.conway.board
        cell = board[x][y]
        self.assertEqual(cell.next_state, False)

    def test_next_state_on_board_can_be_set_true(self):
        (x, y) = (-1, -1)

        state = True
        self.conway.set_next_state_on_board((x,y), state)
        board = self.conway.board
        cell = board[x][y]
        self.assertEqual(cell.next_state, True)

if __name__ == '__main__':
    unittest.main()
