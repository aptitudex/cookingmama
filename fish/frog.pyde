#DEEP FRY

import random

def setup():
    size(680, 680)
    background(0)
    stroke(255)
    fill(255)
    textSize(80)
    
def draw():
    if mousePressed:
        
    filter(ERODE)
    filter(POSTERIZE, (random.randrange(2, 255)))