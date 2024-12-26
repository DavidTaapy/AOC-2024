# Import require libraries
import os
from itertools import combinations

# Class for solution
class Solution:

    def __init__(self):
        self.input_path: str = "./Day 23/Input.txt"
        self.computers: set = set()
        self.links: set = set()

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
            lines = [line.strip() for line in file.readlines()]
            for line in lines:
                a, b = line.split("-")
                self.computers.update([a, b])
                self.links.update([(a, b), (b, a)])

    # Function to solve the problem
    def solve(self) -> int:
        # Get all three linked with at least on T
        networks = [{computer} for computer in self.computers]
        for network in networks:
            for computer in self.computers:
                if all((computer, other) in self.links for other in network):
                    network.add(computer)
        return ",".join(sorted(max(networks, key=len)))

# Excecute the code
if __name__ == "__main__":
    result = Solution().execute()
    print(result)