class Ship():
    def __init__(self):
        '''initialize data for the ship'''
        self.x = 400 # position
        self.y = 300
        
        self.angle = 0 # rotation angle
        
        self.vx = 0 # velocity
        self.vy = 0
        
        self.al = 0 # alpha value, the little flame effect once thrust
        
        # self.ax = 0 # acceleration
        # self.ay = 0
        
    def display(self):
        '''method to display the ship'''
        
        pushMatrix()
        translate(self.x, self.y)
        rotate(radians(self.angle))
        fill(0) # fill the ship black so that it covers the bullet firing from its center
        stroke(255)
        strokeWeight(1)
        triangle(0, -20, -15, 20, 15, 20)
        
        noStroke() # draw the flame
        fill(255, 0, 0, self.al)
        # shapes of the three flames
        triangle(-6, 21, 6, 21, 0, 34)
        triangle(-13, 21, -5, 21, -8, 32)
        triangle(5, 21, 13, 21, 8, 32)
        
        popMatrix()
        
    def rotl(self):
        '''rotate left'''
        self.angle -= 2
        
    def rotr(self):
        '''rotate right'''
        self.angle += 2
    
    def update(self):
        '''update the position of the ship and add friction / inertia'''
        # self.vx = cos(radians(self.angle - 90)) * 3
        # self.vy = sin(radians(self.angle - 90)) * 3
        
        self.x += self.vx # update postion vector
        self.y += self.vy
        
        self.vx *= 0.99 # dampen speed vector to show friction effect
        self.vy *= 0.99
        
    def thrust(self):
        '''thrust function change the acceleration along the thrusting force'''
        ax = cos(radians(self.angle - 90)) * 0.05 # get the angels of the force / acceleration
        ay = sin(radians(self.angle - 90)) * 0.05
        
        self.vx += ax # update velocity vector in the direction of the force and acceleration
        self.vy += ay
        
        self.al += 5 # increase the transparency value, becoming more and more visible
        
    def offscreen(self):
        '''method to teleport across screen'''
        if self.x > width + 15:
            self.x = - 15
            
        elif self.x < - 15:
            self.x = width + 15
            
        if self.y > height + 15:
            self.y = - 15
            
        elif self.y < - 15:
            self.y = height + 15
        
    def hits(self, asteroid):
        '''method to detect collision on the asteroids, ship dies'''
        d = dist(self.x, self.y, asteroid.x, asteroid.y) # approximate center-to-center distance from the ship to asteroid
        if d < (15 + asteroid.siz * 2): # return collision if asteroid i
            return True
        else:
            return False
    
    def destroy(self):
        '''method to destroy the ship once it is hit by an astroid'''
        # broken into several seperate lines
        strokeWeight(10)
        fill(255, 0, 0)
        point(self.x, self.y) # temporary method to show ship has been hit
        
    def restore(self):
        pass
        
    def teleport(self):
        pass
        
        
    def getAngle(self):
        '''print the angle of heading, for testing purposes'''
        print(self.angle)
        
