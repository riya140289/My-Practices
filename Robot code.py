import numpy as np

class Robot:
    def __init__(self, start_row, start_col, start_direction):
        # Initialize the 5x4 grid
        self.grid = np.zeros((4, 5), dtype=str)  # 4 rows, 5 columns
        self.grid[:] = ' '  # Fill the grid with empty spaces for better visibility
        self.row = start_row  # Row position of the robot
        self.col = start_col  # Column position of the robot
        self.direction = start_direction  # Robot's initial direction
        self.directions = ['N', 'E', 'S', 'W']  # List of directions
        self.update_grid()  # Place the robot's initial position
        self.direction_dictionary = { # Dictionary defining to identify the direction of Robot
            'N': "North",  
            'E': "East",  
            'S': "South",   
            'W': "West"  
        }
    
    def turn(self, new_direction):
        # Change the robot's direction 
        self.direction = new_direction
    
    def move(self):
        # Reset the current position in the grid before moving
        self.grid[self.row, self.col] = ' '
        # Move the robot based on its direction in the instruction
        if self.direction == 'N' and self.row > 0:
            self.row -= 1
        elif self.direction == 'S' and self.row < self.grid.shape[0] - 1:
            self.row += 1
        elif self.direction == 'E' and self.col < self.grid.shape[1] - 1:
            self.col += 1
        elif self.direction == 'W' and self.col > 0:
            self.col -= 1
        # Update the grid after moving
        self.update_grid()
    
    def update_grid(self):
        # Mark robot's current position with Alphabet R
        self.grid[self.row, self.col] = 'R'
    
    def report_position(self):
        # robot's current position 
        return (self.row, self.col, self.direction)

    # Printing the matrix of Robot for Vizualization
    def print_grid(self):
        # Creating the grid
        top_bottom_border = " " + "+---" * self.grid.shape[1] + "+"  # "+---+" pattern design
        print("   " + "   ".join([str(x) for x in range(5)]))  # For columns 0 to 4 printing
        
        for i, row in enumerate(self.grid):
            print(top_bottom_border)  # Print the top border
            print(str(i)+ "| " + " | ".join(row) + " |")  # Print the row with "|"
            
        print(top_bottom_border)  # Print the bottom border

# Example Usage:
robot = Robot(0, 0, 'E')  # Start
instructions = ['E', 'M', 'M', 'N', 'M', 'E', 'M']

print("Initial Grid:")
robot.print_grid()

for instruction in instructions:
    if instruction in ['N', 'E', 'W', 'S']:
        robot.turn(instruction)
        print(f"--Next Step: Instruction Turns to {instruction}-{robot.direction_dictionary[instruction]}--") 
    elif instruction == 'M':
        robot.move()
        print(f"--Next Move--{robot.report_position()}")
    robot.print_grid()

print("Final Position:", robot.report_position())
