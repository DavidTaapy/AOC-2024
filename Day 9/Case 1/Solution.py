# Import require libraries
import os

# Class for solution
class Solution:

    def __init__(self):
        self.input_path: str = "./Day 9/Case 1/Input.txt"
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
            self.input = file.read().strip()

    # Function to solve the problem
    def solve(self) -> int:
        # Create the list of bits
        curr_num = 0
        is_space = False
        bitmap: list[str] = []
        for char in self.input:
            for _ in range(int(char)):
                bitmap.append("." if is_space else str(curr_num))
            curr_num += int(not is_space)
            is_space = not is_space
        # Do the moving
        front_pointer = 0
        back_pointer = len(bitmap) - 1
        num_valid_bits = len([bit for bit in bitmap if bit != "."])
        while front_pointer < num_valid_bits:
            if bitmap[front_pointer] == ".":
                while bitmap[back_pointer] == ".":
                    back_pointer -= 1
                bitmap[front_pointer], bitmap[back_pointer] = bitmap[back_pointer], bitmap[front_pointer]
            front_pointer += 1
        # Calculate checksum
        return self._calculate_checksum(bitmap)

    # Function to calculate checksum
    def _calculate_checksum(self, bitmap: list[str]) -> int:
        return sum([i * int(bit) for i, bit in enumerate(bitmap) if bit != "."])

# Excecute the code
if __name__ == "__main__":
    result = Solution().execute()
    print(result)