# Import require libraries
import os
from operator import xor as XOR, or_ as OR, and_ as AND

# Class for solution
class Solution:

    def __init__(self):
        self.input_path: str = "./Day 24/Input.txt"

    # Function to execute
    def execute(self) -> int:
        return self.solve()

    # Function to solve the problem
    def solve(self) -> int:
        # Just execute each line as code
        curr_directory = os.getcwd()
        file_path = os.path.join(curr_directory, self.input_path)
        max_z = 0
        with open(file_path, "r") as file:
            lines = [line.strip().split() for line in file.readlines() if '->' in line]
            for line in lines:
                _, _, _, _, output = line
                if output[0] == 'z':
                    max_z = max(max_z, int(output[1:]))
        
        result = set()
        for input_one, oper, input_two, _, output in lines:
            if output[0] == "z" and oper != "XOR" and output != f"z{max_z}":
                result.add(output)
            elif (
                oper == "XOR"
                and all(wire[0] not in ["x", "y", "z"] for wire in [output, input_one, input_two])
            ):
                result.add(output)
            elif oper == "AND" and "x00" not in [input_one, input_two]:
                for sub_input_one, sub_oper, sub_input_two, _, _ in lines:
                    if (output == sub_input_one or output == sub_input_two) and sub_oper != "OR":
                        result.add(output)
            elif oper == "XOR":
                for sub_input_one, sub_oper, sub_input_two, _, _ in lines:
                    if (output == sub_input_one or output == sub_input_two) and sub_oper == "OR":
                        result.add(output)
        
        return ",".join(sorted(result))

# Excecute the code
if __name__ == "__main__":
    result = Solution().execute()
    print(result)