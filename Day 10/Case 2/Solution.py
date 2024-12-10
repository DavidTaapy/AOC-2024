# Import require libraries
import os

# Class for solution
class Solution:

    def __init__(self):
        self.input_path: str = "./Day 10/Case 2/Input.txt"
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
            lines = [map(int, list(line.strip())) for line in file.readlines()]
            self.input = [list(line) for line in lines]

    # Function to solve the problem
    def solve(self) -> int:
        # Initialize result
        trialhead_sum: int = 0
        # Iterate through the lines to find trailheads
        for y, row in enumerate(self.input):
            for x, value in enumerate(row):
                if value == 0:
                    trialhead_sum += self._get_distinct_paths(x, y)
        return trialhead_sum

    # Function to get the number of reachable final node given a node
    def _get_distinct_paths(self, x: int, y: int) -> int:

        def initiate_visited_grid() -> list[list[bool]]:
            return [[False for _ in range(len(self.input[0]))] for _ in range(len(self.input))]

        def is_within_bounds(nx: int, ny: int) -> bool:
            return 0 <= nx < len(self.input[0]) and 0 <= ny < len(self.input)

        def dfs(cx: int, cy: int, visited: list[list[bool]]) -> int:
            if self.input[cy][cx] == 9:
                return 1
            visited[cy][cx] = True
            curr_value = self.input[cy][cx]
            num_paths = 0
            directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
            for dx, dy in directions:
                nx, ny = cx + dx, cy + dy
                if is_within_bounds(nx, ny) and not visited[ny][nx] and self.input[ny][nx] == curr_value + 1:
                    num_paths += dfs(nx, ny, visited)
            visited[cy][cx] = False
            return num_paths
        visited_grid = initiate_visited_grid()
        return dfs(x, y, visited_grid)

# Excecute the code
if __name__ == "__main__":
    result = Solution().execute()
    print(result)