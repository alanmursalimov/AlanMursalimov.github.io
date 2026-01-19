x = 575 # Startposition des Herzes
y = 525 # Startposition des Herzes
Keys = []

h = 0 #Healhtbar Minderung Rechteck grösse
w_heart = 45 
h_heart = 30

Aussagen = ""
#Die Funktion "checkCollision", für das ganze Herz, wurde von Gemini 3 Pro geschrieben.
#Es berechnet die Ecken des Herzes und der Knochen. Danach schaut es in jedem Frame nach ob sich diese Werte überschneiden. 
#Wenn dies stimmt, wächst das rote rechteck
def checkCollision(bx, by, bw, bh):
    """
    bx, by = bone x and y position
    bw, bh = bone width and height
    """
    global x, y, h
    
    # Calculate edges of the heart
    heart_left = x
    heart_right = x + w_heart 
    heart_top = y+5
    heart_bottom = y + h_heart
    
    # Calculate edges of the bone
    bone_left = bx
    bone_right = bx + bw
    bone_top = by
    bone_bottom = by + bh
    
    # Check for Overlap
    if (heart_right > bone_left and 
        heart_left < bone_right and 
        heart_bottom > bone_top and 
        heart_top < bone_bottom):
        
        # If all are true, they are touching
        h = h + 1 # Increase damage



#Unterprogramm zut Erstellung der Texte in den Boxen
def Button(x, y, w, h, tx): 
    stroke(violett) #färbt die Knöpfe violett
    strokeWeight(4)
    fill(0)
    rect(x, y, w, h)
    
    fill(violett) #färbt den Text violett
    textAlign(CENTER, CENTER) #richtet den Text in der Mitte aus
    text(tx, x+w/2, y+h/2) #berechnet die Mitte der Box für den Text


#Zeichnet den "StartScreen", indem es die Kampfbox, die Knöpfe und die Healthbar reinzeichnet 
def FightInterface():
    image(sans, 500, 38) #Bild von Sans #######unfinished
    
    fill(255, 255, 0)
    strokeWeight(4)
    rect(1130, 450, 30, 200) #Healthbar
    
    fill(255, 0, 0)
    noStroke()
    rect(1132, 452, 27, h) #Rechteck für die Minderung des Healthbars

    Button(100, 730, 220, 80, "Fight") #"Fight"-Knopf
    Button(360, 730, 220, 80, "Act") #"Act"-Knopf
    Button(620, 730, 220, 80, "Items") #Items"-Knopf
    Button(880, 730, 220, 80, "Mercy") #"Mercy"-Knopf
    
    
    
   
    
a = 100
b = 1075 

#Die erste Attacke die es im Spiel gibt. 
def Attacke1():
    global a, b, Pos_xb, Pos_yb, Aussagen
    Pos_xb = 650
    Pos_yb = 0
    Aussagen = "Greetings child. I see you're lost. Want me to teleport you to your home with magic?"
    textFont(ButtonFont, 25)
    textAlign(LEFT, TOP)
    if millis() >= 1000:
        image(bubble, Pos_xb, Pos_yb, 350, 192)
        text(Aussagen, Pos_xb+125, Pos_yb+20, 200, 250)
        if millis() >= 5000:
            Aussagen = "I guess not today"
            text(Aussagen, Pos_xb+125, Pos_yb+20, 200, 250)
    
    if millis() >= 10000:
        image(bone_vert, a, 400, 20, 250)
        image(bone_vert, b, 400, 20, 250)
        a = a + 3
        b = b - 3
        checkCollision(a, 400, 20, 250)
        checkCollision(b, 400, 20, 250)
        if a >= 1075:
            a = 2000
        if b <= 100:
            b = -2000
    
        
        
def setup():
    global ButtonFont, violett, sans, heart, bone_vert, bubble, backGround
    size(1200, 850)
    pixelDensity(1)
    violett =  color(127, 0, 255) #weist der Variable "violet" die Farbe violett zu
    ButtonFont=loadFont("ButtonsFont.vlw") #Font für den Text
    textFont(ButtonFont, 60)
    frameRate(90)
    
    bone_vert = loadImage("bone_vertical.png")
   # bone_horizontal = loadImage("bone_horizontal.png")
    
    sans = loadImage("sans.png") #normaler Sans
   # sans_clock = loadImage("sans_clock.png") #Sans mit der Uhr als Auge
   # sans_death = loadImage("sans_death.gif") #GIF des sterbenden Sans
   # sans_closed = loadImage("sans_eyes_closed.png") 
   # sans_purple = loadImage("sans_purple_eyes.png") 
    
    backGround = loadImage("galaxy.png") #linker Teil des Hintergrund
    heart = loadImage("heart.png") #Bild des Herzes
    bubble = loadImage("bubble.png") 
    
   
    #FightInterface()



def draw():
    global y, x, h
    image(backGround, 0, 0) #Galaxy Hintergrund
    FightInterface()
    
    stroke(violett)
    strokeWeight(8) 
    fill(0)
    rect(100, 400, 1000, 300) #Kampfbox, in der sich das Herz bewegt
    
   # fill(255, 0, 0)
   # noStroke()
   # rect(1132, 452, 27, h) #Rechteck für die Minderung des Healthbars
    
    
    image(heart, x, y) #Bild vom Herz, das sich bewegt
    Attacke1()
    
    
    h = constrain(h, 0, 200) #Limitiert das Rechteck, das den HP runterbringt
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
    
          
    
