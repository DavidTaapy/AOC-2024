# Import require libraries
import os
from functools import cache

# Class for solution
class Solution:

    def __init__(self):
        self.input_path: str = "./Day 19/Input.txt"
        self.base_designs: list[str] = []
        self.final_designs: list[str] = []

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
            inputs = [line.strip() for line in file.readlines() if line.strip()]
            self.base_designs = inputs[0].split(", ")
            for design in inputs[1:]:
                self.final_designs.append(design)

    # Function to solve the problem
    def solve(self) -> int:
        result = 0
        for final_design in self.final_designs:
            if self._is_feasible(final_design):
                self.base_designs.append(final_design)
                result += 1
        return result
    
    # Function to check if a design is feasible
    @cache
    def _is_feasible(self, final_design: str) -> bool:
        if final_design == '':
            return True
        for i in range(len(final_design)):
            curr_substr = final_design[:i + 1]
            if curr_substr in self.base_designs:
                if self._is_feasible(final_design[i + 1:]):
                    return True
        return False

# Excecute the code
if __name__ == "__main__":
    result = Solution().execute()
    print(result)