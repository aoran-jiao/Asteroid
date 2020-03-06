add_library('minim') # import sound library

# import ship # import ship object
from ship import *

import asteroid_field # import asteroid_field object
from asteroid_field import *

import laser # import laser object
from laser import *

import modes # import modes object
from modes import *
m = Mode() # mode class

score = 0 # initiate score to be 0
mode = 0 # mode0 is normal playing the game; mode1 is gameover

keyl = [False, False, False] # continuous press of the key: rotate left; rotate right; thrust     
player = Ship() # instantiate the ship object
 
field = [] # create a list, to be appended with asteroids

lasers = [] # create a list of lasers

def setup():
    '''initialize imporant vairables'''
    global bu, win # global variable for sounds
    
    size(800, 600)
    background(0)
    frameRate(100)
    
    # sound effects! 
    minim = Minim(this)
    bu = minim.loadFile("laser.wav")
    win = minim.loadFile("win.wav")
    
    # appending asteroids
    for i in range(5):
        field.append(Asteroid(random(100, 300), random(100, 200), random(50, 80)))
        field.append(Asteroid(random(600, 800), random(400, 600), random(50, 80)))
        
def draw():
    '''main function to draw each frame'''
    global win, mode, score # global variables of sound of "win" and mode
    
    
    background(0) # every frame rewrite background to be black
    
    if mode == 1: # mode 1: player is destroyed
        player.destroy()
        m.mode1(score)
        
    if mode == 0: # mode 0: interphase
        m.mode0()
        
        # restart()
        
    if len(field) == 0: # if all asteroids are eliminated, play win music, win mode
        win.play()
        
    if mode == 2: # mode 2 is normal game 
        fill(255)
        text("Score:" + str(score), 10, 40)
        
        for i in lasers: # loop through the laser list
            i.display()
            i.update()
        
            if i.offscreen(): # need to remove the laser that fly offscreen to reduce the size of the laser list
                lasers.remove(i)
    
        # player ship functionalities
        player.display()
        player.offscreen()
        # player.getAngle()
        player.update()
    
    # key control, keyl for continuous pressing of keys
        if keyl[0]:
            player.rotl()
            player.display()
        
        if keyl[1]:
            player.rotr()
            player.display()
    
        if keyl[2]:
            player.thrust()
            player.update()
            player.display()

            
        for i in range(len(field) - 1, -1, -1): # loop through the asteroid list, check in reverse order 
        
            if player.hits(field[i]): # detect collision on the ship and the ship "dies"
                player.destroy()
                mode = 1
            
            field[i].move()
            field[i].display()
            field[i].offscreen()
        
            for j in range(len(lasers) - 1, -1, -1): # collision detection: loop through all the lasers vs. all the asteroids
            # it is inverse order to avoid adding and breaking asteroids at the same time
            
                if lasers[j].hits(field[i]): # if a particular laser hits a particular asteroid
                    score += 1
                    print(score)
                    if field[i].siz > 15: # remove the astroid if it is too small --> only split it further if its size is bigger than 15 
                    
                        newAsteroids = field[i].breakup() # return 2 new smaller asteroids
                    
                        field.append(newAsteroids[0])
                        field.append(newAsteroids[1]) # append the 2 new asteroids to the asteroid field
                    # else:
                        # score += 1
                    field.remove(field[i]) # remove the broken asteroid from the field list
                    lasers.remove(lasers[j]) # remove the hit laser
                
                    break # break the loop once the laser hits the asteroid, and both are removed from respective lists
            
                if lasers[j].offscreen(): # need to remove the laser that fly offscreen to reduce the size of the laser list
                    lasers.remove(lasers[j])

                
        # print(field) # list of all asteroids
        # print(lasers) # list of all bullets
    
def keyPressed():
    global keyl # global variable keyl
    if key == "A" or key == "a":
        keyl[0] = True
        
    elif key == "D" or key == "d":
        keyl[1] = True
        
    elif key == "W" or key == "w":
        keyl[2] = True
        
    elif key == " ":
        if len(lasers) <= 5: # limit the number of max lasers shot to be 5
            lasers.append(Laser(player)) 
            bu.rewind() # play the sound of the laser shooting
            bu.play()
                
def keyReleased():
    global keyl
    if key == "A" or key == "a":
        keyl[0] = False
        
    elif key == "D" or key == "d":
        keyl[1] = False
        
    elif key == "W" or key == "w":
        keyl[2] = False
        
        while player.al > 0: # when not thrusting anymore, flame disappears gradually
            player.al -= 1

def mousePressed():
    global mode
    if mode == 0: # at main page; rect(width/2, height/2, 200, 100) # button of play
        if mouseX >= width/2 - 100 and mouseX <= width/2 + 100 and mouseY >= height/2 - 50 and mouseY <= height/2 + 50: 
            mode = 2 # switch to play mode
            
def restart():
    player = Ship()
    field = []
    lasers = []
    for i in range(10):
        field.append(Asteroid(random(100, 700), random(100, 500), random(50, 80)))
        
    
        
