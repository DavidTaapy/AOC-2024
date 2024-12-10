# Import require libraries
import os

# Map for direction
DIR_MAP: dict[int, tuple[int, int]] = {
    0: (0, -1),
    90: (1, 0),
    180: (0, 1),
    270: (-1, 0)
}

# Map for rotation
ROT_MAP: dict[str, int] = {
    "^": 0,
    ">": 90,
    "v": 180,
    "<": 270
}

# Exception when guard is stuck
class GuardStuckException(Exception):
    pass

# Class for Grid
class Grid:

    def __init__(self, x: int, y: int, is_obstacle: bool):
        self.x: int = x
        self.y: int = y
        self.is_obstacle: bool = is_obstacle

    def check_is_obstacle(self) -> bool:
        return self.is_obstacle

    def set_is_obstacle(self, is_obstacle: bool) -> None:
        self.is_obstacle = is_obstacle

# Class for solution
class Solution():

    def __init__(self):
        self.input_path: str = "./Day 6/Case 2/Input.txt"
        self.guard_x: int = None
        self.guard_y: int = None
        self.guard_rot: int = None
        self.initial_x: int = None
        self.initial_y: int = None
        self.initial_rot: int = None
        self.width: int = None
        self.height: int = None
        self.grid_list: list[list[Grid]] = None
        self.path_traversed: set[tuple[int, int, int]] = set()
        self.infinite_loop_count: int = 0

    # Function to execute
    def execute(self) -> int:
        self.get_inputs(self.input_path)
        return self.solve()

    # Function to get inputs
    def get_inputs(self, file_path_in_dir: str):
        # Define the file path
        curr_directory = os.getcwd()
        file_path = os.path.join(curr_directory, file_path_in_dir)
        # Initialize empty lists
        grid_list: list[list[Grid]] = []
        # Read the file and process lines
        with open(file_path, "r") as file:
            lines = file.readlines()
            lines = [line.strip() for line in lines]
            self.height = len(lines)
            self.width = len(lines[0])
            for y in range(self.height):
                line = lines[y]
                row = []
                for x in range(self.width):
                    grid = Grid(x, y, line[x] == "#")
                    if self._is_guard(line[x]):
                        self.initial_x = self.guard_x = x
                        self.initial_y = self.guard_y = y
                        self.initial_rot = self.guard_rot = ROT_MAP[line[x]]
                    row.append(grid)
                grid_list.append(row)
        # Return a tuple representing the inputs
        self.grid_list = grid_list

    # Function to solve the problem
    def solve(self) -> int:
        # Move the guard around until it is out of bounds
        guard_orig_path = self.simulate()
        for (x_coord, y_coord) in set([(x, y) for x, y, _ in guard_orig_path if x != self.initial_x or y != self.initial_y]):
            self.grid_list[y_coord][x_coord].set_is_obstacle(True)
            self.simulate()
            self.grid_list[y_coord][x_coord].set_is_obstacle(False)
        # Get the result
        return self.infinite_loop_count

    # Function to simulate a given scenario
    def simulate(self) -> set[tuple[int, int, int]]:
        # Initialize the guard
        self.guard_x = self.initial_x
        self.guard_y = self.initial_y
        self.guard_rot = self.initial_rot
        # Reset path traversed
        self.path_traversed = set()
        self.path_traversed.add((self.guard_x, self.guard_y, self.guard_rot))
        # Move the guard around until it is out of bounds
        guard_has_exited = self._guard_has_exited(self.guard_x, self.guard_y)
        while not guard_has_exited:
            try:
                guard_has_exited = self._move()
            except GuardStuckException:
                self.infinite_loop_count += 1
                break
        # Get the result
        return self.path_traversed

    # Function to move guard by one grid
    def _move(self) -> bool:
        new_guard_x = self.guard_x + DIR_MAP[self.guard_rot][0]
        new_guard_y = self.guard_y + DIR_MAP[self.guard_rot][1]
        if self._guard_has_exited(new_guard_x, new_guard_y):
            return True
        else:
            if self.grid_list[new_guard_y][new_guard_x].check_is_obstacle():
                self.guard_rot = (self.guard_rot + 90) % 360
            else:
                self.guard_x = new_guard_x
                self.guard_y = new_guard_y
            if (self.guard_x, self.guard_y, self.guard_rot) in self.path_traversed:
                raise GuardStuckException
            self.path_traversed.add((self.guard_x, self.guard_y, self.guard_rot))
            return False

    # Check if is guard
    def _is_guard(self, char: str) -> bool:
        return char in ROT_MAP

    # Check if guard is out of bounds
    def _guard_has_exited(self, x: int, y: int) -> bool:
        return not (0 <= x < self.width and 0 <= y < self.height)

# Excecute the code
if __name__ == "__main__":
    result = Solution().execute()
    print(result)