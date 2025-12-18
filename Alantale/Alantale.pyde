x = 600 #x Position des Herzes
y = 525 #y Position des Herzes
Keys = []

    
    

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
    stroke(violett)
    strokeWeight(8) 
    fill(0)
    rect(100, 400, 1000, 300) #Kampfbox, in der sich das Herz bewegt
    
    image(sans, 500, 38) #Bild von Sans
    image(heart, x, y) #Bild vom Herz, das sich bewegt
    
    
    Button(100, 730, 220, 80, "Fight") #"Fight"-Knopf
    Button(360, 730, 220, 80, "Act") #"Act"-Knopf
    Button(620, 730, 220, 80, "Items") #Items"-Knopf
    Button(880, 730, 220, 80, "Mercy") #"Mercy"-Knopf
    

    
    
    
    
def setup():
    background(0)
    global ButtonFont, violett, sans, heart, bone_vert
    size(1200, 850)
    violett =  color(127, 0, 255) #weist der Variable "violet" die Farbe violett zu
    ButtonFont=loadFont("ButtonsFont.vlw") #Font für den Text
    textFont(ButtonFont, 60)
    
    bone_vert = loadImage("bone_vertical.png")
    
    
    sans = loadImage("sans.png")#Bild von Sans
    
    backGround = loadImage("galaxy.png") #linker Teil des Hintergrunds
    image(backGround, 0, 1)
    
    heart = loadImage("heart.png") #Bild des Herzes
    
    
    #jdnweqnqdnweiondwendnjdowndonwnjdsajnclasnl
    #Änderung jsjsjsjsjjsjsjsjssjjsjsjjs

def draw():
    global y, x
    FightInterface()
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
    
    image(bone_vert, 500, 400)

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
    
                
          
    
