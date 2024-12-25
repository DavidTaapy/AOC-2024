# Import require libraries
import os

# Constants
HEIGHT = 7
WIDTH = 5

# Class for solution
class Solution:

    def __init__(self):
        self.input_path: str = "./Day 25/Input.txt"
        self.input: str = None
        self.keys: list[list[int]] = []
        self.locks: list[list[int]] = []

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
            self.input = [line.strip() for line in file.readlines()]

    # Function to solve the problem
    def solve(self) -> int:
        # Initialise result
        result = 0
        # Get the locks and keys
        self._get_keys_and_locks()
        # Get the result
        for lock in self.locks:
            for key in self.keys:
                combi = [a + b for a, b in zip(lock, key)]
                result += self._check_combi(combi)
        return result

    # Function to check if combination works
    def _check_combi(self, combi: list[int]) -> bool:
        for column in combi:
            if column >= HEIGHT - 1:
                return False
        return True

    # Function to get the keys and locks
    def _get_keys_and_locks(self) -> None:
        line_pointer = 0
        while line_pointer < len(self.input):
            # Skip the first row if it is a lock
            is_lock = False
            if self.input[line_pointer] == '#' * WIDTH:
                is_lock = True
                line_pointer += 1
            # Get the stats lock / key
            stat = self._get_stats(line_pointer)
            if is_lock:
                self.locks.append(stat)
            else:
                self.keys.append(stat)
            line_pointer += HEIGHT
            # Skip the last row if it is a key
            if not is_lock:
                line_pointer += 1

    # Function to get the lock stats
    def _get_stats(self, line_pointer: int) -> list[int]:
        stat = [0] * WIDTH
        for i in range(HEIGHT - 1):
            line = self.input[line_pointer + i]
            for i in range(WIDTH):
                if line[i] == '#':
                    stat[i] += 1
        return stat

# Excecute the code
if __name__ == "__main__":
    result = Solution().execute()
    print(result)