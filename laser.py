class Laser():
    def __init__(self, ship):
        '''initilize data for the laser bullet, pass ship object's information into the laser object'''
        self.x = ship.x # initial position of the laser = current position of the ship
        self.y = ship.y
        
        self.vx = cos(radians(ship.angle - 90)) * 8 # direction of laser = heading of the ship
        self.vy = sin(radians(ship.angle - 90)) * 8 
        
    def update(self):
        '''update the position of the laser bullets based on its velocity'''
        self.x += self.vx
        self.y += self.vy
        
    def display(self):
        '''method to display the laser'''
        
        pushMatrix() # add this so that strokeweight doesn't affect anything else
        
        stroke(255)
        strokeWeight(5)
        point(self.x, self.y)
        
        popMatrix()
        
    def hits(self, asteroid):
        '''method to detect collision, whether this laser hits an asteroid'''
        # approximate as a circle: radius
        d = dist(self.x, self.y, asteroid.x, asteroid.y) # calculate the center-to-center distance between the astroid and the bullet
        return d < asteroid.siz * 2 # return whether there is a collision
    
    def offscreen(self):
        '''method to indicate that the laser is offscreen'''
        a = self.x > width + 1000 # make the margin bigger to limit the number of continuous bullets fired
        b = self.x < 0 - 1000
        c = self.y > height + 800
        d = self.y < 0 - 800
        
        return a or b or c or d # return True if any of the 4 conditions is met
            

           
