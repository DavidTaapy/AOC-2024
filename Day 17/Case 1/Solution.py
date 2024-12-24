# Import require libraries
import os
import re

# Class for solution
class Solution:

    def __init__(self):
        self.input_path: str = "./Day 17/Case 1/Input.txt"
        self.registers: dict[str, int] = {}
        self.instructions: list[str] = []
        self.instr_pointer = 0
        self.result = []

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
            lines = [line.strip() for line in file.readlines() if line.strip()]
            self.registers['A'] = int(re.findall(r'\d+', lines[0])[0])
            self.registers['B'] = int(re.findall(r'\d+', lines[1])[0])
            self.registers['C'] = int(re.findall(r'\d+', lines[2])[0])
            self.instructions = re.findall(r'\d+', lines[3])

    # Function to solve the problem
    def solve(self) -> str:
        # Start doing the operations
        while self.instr_pointer < len(self.instructions):
            try:
                self._perform_op()
            except:
                break
        return ",".join(self.result)

    # Function to get combo operand
    def _get_combo_operand(self) -> int:
        op = self._get_literal_operand()
        if op == 4:
            op = self.registers['A']
        elif op == 5:
            op = self.registers['B']
        elif op == 6:
            op = self.registers['C']
        return op
    
    # Function to get literal operand
    def _get_literal_operand(self) -> int:
        op = int(self.instructions[self.instr_pointer])
        self.instr_pointer += 1
        return op

    # Function to perform an operation
    def _perform_op(self) -> str:
        op_code = self.instructions[self.instr_pointer]
        self.instr_pointer += 1
        if op_code == "0": # ADV
            combo = self._get_combo_operand()
            self.registers['A'] = self.registers['A'] // (2 ** combo)
        elif op_code == "1": #BXL
            literal = self._get_literal_operand()
            self.registers['B'] = self.registers['B'] ^ literal
        elif op_code == "2": # BST
            combo = self._get_combo_operand()
            self.registers['B'] = combo % 8
        elif op_code == "3": # JNZ
            if self.registers['A'] != 0:
                literal = self._get_literal_operand()
                self.instr_pointer = literal
        elif op_code == "4": # BXC
            _ = self._get_literal_operand()
            self.registers['B'] = self.registers['B'] ^ self.registers['C']
        elif op_code == "5": # OUT
            combo = self._get_combo_operand()
            output = combo % 8
            self.result.append(str(output))
        elif op_code == "6": # BDV
            combo = self._get_combo_operand()
            self.registers['B'] = self.registers['A'] // (2 ** combo)
        elif op_code == "7":
            combo = self._get_combo_operand()
            self.registers['C'] = self.registers['A'] // (2 ** combo)
        else:
            raise Exception("No valid op code given!")

# Excecute the code
if __name__ == "__main__":
    result = Solution().execute()
    print(result)