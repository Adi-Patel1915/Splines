import pygame as game
import random as rand

#Classes:--------------
class POINT():
    def __init__(self):
        self.radius = 5
        self.xval = rand.randint(0, 500)
        self.yval = rand.randint(0, 500)
        self.pos = game.Vector2(self.xval, self.yval)
        self.surface = game.display.get_surface()
    
    def drawPoint(self):
        game.draw.circle(self.surface, (0, 0, 0), self.pos, self.radius)
#----------------------

def canvasFunc(Width, Height):
    Canvas = game.display.set_mode((Width, Height))
    game.display.set_caption("Canvas")
    return Canvas

def InitiatorFunc():
    Canvas = canvasFunc(500, 500)
    FPS = 60
    clock = game.time.Clock()
    switch = True

    #Class instances:-----
    point = POINT()
    #---------------------

    while switch:
        for event in game.event.get():
            if event.type == game.QUIT:
                switch = False
    
        #Main code goes here:
        Canvas.fill((171, 171, 171))
        point.drawPoint()
        #--------------------

        game.display.update()
        clock.tick(FPS)
    return None

# def main(Canvas):
#     Canvas.fill((171, 171, 171))
InitiatorFunc()