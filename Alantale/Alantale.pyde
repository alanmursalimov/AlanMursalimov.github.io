x = 575 #x-coordinate of the heart's starting position (will be changed by moving the heart)
y = 525 #y-coordinate of the heart's starting position (will be changed by moving the heart) 
Keys = []

height_healthbar = 0 #original height of the red rectangle which is used to display the player's health 
w_heart = 32
h_heart = 30
def checkCollision(bx, by, bw, bh):
    """
    the function "checkCollision" was written by Gemini 3 Pro 
    It calculates the corners of the heart and bones. After thet it checks for overlapping values every frame. 
    if they overlap, the red rectangle grows
    """
    global x, y, height_healthbar
    ####################
    noFill()
    strokeWeight(1)
    
    stroke(0, 255, 0)
    rect(x+13, y+10, w_heart, h_heart+5)
    
    stroke(255, 0, 0)
    rect(bx, by, bw, bh)
    ####################
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




#procedure for creating the text in the boxes
def Button(x, y, w, h, tx):
    """
    subfuction for creating the decorative boxes, where values are used for the
    variables in the "Fightinetrface()" subfunction.
    """ 
    stroke(violett) #colors the buttons purple
    strokeWeight(4)
    fill(0)
    rect(x, y, w, h)
    
    fill(violett) #colors the text purple
    textAlign(CENTER, CENTER) #centers the text
    textFont(ButtonFont, 60)
    text(tx, x+w/2, y+h/2) #calculates the middle of the boxes for the text

#Draws the "Start Screen" by adding the combat box, buttons, and health bar. 
def FightInterface():
    """
    Draw the fighting box in which the heart moves and the decorative 
    buttons.
    """
    image(sans, 500, 38) #image of Sans 
    
    fill(255, 255, 0)
    strokeWeight(4)
    rect(1130, 450, 30, 200) #healthbar
    
    fill(255, 0, 0)
    noStroke()
    rect(1132, 452, 27, height_healthbar) #rectangle to show healthloss

    Button(100, 730, 220, 80, "Fight") #"Fight"-Button
    Button(360, 730, 220, 80, "Act") #"Act"-Button
    Button(620, 730, 220, 80, "Items") #Items"-Button
    Button(880, 730, 220, 80, "Mercy") #"Mercy"-Button
    
    
    
   
Xbone1 = 100 #x position of the first bone
Xbone2 = 1075  #x position of the second bone
Vbones = 5 #bonespeed
Ybones = 400 #y coordinate of the bones
#Sans' first attack 
def Attacke1():
    """
    2 bones on each side move in the opposite direction. In doing so, 
    you must move the heart either all the way up or all the way down to avoid damage
    """
    global Xbone1, Xbone2, Pos_xb, Pos_yb, Vbones, Ybones
    Pos_xb = 650 #x-position of the speech bubble
    Pos_yb = 0 #y-position of the speech bubble
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
    """
    As soon as the time is over or equal to 7.5 seconds, the first attack begins with 2 bones.
    The bones move from the side edges of the battle box to the other side and bounce back
    when they reach the edge. 
    """
    elif millis() >= 7500 and millis() < 13800:
        image(bone_vert, Xbone1, Ybones, 20, 250)
        image(bone_vert, Xbone2, Ybones, 20, 250)
        Xbone1 = Xbone1 + Vbones
        Xbone2 = Xbone2 - Vbones
        checkCollision(Xbone1, Ybones, 20, 250)
        checkCollision(Xbone2, Ybones, 20, 250)
        if Xbone1 >= 1050:
            Vbones = -Vbones
            Ybones = Ybones + 40
            
PosWave = -3000
Vwave = 7
def Attacke2():
    """
    An image of bones of various sizes with a wavy hitbox 
    (created with a sine function) moves to the right. The heart must 
    move up and down in a small space. Then
    the hitbox moves to the left, creating the effect of 
    rewinding time.
    """
    global PosWave, PosHitboxY, Vwave
    Pos_xb = 650 #x-position der Sprechblase
    Pos_yb = 0 #Y-Position der Sprechblase
    textFont(speech, 25)
    textAlign(LEFT, TOP) #Positioniert den Text oben links
    
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
            
        
Ybone_horizontal = False
Ybone_Pos = 0
Xbone_Pos = 1000
FrameCounter = 0
side = 0
def Attacke3():
    """
    Shoots horizontal bones from the sides at heart level to the left or right.
    """
    global Ybone_horizontal, Ybone_Pos, Xbone_Pos, FrameCounter, side
    if millis() >= 38000 and millis() < 100000:
            if Ybone_horizontal == False:
                Ybone_Pos = y+15
                Ybone_horizontal = True
                Xbone_Pos = 1000
            #image(bone_horizontal, Xbone_Pos, Ybone_Pos, 250, 20)
            #checkCollision(Xbone_Pos, Ybone_Pos, 250, 20)
            Xbone_Pos = Xbone_Pos - 10
            
            FrameCounter =  FrameCounter + 1 #Adds the value 1 to the variable "FrameCounter" for each frame.
            if  FrameCounter >= 50:
                side = round(random(3))
                FrameCounter = 0
            if side == 0:
                image(bone_horizontal, side+100-Xbone_Pos, Ybone_Pos, 250, 20)
                Ybone_horizontal = True
                Ybone_horizontal = True
            elif side == 1:
                image(bone_horizontal, side*1000+Xbone_Pos, Ybone_Pos, 250, 20)
                Ybone_horizontal = True
                Ybone_horizontal = True
    elif millis() >= 40000:
        Ybone_horizontal = False
    
        
        
def setup():
    global ButtonFont, violett, sans, heart, bone_vert, bubble, backGround, sans_closed, speech, bone_wave, sans_purple, sans_clock, bone_horizontal
    size(1200, 850)
    pixelDensity(1) #This function is used for rendering images. It also ensures smooth gameplay.
    
    violett =  color(127, 0, 255) #assigns the color purple to the variable "violet"
    ButtonFont=loadFont("ButtonsFont.vlw") #font for the text
    speech = loadFont("speech.vlw") #font for the speech bubble
    
    bone_vert = loadImage("bone_vertical.png") #vertical bone
    bone_horizontal = loadImage("bone_horizontal.png") #horizontal bone
    bone_wave = loadImage("bone_wave.png") #bone wave
    
    sans = loadImage("sans.png") #normal sans
    sans_clock = loadImage("sans_clock.png") #sans with a watch as an eye
    sans_death = loadImage("sans_death.gif") #GIF of the dying sans
    sans_closed = loadImage("sans_eyes_closed.png") #sans with his eyes closed
    sans_purple = loadImage("sans_purple_eyes.png") #sans purple eyes
    
    backGround = loadImage("galaxy.png") #image of the background
    heart = loadImage("heart.png") #image of the heart
    bubble = loadImage("bubble.png") #image of the speech bubble
    
    


death_point = 0
def draw():
    global y, x, height_healthbar, death_point
    image(backGround, 0, 0) #Galaxy Hintergrund
    FightInterface()
    
    stroke(violett)
    strokeWeight(8) 
    fill(0)
    rect(100, 400, 1000, 300) #Kampfbox, in der sich das Herz bewegt
    
    image(heart, x, y) #Bild vom Herz, das sich bewegt
    if height_healthbar <= 200:
        Attacke1()
        Attacke2()
        Attacke3()
        
    #########################    
    if height_healthbar >= 200:
        if death_point == 0:
            death_point = millis()
        elif millis() - death_point > 1000:
            background(0)
            image(heart, x, y)
        elif millis() - death_point > 2000:
            background(0)
            image(loadImage("broken_heart.png"),x, y)
            exit()
       ################################noch nicht fertig!!! 

    height_healthbar = constrain(height_healthbar, 0, 200) #Limitiert das Rechteck, das den HP runterbringt
    x = constrain(x, 97, 1043) #Limitiert die Bewegungen des Herzes auf die Kampfbox
    y = constrain(y, 397, 643) #Limitiert die Bewegungen des Herzes auf die Kampfbox
    #Bewegung mit WASD Tasten
    if UP in Keys: 
        y = y-5
    if DOWN in Keys:
        y = y+5
    if LEFT in Keys:
        x = x-5
    if RIGHT in Keys:
        x = x+5


#Wenn eine Pfeiltaste gedrückt wird speichert es diesen Wert (z.B. "UP") in der Liste "Keys"
def keyPressed():
    if key == CODED:
        Keys.append(keyCode)

#Wenn die Pfeiltaste losgelassen wird dann wird der Wert aus der Liste gelöscht. 
#Das tut er ständig damit maximal 2 Werte in der Liste sein können.
def keyReleased():
    if key == CODED:
        while keyCode in Keys:
            Keys.remove(keyCode)
    
          
    
