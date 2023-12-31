from settings import *
import moderngl as mgl
import pygame as pg
import sys
from camera import Camera
from light import Light
from mesh import Mesh
from scene import Scene


class Engine:
    def __init__(self):
        pg.init()
        pg.display.gl_set_attribute(pg.GL_CONTEXT_MAJOR_VERSION, 3)
        pg.display.gl_set_attribute(pg.GL_CONTEXT_MINOR_VERSION, 3)
        pg.display.gl_set_attribute(pg.GL_CONTEXT_PROFILE_MASK, pg.GL_CONTEXT_PROFILE_CORE)
        pg.display.gl_set_attribute(pg.GL_DEPTH_SIZE, 24)

        pg.display.set_mode(WIN_RES, flags=pg.OPENGL | pg.DOUBLEBUF)
        self.ctx = mgl.create_context()

        self.ctx.enable(flags=mgl.DEPTH_TEST | mgl.CULL_FACE | mgl.BLEND)
        self.ctx.gc_mode = 'auto'

        self.clock = pg.time.Clock()
        self.time = 0
        self.delta_time = 0

        pg.event.set_grab(True)
        pg.mouse.set_visible(False)

        self.is_running = True

        self.light = Light()
        self.camera = Camera(self)
        self.mesh = Mesh(self)
        self.scene = Scene(self)

    def handle_events(self):
        for event in pg.event.get():
            if event.type == pg.QUIT or (event.type == pg.KEYDOWN and event.key == pg.K_ESCAPE):
                self.is_running = False

    def update(self):
        self.camera.update()
        self.scene.update()

        self.time = pg.time.get_ticks() * 0.001
        pg.display.set_caption(f'{self.clock.get_fps() :.0f}')
        self.delta_time = self.clock.tick(60)

    def render(self):
        self.ctx.clear(color=BG_COLOR)

        self.scene.render()

        pg.display.flip()

    def run(self):
        while self.is_running:
            self.handle_events()
            self.update()
            self.render()
        self.mesh.destroy()
        pg.quit()
        sys.exit()


if __name__ == '__main__':
    app = Engine()
    app.run()
