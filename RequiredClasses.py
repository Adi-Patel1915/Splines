import pygame as game

#================================================

class POINT:
    def __init__(self, center : list, Layer):
        self.layer = Layer
        self.center = center
        self.radius = 5
        self.draging = False
        self.offsetxpos = 0
        self.offsetypos = 0
        self.color = "black"
        self.updateHitbox()

    def updateHitbox(self):
        self.hitbox = game.rect.Rect(self.center[0] - self.radius, self.center[1] - self.radius, self.radius*2, self.radius*2) 

    def Draw(self):
        game.draw.circle(self.layer, self.color, tuple(self.center), self.radius)
        #game.draw.rect(Canvas, "light green", self.hitbox, 1)

#================================================

