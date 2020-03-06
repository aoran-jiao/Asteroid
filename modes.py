class Mode():
    '''a template to store all the modes'''
    def mode1(self, score): 
        '''mode1 is game over'''
        imageMode(CORNER)
        image(loadImage("victory.png"), 0, 0, width, height)
        fill(255, 0, 0)
        textMode(CENTER)
        fill(255, 0, 0)
        textSize(35)
        text("Game Over", width/2 - 100, height/2) 
        text("Your Score: " + str(score), width/2 - 100, height/2 + 150)
        
    def mode0(self): # title page
       background(255)
       
       textMode(CENTER) 
       textSize(50)
       strokeWeight(6)
       if (frameCount / 60) % 2 == 0: # flashing effect
          fill(255, 0, 0)
       else:
           fill(0, 0, 255)
    
       text("Asteroid", width/2 - 150, height/2 - 300) # title
    
       rectMode(CENTER)
       noFill()
       stroke(0)
       strokeWeight(1)
       rect(width/2, height/2, 200, 100, 5) # button play
       fill(0, 0, 255)
       textSize(60)
       text("PLAY", width/2 - 70, height/2 + 30)
       
       noFill()
       stroke(0)
       strokeWeight(1)
       rect(width/2, height/2 + 150, 200, 100, 5) # button instructions
       fill(0, 0, 255)
       textSize(30)
       text("Instructions", width/2 -80, height/2 + 160)
       
       '''
       noFill()
       stroke(0)
       strokeWeight(1)
       rect(200, 600, 200, 100, 5) # button instructions
       '''
       
       ellipseMode(CENTER) # button for player 1 red
       fill(255, 0, 0, 120)
       stroke(100)
       strokeWeight(1)
       ellipse(width/2 - 200, height/2 - 200, 180, 100)
       fill(255)
       textMode(CENTER)
       textSize(30)
       text("Player1", width/2 - 250, height/2 - 190)
       
       pushMatrix() # button for player 2 blue
       translate(400, 0)
       fill(0, 0, 255, 120)
       stroke(100)
       strokeWeight(1)
       ellipse(width/2 - 200, height/2 - 200, 180, 100)
       fill(255)
       textMode(CENTER)
       textSize(30)
       text("Player2", width/2 - 250, height/2 - 190)
       popMatrix()
       
       textMode(CENTER)
       fill(0, 255, 0)
       stroke(1)
       text("Press 'esc' to finish the game", width/2 - 30, height - 40)
        
    def win(self):
        pass
        
        
        
