# Import require libraries
import os
import re

# Constants
OFFSET = 10000000000000

# Class for solution
class Solution:

    def __init__(self):
        self.input_path: str = "./Day 13/Case 1/Input.txt"
        self.input: list[list[int, int], list[int, int], list[int, int]] = None

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
            # Read the lines and initialize the output
            lines = file.readlines()
            result = []
            line_index = 0
            while line_index < len(lines):
                curr_line_values = []
                for offset in range(3):
                    values = list(map(int, re.findall(r'\d+', lines[line_index + offset])))
                    curr_line_values.append(values)
                result.append(curr_line_values)
                line_index += 4
            self.input = result

    # Function to solve the problem
    def solve(self) -> int:
        # Intialize tokens required
        tokens_required = 0
        # Check if each scenario is reachable and if so, return the lowest number of tokens required
        for scenario in self.input:
            curr_scenario_cost = self._find_lowest_cost(scenario)
            if 0 < curr_scenario_cost:
                tokens_required += curr_scenario_cost
        return tokens_required

    # Function to find lowest cost required
    def _find_lowest_cost(self, scenario: list[list[int, int], list[int, int], list[int, int]]) -> int:
        # Initialize
        ax, ay = scenario[0]
        bx, by = scenario[1]
        px, py = scenario[2]
        px, py = px + OFFSET, py + OFFSET
        # Get number of presses for A and B
        presses_a = (px * by - py * bx) / (ax * by - ay * bx)
        presses_b = (px - ax * presses_a) / bx
        if presses_a % 1 == presses_b % 1 == 0:
            return int(presses_a * 3 + presses_b)
        return 0         

# Excecute the code
if __name__ == "__main__":
    result = Solution().execute()
    print(result)