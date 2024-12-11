# Import require libraries
import os
from functools import cache

# Constants
NUM_SPLITS = 75

# Class for solution
class Solution:

    def __init__(self):
        self.input_path: str = "./Day 11/Case 2/Input.txt"
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
            self.input = list(map(int, file.read().strip().split(" ")))

    # Function to solve the problem
    def solve(self) -> int:
        result = sum(self._handle_num(number, 75) for number in self.input)
        return result

    # Function to handle the number
    @cache
    def _handle_num(self, number: int, steps: int) -> int:
        if steps == 0:
            return 1
        if number == 0:
            return self._handle_num(1, steps - 1)
        str_num = str(number)
        if len(str_num) % 2 == 0:
            split_index = len(str_num) // 2
            return self._handle_num(int(str_num[:split_index]), steps - 1) + self._handle_num(int(str_num[split_index:]), steps - 1)
        return self._handle_num(number * 2024, steps - 1)
        
# Excecute the code
if __name__ == "__main__":
    result = Solution().execute()
    print(result)