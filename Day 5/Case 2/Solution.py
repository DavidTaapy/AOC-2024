# Import require libraries
import os

# Class for solution
class Solution():

    def __init__(self):
        self.input_path: str = "./Day 5/Case 2/Input.txt"

    # Function to execute
    def execute(self) -> int:
        inputs = self.get_inputs(self.input_path)
        return self.solve(inputs)
        
    # Function to get inputs
    def get_inputs(self, file_path_in_dir: str) -> tuple[list[list[int]], list[list[int]]]:
        # Define the file path
        curr_directory = os.getcwd()
        file_path = os.path.join(curr_directory, file_path_in_dir)
        # Initialize empty lists
        page_rules = []
        updates = []
        # Read the file and process lines
        with open(file_path, "r") as file:
            for line in file:
                # Split the line into two parts and convert to integers
                if '|' in line:
                    page_rules.append(list(map(int, line.split('|'))))
                elif ',' in line:
                    updates.append(list(map(int, line.split(','))))
        # Return a tuple representing the inputs
        return (page_rules, updates)

    # Function to solve the problem
    def solve(self, inputs: tuple[list[list[int]], list[list[int]]]) -> int:
        # Get the inputs
        (page_rules, updates) = inputs
        # Get the page rule dict
        page_rule_dict = self._get_page_rule_dict(page_rules)
        # Filter out safe updates
        unsafe_updates = [update for update in updates if not self._is_safe_update(update, page_rule_dict)]
        # Get the result
        return sum(self._get_middle_number_after_fixing(unsafe_updates[i], page_rule_dict) for i in range(len(unsafe_updates)))
    
    # Max page rule dictionary, with each key representing a page, and the values a list of pages that needs to come before it
    def _get_page_rule_dict(self, page_rules: list[list[int]]) -> dict[int, int]:
        page_rule_dict = {}
        for rule in page_rules:
            before_page, after_page = rule
            if after_page not in page_rule_dict:
                page_rule_dict[after_page] = []
            page_rule_dict[after_page].append(before_page)
        return page_rule_dict
    
    # Check if an update is safe
    def _is_safe_update(self, update: list[int], page_rule_dict: dict[int, int]) -> bool:
        for i in range(len(update)):
            for j in range(i, len(update)):
                if update[i] in page_rule_dict and update[j] in page_rule_dict[update[i]]:
                    return False
        return True
    
    # Get middle page number
    def _get_middle_number_after_fixing(self, update: list[int], page_rule_dict: dict[int, int]) -> int:
        for i in range(len(update)):
            for j in range(i, len(update)):
                if update[i] in page_rule_dict and update[j] in page_rule_dict[update[i]]:
                    update = self._swap_elements(update, i, j)
                    return self._get_middle_number_after_fixing(update, page_rule_dict)
        return self._get_middle_number(update)
    
    # Swap elements
    def _swap_elements(self, update: list[int], x: int, y: int) -> list[int]:
        temp = update[x]
        update[x] = update[y]
        update[y] = temp
        return update
    
    # Get middle page number
    def _get_middle_number(self, update: list[int]) -> int:
        return update[len(update) // 2]
    
# Excecute the code
if __name__ == "__main__":
    result = Solution().execute()
    print(result)