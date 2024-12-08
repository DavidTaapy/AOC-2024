# Import require libraries
import os

# Class for solution
class Solution():

    def __init__(self):
        self.input_path: str = "./Day 8/Case 1/Input.txt"
        self.inputs: dict[str, list[tuple[int, int]]]
        self.width: int = None
        self.height: int = None
        self.antinodes: set = set()

    # Function to execute
    def execute(self) -> int:
        self.get_inputs(self.input_path)
        return self.solve()
        
    # Function to get inputs
    def get_inputs(self, file_path_in_dir: str):
        # Define the file path
        curr_directory = os.getcwd()
        file_path = os.path.join(curr_directory, file_path_in_dir)
        # Initialize dict for input
        input_dict: dict[str, list[tuple[int, int]]] = {}
        # Read the file and process lines
        with open(file_path, "r") as file:
            lines = [line.strip() for line in file.readlines()]
            self.height = len(lines)
            self.width = len(lines[0])
            for y in range(self.height):
                for x in range(self.width):
                    char = lines[y][x]
                    if char != ".":
                        if char not in input_dict:
                            input_dict[char] = []
                        input_dict[char].append((x, y))
        self.inputs = input_dict

    # Function to solve the problem
    def solve(self) -> int:
        # Get result
        for _, coords in self.inputs.items():
            self._add_antinodes(coords)
        return len(self.antinodes)
    
    # Function to get antinodes given a bunch of coordinates
    def _add_antinodes(self, coords: list[tuple[int, int]]) -> None:
        len_coords = len(coords)
        for i in range(len_coords):
            for j in range(i + 1, len_coords):
                antinodes = self._get_antinodes(coords[i], coords[j])
                for antinode in antinodes:
                    if self._is_in_boundary(antinode):
                        self.antinodes.add(antinode)

    # Function to get the pair of antinodes given 2 locations
    def _get_antinodes(self, loc_one: tuple[int, int], loc_two: tuple[int, int]) -> list[tuple[int, int]]:
        x_diff = loc_two[0] - loc_one[0]
        y_diff = loc_two[1] - loc_one[1]
        return [(loc_one[0] - x_diff, loc_one[1] - y_diff), (loc_two[0] + x_diff, loc_two[1] + y_diff)]

    # Function to check if location is within bounds
    def _is_in_boundary(self, coords: tuple[int, int]) -> bool:
        return 0 <= coords[0] < self.width and 0 <= coords[1] < self.height

# Excecute the code
if __name__ == "__main__":
    result = Solution().execute()
    print(result)