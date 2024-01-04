from model import *
from planet import PlanetSettings
from settings import *
import numpy as np


class Scene:
    def __init__(self, app):
        self.app = app
        self.objects = []
        self.planet_settings = PlanetSettings()
        self.load()
        # skybox
        self.skybox = SkyBox(app)

    def add_object(self, obj):
        self.objects.append(obj)

    def load(self):
        app = self.app
        add = self.add_object

        add(ExtendedBaseModel(app, vao_name='sun', tex_id='sun', pos=(0, -2, 0)))

        self.set_planet_scene()

    def render(self):
        for obj in self.objects:
            obj.render()
        self.skybox.render()

    def set_planet_scene(self):
        app = self.app
        add = self.add_object

        for planet in self.planet_settings.planets:
            add(CustomPlanet(app, vao_name=planet.name, tex_id=planet.name, pos=(0, -2, -10),
                             scale=(planet.scale, planet.scale, planet.scale), orbit_speed=planet.orbit_speed * ORBIT_SPEED_MULTIPLIER,
                             orbit_radius=planet.orbit_radius * RADIUS_MULTIPLIER))

