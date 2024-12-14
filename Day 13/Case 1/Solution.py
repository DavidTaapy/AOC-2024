# Import require libraries
import os
import re

# Constants
FAILURE_COST = 1000

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
            if curr_scenario_cost < FAILURE_COST:
                tokens_required += curr_scenario_cost
        return tokens_required

    # Function to find lowest cost required
    def _find_lowest_cost(self, scenario: list[list[int, int], list[int, int], list[int, int]]) -> int:
        # Initialize
        result = FAILURE_COST
        button_a = scenario[0]
        button_b = scenario[1]
        destination = scenario[2]
        # Button A Dominant
        result = min(result, self._get_cost_given_dominant((button_a, 3), (button_b, 1), destination))
        # Button B Dominant
        result = min(result, self._get_cost_given_dominant((button_b, 1), (button_a, 3), destination))
        # Return result
        return result
    
    # Function to check given a dominant button what's the number of moves required
    def _get_cost_given_dominant(self, dominant: tuple[tuple[int, int], int], non_dominant: tuple[tuple[int, int], int], destination: tuple[int, int]) -> int:
        dominant_move, dominant_cost = dominant
        non_dominant_move, non_dominant_cost = non_dominant
        curr_loc = destination
        curr_cost = 0
        while self._is_valid_coord(curr_loc) and not self._is_reachable(dominant_move, curr_loc):
            curr_loc = (curr_loc[0] - non_dominant_move[0], curr_loc[1] - non_dominant_move[1])
            curr_cost += non_dominant_cost
        if self._is_valid_coord(curr_loc):
            curr_cost += self._get_num_moves(dominant_move, curr_loc) * dominant_cost
            return curr_cost
        return FAILURE_COST
    
    # Function to check a location is reachable given a move
    # Returns 0 if not reachable
    # Returns the number of times if reachable
    def _is_reachable(self, move: list[int, int], location: list[int, int]) -> bool:
        if location[0] % move[0] or location[1] % move[1]:
            return False
        return location[0] // move[0] == location[1] // move[1]
    
    # Function to get number of moves required
    def _get_num_moves(self, move: list[int, int], location: list[int, int]) -> int:
        return location[0] // move[0]
    
    # Function to check if coordinate is valid
    def _is_valid_coord(self, coord: list[int, int]) -> bool:
        return coord[0] >= 0 and coord[1] >= 0

# Excecute the code
if __name__ == "__main__":
    result = Solution().execute()
    print(result)