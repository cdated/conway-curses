#!/usr/bin/env python

from cell import Cell

class Conway():
    def __init__(self, bounds=(0, 5)):
        self.bounds = bounds
        self.board = self.create_new_board()

    def create_new_board(self):
        (min, max) = self.bounds
        dimension = max - min
        return [[Cell(position=(x, y),bounds=self.bounds) for y in xrange(dimension)] for x in xrange(dimension)] 

    def update_each_cells_state(self):
        dimension = len(self.board)
        for i in range(dimension):
            for j in range(dimension):
                cell = self.board[j][i]
                neighbors = cell.get_neighbors()
                self.update_cell_based_on_neighbor(cell, neighbors)

    def update_cell_based_on_neighbor(self, cell, neighbors):
        num_of_living_neighbors = 0
        for neighbor in neighbors:
            (x, y) = neighbor
            neighbor_cell = self.board[x][y]
            if neighbor_cell.alive:
                num_of_living_neighbors += 1

        if cell.is_alive(num_of_living_neighbors):
            self.set_next_state_on_board(cell.position, True)
        else:
            self.set_next_state_on_board(cell.position, False)

    def update_board(self):
        dimension = len(self.board)
        for i in range(dimension):
            for j in range(dimension):
                cell = self.board[j][i]
                cell.apply_next_state()

    def set_next_state_on_board(self, position, state):
        (x,y) = position
        cell = self.board[x][y]
        cell.next_state = state

    def set_initial_state_on_board(self, position, state):
        (x,y) = position
        cell = self.board[x][y]
        cell.alive = state

    def get_alive_positions(self):
        dimension = len(self.board)
        positions = []
        for i in range(dimension):
            for j in range(dimension):
                if self.board[j][i].alive:
                    positions.append((j,i))

        return positions
