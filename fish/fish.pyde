add_library('sound')
x2=511
y2=348
y3=348
move_l=False
speed1=10
speed2=10
flagY = 400
yTrue = True
grillY = 445
dubb = 45
move = False

    

def setup():
    global textvar, img, mama, play, help, table, file, gameplaying, x2, y2, y3, move_l, click1, speed1, speed2, itsher, counter, neg

    size(1000, 1000)
    file = SoundFile(this, "mama.mp3")
    img = loadImage("914.jpg")
    mama = loadImage("mama.png")
    play = loadImage("letscook.png")
    help = loadImage("help.png")
    table = loadImage("table.png")
    itsher = loadImage("mamaimg.png")
    counter = 1
    textvar = 0
    neg = False
    file.play()
    gameplaying = 0
def draw():
    global neg, counter
    if neg == False:
        counter += 1
    else:
        counter -= 1
        if counter == 0:
            neg = False
        
        
    if gameplaying == 0:
        bgtexture(0)
        fishbody(80, 150)
        #you suck maurice
        attribution(250, 900)
        titleimages()
    else:
        background("#FFFFFF")
        fill("#61B5FC")
        rect(0, 0, 4000, 2000)
        fill("#A7D39E")
        rect(0, 500, 4000, 700)
        displayDumpster(560, 448, 200, 140, 511, 348)
        flag()
        riseFlag()
        bbqGrill()
        closeGrill()
        image(itsher, 500- counter, 430 + counter, itsher.width * 2, itsher.height * 2)
        noStroke()
        rect(0, 800, 600, 500)
        textcall()
    
    if counter >= 10:
        neg = True
     
            
def textcall():
    global textvar
    textSize(40)
    fill("#000000")
    if mousePressed:
        textvar += 1
    if textvar == 0:
        text("the name's mama. click the screen to advance", 10, 850, 600, 8000)
    elif textvar == 1:
        text("originally, we wanted this to be a game", 10, 850, 600, 8000)
    elif textvar == 2:
        text("but we ran out of time :(", 10, 850, 600, 8000)
    elif textvar == 3:
        text("so now it's just an interactive scene", 10, 850, 600, 8000)
    elif textvar == 4:
        text("haha", 10, 850, 600, 8000)
    elif textvar == 5:
        text("hahahahahaha...", 10, 850, 600, 8000)
    elif textvar == 6:
        text("hah...", 10, 850, 600, 8000)
    elif textvar == 7:
        text("moving on", 10, 850, 600, 8000)
    elif textvar == 8:
        text("what else? hmm", 10, 850, 600, 8000)
    elif textvar == 9:
        text("ever hear of GitHub?", 10, 850, 600, 8000)
    elif textvar == 10:
        text("it's literally my life", 10, 850, 600, 8000)
    elif textvar == 11:
        text("sometimes mac files screw it up though", 10, 850, 600, 8000)
    elif textvar == 12:
        text("<3 version control", 10, 850, 600, 8000)
    elif textvar == 13:
        text("man, I'm tired", 10, 850, 600, 8000)
def titleimages():
    image(mama, 150, 50, mama.width, mama.height)
    image(play, 250, 700, play.width + 50, play.height + 12)
    if mouseX>=250 and mouseX<= 700 and mouseY >= 700 and mouseY <= 800:
        image(play, 246, 690, play.width + 60, play.height + 22)
        
def bgtexture(posx):
    for x in range(0, 1000, 100):
        for y in range(0, 1000, 100):
            image(table, x, y, table.width, table.height)


def attribution(posx, posy):
    textSize(40)
    fill("#EDA5CD")
    text("by team poputepipikku", posx, posy)
    
    
def fishbody(offsetx, offsety):
    noStroke()
    
    fill("#DEE7FA")
    beginShape()
    vertex(459 + offsetx, 290+ offsety)
    vertex(479+ offsetx, 292+ offsety)
    vertex(492+ offsetx, 312+ offsety)
    vertex(507+ offsetx, 333+ offsety)
    vertex(530+ offsetx, 344+ offsety)
    vertex(555+ offsetx, 350+ offsety)
    vertex(561+ offsetx, 349+ offsety)
    vertex(561+ offsetx, 349+ offsety)
    vertex(566+ offsetx, 357+ offsety)
    vertex(542+ offsetx, 363+ offsety)
    vertex(535+ offsetx, 375+ offsety)
    vertex(522+ offsetx, 394+ offsety)
    vertex(455+ offsetx, 349+ offsety)
    endShape()
    
    
    fill("#484C6C")
    beginShape()
    vertex(463+ offsetx, 291+ offsety)
    vertex(480+ offsetx, 329+ offsety)
    vertex(493+ offsetx, 351+ offsety)
    vertex(517+ offsetx, 375+ offsety)
    vertex(525+ offsetx, 378+ offsety)
    vertex(515+ offsetx, 413+ offsety)
    vertex(505+ offsetx, 423+ offsety)
    vertex(486+ offsetx, 437+ offsety)
    vertex(447+ offsetx, 449+ offsety)
    vertex(447+ offsetx, 295+ offsety)
    endShape()
    
    fill("#484C6C")
    beginShape()
    vertex(479+ offsetx, 291+ offsety)
    vertex(504+ offsetx, 330+ offsety)
    vertex(522+ offsetx, 340+ offsety)
    vertex(536+ offsetx, 347+ offsety)
    vertex(561+ offsetx, 352+ offsety)
    vertex(561+ offsetx, 351+ offsety)
    vertex(565+ offsetx, 355+ offsety)
    vertex(570+ offsetx, 352+ offsety)
    vertex(570+ offsetx, 348+ offsety)
    vertex(565+ offsetx, 345+ offsety)
    vertex(566+ offsetx, 345+ offsety)
    vertex(566+ offsetx, 338+ offsety)
    vertex(571+ offsetx, 334+ offsety)
    vertex(571+ offsetx, 329+ offsety)
    vertex(564+ offsetx, 322+ offsety)
    vertex(529+ offsetx, 308+ offsety)
    vertex(521+ offsetx, 300+ offsety)
    vertex(524+ offsetx, 300+ offsety)
    vertex(516+ offsetx, 296+ offsety)
    vertex(502+ offsetx, 284+ offsety)
    vertex(485+ offsetx, 278+ offsety)
    
    endShape()

    fill("#DEE7FA")
    beginShape()
    vertex(443+ offsetx, 448+ offsety)
    vertex(487+ offsetx, 431+ offsety)
    vertex(497+ offsetx, 411+ offsety)
    vertex(502+ offsetx, 393+ offsety)
    vertex(495+ offsetx, 376+ offsety)
    vertex(487+ offsetx, 372+ offsety)
    vertex(467+ offsetx, 359+ offsety)
    vertex(451+ offsetx, 353+ offsety)    
    endShape()
    
    fill("#867200")
    beginShape()
    vertex(302+ offsetx, 391+ offsety)
    vertex(285+ offsetx, 367+ offsety)
    vertex(279+ offsetx, 346+ offsety)
    vertex(285+ offsetx, 333+ offsety)
    vertex(304+ offsetx, 320+ offsety)
    vertex(315+ offsetx, 314+ offsety)
    vertex(317+ offsetx, 307+ offsety)
    vertex(324+ offsetx, 305+ offsety)
    vertex(325+ offsetx, 294+ offsety)
    vertex(335+ offsetx, 293+ offsety)
    vertex(334+ offsetx, 282+ offsety)
    vertex(346+ offsetx, 271+ offsety)
    vertex(360+ offsetx, 275+ offsety)
    vertex(358+ offsetx, 263+ offsety)
    vertex(374+ offsetx, 269+ offsety)
    vertex(378+ offsetx, 254+ offsety)
    vertex(387+ offsetx, 261+ offsety)
    vertex(385+ offsetx, 246+ offsety)
    vertex(404+ offsetx, 258+ offsety)
    vertex(402+ offsetx, 239+ offsety)
    vertex(421+ offsetx, 254+ offsety)
    vertex(420+ offsetx, 234+ offsety)
    vertex(438+ offsetx, 250+ offsety)
    vertex(439+ offsetx, 226+ offsety)
    vertex(455+ offsetx, 248+ offsety)
    vertex(460+ offsetx, 226+ offsety)
    vertex(474+ offsetx, 254+ offsety)
    vertex(478+ offsetx, 237+ offsety)
    vertex(483+ offsetx, 277+ offsety)
    vertex(430+ offsetx, 452+ offsety)
    vertex(423+ offsetx, 500+ offsety)
    vertex(414+ offsetx, 468+ offsety)
    vertex(403+ offsetx, 506+ offsety)
    vertex(394+ offsetx, 480+ offsety)
    vertex(382+ offsetx, 509+ offsety)
    vertex(380+ offsetx, 491+ offsety)
    vertex(366+ offsetx, 507+ offsety)
    vertex(363+ offsetx, 492+ offsety)
    vertex(350+ offsetx, 502+ offsety)
    vertex(343+ offsetx, 490+ offsety)
    vertex(319+ offsetx, 482+ offsety)
    vertex(317+ offsetx, 467+ offsety)
    vertex(305+ offsetx, 456+ offsety)
    endShape()
        
    
    # FISH
    fill("#FFF300")
    beginShape()
    vertex(318+ offsetx, 423+ offsety)
    vertex(334+ offsetx, 438+ offsety)
    vertex(352+ offsetx, 454+ offsety)
    vertex(372+ offsetx, 458+ offsety)
    vertex(406+ offsetx, 457+ offsety)
    vertex(442+ offsetx, 448+ offsety)
    vertex(461+ offsetx, 424+ offsety)
    vertex(464+ offsetx, 391+ offsety)
    vertex(462+ offsetx, 348+ offsety)
    vertex(461+ offsetx, 330+ offsety)
    vertex(455+ offsetx, 316+ offsety)
    vertex(462+ offsetx, 293+ offsety)
    vertex(478+ offsetx, 289+ offsety)
    vertex(427+ offsetx, 281+ offsety)
    vertex(363+ offsetx, 303+ offsety)
    vertex(354+ offsetx, 312+ offsety)
    vertex(322+ offsetx, 348+ offsety)
    vertex(315+ offsetx, 383+ offsety)
    vertex(301+ offsetx, 392+ offsety)
    vertex(291+ offsetx, 390+ offsety)
    vertex(251+ offsetx, 352+ offsety)
    vertex(239+ offsetx, 352+ offsety)
    vertex(240+ offsetx, 363+ offsety)
    vertex(250+ offsetx, 407+ offsety)
    vertex(250+ offsetx, 455+ offsety)
    vertex(250+ offsetx, 473+ offsety)
    vertex(258+ offsetx, 488+ offsety)
    vertex(280+ offsetx, 462+ offsety)
    vertex(296+ offsetx, 429+ offsety)
    endShape()
    
    fill("#FFFFFF")
    ellipse(497+ offsetx, 314+ offsety, 40, 40)
    
    fill("#000000")
    ellipse(497+ offsetx, 314+ offsety, 20, 20)
    
    
# DUMPSTER DISPLAY

def displayDumpster(x, y, w, h, x1, y1):
    global x2, y2, y3, speed1, speed2, move_l
    rectMode(CENTER)
    fill(20, 90, 50)
    rect(x, y, w, h+110)
    fill(0)
    rect(561, 352, 196, 55)
    # Left Rectangle animation
    if mouseX >= 461 and mouseX <= 559 and mouseY >= 320 and mouseY <= 380:
        if mousePressed:
            speed1-=1
    else:
        speed1=1
    y2+=speed1
    y2=constrain(y2, 308, 348)
    #Right rectangle animation
    if mouseX >= 561 and mouseX <= 662 and mouseY >= 320 and mouseY <= 380:
        if mousePressed:
            speed2-=1
    else:
        speed2=1
    y3+=speed2
    y3=constrain(y3, 308, 348)
    fill(39, 55, 70)
    rect(x1, y2, w-101, h-80) 
    rect(x+51, y3, w-100, h-80) 
    fill(255)
    rect(561, 435, w-100, h-100)
    fill(20, 90, 50)
    textSize(30)
    text('Trash', 520, 448)
    fill(0)
    for i in range(5):
        line(x-99,  y2, x-99, y2-30)
        x+=20
    for i in range(5):
        line(x-85,  y3, x-85, y3-30)
        x+=20
    x=560
    
    #FLAG DISPLAY
def flag():
    rectMode(CORNER)
    noStroke()
    global flagY
#flag post   
    fill(193,193,180)
    rect(85, 25, 10, 575)
#pole string   
    fill(0)
    rect(82, 25,1, 575)
#knob    
    fill(244,238,66)
    ellipse(91, 26, 15, 15)
#flag    
    fill(255)
    rect(95, flagY, 165, 100)
#blue flag lines    
    fill(0,0,100)
    rect(95, flagY, 75, 55)
#red flag lines    
    fill(180,0,0)
    rect(170, flagY, 90, 10)
    rect(170, flagY+ 20, 90, 10)
    rect(170, flagY+ 40, 90, 10)
    rect(95, flagY+ 59, 165, 10)
    rect(95, flagY+ 80, 165, 10)
#stars    
    fill(200)
    ellipse(110, flagY+ 10, 5, 5)
    ellipse(130, flagY+ 10, 5, 5)
    ellipse(150, flagY+ 10, 5, 5)
    ellipse(110, flagY+ 28, 5, 5)
    ellipse(130, flagY + 28, 5, 5)
    ellipse(150, flagY+ 28, 5, 5)
    ellipse(110, flagY+ 45, 5, 5)
    ellipse(130, flagY+ 45, 5, 5)
    ellipse(150, flagY+ 45, 5, 5)
    
def riseFlag():
    global yTrue, flagY
    if yTrue == True:
        flagY-= 1
    if flagY== 50:
        yTrue = False
        
def bbqGrill():
    #grill
    fill(0)
    rect(530, 550, 135, 130)
    rect(520, 550, 15, 150)
    
    #grillWheel
    noFill()
    strokeWeight(1)
    line(666, 660, 666, 700)
    line(635, 680, 685, 680)
    line(680, 665, 650, 695)
    line(650, 665, 680, 695)
    strokeWeight(3)
    ellipse(665, 680, 40, 40)
    
    #grill top
    fill(0)
    beginShape()
    vertex(683, 517)
    vertex(683, 528)
    vertex(710, 504)
    vertex(705, 504)
    vertex(683, 517)
    endShape()
    ellipse(708, 503, 17, 17)
    fill(120)
    noStroke()
    rect(500, 500, 185, 50)
    
    #Burners
    fill(255)
    for burner in range(520, 685, 50):
        stroke(0)
        ellipse(burner, 525, 20, 20)    
        line(burner, 520, burner, 525)
        
    #stroke(0)
    
    
def closeGrill():
    global grillY, move, dubb
    noStroke()
    fill("#460000")
    rect(500, 445, 185, 55, dubb, dubb, 0, 0)
    fill(0)
    rect(500, grillY, 185, 55, 45, 45, 0, 0)
    
    fill(255)
    ellipse(592, grillY + 25, 25, 25)
    
    stroke(170, 2, 2)
    line(592, grillY + 25, 592, grillY + 15)
    stroke(0)
    if grillY == 420:
        dubb=0
    if keyPressed:
        if key == 'U' or key == 'u':
            grillY -= 1
            if grillY <400:
                grillY= 400
            constrain(grillY,445,400)


# test


def mousePressed():
    global gameplaying
    if mouseX>=250 and mouseX<= 700 and mouseY >= 700 and mouseY <= 800:
        print("game play")
        gameplaying += 1
        background("#FFFFFF")
        print(gameplaying)
    