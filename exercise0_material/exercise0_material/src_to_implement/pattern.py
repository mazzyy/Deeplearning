import numpy as np

from matplotlib import pyplot as plt

class Checker(object):
    def __init__(self, resolution, tile_size):
        if not isinstance(tile_size, int):
            raise ValueError("tile_size must be an integar")
        if not isinstance(resolution, int):
            raise ValueError("resolution must be an integar")
        if (resolution % (2*tile_size)):
            raise ValueError("resolution must be divisible by 2*tile_size")

        self.tile_size = tile_size
        self.resolution = resolution
        self.output = np.ones((resolution, resolution), dtype=np.uint8)
        self.black = np.zeros((tile_size, tile_size), dtype=np.uint8)
        self.white = np.ones((tile_size, tile_size), dtype=np.uint8)

    def draw(self):
        reps = int(self.resolution/(2*self.tile_size))
        first_row = np.tile(np.hstack((self.black, self.white)), (1,reps))
        second_row = np.tile(np.hstack((self.white, self.black)), (1,reps))
        board = np.tile(np.vstack((first_row, second_row)), (reps,1))
        self.output = board
        return self.output.copy()

    def show(self, headless=False):
        plt.imshow(self.output, cmap='gray')
        if headless:
            plt.savefig("plot_checkers.png")
            # plt.show()


ch = Checker(50, 25)
ch.draw()
ch.show(headless=True)