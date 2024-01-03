import pygame as pg
import moderngl as mgl


class Texture:
    def __init__(self, ctx):
        self.ctx = ctx
        self.textures = {}
        self.textures[0] = self.get_texture(path='textures/test.jpg')
        self.textures[1] = self.get_texture(path='textures/test2.jpg')
        self.textures[2] = self.get_texture(path='textures/test3.jpg')
        self.textures['cat'] = self.get_texture(path='obj/CatModel/cat_texture.jpg')
        self.textures['earth'] = self.get_texture(path='obj/Earth/Textures/Diffuse_2K.png')

    def get_texture(self, path):
        texture = pg.image.load(path).convert()
        texture = pg.transform.flip(texture, False, True)
        texture = self.ctx.texture(size=texture.get_size(), components=3,
                                   data=pg.image.tostring(texture, 'RGB'))
        # mipmaps
        texture.filter = (mgl.LINEAR_MIPMAP_LINEAR, mgl.LINEAR)
        texture.build_mipmaps()
        # AF
        texture.anisotropy = 32.0
        return texture

    def destroy(self):
        [tex.release() for tex in self.textures.values()]