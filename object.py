import pyxel
from camera import camera

class Object:

    def __init__(self, x, y, width, height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height

    def update(self):
        pass

    def draw(self):
        pyxel.rect(self.x, self.y, self.width, self.height, 8)


# A ball that bounces around the screen
class BouncingBall(Object):

    def __init__(self, x, y, radius):
        super().__init__(x, y, radius * 2, radius * 2)
        self.radius = radius
        self.vx = 1
        self.vy = 1
        self.width, self.height = radius * 2, radius * 2

    def update(self):
        self.x += self.vx
        self.y += self.vy

        if self.x < 0 or self.x > camera.max_x - self.width:
            self.vx *= -1
        if self.y < 0 or self.y > camera.max_y - self.height:
            self.vy *= -1

    def draw(self):
        pyxel.circ(self.x + self.radius, self.y + self.radius, self.radius, 9)

class GravityBall(Object):

    def __init__(self, x, y, radius):
        super().__init__(x, y, radius * 2, radius * 2)
        self.radius = radius
        self.vy = 0
        self.gravity = 0.5
        self.width, self.height = radius * 2, radius * 2
        self.direction = 1

    def update(self):

        self.x += self.direction

        if self.x < 0 or self.x > camera.max_x - self.width:
            self.direction *= -1
            self.x = max(0, min(self.x, camera.max_x - self.width))

        self.vy += self.gravity
        self.y += self.vy

        if self.y > camera.max_y - self.height:
            # A DECOMMENTER POUR AVOIR UNE BALLE _*LOURDE*_
            # camera.rumble(20, 10)
            self.y = camera.max_y - self.height
            self.vy = -12

    def draw(self):
        pyxel.circ(self.x + self.radius, self.y + self.radius, self.radius, 10)