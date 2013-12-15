#!/usr/bin/env python

import unittest
from ..cell import Cell

class Test_Cell(unittest.TestCase):

    def setUp(self):
        self.cell = Cell(alive=True, position=(-1,-1), bounds=(-5,0))

    def test_cell_position_on_init(self):
        new_cell = Cell(alive=True, position=(1,4))

        self.assertNotEqual(self.cell.position, new_cell.position)

    def test_cell_state_on_init(self):
        self.assertEqual(self.cell.alive, True)

    def test_cell_get_neighbors_returns_list(self):
        neighbors = self.cell.get_neighbors()

        self.assertEqual(type(neighbors), list)

    def test_cell_neighbor_count(self):
        neighbors = self.cell.get_neighbors()

        self.assertTrue(len(neighbors) > 2)
        self.assertTrue(len(neighbors) < 9)

    def test_valid_cell_position(self):
        cell = self.cell
        (x_coord, y_coord) = (cell.position[0], cell.position[1])
        (min, max) = (cell.bounds[0], cell.bounds[1])
        self.assertTrue(x_coord > min)
        self.assertTrue(x_coord < max)
        self.assertTrue(y_coord > min)
        self.assertTrue(y_coord < max)
        self.assertFalse(cell.position in cell.neighbors)

    def test_cell_is_alive(self):
        cell = Cell(alive=True)

        num_living_neighbors = 1
        self.assertEqual(cell.is_alive(num_living_neighbors), False)

        num_living_neighbors = 2
        self.assertNotEqual(cell.is_alive(num_living_neighbors), False)

        num_living_neighbors = 3
        self.assertEqual(cell.is_alive(num_living_neighbors), True)

        num_living_neighbors = 4
        self.assertEqual(cell.is_alive(num_living_neighbors), False)

    def test_cell_is_reborn(self):
        cell = Cell(alive=False)

        num_living_neighbors = 2
        self.assertEqual(cell.is_alive(num_living_neighbors), False)

        num_living_neighbors = 3
        self.assertEqual(cell.is_alive(num_living_neighbors), True)

if __name__ == '__main__':
    unittest.main()
