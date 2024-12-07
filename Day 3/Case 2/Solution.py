# Import require libraries
import os
import re

# Class for solution
class Solution():

    def __init__(self):
        self.input_path: str = "./Day 3/Case 2/Input.txt"

    # Function to execute
    def execute(self) -> int:
        inputs = self.get_inputs(self.input_path)
        return self.solve(inputs)
        
    # Function to get inputs
    def get_inputs(self, file_path_in_dir: str) -> tuple[str]:
        # Define the file path
        curr_directory = os.getcwd()
        file_path = os.path.join(curr_directory, file_path_in_dir)
        # Read the file and process lines
        with open(file_path, "r") as file:
            input = file.read()
        # Return a tuple representing the inputs
        return (input, )

    # Function to solve the problem
    def solve(self, inputs: tuple[str]) -> int:
        # Get the inputs
        (input, ) = inputs
        # Initialize result
        result = 0
        # Get the matching substrings
        pattern = r"(mul|do|don\'t)\((\d+,\d+|)\)"
        enabled = True
        matches = self._find_substrings(pattern, input)
        for match in matches:
            operation, nums = match
            if operation != "mul":
                enabled = operation == "do"
                continue
            first_num, second_num = map(int, nums.split(","))
            if enabled and self._has_valid_len(first_num, second_num):
                result += first_num * second_num
        # Get the result
        return result
    
    # Function to get matching substrings
    def _find_substrings(self, pattern: str, string: str) -> list[str]:
        matches = re.findall(pattern, string)
        return matches
    
    # Function to check length of numbers
    def _has_valid_len(self, first_num: int, second_num: int) -> bool:
        return (1 <= first_num <= 1000) and (1 <= second_num <= 1000) 

    
# Excecute the code
if __name__ == "__main__":
    result = Solution().execute()
    print(result)