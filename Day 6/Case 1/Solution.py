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

# Class for Grid
class Grid:

    def __init__(self, x: int, y: int, is_obstacle: bool, visited: bool = False):
        self.x: int = x
        self.y: int = y
        self.visited: bool = visited
        self.is_obstacle: bool = is_obstacle

    def set_visited(self, visited: bool) -> None:
        self.visited = visited

    def check_is_visited(self) -> bool:
        return self.visited

    def check_is_obstacle(self) -> bool:
        return self.is_obstacle

# Class for solution
class Solution():

    def __init__(self):
        self.input_path: str = "./Day 6/Case 1/Input.txt"
        self.guard_x: int = None
        self.guard_y: int = None
        self.guard_rot: int = None
        self.width: int = None
        self.height: int = None
        self.grid_list: list[list[Grid]] = None

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
                        grid.set_visited(True)
                        self.guard_x = x
                        self.guard_y = y
                        self.guard_rot = ROT_MAP[line[x]]
                    row.append(grid)
                grid_list.append(row)
        # Return a tuple representing the inputs
        self.grid_list = grid_list

    # Function to solve the problem
    def solve(self) -> int:
        # Move the guard around until it is out of bounds
        guard_has_exited = self._guard_has_exited(self.guard_x, self.guard_y)
        while not guard_has_exited:
            guard_has_exited = self._move()
        # Get the result
        return self._get_num_visited()
    
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
                self.grid_list[self.guard_y][self.guard_x].set_visited(True)
            return False

    # Function to count how many grids are visited
    def _get_num_visited(self) -> int:
        return sum(self.grid_list[y][x].check_is_visited() for x in range(self.width) for y in range(self.height))

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