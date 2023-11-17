import pygame as game
game.init()
#Classes-----------
class POINT:
    def __init__(self):
        self.x = 0
        self.y = 0
        self.center = [self.x, self.y]
        self.radius = 5
        self.draging = False
        self.updateHitbox()

    def updateHitbox(self):
        self.hitbox = game.rect.Rect(self.center[0] - self.radius, self.center[1] - self.radius, self.radius*2, self.radius*2) 

    def Draw(self):
        game.draw.circle(Canvas, "red", tuple(self.center), self.radius)


#------------------


Canvas = game.display.set_mode((1920, 1200))
game.display.set_caption("Canvas")
game.display.toggle_fullscreen()
def dragChecker(Point : POINT):
        offsetxpos, offsetypos = 0, 0
        for event in game.event.get():
            if event.type == game.MOUSEBUTTONDOWN:
                if event.button == 1:
                    mouseXpos, mouseYpos = event.pos
                    if Point.hitbox.collidepoint(event.pos):
                        Point.draging = True
                        offsetxpos = Point.center[0] - mouseXpos
                        offsetypos = Point.center[1] - mouseYpos
            
            elif event.type == game.MOUSEBUTTONUP:
                if event.button == 1:
                    Point.draging = False
            
            elif event.type == game.MOUSEMOTION:
                if Point.draging:
                    mouseXpos, mouseYpos = event.pos
                    Point.center[0] = mouseXpos + offsetxpos
                    Point.center[1] = mouseYpos + offsetypos
                    Point.updateHitbox()

def main():
    Point_test = POINT()
    FPS = 144
    clock = game.time.Clock()
    switch = True
    
    while switch:
        dragChecker(Point_test)
        Canvas.fill((171, 171, 171))
        Point_test.Draw()
        game.display.update()
        clock.tick(FPS)
    return None

main()