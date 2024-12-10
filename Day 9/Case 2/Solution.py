# Import require libraries
import os

# Class for solution
class Solution:

    def __init__(self):
        self.input_path: str = "./Day 9/Case 2/Input.txt"
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
        back_pointer = len(bitmap) - 1
        while back_pointer > 0:
            front_pointer = 0
            file_length, file_start = self._get_file_info(bitmap, back_pointer)
            if bitmap[back_pointer] == ".":
                back_pointer = file_start - 1
            else:
                while front_pointer < back_pointer:
                    poss_swap_length, _ = self._get_file_info(bitmap, front_pointer)
                    if bitmap[front_pointer] == ".":
                        if poss_swap_length >= file_length:
                            bitmap[front_pointer:front_pointer + file_length] = bitmap[file_start:file_start + file_length]
                            bitmap[file_start:file_start + file_length] = ["." for _ in range(file_length)]
                            break
                    front_pointer += poss_swap_length
                back_pointer -= file_length
        # Calculate checksum
        return self._calculate_checksum(bitmap)

    # Function to get the contiguous file length and start index given a bitmap and index
    def _get_file_info(self, bitmap: list[str], index: int) -> tuple[int, int]:
        # Get the character we are looking at
        char = bitmap[index]
        # Search the bits in front
        front_pointer = index
        while front_pointer - 1 > 0 and bitmap[front_pointer - 1] == char:
            front_pointer -= 1
        # Search the bits behind
        back_pointer = index
        while back_pointer + 1 < len(bitmap) and bitmap[back_pointer + 1] == char:
            back_pointer += 1
        # Return the length and start index
        return back_pointer - front_pointer + 1, front_pointer
   
    # Function to calculate checksum
    def _calculate_checksum(self, bitmap: list[str]) -> int:
        return sum([i * int(bit) for i, bit in enumerate(bitmap) if bit != "."])

# Excecute the code
if __name__ == "__main__":
    result = Solution().execute()
    print(result)