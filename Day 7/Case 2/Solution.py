# Import require libraries
import os

# Class for solution
class Solution():

    def __init__(self):
        self.input_path: str = "./Day 7/Case 2/Input.txt"
        self.inputs: dict[int, list[list[int]]]

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
        input_dict: dict[int, list[list[int]]] = {}
        # Read the file and process lines
        with open(file_path, "r") as file:
            for line in file:
                output, input = line.split(": ")
                output = int(output)
                input_list = list(map(int, input.split(" ")))
                if output not in input_dict:
                    input_dict[output] = []
                input_dict[output].append(input_list)
        self.inputs = input_dict

    # Function to solve the problem
    def solve(self) -> int:
        # Initialize result
        result = 0
        # Check if line if it can be done
        for output, list_inputs in self.inputs.items():
            for input in list_inputs:
                result += output if self._check_is_possible(output, input) else 0
        return result
    
    # Function to check given an output and a list of inputs, is it possible to add a + or * operator to make it work
    def _check_is_possible(self, output: int, input: list[int]) -> bool:
        # If only one input, it will only work if it is the output
        if len(input) == 1:
            return output == input[0]
        # If last operator is addition and multiplication respectively
        addition_works = self._check_is_possible(output - input[-1], input[:-1])
        multiplication_works = self._check_is_possible(output // input[-1], input[:-1]) if output % input[-1] == 0 else False
        concatenation_works = self._check_is_possible((output - input[-1]) / 10 ** len(str(input[-1])), input[:-1])
        return addition_works or multiplication_works or concatenation_works

# Excecute the code
if __name__ == "__main__":
    result = Solution().execute()
    print(result)