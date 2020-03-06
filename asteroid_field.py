class Asteroid():
    '''pass in parameters on the asteroid's location for the breakup function'''
    def __init__(self, x, y, sizz):
        '''initilize data for the asteroid, if parameters passed in: x, y location are determined by these paremeter; if no parameters, defaults are random'''
        self.x = x
        self.y = y
        
        self.dx = random(-0.5, 0.5) # improvement, speed of asteroid depends on its mass: i.e. smaller asteroids move faster
        self.dy = random(-0.5, 0.5)
        
        self.siz = sizz / 2 # every time size decrease by a half, split into 2 smaller asteroids 
        
        self.total_vertex = int(random(5, 15)) # total number of vertex is between 5 and 15
        self.offset = [] # create a list of offset parameter to be passed into display function
        
        for i in range(self.total_vertex):
            self.offset.append(random(-self.siz + 10, self.siz + 10)) # offset as a function of the size of the asteroid, make its shape irregular
        
    def move(self):
        '''method to move the asteroid'''
        self.x += self.dx
        self.y += self.dy
        
    def display(self): 
        '''method to display the asteroid'''
        pushMatrix()
        
        noFill()
        stroke(255)
        strokeWeight(1)
        #  ellipse(self.x, self.y, self.siz, self.siz) # circle astroids
        translate(self.x, self.y)
        beginShape() # irregular shape asteroids
        for i in range(self.total_vertex):
            a = map(i, 0, self.total_vertex, 0, 360)
            r = self.siz + self.offset[i] # offset each angle so that the polygons are irregular
            x = r * cos(radians(a)) # convert to polar coordinates
            y = r * sin(radians(a))
            vertex(x, y)
            
        endShape(CLOSE)
        
        popMatrix()
        
    def offscreen(self):
        '''method to teleport across screen'''
        if self.x > width + self.siz:
            self.x = - self.siz
            
        elif self.x < - self.siz:
            self.x = width + self.siz
            
        if self.y > height + self.siz:
            self.y = - self.siz
            
        elif self.y < - self.siz:
            self.y = height + self.siz
        
    def breakup(self):
        '''method to break one asteroid into two new smaller ones'''
        newA = [] # new asteroid list
        newA.append(Asteroid(self.x, self.y, self.siz))
        newA.append(Asteroid(self.x, self.y, self.siz))
        return newA # the list containing two new asteroids at the same location of the broken asteroid
        
    
    
    
