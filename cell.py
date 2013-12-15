#!/usr/bin/env python

class Cell():
    # postion(X, Y)
    def __init__(self, alive=False, position=(0,0), bounds=(0, 5)):
        # position(x, y)
        self.position = position
        self.alive = alive
        self.next_state = False

        # bounds(min, max)
        self.bounds = bounds

        self.neighbors = self.get_neighbors()

    def get_neighbors(self):
        neighbors = []
        (x_coord, y_coord) = (self.position[0], self.position[1])
        for i in range(3):
            for j in range(3):
                new_position = (x_coord + j - 1, y_coord + i - 1)

                if self.get_valid_position(new_position):
                    neighbors.append(new_position)

        return neighbors

    def get_valid_position(self, position):
        (x_coord, y_coord) = (position[0], position[1])
        (min, max) = (self.bounds[0], self.bounds[1])

        if position == self.position:
            return False

        # Test X bounds
        if (x_coord < min) or (x_coord > max - 1):
            return False

        # Test Y bounds
        if (y_coord < min) or (y_coord > max - 1):
            return False

        return True

    def is_alive(self, num_living_neighbors):
        ''' if alive, stay alive with 2 or 3 neighbors
            if dead, revive with exactly 3 neighbors
            otherwise die'''

        if self.alive:
            if num_living_neighbors in [2, 3]:
                return True
            else:
                return False
        else:
           if num_living_neighbors == 3:
                return True 

        return False

    def apply_next_state(self):
        self.alive = self.next_state
