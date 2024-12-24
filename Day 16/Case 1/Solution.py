# Import require libraries
import os
from queue import PriorityQueue

# Constants
DIR_MAP: dict[int, tuple[int, int]] = {
    0: (0, -1),
    90: (1, 0),
    180: (0, 1),
    270: (-1, 0)
}

# Class for solution
class Solution:

    def __init__(self):
        self.input_path: str = "./Day 16/Case 1/Input.txt"
        self.input: str = None

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
        # Instantiate the reinder
        x, y = self._find_reindeer()
        rot = 90
        # Keep moving until the endpoint
        prior_queue = PriorityQueue()
        prior_queue.put((0, x, y, rot))
        visited_set = set()
        while prior_queue:
            score, x, y, rot = prior_queue.get()
            visited_set.add((x, y))
            if self.input[y][x] == 'E':
                return score
            for delta_angle in [-90, 0, 90]:
                new_rot = (rot + delta_angle) % 360
                dx, dy = DIR_MAP[new_rot]
                nx, ny = x + dx, y + dy
                if self._is_in_bounds(nx, ny) and self.input[ny][nx] != '#' and (nx, ny) not in visited_set:
                    prior_queue.put((score + 1001 - 1000 * (rot == new_rot), nx, ny, new_rot))
        raise Exception("Cannot find exit!")
    
    # Check if coordinates is within bounds
    def _is_in_bounds(self, x: int, y: int) -> bool:
        return 0 <= x < len(self.input[0]) and 0 <= y < len(self.input)

    # Find the reindeer
    def _find_reindeer(self) -> tuple[int, int]:
        for y, row in enumerate(self.input):
            for x, char in enumerate(row):
                if char == 'S':
                    return (x, y)
        raise Exception("Reindeer not found!")

# Excecute the code
if __name__ == "__main__":
    result = Solution().execute()
    print(result)