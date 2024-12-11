# Import require libraries
import os

# Constants
NUM_SPLITS = 25

# Class for solution
class Solution:

    def __init__(self):
        self.input_path: str = "./Day 11/Case 1/Input.txt"
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
        curr_list = self.input
        for _ in range(NUM_SPLITS):
            new_list = []
            for num in curr_list:
                new_list += self._handle_num(num)
            curr_list = new_list
        return len(curr_list)

    # Function to handle the number
    def _handle_num(self, number: int) -> list[int]:
        if number == 0:
            return [1]
        num_str = str(number)
        if len(num_str) % 2 == 0:
            split_index = len(num_str) // 2
            return [int(num_str[:split_index]), int(num_str[split_index:])]
        return [number * 2024]
    
# Excecute the code
if __name__ == "__main__":
    result = Solution().execute()
    print(result)