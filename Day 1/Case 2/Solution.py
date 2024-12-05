# Import require libraries
import os

# Class for solution
class Solution():

    def __init__(self):
        self.input_path: str = "./Day 1/Case 2/Input.txt"
        self.execute()

    # Function to execute
    def execute(self) -> None:
        inputs = self.get_inputs(self.input_path)
        result = self.solve(inputs)
        print(result)
        
    # Function to get inputs
    def get_inputs(self, file_path_in_dir: str) -> tuple[dict[int, int], dict[int, int]]:
        # Define the file path
        curr_directory = os.getcwd()
        file_path = os.path.join(curr_directory, file_path_in_dir)
        # Initialize empty dicts
        left_dict = {}
        right_dict = {}
        # Read the file and process lines
        with open(file_path, "r") as file:
            for line in file:
                # Split the line into two parts and convert to integers
                left, right = map(int, line.split())
                self._add_element_to_dict(left, left_dict)
                self._add_element_to_dict(right, right_dict)
        # Return a tuple representing the inputs
        return (left_dict, right_dict)

    # Function to solve the problem
    def solve(self, inputs: tuple[dict[int, int], dict[int, int]]) -> int:
        # Get the inputs
        (left_dict, right_dict) = inputs
        # Sort the lists
        result = 0
        for left_num, left_freq in left_dict.items():
            if left_num in right_dict:
                result += left_freq * (left_num * right_dict[left_num])
        return result

    # Add element to dictionary if it does not exist, else increment value by 1
    def _add_element_to_dict(self, element: int, curr_dict: dict[int, int]) -> None:
        if element not in curr_dict:
            curr_dict[element] = 1
        else:
            curr_dict[element] += 1
    
# Excecute the code
if __name__ == "__main__":
    Solution()