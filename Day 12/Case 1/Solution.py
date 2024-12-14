# Import require libraries
import os

# Constants
DIR_MAP = [(0, 1), (1, 0), (0, -1), (-1, 0)]

# Class for solution
class Solution:

    def __init__(self):
        self.input_path: str = "./Day 12/Case 1/Input.txt"
        self.input: list[list[str]] = None
        self.height: int = None
        self.width: int = None

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
            lines = [list(line.strip()) for line in file.readlines()]
            self.input = lines       
            self.height = len(lines)
            self.width = len(lines[0])       

    # Function to solve the problem
    def solve(self) -> int:
        # Get the total number of fences required
        total_price = 0
        # Get the clusters
        clusters = self._get_clusters_info()
        for cluster in clusters:
            cluster_size = len(cluster)
            total_price += sum([num_fences for _, _, num_fences in cluster]) * cluster_size
        # Return the total price
        return total_price

    # Function to get the different clusters
    def _get_clusters_info(self) -> list[set[tuple[int, int, int]]]:
        # Initialize the clusters and visited set
        clusters = []
        visited = set()
        # Loop through all the coordinates
        for y in range(self.height):
            for x in range(self.width):
                # If the coordinate is visited, skip
                if (x, y) in visited:
                    continue
                # Get the species of the current coordinate
                curr_species = self.input[y][x]
                # Initialize the cluster and stack
                cluster = set()
                stack = [(x, y)]
                # Loop through the stack
                while stack:
                    curr_x, curr_y = stack.pop()
                    # If the coordinate is visited, skip
                    if (curr_x, curr_y) in visited:
                        continue
                    # Add the coordinate to the cluster
                    cluster.add((curr_x, curr_y, self._get_num_fences(curr_x, curr_y, curr_species)))
                    visited.add((curr_x, curr_y))
                    # Loop through all the directions
                    for dx, dy in DIR_MAP:
                        new_x, new_y = curr_x + dx, curr_y + dy
                        if self._is_within_boundaries(new_x, new_y) and self.input[new_y][new_x] == curr_species:
                            stack.append((new_x, new_y))
                clusters.append(cluster)
        return clusters

    # Function to calculate checksum
    def _get_num_fences(self, x: int, y: int, curr_species: str) -> int:
        # Initialize result
        num_fences_required = 0
        # Check how many boundaries with non homogeneous species or empty spaces there are
        for dx, dy in DIR_MAP:
            new_x, new_y = x + dx, y + dy
            if self._is_within_boundaries(new_x, new_y) and self.input[new_y][new_x] == curr_species:
                continue
            num_fences_required += 1
        return num_fences_required

    # Function to check if given coordinates is within the boundary
    def _is_within_boundaries(self, x: int, y: int) -> bool:
        return 0 <= x < self.width and 0 <= y < self.height

# Excecute the code
if __name__ == "__main__":
    result = Solution().execute()
    print(result)