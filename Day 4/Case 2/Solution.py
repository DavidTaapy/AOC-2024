# Import require libraries
import os

# Class for solution
class Solution():

    def __init__(self):
        self.input_path: str = "./Day 4/Case 2/Input.txt"

    # Function to execute
    def execute(self) -> int:
        inputs = self.get_inputs(self.input_path)
        return self.solve(inputs)
        
    # Function to get inputs
    def get_inputs(self, file_path_in_dir: str) -> tuple[list[list[str]]]:
        # Define the file path
        curr_directory = os.getcwd()
        file_path = os.path.join(curr_directory, file_path_in_dir)
        # Initialize empty lists
        input = []
        # Read the file and process lines
        with open(file_path, "r") as file:
            for line in file:
                # Split the line into two parts and convert to integers
                input.append(list(line.strip()))
        # Return a tuple representing the inputs
        return (input, )

    # Function to solve the problem
    def solve(self, inputs: tuple[list[list[str]]]) -> int:
        # Get the inputs
        (input, ) = inputs
        width = len(input[0])
        height = len(input)
        # Get the result
        result = 0
        for y in range(height):
            for x in range(width):
                result += self._get_x_mas_count(input, x, y, width, height)
        return result
    
    # Function to check how many times a character is involved in XMAS
    def _get_x_mas_count(self, input: list[list[str]], x: int, y: int, width: int, height: int) -> int:
        result = 0
        if input[y][x] == "A":
            result += self._check_has_two_mas_in_diagonals(input, x, y, width, height) 
        return result

    # Function to check if the diagonal spells XMAS
    def _check_has_two_mas_in_diagonals(self, input: list[list[str]], x: int, y: int, width: int, height: int) -> int:
        mas_counts = 0
        if x + 1 < width and x - 1 >= 0:
            if y + 1 < height and y - 1 >= 0:
                mas_counts = int(input[y-1][x-1] + input[y][x] + input[y+1][x+1] == "MAS") + \
                    int(input[y-1][x+1] + input[y][x] + input[y+1][x-1] == "MAS") + \
                    int(input[y+1][x-1] + input[y][x] + input[y-1][x+1] == "MAS") + \
                    int(input[y+1][x+1] + input[y][x] + input[y-1][x-1] == "MAS")
        return int(mas_counts >= 2)
    
# Excecute the code
if __name__ == "__main__":
    result = Solution().execute()
    print(result)