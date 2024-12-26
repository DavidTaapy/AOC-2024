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
        global_vars = globals()
        max_z = 0
        with open(file_path, "r") as file:
            lines = [line.strip() for line in file.readlines()]
            for line in lines:
                if "->" in line:
                    input_one, operation, input_two, _, output = line.split()
                    exec(f"{output} = lambda: {operation}({input_one}(), {input_two}())", global_vars)
                    if output[0] == 'z':
                        max_z = max(max_z, int(output[1:]))
                else:
                    exec(line.replace(":", " = lambda:"), global_vars)
                    
        result = sum(eval(f'z{i:02}()<<{i}') for i in range(max_z + 1))
        return result

# Excecute the code
if __name__ == "__main__":
    result = Solution().execute()
    print(result)