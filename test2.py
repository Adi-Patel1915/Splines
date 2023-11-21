import pygame as game
import random as rand
game.init()
#Classes-----------
class POINT:
    def __init__(self, center : list):
        self.center = center
        self.radius = 10
        self.draging = False
        self.offsetxpos = 0
        self.offsetypos = 0
        self.color = (16, 12, 8)
        self.updateHitbox()

    def updateHitbox(self):
        self.hitbox = game.rect.Rect(self.center[0] - self.radius, self.center[1] - self.radius, self.radius*2, self.radius*2) 

    def Draw(self):
        game.draw.circle(Canvas, self.color, tuple(self.center), self.radius)
        game.draw.rect(Canvas, "light green", self.hitbox, 1)

#=====================================

#class ALINE():
#------------------


Canvas = game.display.set_mode((500, 500))
game.display.set_caption("Canvas")
#game.display.toggle_fullscreen()
draggingPoint = None

def dragChecker(Point : POINT, Events):
        global draggingPoint
        for event in Events:
            if event.type == game.MOUSEBUTTONDOWN:
                if event.button == 1:
                    mouseXpos, mouseYpos = event.pos
                    if Point.hitbox.collidepoint(event.pos):
                        if draggingPoint is None:
                            draggingPoint = Point
                            Point.draging = True
                        Point.offsetxpos = Point.center[0] - mouseXpos
                        Point.offsetypos = Point.center[1] - mouseYpos
            
            elif event.type == game.MOUSEBUTTONUP:
                if event.button == 1:
                    draggingPoint = None
                    Point.draging = False
            
            elif event.type == game.MOUSEMOTION:
                if Point.draging:
                    mouseXpos, mouseYpos = event.pos
                    Point.center[0] = mouseXpos + Point.offsetxpos
                    Point.center[1] = mouseYpos + Point.offsetypos
                    Point.updateHitbox()

def main():
    # Point_test = POINT([100, 100])
    # Point_test2 = POINT([200, 200])
    # Point_test3 = POINT([300, 300])
    Points = [POINT([rand.randint(0, 499), rand.randint(0, 499)]) for i in range(10)]
    FPS = 144
    clock = game.time.Clock()
    switch = True
    
    while switch:
        events = game.event.get()
        for event in events:
            if event.type == game.QUIT:
                switch = False
        # dragChecker(Point_test, events)
        # dragChecker(Point_test2, events)
        # dragChecker(Point_test3, events)
        dragcheckerlst = [dragChecker(point, events) for point in Points]
        Canvas.fill((171, 171, 171))
        # Point_test.Draw()
        # Point_test2.Draw()
        # Point_test3.Draw()
        draw = [point.Draw() for point in Points]
        game.draw.aalines(Canvas, "green", False, [point.center for point in Points], 1)
        game.display.update()
        clock.tick(FPS)
    return None

main()