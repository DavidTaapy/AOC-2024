# Import require libraries
import os

# Constants
DIR_MAP = {
    '^': (0, -1),
    'v': (0, 1),
    '<': (-1, 0),
    '>': (1, 0)
}

# Class for solution
class Solution:

    def __init__(self):
        self.input_path: str = "./Day 15/Case 1/Input.txt"
        self.grid: list[list[str]] = []
        self.moves: str = ""

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
            input = [line.strip() for line in file.readlines()]
            is_grid_info = True
            for line in input:
                if line == '':
                    is_grid_info = False
                elif is_grid_info:
                    self.grid.append(list(line))
                else:
                    self.moves += line

    # Function to solve the problem
    def solve(self) -> int:
        # Find robot coordinates
        robot_coord: tuple[int, int] = self._find_robot_coords()
        # Make the moves
        for move in self.moves:
            robot_coord = self._make_move(robot_coord, move)
        return self._get_sum_of_gps_coord()
    
    # Function to get the gps coordinates
    def _get_sum_of_gps_coord(self) -> int:
        sum_gps_coord = 0
        for y in range(len(self.grid)):
            for x in range(len(self.grid[0])):
                if self.grid[y][x] == 'O':
                    sum_gps_coord += 100 * y + x
        return sum_gps_coord
    
    # Function to make a move given the robot's coordinates and the move to make
    def _make_move(self, robot_coord: tuple[int, int], move: str) -> tuple[int, int]:
        x, y = robot_coord
        dx, dy = DIR_MAP[move]
        nx, ny = x + dx, y + dy
        if self.grid[ny][nx] == '.':
            self.grid[y][x] = '.'
            self.grid[ny][nx] = '@'
            return (nx, ny)
        if self.grid[ny][nx] == '#':
            return (x, y)
        return self._move_box(robot_coord, move)
    
    # Function that moves the boxes and returns the coordinate of the robot after moving
    def _move_box(self, robot_coord: tuple[int, int], move: str) -> tuple[int, int]:
        x, y = robot_coord
        dx, dy = DIR_MAP[move]
        last_box_x, last_box_y = x + dx, y + dy
        # Find the last box
        while self.grid[last_box_y + dy][last_box_x + dx] == 'O':
            last_box_x += dx
            last_box_y += dy
        # Nothing moves
        if self.grid[last_box_y + dy][last_box_x + dx] == '#':
            return (x, y)
        # Reflect the new state in the grid if boxes are moved
        self.grid[y][x] = '.'
        self.grid[y + dy][x + dx] = '@'
        if last_box_y == y:
            nx = x + dx
            while dx * (nx) < dx * (last_box_x + dx):
                nx += dx
                self.grid[last_box_y][nx] = 'O'
        elif last_box_x == x:
            ny = y + dy
            while dy * (ny) < dy * (last_box_y + dy):
                ny += dy
                self.grid[ny][last_box_x] = 'O'
        return (x + dx, y + dy)

    # Function to find the coordinate of the robots
    def _find_robot_coords(self) -> tuple[int, int]:
        for y in range(len(self.grid)):
            for x in range(len(self.grid[0])):
                if self.grid[y][x] == '@':
                    return (x, y)
        raise Exception("No robot found in grid!")

# Excecute the code
if __name__ == "__main__":
    result = Solution().execute()
    print(result)