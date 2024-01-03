import pygame as pg
import moderngl as mgl



class Texture:
    def __init__(self, ctx):
        self.ctx = ctx
        self.textures = {}
        self.textures[0] = self.get_texture(path='textures/test.jpg')

    def get_texture(self, path):
        texture = pg.image.load(path).convert()
        texture = pg.transform.flip(texture, False, True)
        texture = self.ctx.texture(size=texture.get_size(), components=3,
                                   data=pg.image.tostring(texture, 'RGB'))
        return texture

    def destroy(self):
        [tex.release() for tex in self.textures.values()]