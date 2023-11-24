import pygame as game
import random as rand
import RequiredFunctions as rFunc
import RequiredClasses as rCls
#------------------
game.init()
Canvas = game.display.set_mode((500, 500))
game.display.set_caption("Canvas")
#game.display.toggle_fullscreen()
draggingPoint = None


#Points = [POINT([rand.randint(0, 499), rand.randint(0, 499)]) for i in range(5)]
pointtest = rCls.POINT([250, 250], Canvas)
pointtest2 = rCls.POINT([10, 10], Canvas)
Points = [pointtest, pointtest2]
FPS = 144
clock = game.time.Clock()
switch = True
    
while switch:
    events = game.event.get()
    for event in events:
        if event.type == game.QUIT:
            switch = False

    for i in Points:
        rFunc.Dragger(i, events, draggingPoint)
        rFunc.CollisionDetection(Points)
    Canvas.fill((171, 171, 171))
    #game.draw.aalines(Canvas, "green", True, [point.center for point in Points], 1)
    for i in Points:
        i.Draw()
    game.display.update()
    clock.tick(FPS)