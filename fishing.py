import pyxel
from camera import Camera
from object import *

class Game:
    def __init__(self):
        pyxel.init(240, 160)
        self.camera = Camera(120, 80)
        pyxel.load("mygame.pyxres")
        self.objects = {}
        self.objects["BouncingBall"] = BouncingBall(50, 50, 10, self.camera)
        self.objects["GravityBall"] = GravityBall(100, 100, 10, self.camera)
        pyxel.run(self.update, self.draw)

    def update(self):
        if pyxel.btn(pyxel.KEY_UP):
            self.camera.move(0, -1)
        if pyxel.btn(pyxel.KEY_DOWN):
            self.camera.move(0, 1)
        if pyxel.btn(pyxel.KEY_LEFT):
            self.camera.move(-1, 0)
        if pyxel.btn(pyxel.KEY_RIGHT):
            self.camera.move(1, 0)
        if pyxel.btnp(pyxel.KEY_Q):
            self.camera.rumble(20, 5)
        for obj in self.objects.values(): obj.update()
        if pyxel.btn(pyxel.KEY_SPACE):
            self.camera.center_to(self.objects["BouncingBall"].x, self.objects["BouncingBall"].y)
        if pyxel.btn(pyxel.KEY_R):
            self.camera.center_to(self.objects["GravityBall"].x, self.objects["GravityBall"].y)
        self.camera.update()
        print(self.camera.get_position())

    def draw(self):
        pyxel.cls(0)
        pyxel.bltm(0, 0, 0, 0, 0, 480, 320)
        pyxel.circ(120, 80, 20, 7)
        for obj in self.objects.values(): obj.draw()


Game()