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
    Unterfunktion für die Erstellung der dekorativen Knöpfe, wobei für die
    Variablen Werte in der "Fightinetrface()" Unterfunktion eingesetzt werden.
    """ 
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
    """
    Zeichnet die Kampfbox in der sich das Herz bewegt und die dekorative 
    Knöpfe
    """
    image(sans, 500, 38) #Bild von Sans 
    
    fill(255, 255, 0)
    strokeWeight(4)
    rect(1130, 450, 30, 200) #Healthbar
    
    fill(255, 0, 0)
    noStroke()
    rect(1132, 452, 27, height_healthbar) #Rechteck für die Minderung des Healthbars

    Button(100, 730, 220, 80, "Fight") #"Fight"-Knopf
    Button(360, 730, 220, 80, "Act") #"Act"-Knopf
    Button(620, 730, 220, 80, "Items") #Items"-Knopf
    Button(880, 730, 220, 80, "Mercy") #"Mercy"-Knopf
    
    
    
   
Xbone1 = 100 #x position des ersten Knochen
Xbone2 = 1075  #x position des zweiten Knochen
Vbones = 5 #Geschwindigkeit der Knochen
Ybones = 400 #X Position der Knochen
#Die erste Attacke die es im Spiel gibt. 
def Attacke1():
    """
    2 Knochen von jeder Seite bewegen sich in die Gegenrichtung. Dabei muss 
    man das Herz entweder ganz nach oben oder unten Bewegen um keinen Schaden 
    zu kriegen.
    """
    global Xbone1, Xbone2, Pos_xb, Pos_yb, Vbones, Ybones
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
    Ein Bild von Knochen in verschiedener Grösse mit einer Welligen Hitbox 
    (mit einer Sinusfunktion erstellt) bewegt sich nach rechts. Dabei muss 
    das Herz sich in einem kleinem Raum nach oben und unten bewegen. Danach
    bewegt sich die Hitbox nach links, was den Effekt ergibt dass die Zeit 
    zurückgespult wird.
    """
    global PosWave, PosHitboxY, Vwave
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
        if millis() >= 18000 and millis() < 28000:
            image(sans_purple, 500, 38) 
            PosWave = PosWave + Vwave
            
        elif millis() >= 28000 and millis() < 38000:
            image(sans_clock, 500, 38)
            PosWave = PosWave - Vwave
        
        image(bone_wave, PosWave, 400) 
        
        #Die Schleife zeichnet die Hitbox für die welligen Knochen mithilfe einer Sinusfunktion
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
    Schiesst horizontale Knochen von den Seiten auf der Höhe des Herzes nach links oder rechts
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
            
            FrameCounter =  FrameCounter + 1 #Addiert jedes Frame den Wert 1 zu der Variable "FrameCounter"
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
    
          
    
