import pyxel
import math

class Particle:

    def __init__(self, x, y, vx, vy, r, color):
        self.x = x
        self.y = y
        self.vx = vx
        self.vy = vy
        self.r = r
        self.color = color

    def update(self):
        self.x += self.vx
        self.y += self.vy
        self.r += 0.2

    def draw(self):
        pyxel.circ(int(self.x), int(self.y), self.r, self.color)

class BubbleGenerator:

    def __init__(self, x, y, hmax=30):
        self.x = x
        self.y = y
        self.hmax = hmax
        self.particles = []

    def update(self, x, y):
        self.x = x
        self.y = y
        if pyxel.frame_count % 6 == 0:
            vx = pyxel.rndf(-0.5, 0.5)
            vy = -pyxel.rndf(1,2)
            self.particles.append(Particle(self.x, self.y, vx, vy, 0.5, [1,5,6,12][pyxel.rndi(0,3)]))

        for particle in self.particles:
            particle.update()
            if particle.y < (self.y-self.hmax):
                self.particles.remove(particle)

    def draw(self):
        for particle in self.particles:
            particle.draw()

bubble = None

class App:

    def __init__(self):

        global bubble
        bubble = BubbleGenerator(120, 100, 50)
        pyxel.init(240, 160)
        colors = pyxel.colors.to_list()
        colors.append(0xFF0000)
        pyxel.colors.from_list(colors)
        pyxel.load("mygame.pyxres")
        pyxel.run(self.update, self.draw)

    def update(self):
        bubble.update(pyxel.mouse_x, pyxel.mouse_y)
        if pyxel.btnp(pyxel.KEY_ESCAPE):
            pyxel.quit()

    def draw(self):
        pyxel.cls(0)
        bubble.draw()

App()
