# Import require libraries
import os

# Class for solution
class Solution():

    def __init__(self):
        self.input_path: str = "./Day 1/Case 1/Input.txt"

    # Function to execute
    def execute(self) -> int:
        inputs = self.get_inputs(self.input_path)
        return self.solve(inputs)
        
    # Function to get inputs
    def get_inputs(self, file_path_in_dir: str) -> tuple[list, list]:
        # Define the file path
        curr_directory = os.getcwd()
        file_path = os.path.join(curr_directory, file_path_in_dir)
        # Initialize empty lists
        left_list = []
        right_list = []
        # Read the file and process lines
        with open(file_path, "r") as file:
            for line in file:
                # Split the line into two parts and convert to integers
                left, right = map(int, line.split())
                left_list.append(left)
                right_list.append(right)
        # Return a tuple representing the inputs
        return (left_list, right_list)

    # Function to solve the problem
    def solve(self, inputs: tuple[list, list]) -> int:
        # Get the inputs
        (left_list, right_list) = inputs
        # Sort the lists
        left_list.sort()
        right_list.sort()
        # Get the result
        return sum(abs(left_list[i] - right_list[i]) for i in range(len(left_list)))
    
# Excecute the code
if __name__ == "__main__":
    result = Solution().execute()
    print(result)