# Import require libraries
import os

# Class for solution
class Solution():

    def __init__(self):
        self.input_path: str = "./Day 4/Case 1/Input.txt"

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
                result += self._get_xmas_count(input, x, y, width, height)
        return result
    
    # Function to check how many times a character is involved in XMAS
    def _get_xmas_count(self, input: list[list[str]], x: int, y: int, width: int, height: int) -> int:
        result = 0
        transposed_input = self._transpose(input)
        if input[y][x] == "X":
            result += self._check_all_straights(input, transposed_input, x, y, width, height) + self._check_all_diagonals(input, x, y, width, height) 
        return result
    
    # Function to check if the horizontal spells XMAS
    def _check_all_straights(self, input: list[list[str]], transposed_input: list[list[str]], x: int, y: int, width: int, height: int) -> int:
        result = self._check_horizontal(input[y], x, width) + \
            self._check_horizontal(transposed_input[x], y, height)
        return result

    # Function to check if the right spells XMAS
    def _check_horizontal(self, input: list[str], x: int, width: int) -> int:
        result = 0
        if x + 3 < width:
            result += int(''.join(input[x:x+4]) == "XMAS")
        if x - 3 >= 0:
            result += int(''.join(input[x-3:x+1][::-1]) == "XMAS")
        return result

    # Function to check if the diagonal spells XMAS
    def _check_all_diagonals(self, input: list[list[str]], x: int, y: int, width: int, height: int) -> int:
        result = 0
        if x + 3 < width:
            if y + 3 < height:
                result += int(input[y][x] + input[y+1][x+1] + input[y+2][x+2] + input[y+3][x+3] == "XMAS")
            if y - 3 >= 0:
                result += int(input[y][x] + input[y-1][x+1] + input[y-2][x+2] + input[y-3][x+3] == "XMAS")
        if x - 3 >= 0:
            if y + 3 < height:
                result += int(input[y][x] + input[y+1][x-1] + input[y+2][x-2] + input[y+3][x-3] == "XMAS")
            if y - 3 >= 0:
                result += int(input[y][x] + input[y-1][x-1] + input[y-2][x-2] + input[y-3][x-3] == "XMAS")
        return result
    
    # Tranpose matrix
    def _transpose(self, matrix: list[list[str]]) -> list[list[str]]:
        return [list(row) for row in zip(*matrix)]
    
# Excecute the code
if __name__ == "__main__":
    result = Solution().execute()
    print(result)