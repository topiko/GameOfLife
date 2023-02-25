
import numpy as np
from scipy.signal import convolve2d


class GameOfLife():

    def __init__(self, W: int=10, H: int=10):

        self._state = np.zeros((W,H), dtype=int)
        self._neighborhood = np.ones((3,3))
        self._neighborhood[1,1] = 0

    def set_state(self, state):
        self._state = state

    def update(self):
        """
        Rules:
            Any live cell with two or three live neighbours survives.
            Any dead cell with three live neighbours becomes a live cell.
            All other live cells die in the next generation. Similarly, all other dead cells stay dead.
        """


        number_neighbors = \
                convolve2d(self._state, self._neighborhood, mode='same')

        # Rule 1:
        mask1 = (self._state == 1) & (np.isin(number_neighbors, (2,3)))

        # Rule 2:
        mask2 = (self._state == 0) & (number_neighbors == 3)

        # Rule 3:
        mask3 = (self._state == 1) & ~mask1


        # Do update:
        self._state[mask1] = 1
        self._state[mask2] = 1
        self._state[mask3] = 0



    def get_state(self):
        return self._state
