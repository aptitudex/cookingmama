
Pikachu’s cheeks flicker- they are not static!


# ELIZABETH ZIEMER- Finished 3/4/2018
# Pikachu! His cheeks flicker and flash. Official Pokemon artwork is featured in the background, (C) Poke'mon Company/Nintendo/Game Freak/Creatures Inc


import random

def setup():
    size(200, 200)
    global img
    global img1
    img = loadImage("logo.png")  
    img1 = loadImage("group.png")
    background("#2a75bb")
    smooth(8)
    image(img, 20, 50, img.width / 5, img.height / 5)


def draw():
    tint(0, 153, 204, 126)
    image(img1, -30, 138, img.width / 3, img.height / 2.8)
    beginShape()
    strokeWeight(1.2)
    strokeJoin(ROUND)
    fill("#F1CE7C")
    vertex(50, 60)
    vertex(35, 55)
    vertex(32, 55)
    vertex(30, 40)
    vertex(28, 30)
    vertex(24, 25)
    vertex(20, 30)
    vertex(18, 40)
    vertex(17, 55)
    vertex(10, 60)
    vertex(9, 63)
    vertex(6, 69)
    vertex(5, 69)
    vertex(0, 67)
    vertex(0, 150)
    vertex(2, 148)
    vertex(5, 146)
    vertex(8, 144)
    vertex(12, 140)
    vertex(19, 135)
    vertex(22, 130)
    vertex(50, 110)
    vertex(53, 108)
    vertex(60, 90)
    vertex(58, 80)
    vertex(60, 70)
    vertex(62, 65)
    vertex(64, 60)
    vertex(66, 55)
    vertex(70, 50)
    vertex(70, 48)
    vertex(69, 45)
    vertex(60, 48)
    endShape(CLOSE)
    #pikacheeks
    for x in range(0, 10):
        randred = random.randrange(215, 600, 50)
        randblue = random.randrange(82, 200, 2)
        fill(randred, 62, randblue)
        ellipse(15, 80, 10, 10)
        ellipse(45, 100, 10, 10)
    #eyes of my enemies
    fill("#000000")
    ellipse(30, 70, 5, 5)
    ellipse(50, 80, 5, 5)
    fill("#3E3938")
    beginShape()
    vertex(33, 80)
    vertex(40, 83)
    vertex(36, 85)
    endShape(CLOSE)
    beginShape()
    vertex(30, 90)
    vertex(33, 94)
    endShape()
    beginShape()
    vertex(33, 94)
    vertex(34, 90)
    endShape()
    beginShape()
    strokeJoin(ROUND)
    vertex(33, 94)
    vertex(36, 94)
    endShape()





