x = 575 # Startposition des Herzes
y = 525 # Startposition des Herzes
Keys = []

h = 0 #Healhtbar Minderung Rechteck grösse
w_heart = 32
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
    ####################
    noFill()
    strokeWeight(1)
    
    stroke(0, 255, 0)
    rect(x+13, y+10, w_heart, h_heart+5)
    
    stroke(255, 0, 0)
    rect(bx, by, bw, bh)
    ####################
    # Calculate edges of the heart
    heart_left = x + 13
    heart_right = x + w_heart 
    heart_top = y+10
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
    #if h >= 200:
     #   background(0)
      #  exit()



#Unterprogramm zur Erstellung der Texte in den Boxen
def Button(x, y, w, h, tx): 
    stroke(violett) #färbt die Knöpfe violett
    strokeWeight(4)
    fill(0)
    rect(x, y, w, h)
    
    fill(violett) #färbt den Text violett
    textAlign(CENTER, CENTER) #richtet den Text in der Mitte aus
    textFont(ButtonFont, 60)
    text(tx, x+w/2, y+h/2) #berechnet die Mitte der Box für den Text


#Zeichnet den "StartScreen", indem es die Kampfbox, die Knöpfe und die Healthbar reinzeichnet 
def FightInterface():
    image(sans, 500, 38) #Bild von Sans 
    
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
    
    
    
   
a = 100 #x position des ersten Knochen
b = 1075  #x position des zweiten Knochen
v = 5 #Geschwindigkeit der BEwegung
Ybones = 400 #X Position der Knochen
#Die erste Attacke die es im Spiel gibt. 
def Attacke1():
    global a, b, Pos_xb, Pos_yb, v, Ybones
    Pos_xb = 650 #X-Position der Sprechblase
    Pos_yb = 0 #Y-Position der Sprechblase
    textFont(speech, 25)
    textAlign(LEFT, TOP) #Positioniert den Text oben links
    
    #Sobald sich die Zeit innerhalb des Intervalls zwischen 1 und 5 Sekunden 
    #befindet, zeichnet er die erste Sprechblase mit dem Text
    if millis() >= 1000 and millis() < 5000: 
        image(bubble, Pos_xb, Pos_yb, 350, 192)
        text("Greetings child. I see you're lost. Want me to teleport you to your home with magic?", 
             int(Pos_xb+125), int(Pos_yb+20), 200, 250)
        
    #Das gleiche wie beim ersten Intervall aber zwischen 5 und 7 Sekunden.
    #Dabei wird ein neues Bild von Sans mit geschlossenen Augen und eine neue Sprechblase mit neuem Text gezeichnet
    elif millis() >= 5000 and millis() < 7000:
            image(sans_closed, 500, 38)
            image(bubble, Pos_xb, Pos_yb, 350, 192)
            text("I guess not today", 
                 int(Pos_xb+125), int(Pos_yb+20), 200, 250)
    #Sobald die Zeit über oder gleich 7.5 Sekunden ist, beginnt die erste Attacke mit 2 Knochen.
    #Die Knochen bewegen sich von den Seitenrändern der Kampfbox zu der anderen Seite und prallen
    #beim Erreichen des Randes wieder ab. 
    elif millis() >= 7500 and millis() < 13800:
        image(bone_vert, a, Ybones, 20, 250)
        image(bone_vert, b, Ybones, 20, 250)
        a = a + v
        b = b - v
        checkCollision(a, Ybones, 20, 250)
        checkCollision(b, Ybones, 20, 250)
        if a >= 1050:
            v = -v
            Ybones = Ybones + 40
            
PosWave = -3000
Vwave = 7
def Attacke2():
    global PosWave, PosHitboxY, V
    Pos_xb = 650 #X-Position der Sprechblase
    Pos_yb = 0 #Y-Position der Sprechblase
    textFont(speech, 25)
    textAlign(LEFT, TOP) #Positioniert den Text oben links
    
    #Sobald das Zeitintervall zwischen 14 und 17 Sekunden liegt, wird eine Sprechblase gezeichnet
    if millis() >= 14000 and millis() < 17000:
        image(bubble, Pos_xb, Pos_yb, 350, 192)
        text("Not bad. Let's increase the difficulty", 
             Pos_xb+125, Pos_yb+20, 200, 250)
        
    #Sobald das Zeitintervall zwischen 18 und 28 Sekunden liegt, 
    #kommt das Bild mit Knochen die wie eine Welle positioniert sind
    elif millis() >= 18000 and millis() < 38000:
        image(sans_purple, 500, 38) 
        image(bone_wave, PosWave, 400) 
        PosWave = PosWave + Vwave
        #Die Schleife zeichnet die Hitbox für die welligen Knochen mithilfe einer Sinusfunktion
        for i in range(-100, 2850, 30):
            PosY = 600 + sin(i*0.00495) * 50
            checkCollision(i+PosWave+120, PosY, 10, 50)
            checkCollision(i+PosWave+120, PosY-150, 10, 50)
            
        if PosWave >= 1100:
            Vwave = -Vwave
        
        
def setup():
    global ButtonFont, violett, sans, heart, bone_vert, bubble, backGround, sans_closed, speech, bone_wave, sans_purple
    size(1200, 850)
    pixelDensity(1) #Diese Funktion ist für das rendering der Bilder da. Sorgt auch für flüssiges Gameplay
    
    violett =  color(127, 0, 255) #weist der Variable "violet" die Farbe violett zu
    ButtonFont=loadFont("ButtonsFont.vlw") #Font für den Text
    speech = loadFont("speech.vlw") #Font für die Sprechblase
    
    bone_vert = loadImage("bone_vertical.png") #vertikaler Knochen
    bone_horizontal = loadImage("bone_horizontal.png") #horizontaler Knochen
    bone_wave = loadImage("bone_wave.png") #wellige Reihe an Knochen
    
    sans = loadImage("sans.png") #normaler Sans
    sans_clock = loadImage("sans_clock.png") #Sans mit der Uhr als Auge
    sans_death = loadImage("sans_death.gif") #GIF des sterbenden Sans
    sans_closed = loadImage("sans_eyes_closed.png") #Sans mit geschlossenen Augen
    sans_purple = loadImage("sans_purple_eyes.png") #Sans mit violetten Augen
    
    backGround = loadImage("galaxy.png") #linker Teil des Hintergrund
    heart = loadImage("heart.png") #Bild des Herzes
    bubble = loadImage("bubble.png") #Bild einer Sprechblase
    
    



def draw():
    global y, x, h
    image(backGround, 0, 0) #Galaxy Hintergrund
    FightInterface()
    
    stroke(violett)
    strokeWeight(8) 
    fill(0)
    rect(100, 400, 1000, 300) #Kampfbox, in der sich das Herz bewegt
    
    image(heart, x, y) #Bild vom Herz, das sich bewegt
    Attacke1()
    Attacke2()
    
    
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
    
          
    
