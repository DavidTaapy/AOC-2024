# Import require libraries
import os
from collections import defaultdict
from itertools import pairwise

# Constants
NUM_GENERATION = 2000

# Class for solution
class Solution:

    def __init__(self):
        self.input_path: str = "./Day 22/Input.txt"
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
            self.input = [int(val) for val in file.readlines()]

    # Function to solve the problem
    def solve(self) -> int:
        pat_scores = defaultdict(int)
        for secret in self.input:
            nums = [secret]
            for _ in range(NUM_GENERATION):
                secret = self._generate_next_secret(secret)
                nums.append(secret)
            diffs = [b%10 - a%10 for a,b in pairwise(nums)]
            seen = set()
            for i in range(len(nums)-4):
                pat = tuple(diffs[i:i+4])
                if pat not in seen:
                    pat_scores[pat] += nums[i+4] % 10
                    seen.add(pat)
        return max(pat_scores.values())
    
    # Function to generate next secret
    def _generate_next_secret(self, secret: int) -> int:
        # Part 1
        value = secret * 64
        secret = self._prune_secret(self._mix_secret(value, secret))
        # Part 2
        value = secret // 32
        secret = self._prune_secret(self._mix_secret(value, secret))
        # Part 3
        value = secret * 2048
        secret = self._prune_secret(self._mix_secret(value, secret))
        return secret

    # Function to mix result
    def _mix_secret(self, value: int, secret: int) -> int:
        return value ^ secret
    
    # Function to prune result
    def _prune_secret(self, value: int) -> int:
        return value % 16777216

# Excecute the code
if __name__ == "__main__":
    result = Solution().execute()
    print(result)