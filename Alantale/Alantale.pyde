"""
==================================================================
 Filename: Alantale.pyde
 Description: Undertale-inspired boss fight game. The player controls
 a heart with the arrow keys and must dodge Sans's attcaks with bones.
 Copyright: GPL
 Created: 24.03.2026
 Author: Alan Mursalimov & Nevin Rohner
==================================================================
"""
x = 575 #x-coordinate of the heart's starting position (will be changed by moving the heart)
y = 525 #y-coordinate of the heart's starting position (will be changed by moving the heart) 
Keys = [] #list for determining in what direction the heart should move
Pos_xb = 650 #X-position of the speech bubble
Pos_yb = 0 #Y-position of the speech bubble
violett =  color(127, 0, 255) #assigns the color purple to the variable "violet"

height_healthbar = 0 #tracks the current damage dealt; grows as the player takes hits
w_heart = 32 #The width of the heart
h_heart = 30 #The height of the heart
def checkCollision(bx, by, bw, bh):
    """
    The function "checkCollision" was written by Gemini 3 Pro 
    It calculates the corners of the heart and bones. After that, it checks for overlapping values every frame.
    If they overlap, the health bar grows to indicate damage.
    """
    global x, y, height_healthbar

    #calculates edges of the heart
    heart_left = x + 13
    heart_right = x + w_heart 
    heart_top = y+10
    heart_bottom = y + h_heart
    
    #calculates edges of the bone
    bone_left = bx
    bone_right = bx + bw
    bone_top = by
    bone_bottom = by + bh
    
    #checks for overlap
    if (heart_right > bone_left and 
        heart_left < bone_right and 
        heart_bottom > bone_top and 
        heart_top < bone_bottom):
        
        #if everything is true they are touching
        height_healthbar = height_healthbar + 1 #increases damage





def Button(x, y, w, h, tx):
    """
    subfunction for creating the decorative boxes; values are passed in from
    the "FightInterface()" function.
    """ 
    stroke(violett) #colors the buttons purple
    strokeWeight(4)
    fill(0)
    rect(x, y, w, h)
    
    fill(violett) #colors the text purple
    textAlign(CENTER, CENTER) #centers the text
    textFont(ButtonFont, 60)
    text(tx, x+w/2, y+h/2) #calculates the middle of the boxes for the text

def FightInterface():
    """
    Draws the fight UI each frame: Sans's image, the health bar, and the four action buttons.
    The battle box itself is drawn in draw().
    """
    image(sans, 500, 38) #image of Sans 
    
    fill(255, 255, 0)
    strokeWeight(4)
    rect(1130, 450, 30, 200) #healthbar
    
    fill(255, 0, 0)
    noStroke()
    rect(1132, 452, 27, height_healthbar) #rectangle to show healthloss

    Button(100, 730, 220, 80, "Fight") # "Fight" button
    Button(360, 730, 220, 80, "Act") # "Act" button
    Button(620, 730, 220, 80, "Items") # "Items" button
    Button(880, 730, 220, 80, "Mercy") # "Mercy" button
    
    
    
   
Xbone1 = 100 #x position of the first bone
Xbone2 = 1075  #x position of the second bone
Vbones = 5 #bonespeed
Ybones = 400 #y coordinate of the bones
def Attack1():
    """
    2 bones on each side move in the opposite direction. To avoid damage the player needs
    to move all the way up or down.
    """
    global Xbone1, Xbone2, Pos_xb, Pos_yb, Vbones, Ybones
    textFont(speech, 25)
    textAlign(LEFT, TOP) #positions the text in the top left

    #As soon as the time is between 1 and 5 seconds, 
    #it draws the first speech bubble with the text
    if millis() >= 1000 and millis() < 5000: 
        image(bubble, Pos_xb, Pos_yb, 350, 192)
        text("Greetings child. I see you're lost. Want me to teleport you to your home with magic?", 
             int(Pos_xb+125), int(Pos_yb+20), 200, 250)
        
    #Same as the first interval, but between 5 and 7 seconds.
    #A new image of Sans with closed eyes and a new speech bubble with new text is drawn.
    elif millis() >= 5000 and millis() < 7000:
            image(sans_closed, 500, 38)
            image(bubble, Pos_xb, Pos_yb, 350, 192)
            text("I guess not today", 
                 int(Pos_xb+125), int(Pos_yb+20), 200, 250)

#As soon as the time is over or equal to 7.5 seconds, the first attack begins with 2 bones.
#The bones move from the side edges of the battle box to the other side and bounce back
#when they reach the edge. 
    elif millis() >= 7500 and millis() < 13800:
        image(bone_vert, Xbone1, Ybones, 20, 250)
        image(bone_vert, Xbone2, Ybones, 20, 250)
        checkCollision(Xbone1, Ybones, 20, 250)
        checkCollision(Xbone2, Ybones, 20, 250)
        Xbone1 = Xbone1 + Vbones
        Xbone2 = Xbone2 - Vbones

        if Xbone1 >= 1050:
            Vbones = -Vbones
            Ybones = Ybones + 40
    
            
PosWave = -3000 #Start X position of the picture (wave of bones)
Vwave = 7 #The speed with which the picture moves
def Attack2():
    """
    An image of bones of various sizes with a wavy hitbox 
    (created with a sine function) moves to the right. The heart must 
    move up and down in a small space. Then
    the hitbox moves to the left, creating the effect of 
    rewinding time.
    """
    global PosWave, PosHitboxY, Vwave
    textFont(speech, 25)
    textAlign(LEFT, TOP) #positions the text in the top left
    
    #As soon as the time interval is between 14 and 17 seconds, a speech bubble is drawn.
    if millis() >= 14000 and millis() < 17000:
        image(bubble, Pos_xb, Pos_yb, 350, 192)
        text("Not bad. Let's increase the difficulty", 
             Pos_xb+125, Pos_yb+20, 200, 250)
        
    #As soon as the time interval is between 18 and 28 seconds, 
    #the image with bones positioned like a wave appears.
    elif millis() >= 18000 and millis() < 38000:
        if millis() >= 18000 and millis() < 28000:
            image(sans_purple, 500, 38) 
            PosWave = PosWave + Vwave
            
        elif millis() >= 28000 and millis() < 38000:
            image(sans_clock, 500, 38)
            PosWave = PosWave - Vwave
        
        image(bone_wave, PosWave, 400) 
        
        #The loop draws the hitbox for the wavy bones using a sine function.
        for i in range(-100, 2850, 30):
            PosY = 600 + sin(i*0.00495) * 50
            checkCollision(i+PosWave+120, PosY, 10, 50)
            checkCollision(i+PosWave+120, PosY-150, 10, 50)
            

Ybone_horizontal = False #True while a bone is in flight; resets to False when the bone leaves the screen
Ybone_Pos = 0 #Y-start-coordinate of the bone
Xbone_Pos = 1000 #x-coordinate of the bone (resets each time a new bone spawns)
side = 0 #variable for determining from which side the bone is flying from
def Attack3():
    """
    Shoots horizontal bones from the sides at heart level to the left or right.
    """
    global Ybone_horizontal, Ybone_Pos, Xbone_Pos, FrameCounter, side
    if millis() >= 38000 and millis() < 53000:
            if Xbone_Pos >= 1300:
                Ybone_horizontal = False
                
            if Xbone_Pos >= -250 and Xbone_Pos <= 1200:
                Ybone_horizontal = True
                
            if Ybone_horizontal == False:
                Ybone_Pos = y+15
                Xbone_Pos = 0
                side = int(random(0, 2))
                Ybone_horizontal = True
            
            Xbone_Pos = Xbone_Pos + 15    
            
            if side == 0:
                image(bone_horizontal, side+Xbone_Pos, Ybone_Pos, 250, 20)
                checkCollision(side+Xbone_Pos, Ybone_Pos, 250, 20)
            else:
                image(bone_horizontal, side*1200-Xbone_Pos, Ybone_Pos, 250, 20)
                checkCollision(side*1200-Xbone_Pos, Ybone_Pos, 250, 20)
                
    else:
        Ybone_horizontal = False
    
    
    
    
rotate_angle = 0 #current rotation angle; incremented each frame to spin the bones
def Attack4():
    """
    Sans recites a poem, then 3 bones appear and spin around their own center.
    """
    global rotate_angle
    textFont(speech, 25)
    textAlign(LEFT, TOP)
    
    #Sans' poem
    if millis() >= 52000 and millis() < 57000:
            image(bubble, Pos_xb, Pos_yb, 350, 192)
            text("Roses are red, violets are blue", 
                 Pos_xb+125, Pos_yb+20, 200, 250)
    if millis() >= 57000 and millis() < 62000:
        image(bubble, Pos_xb, Pos_yb, 350, 192)
        text("Everyone is  gone, and I am stuck here with you.", 
                 Pos_xb+125, Pos_yb+20, 200, 250)
    if millis() >= 62000 and millis() < 67000:
        image(bubble, Pos_xb, Pos_yb, 350, 192)
        text("I am tired of waiting, so lets end this fast", 
                 Pos_xb+125, Pos_yb+20, 200, 250)
    if millis() >= 67000 and millis() < 72000:
        image(bubble, Pos_xb, Pos_yb, 350, 192)
        text("Cause you are the one leaving, and I am the one staying.", 
                 Pos_xb+125, Pos_yb+20, 200, 250)
        
    #The attack with the 3 bones
    if millis() >= 72000 and millis() < 90000:
        rotate_angle = rotate_angle + 1 #increases the rotation angle by 1 per frame

        for i in 250, 605, 920: #goes though each bone one by one
            pushMatrix() #saves the current coordinate system
            translate(i, 555) #moves the origin to the center of the bone
            rotate(rotate_angle/40.) #rotates the bones around their center
            image(bone_horizontal, -200, -10, 400, 20)
            popMatrix() #resets the coordinate system back to normal

            #loop for creating multiple small hitboxes which orbit the middle point of each bone
            for r in range(-200, 200, 20):
                hitbox_x = i + r * cos(rotate_angle/40.) #formula for orbiting a point on the X axis
                hitbox_y = 555 + r * sin(rotate_angle/40.) #formula for orbiting a point on the Y axis
                checkCollision(hitbox_x - 10, hitbox_y - 10, 20, 20)
                
        
End_pos_Y = 0 #y-coordinate of the bone used in the final attack; increases each frame to move it downward
def Attack5():
    """
    Sans gets tired and launches one final bone from the top at the heart.
    The bone follows the heart on the x-axis. The player needs to have enough
    health to survive the attack.
    """
    global End_pos_Y
    textFont(speech, 25)
    textAlign(LEFT, TOP)
    
    #Sans's dialogue lines, displayed in speech bubbles
    if millis() >= 90000 and millis() < 150000:
        image(sans_dizzy, 500, 38)
        if millis() >= 100000 and millis() < 105000:
            image(bubble, Pos_xb, Pos_yb, 350, 192)
            text("*Huff. Puff.* I'm getting dizzy.", 
                    Pos_xb+125, Pos_yb+20, 200, 250)
        elif millis() >= 105000 and millis() < 110000:
            image(bubble, Pos_xb, Pos_yb, 350, 192)
            text("You're strong. *Huff. Puff.* ", 
                    Pos_xb+125, Pos_yb+20, 200, 250)
        elif millis() >= 115000 and millis() < 120000:
            image(bubble, Pos_xb, Pos_yb, 350, 192)
            text("Die!", 
                    Pos_xb+125, Pos_yb+20, 200, 250)
            #Sans launches a bone from the top at the heart
            End_pos_Y = End_pos_Y + 10 #Y-Axis movement of the bone
            image(bone_vert, x, End_pos_Y, 20, 280)
            checkCollision(x, End_pos_Y, 20, 280)        

        #Shows the different stages of the dying sans
        elif millis() >= 125000 and millis() < 127000: 
            image(sans_death2, 500, 38)
        elif millis() >= 127000 and millis() < 129000:
            image(sans_death3, 500, 38)
        elif millis() >= 129000 and millis() < 131000:
            image(sans_death4, 500, 38)
        elif millis() >= 131000:
            image(loadImage("end_screen.png"), 0, 0)
            exit()
            
        
def setup():
    global ButtonFont, sans, heart, bone_vert, bubble, backGround, sans_closed, speech, bone_wave, sans_purple, sans_clock, bone_horizontal, sans_dizzy, sans_death2, sans_death3, sans_death4
    size(1200, 850)
    pixelDensity(1) #forces standard resolution to prevent blurry images on HiDPI (Retina) screens
    
    ButtonFont=loadFont("ButtonsFont.vlw") #font for the text
    speech = loadFont("speech.vlw") #font for the speech bubble
    
    bone_vert = loadImage("bone_vertical.png") #vertical bone
    bone_horizontal = loadImage("bone_horizontal.png") #horizontal bone
    bone_wave = loadImage("bone_wave.png") #bone wave
    
    #all Sans images were based on "Undertale Sans Sprite V5" by "AverageEnthusiastArt", edited by Nevin Rohner
    sans = loadImage("sans.png") #normal sans
    sans_clock = loadImage("sans_clock.png") #sans with a watch as an eye
    sans_dizzy = loadImage("sans_dizzy.png") #Sans death animation, frame 1
    sans_death2 = loadImage("sans_death2.png") #Sans death animation, frame 2
    sans_death3 = loadImage("sans_death3.png") #Sans death animation, frame 3
    sans_death4 = loadImage("sans_death4.png") #Sans death animation, frame 4
    sans_closed = loadImage("sans_eyes_closed.png") #sans with his eyes closed
    sans_purple = loadImage("sans_purple_eyes.png") #sans purple eyes
    
    #the background
    backGround = loadImage("galaxy.png") #image of the background
    heart = loadImage("heart.png") #image of the heart
    bubble = loadImage("bubble.png") #image of the speech bubble
    


death_point = 0 #stores the time when the player died; 0 means the player is still alive
def draw():
    global y, x, height_healthbar, death_point
    image(backGround, 0, 0) #galaxy background
    FightInterface()
    
    stroke(violett)
    strokeWeight(8) 
    fill(0)
    rect(100, 400, 1000, 300) #battle box in which the heart moves
    
    image(heart, x, y) #image of the heart that moves
    #While the red healthbar rectangle is smaller than 200 the Attacks may be drawn
    if height_healthbar <= 200:
        Attack1()
        Attack2()
        Attack3()
        Attack4()
        Attack5()

    #If the red healthbar rectangle is bigger than 200 then it should show the endscreen
    if height_healthbar >= 200: 
        #set the death_point variable to millis so we can subtract it
        if death_point == 0:
            death_point = millis()
        background(0)
        #if less than 1.5 seconds have passed since death, draw the regular heart (frozen in place)
        if millis() - death_point < 1500:
            image(heart, x, y)
        #after 1.5 seconds, switch to the broken heart and exit
        elif millis() - death_point < 2000:
            image(loadImage("broken_heart.png"),x, y)
        elif millis() -death_point < 3000:
            image(loadImage("game_over.png"), 0, 0)
            exit()

    height_healthbar = constrain(height_healthbar, 0, 200) #limits the rectangle size that reduces HP
    x = constrain(x, 97, 1043) #limits the heart's movement to the battle box in x direction
    y = constrain(y, 397, 643) #limits the heart's movement to the battle box in y direction
    #Movement with arrow keys
    if height_healthbar < 200:
        if UP in Keys: 
            y = y-5
        if DOWN in Keys:
            y = y+5
        if LEFT in Keys:
            x = x-5
        if RIGHT in Keys: 
            x = x+5


#When an arrow key is pressed, its value (e.g. "UP") is stored in the "Keys" list
def keyPressed():
    if key == CODED:
        Keys.append(keyCode)

#When an arrow key is released, its value is removed from the list, stopping movement in that direction.
def keyReleased():
    if key == CODED:
        while keyCode in Keys:
            Keys.remove(keyCode)
    
          
    
