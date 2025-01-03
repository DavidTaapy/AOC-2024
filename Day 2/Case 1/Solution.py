# Import require libraries
import os

# Class for solution
class Solution():

    def __init__(self):
        self.input_path: str = "./Day 2/Case 1/Input.txt"

    # Function to execute
    def execute(self) -> int:
        inputs = self.get_inputs(self.input_path)
        return self.solve(inputs)
        
    # Function to get inputs
    def get_inputs(self, file_path_in_dir: str) -> tuple[list[list[int]]]:
        # Define the file path
        curr_directory = os.getcwd()
        file_path = os.path.join(curr_directory, file_path_in_dir)
        # Initialize empty lists
        inputs = []
        # Read the file and process lines
        with open(file_path, "r") as file:
            for line in file:
                # Split the line into two parts and convert to integers
                curr_line = list(map(int, line.split()))
                inputs.append(curr_line)
        # Return a tuple representing the inputs
        return (inputs, )

    # Function to solve the problem
    def solve(self, inputs: tuple[list[list[int]]]) -> int:
        # Get the inputs
        (input, ) = inputs
        # Sort the lists
        result = 0
        for line in input:
            if self._check_safe_increasing(line) or self._check_safe_decreasing(line):
                result += 1
        # Get the result
        return result
    
    # Function to check that line increases safely
    def _check_safe_increasing(self, line: list[int]) -> bool:
        for i in range(1, len(line)):
            if not (1 <= line[i] - line[i - 1] <= 3):
                return False
        return True
    
    # Function to check that line decreases safely
    def _check_safe_decreasing(self, line: list[int]) -> bool:
        for i in range(1, len(line)):
            if not (1 <= line[i - 1] - line[i] <= 3):
                return False
        return True

    
# Excecute the code
if __name__ == "__main__":
    result = Solution().execute()
    print(result)