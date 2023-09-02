class Elevator:
    def __init__(self, bottom, top, current):
        """Initializes the Elevator instance."""
        self.bottom = bottom
        self.top = top
        self.current = current
        
    def up(self):
        """Makes the elevator go up one floor."""
        if self.top > self.current:
            self.current += 1
        
    def down(self):
        """Makes the elevator go down one floor."""
        if self.bottom < self.current:
            self.current -= 1
        
    def go_to(self, floor):
        """Makes the elevator go to the specific floor."""
        if self.current < floor:
            for i in range(floor - self.current):
                """use 'up' method inside 'go_to' method"""
                self.up()
        elif self.current > floor:
            for i in range(self.current - floor):
                self.current -= 1
                
    def __str__(self):
        """Outputs a message with the current floor number"""
        return "Current floor: {}".format(self.current)

elevator = Elevator(-1, 10, 0)

elevator.up() 
print(elevator.current) #should output 1

elevator.down() 
print(elevator.current) #should output 0

elevator.go_to(10) 
print(elevator.current) #should output 10


# Go to the top floor. Try to go up, it should stay. Then go down.
elevator.go_to(10)
elevator.up()
elevator.down()
print(elevator.current) # should be 9
# Go to the bottom floor. Try to go down, it should stay. Then go up.
elevator.go_to(-1)
elevator.down()
elevator.down()
elevator.up()
elevator.up()
print(elevator.current) # should be 1

elevator.go_to(5)
print(elevator)