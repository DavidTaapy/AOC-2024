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
        
        check_func = lambda c, y: any(y == oper and c in (in_one, in_two) for in_one, oper, in_two, _, _ in lines)

        result = sorted(out for in_one, oper, in_two, _, out in lines if
            oper == "XOR" and all(d[0] not in 'xyz' for d in (in_one, in_two, out)) or
            oper == "AND" and not "x00" in (in_one, in_two) and check_func(out, 'XOR') or
            oper == "XOR" and not "x00" in (in_one, in_two) and check_func(out, 'OR') or
            oper != "XOR" and out[0] == 'z' and out != f"z{max_z}")
        
        return ",".join(result)

# Excecute the code
if __name__ == "__main__":
    result = Solution().execute()
    print(result)