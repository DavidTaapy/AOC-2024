# Import require libraries
import os
from queue import PriorityQueue

# Constants
GRID_SIZE = 71
NUM_TO_FALL = 1024

# Direction Map
DIR_MAP: dict[int, tuple[int, int]] = {
    0: (0, -1),
    90: (1, 0),
    180: (0, 1),
    270: (-1, 0)
}

# Class for solution
class Solution:

    def __init__(self):
        self.input_path: str = "./Day 18/Input.txt"
        self.locs: list[tuple[int, int]] = []

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
            lines = file.readlines()
            for line in lines:
                x, y = list(map(int, line.split(",")))
                self.locs.append((x, y))

    # Function to solve the problem
    def solve(self) -> int:
        # Iterate through the obstacles
        num_to_fall = NUM_TO_FALL + 1
        while True:
            try:
                self._simulate(num_to_fall)
                num_to_fall += 1
            except:
                return self.locs[num_to_fall - 1]
            
    def _simulate(self, num_to_fall: int) -> int:
        # Add obstacles
        grid_map = [['.' for _ in range(GRID_SIZE)] for _ in range(GRID_SIZE)]
        obstacles = self.locs[:num_to_fall]
        for x, y in obstacles:
            grid_map[y][x] = '#'
        # Track location
        prior_queue = PriorityQueue()
        prior_queue.put((0, 0, 0))
        visited_set = set()
        while prior_queue:
            score, x, y = prior_queue.get()
            visited_set.add((x, y))
            if (x, y) == (GRID_SIZE - 1, GRID_SIZE - 1):
                return score
            for rot in DIR_MAP:
                dx, dy = DIR_MAP[rot]
                nx, ny = x + dx, y + dy
                if self._is_in_bounds(nx, ny) and grid_map[ny][nx] != '#' and (nx, ny) not in visited_set:
                    if (score + 1, nx, ny) not in prior_queue.queue:
                        prior_queue.put((score + 1, nx, ny))
        raise Exception("Cannot find exit!")
    
    # Check if coordinates is within bounds
    def _is_in_bounds(self, x: int, y: int) -> bool:
        return 0 <= x < GRID_SIZE and 0 <= y < GRID_SIZE

# Excecute the code
if __name__ == "__main__":
    result = Solution().execute()
    print(result)