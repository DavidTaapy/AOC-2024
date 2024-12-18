# Import require libraries
import os
from typing import Dict, List, Set

# Define Data Type required
Point = Dict[str, int]

# Constants
DIRECTIONS: Dict[str, Point] = {
    "^": {"x": 0, "y": -1},
    ">": {"x": 1, "y": 0},
    "v": {"x": 0, "y": 1},
    "<": {"x": -1, "y": 0},
}

# Class for solution
class Solution:

    def __init__(self):
        self.input_path: str = "./Day 15/Case 2/Input.txt"
        self.grid: list[list[str]] = []
        self.moves: str = ""

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
            input = [line.strip() for line in file.readlines()]
            is_grid_info = True
            for line in input:
                if line == '':
                    is_grid_info = False
                elif is_grid_info:
                    self.grid.append(list(line))
                else:
                    self.moves += line

    # Function to solve the problem
    def solve(self) -> int:
        # Initialize Variables
        walls: Set[str] = set()
        boxes: List[Point] = []
        robot: Dict[str, int] = {"x": 0, "y": 0}
        height = len(self.grid)
        width = len(self.grid)

        # Initialize walls, boxes, and robot position
        for y in range(height):
            for x in range(width):
                if self.grid[y][x] == "@":
                    robot = {"x": x * 2, "y": y}
                if self.grid[y][x] == "#":
                    walls.add(f"{x * 2},{y}")
                    walls.add(f"{x * 2 + 1},{y}")
                if self.grid[y][x] == "O":
                    boxes.append({"x": x * 2, "y": y})

        # Recursive function to try moving all boxes
        def move_box(
            collided_box: Point, direction: Point, movements: List[Dict[str, Point]]
        ) -> bool:
            # Try both positions of the moved box
            next_positions = [
                {
                    "x": collided_box["x"] + direction["x"],
                    "y": collided_box["y"] + direction["y"],
                },
                {
                    "x": collided_box["x"] + 1 + direction["x"],
                    "y": collided_box["y"] + direction["y"],
                },
            ]
            # If collided with a wall, stop all movements
            for next_pos in next_positions:
                if f"{next_pos['x']},{next_pos['y']}" in walls:
                    return False
            # Find all boxes that are collided with
            collided_boxes = [
                box
                for box in boxes
                if any(
                    (box["x"] == collided_box["x"] and box["y"] == collided_box["y"])
                    is False
                    and (
                        (box["x"] == next_pos["x"] or box["x"] + 1 == next_pos["x"])
                        and box["y"] == next_pos["y"]
                    )
                    for next_pos in next_positions
                )
            ]
            # If there are no collided boxes, all movements are good
            if not collided_boxes:
                return True
            # Check for conflicts
            conflicts = False
            for box in collided_boxes:
                if move_box(box, direction, movements):
                    # If box can move and not already processed, add to movements
                    if not any(
                        b["x"] == box["x"] and b["y"] == box["y"]
                        for b in [m["box"] for m in movements]
                    ):
                        movements.append({"box": box, "direction": direction})
                else:
                    # If box can't move, prevent any movements
                    conflicts = True
                    break
            return not conflicts

        # Process each instruction
        for instruction in self.moves:
            direction = DIRECTIONS[instruction]
            position = {"x": robot["x"] + direction["x"], "y": robot["y"] + direction["y"]}
            # Only try to move if no wall is in the way
            if f"{position['x']},{position['y']}" not in walls:
                collided_box = next(
                    (
                        box
                        for box in boxes
                        if (box["x"] == position["x"] or box["x"] + 1 == position["x"])
                        and box["y"] == position["y"]
                    ),
                    None,
                )
                # If there is a collided box, try to move all affected
                if collided_box is not None:
                    movements: List[Dict[str, Point]] = []
                    if move_box(collided_box, direction, movements):
                        for movement in movements:
                            movement["box"]["x"] += movement["direction"]["x"]
                            movement["box"]["y"] += movement["direction"]["y"]
                        collided_box["x"] += direction["x"]
                        collided_box["y"] += direction["y"]
                        robot = position
                else:
                    robot = position

        # Calculate the score
        score = sum(box["y"] * 100 + box["x"] for box in boxes)
        return score

# Excecute the code
if __name__ == "__main__":
    result = Solution().execute()
    print(result)