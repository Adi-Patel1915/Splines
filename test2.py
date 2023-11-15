import pygame as game
import random as rand
game.init()
#Classes-----------





#------------------


def canvasFunc(Width, Height):
    Canvas = game.display.set_mode((Width, Height))
    game.display.set_caption("Canvas")
    game.display.toggle_fullscreen()
    return Canvas
def InitiatorFunc():
    Canvas = canvasFunc(1920, 1200)
    FPS = 144
    clock = game.time.Clock()
    switch = True
    draging = False
    center = [1920/2, 1200/2]
    radius = 10
    fontTest = game.font.Font("SansSerifCollection.ttf", 16)
    textTest = fontTest.render(f"Center: x:{center[0]}  y:{center[1]}", True, (0, 0, 0), None)

    while switch:
        crect = game.rect.Rect(center[0] - radius, center[1] - radius, radius*2, radius*2)
        for event in game.event.get():
            if event.type == game.QUIT:
                switch = False
            elif event.type == game.MOUSEBUTTONDOWN:
                if event.button == 1:
                    xpos, ypos = event.pos
                    if crect.collidepoint(event.pos):
                        draging = True
                        offsetxpos = center[0] - xpos
                        offsetypos = center[1] - ypos
            
            elif event.type == game.MOUSEBUTTONUP:
                if event.button == 1:
                    draging = False
            
            elif event.type == game.MOUSEMOTION:
                if draging:
                    xpos, ypos = event.pos
                    center[0] = xpos + offsetxpos
                    center[1] = ypos + offsetypos
        #Main code goes here:
        Canvas.fill((171, 171, 171))
        game.draw.circle(Canvas, "red", tuple(center), radius)
        #--------------------
        game.display.update()
        clock.tick(FPS)
    return None

InitiatorFunc()