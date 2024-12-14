# Import require libraries
import os
import re
import numpy as np
from scipy.fft import fft2

# Constants
WIDTH = 101
HEIGHT = 103
NUM_MOVES = 100

# Class for solution
class Solution:

    def __init__(self):
        self.input_path: str = "./Day 14/Case 2/Input.txt"
        self.input: list[tuple[int, int, int, int]] = None

    # Function to execute
    def execute(self) -> int:
        self.get_inputs(self.input_path)
        return self.solve()

    # Function to get inputs
    def get_inputs(self, file_path_in_dir: str):
        # Define the file path
        curr_directory = os.getcwd()
        file_path = os.path.join(curr_directory, file_path_in_dir)
        # Read the file and process lines
        with open(file_path, "r") as file:
            data = []
            lines = file.readlines()
            for line in lines:
                x, y, dx, dy = list(map(int, re.findall(r'-?\d+', line)))
                data.append((x, y, dx, dy))
            self.input = data

    # Function to solve the problem
    def solve(self) -> int:
        robots = self.input
        result = index = None
        for move in range(WIDTH * HEIGHT):
            m = self._get_fft_real_min(robots, move)
            if result is None or m < result:
                result = m
                index = move
        return index

    # Function to get the fft_real_min
    def _get_fft_real_min(self, robots: list[tuple[int, int, int, int]], moves: int) -> int:
        array = np.zeros((WIDTH, HEIGHT), bool)
        for x, y, dx, dy in robots:
            array[(x + moves * dx) % WIDTH, (y + moves * dy) % HEIGHT] = True
        f_transform = fft2(array)
        return np.min(np.real(f_transform))
    
# Excecute the code
if __name__ == "__main__":
    result = Solution().execute()
    print(result)