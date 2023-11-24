import pygame as game
import random as rand
game.init()
#Classes-----------
class POINT:
    def __init__(self, center : list):
        self.center = center
        self.radius = 1
        self.draging = False
        self.offsetxpos = 0
        self.offsetypos = 0
        self.color = "black"
        self.updateHitbox()

    def updateHitbox(self):
        self.hitbox = game.rect.Rect(self.center[0] - self.radius, self.center[1] - self.radius, self.radius*2, self.radius*2) 

    def Draw(self):
        game.draw.circle(Canvas, self.color, tuple(self.center), self.radius)
        #game.draw.rect(Canvas, "light green", self.hitbox, 1)

#=====================================

#------------------

Canvas = game.display.set_mode((500, 500))
game.display.set_caption("Canvas")
game.display.toggle_fullscreen()
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


def CollisionDetection(Pointlst : list):
    for point in Pointlst:
        checklist = [i.hitbox for i in Pointlst]
        checklist.remove(point.hitbox)
        if point.hitbox.collidelist(checklist) >= 0:
            point.color = "red"
        else:
            point.color = "black"

def main():
    #Points = [POINT([rand.randint(0, 499), rand.randint(0, 499)]) for i in range(5)]
    Points = []
    xc = 100
    yc = 100
    point1 = POINT([xc, yc])
    point2 = POINT([xc + 300, yc])
    point3 = POINT([xc + 300, yc + 300])
    point4 = POINT([xc, yc + 300])
    Points.append(point1)
    Points.append(point2)
    Points.append(point3)
    Points.append(point4)
    FPS = 144
    clock = game.time.Clock()
    switch = True
    
    while switch:
        events = game.event.get()
        for event in events:
            if event.type == game.QUIT:
                switch = False

        for i in Points:
            dragChecker(i, events)
            CollisionDetection(Points)
        Canvas.fill((171, 171, 171))
        #game.draw.aalines(Canvas, "green", True, [point.center for point in Points], 1)
        for i in Points:
            i.Draw()
        game.display.update()
        clock.tick(FPS)
    return None

main()