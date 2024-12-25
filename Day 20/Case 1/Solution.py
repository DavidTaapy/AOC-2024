# Import require libraries
import os
from queue import PriorityQueue
from itertools import combinations

# Constants
DIR_MAP = {
    0: (0, -1),
    90: (1, 0),
    180: (0, 1),
    270: (-1, 0),
}

# Class for solution
class Solution:

    def __init__(self):
        self.input_path: str = "./Day 20/Input.txt"
        self.input: list[list[str]] = None
        self.start_loc: tuple[int, int] = None
        self.end_loc: tuple[int, int] = None

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
            self.input = [list(line.strip()) for line in file.readlines()]

    # Function to solve the problem
    def solve(self) -> int:
        # Get starting and ending locations
        self._get_scenario_details()
        # Simulate to find the original best path
        result = self._simulate(self.input, 2)
        return result

    # Function to simulate given a grid
    def _simulate(self, grid: list[list[str]], can_skip: int) -> tuple[int, list[tuple[int, int]]]:
        # Instantiate result
        result = 0
        # Initiate the priority queue
        dist_dict = {self.start_loc: 0}
        queue = [self.start_loc]
        for (x, y) in queue:
            for _, (dx, dy) in DIR_MAP.items():
                nx, ny = x + dx, y + dy
                if self._is_in_boundary(nx, ny, grid) and (nx, ny) not in dist_dict and self.input[ny][nx] != '#':
                    dist_dict[(nx, ny)] = dist_dict[(x, y)] + 1
                    queue += [(nx, ny)]             
        # Go through each combinations to check if skippable
        for ((x1, y1), score_1), ((x2, y2), score_2) in combinations(dist_dict.items(), 2):
            dist = abs(x2 - x1) + abs(y2 - y1)
            if dist == can_skip and score_2 - score_1 - dist >= 100:
                result += 1
        return result

    # Function to get starting and ending locations
    def _get_scenario_details(self) -> None:
        for y, row in enumerate(self.input):
            for x, char in enumerate(row):
                if char == 'S':
                    self.start_loc = (x, y)
                elif char == 'E':
                    self.end_loc = (x, y)

    # Function to check if a loc is in boundary
    def _is_in_boundary(self, x: int, y: int, grid: list[list[int]]) -> bool:
        return 0 <= x < len(grid[0]) and 0 <= y < len(grid)

# Excecute the code
if __name__ == "__main__":
    result = Solution().execute()
    print(result)