import pyxel
from camera import camera
from object import *

class Game:
    def __init__(self):
        pyxel.init(240, 160)
        camera.init(120, 80)
        pyxel.load("mygame.pyxres")
        self.objects = {}
        self.objects["BouncingBall"] = BouncingBall(50, 50, 10)
        self.objects["GravityBall"] = GravityBall(100, 100, 10)
        pyxel.run(self.update, self.draw)

    def update(self):
        if pyxel.btn(pyxel.KEY_UP):
            camera.move(0, -1)
        if pyxel.btn(pyxel.KEY_DOWN):
            camera.move(0, 1)
        if pyxel.btn(pyxel.KEY_LEFT):
            camera.move(-1, 0)
        if pyxel.btn(pyxel.KEY_RIGHT):
            camera.move(1, 0)
        if pyxel.btnp(pyxel.KEY_Q):
            camera.rumble(20, 5)
        for obj in self.objects.values(): obj.update()
        if pyxel.btn(pyxel.KEY_SPACE):
            camera.center_to(self.objects["BouncingBall"].x+self.objects["BouncingBall"].width/2, self.objects["BouncingBall"].y+self.objects["BouncingBall"].height/2)
        if pyxel.btn(pyxel.KEY_R):
            camera.center_to(self.objects["GravityBall"].x+self.objects["GravityBall"].width/2, self.objects["GravityBall"].y+self.objects["GravityBall"].height/2)
        camera.update()
        print(camera.get_position())

    def draw(self):
        pyxel.cls(0)
        pyxel.bltm(0, 0, 0, 0, 0, 480, 320)
        pyxel.circ(120, 80, 20, 7)
        for obj in self.objects.values(): obj.draw()


Game()