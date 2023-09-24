class Grid:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.obstacles = set()

    def add_obstacle(self, x, y):
        self.obstacles.add((x, y))

    def has_obstacle(self, x, y):
        return (x, y) in self.obstacles

    def is_within_boundary(self, x, y):
        return 0 <= x < self.width and 0 <= y < self.height


class Rover:
    DIRECTIONS = ['N', 'E', 'S', 'W']

    def __init__(self, x, y, direction, grid):
        self.x = x
        self.y = y
        self.direction = direction
        self.grid = grid
        self.obstacle_detected = False  # Initialize obstacle detection status


    def move(self):
        if self.direction == 'N':
            new_x, new_y = self.x, self.y + 1
        elif self.direction == 'E':
            new_x, new_y = self.x + 1, self.y
        elif self.direction == 'S':
            new_x, new_y = self.x, self.y - 1
        else:  # West
            new_x, new_y = self.x - 1, self.y

        if self.grid.is_within_boundary(new_x, new_y) and not self.grid.has_obstacle(new_x, new_y):
            self.x, self.y = new_x, new_y

    def turn_left(self):
        current_index = self.DIRECTIONS.index(self.direction)
        self.direction = self.DIRECTIONS[(current_index - 1) % 4]

    def turn_right(self):
        current_index = self.DIRECTIONS.index(self.direction)
        self.direction = self.DIRECTIONS[(current_index + 1) % 4]

    def send_status_report(self):
        status = f"Current Position: ({self.x}, {self.y}), Facing: {self.direction}"
        if self.obstacle_detected:
            status += "\nObstacle detected!"
        else:
            status += "\nNo obstacles detected."
        return status
    


if __name__ == "__main__":
    mars_grid = Grid(10, 10)
    mars_grid.add_obstacle(2,2)
    mars_grid.add_obstacle(3, 5)

    mars_rover = Rover(0, 0, 'N', mars_grid)

    commands = "MMRMLM"
    for command in commands:
        if command == 'M':
            mars_rover.move()
        elif command == 'L':
            mars_rover.turn_left()
        elif command == 'R':
            mars_rover.turn_right()

    print(mars_rover.send_status_report())
