from model import *


class Scene:
    def __init__(self, app):
        self.app = app
        self.objects = []
        self.load()
        # skybox
        self.skybox = SkyBox(app)

    def add_object(self, obj):
        self.objects.append(obj)

    def load(self):
        app = self.app
        add = self.add_object

        add(CustomPlanet(app, vao_name='earth', tex_id='earth', pos=(0, -2, -20)))
        add(CustomPlanet(app, vao_name='mercury', tex_id='mercury', pos=(0, -2, -10), scale=(0.5, 0.5, 0.5)))

    def render(self):
        for obj in self.objects:
            obj.render()
        self.skybox.render()
