# Import require libraries
import os
import re

# Constants
WIDTH = 101
HEIGHT = 103
NUM_MOVES = 100

# Class for solution
class Solution:

    def __init__(self):
        self.input_path: str = "./Day 14/Case 1/Input.txt"
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
        final_dict_pos = {}
        for robot in robots:
            final_position = self._get_final_pos(robot)
            if final_position not in final_dict_pos:
                final_dict_pos[final_position] = 1
            else:
                final_dict_pos[final_position] += 1
        return self._calculate_safety_factor(final_dict_pos)
    
    # Function to get the final position of the robot
    def _get_final_pos(self, robot: tuple[int, int, int, int]) -> tuple[int, int]:
        x, y, dx, dy = robot
        final_x = (x + NUM_MOVES * dx) % WIDTH
        final_y = (y + NUM_MOVES * dy) % HEIGHT
        return (final_x, final_y)
    
    # Function to get the safety factor
    def _calculate_safety_factor(self, final_dict_pos: dict[tuple[int, int], int]) -> int:
        q_counts = [0, 0, 0, 0]
        hori_line, vert_line = HEIGHT // 2, WIDTH // 2
        for (x, y), num_robots in final_dict_pos.items():
            if x == vert_line or y == hori_line:
                continue
            quadrant = (x > vert_line) * 2 + (y > hori_line)
            q_counts[quadrant] += num_robots
        return q_counts[0] * q_counts[1] * q_counts[2] * q_counts[3]

# Excecute the code
if __name__ == "__main__":
    result = Solution().execute()
    print(result)