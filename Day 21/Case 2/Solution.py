# Import require libraries
import os
from sys import maxsize
from itertools import pairwise, permutations
from functools import cache

# Constants
MAX_DEPTH = 25
DIR_BASE_LOOKUP = {
    ('A', 'A'): 'A', ('^', '^'): 'A', ('>', '>'): 'A', ('v', 'v'): 'A', ('<', '<'): 'A',
    ('A', '^'): '<A', ('^', 'A'): '>A', ('A', '>'): 'vA', ('>', 'A'): '^A',
    ('v', '^'): '^A', ('^', 'v'): 'vA', ('v', '<'): '<A', ('<', 'v'): '>A',
    ('v', '>'): '>A', ('>', 'v'): '<A', ('A', 'v'): '<vA', ('v', 'A'): '^>A',
    ('A', '<'): 'v<<A', ('<', 'A'): '>>^A', ('>', '<'): '<<A', ('<', '>'): '>>A',
    ('<', '^'): '>^A', ('^', '<'): 'v<A', ('>', '^'): '<^A', ('^', '>'): 'v>A'
}
DIRS = [
    [('^', -1), ('v', 1)],
    [('<', -1), ('>', 1)],
]
NUMPAD = [
    ['7', '8', '9'],
    ['4', '5', '6'],
    ['1', '2', '3'],
    [' ', '0', 'A']
]
NUMPAD_LOOKUP = {
    '7': (0, 0), '8': (0, 1), '9': (0, 2),
    '4': (1, 0), '5': (1, 1), '6': (1, 2),
    '1': (2, 0), '2': (2, 1), '3': (2, 2),
    ' ': (3, 0), '0': (3, 1), 'A': (3, 2),
}

# Class for solution
class Solution:

    def __init__(self):
        self.input_path: str = "./Day 21/Input.txt"
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
            self.input = [line.strip() for line in file.readlines()]

    # Function to solve the problem
    def solve(self) -> int:
        return sum(self._solve_code(code) * int(code[:-1]) for code in self.input)

    # Function to solve a given code
    def _solve_code(self, s: str) -> int:
        return sum(
            self._dir_solve(self._num_solve(key_start, key_end))
            for key_start, key_end in pairwise(f"A{s}")
        )

    # Function to solve a given code
    def _num_solve(self, key_start: str, key_end: str) -> str:
        # Get the keys and directions for x and y
        y0, x0 = NUMPAD_LOOKUP[key_start]
        y1, x1 = NUMPAD_LOOKUP[key_end]
        y_dist, x_dist = y1 - y0, x1 - x0
        y_key, y_dir = DIRS[0][y_dist > 0]
        x_key, x_dir = DIRS[1][x_dist > 0]
        # To dodge blank corner
        start_move = ""
        mov_s = ""
        if (y0 == 3 or y1 == 3) and (x0 == 0 or x1 == 0):
            if x0 == 0:
                start_move = '>'
                mov_s = y_key * abs(y_dist) + x_key * (abs(x_dist) - 1)
            else:
                start_move = '^'
                mov_s = y_key * (abs(y_dist) - 1) + x_key * abs(x_dist)
        else:
            mov_s = y_key * abs(y_dist) + x_key * abs(x_dist)
        # Generate all possible inputs
        possible_inputs = [
            f"{start_move}{''.join(x)}A"
            for x in set(permutations(mov_s))
        ]
        # Iterate through all possible inputs
        min_score = maxsize
        min_input = ""
        for inputs in possible_inputs:
            score = self._dir_solve(inputs)
            if score < min_score:
                min_score = score
                min_input = inputs
        return min_input
    
    # Function to do directional DFS
    @cache
    def _dir_solve(self, inputs: str, depth=MAX_DEPTH):
        if depth == 0:
            return len(inputs)
        return sum(
            self._dir_solve(DIR_BASE_LOOKUP[key_start, key_end], depth - 1)
            for key_start, key_end in pairwise(f"A{inputs}")
        )

    # Function to get complexity
    def _get_complexity(self, value: int, code: str) -> int:
        code_value = int(code[:-1])
        return value * code_value

# Excecute the code
if __name__ == "__main__":
    result = Solution().execute()
    print(result)