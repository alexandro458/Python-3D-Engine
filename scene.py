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

        sun = self.planet_settings.sun
        sun_scale = self.planet_settings.sun.scale * SCALE_MULTIPLIER
        add(Sun(app, vao_name=sun.name, tex_id=sun.name, pos=(0, 0, 0),
                              scale=(sun_scale, sun_scale, sun_scale)))

        self.set_planet_scene()

    def render(self):
        for obj in self.objects:
            obj.render()
        self.skybox.render()

    def set_planet_scene(self):
        app = self.app
        add = self.add_object

        for planet in self.planet_settings.planets:
            scale = planet.scale * SCALE_MULTIPLIER
            add(CustomPlanet(app, vao_name=planet.name, tex_id=planet.name, pos=(0, -2, -10),
                             scale=(scale, scale, scale),
                             orbit_speed=planet.orbit_speed * ORBIT_SPEED_MULTIPLIER,
                             orbit_radius=planet.orbit_radius * RADIUS_MULTIPLIER))
