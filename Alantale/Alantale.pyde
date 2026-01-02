x = 600 #x Position des Herzes
y = 525 #y Position des Herzes
Keys = []
h = 0 #Healhtbar Minderung Rechteck grösse

    
w_heart = 30 
h_heart = 30

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
    heart_top = y
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
        h = h + 2 # Increase damage



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

    Button(100, 730, 220, 80, "Fight") #"Fight"-Knopf
    Button(360, 730, 220, 80, "Act") #"Act"-Knopf
    Button(620, 730, 220, 80, "Items") #Items"-Knopf
    Button(880, 730, 220, 80, "Mercy") #"Mercy"-Knopf
    
    
    
    
    
#Die erste Attacke die es im Spiel gibt. 
def Attacke1():
    for a in range(450, 650, 20):
        image(bone_vert, a, a, 20, 250)
        checkCollision(a, a, 20, 250)
            
    for b in range(850, 900, 20):
        image(bone_vert, 900, b, 20, 250) #######unfinished
        checkCollision(900, b, 20, 250)
    
    
    
def setup():
    global ButtonFont, violett, sans, heart, bone_vert, backGround
    background(0)
    size(1200, 850)
    violett =  color(127, 0, 255) #weist der Variable "violet" die Farbe violett zu
    ButtonFont=loadFont("ButtonsFont.vlw") #Font für den Text
    textFont(ButtonFont, 60)
    frameRate(90)
    
    bone_vert = loadImage("bone_vertical.png")
    sans = loadImage("sans.png")#############Bild von Sans
    backGround = loadImage("galaxy.png") #linker Teil des Hintergrunds
    heart = loadImage("heart.png") #Bild des Herzes
    
    image(backGround, 0, 1) #Galaxy Hintergrund
    
    FightInterface()



def draw():
    global y, x, h
    stroke(violett)
    strokeWeight(8) 
    fill(0)
    rect(100, 400, 1000, 300) #Kampfbox, in der sich das Herz bewegt
    
    fill(255, 0, 0)
    noStroke()
    rect(1132, 452, 27, h) #Rechteck für die Minderung des Healthbars
    
    
    image(heart, x, y) #Bild vom Herz, das sich bewegt
    Attacke1()
    
    
    h = constrain(h, 0, 200)
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
    
          
    
