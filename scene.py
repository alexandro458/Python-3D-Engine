from model import *
from planet import PlanetSettings
from settings import *


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
        self.sun = Sun(app, vao_name=sun.name, tex_id=sun.name, pos=(0, 0, 0),
                       scale=(sun_scale, sun_scale, sun_scale))

        self.set_planet_scene()

    def set_planet_scene(self):
        app = self.app
        add = self.add_object

        for planet in self.planet_settings.planets:
            scale = planet.scale * SCALE_MULTIPLIER
            add(CustomPlanet(app, vao_name=planet.name, tex_id=planet.name, pos=(0, -2, -10),
                             scale=(scale, scale, scale),
                             orbit_speed=planet.orbit_speed * ORBIT_SPEED_MULTIPLIER,
                             orbit_radius=planet.orbit_radius * RADIUS_MULTIPLIER,
                             rotation_speed=ROTATION_SPEED_MULTIPLIER * planet.rotation_speed * (1 / scale)))

    def render(self):
        for obj in self.objects:
            obj.render()
        self.sun.render()
        self.skybox.render()

    def update(self):
        for planet in self.objects:
            pos_tuple = self.calculate_orbit(planet.orbit_radius, planet.orbit_speed)
            planet.pos = (pos_tuple[0], -2, pos_tuple[1])

            rotation = self.calculate_rotation(planet.rotation_speed)
            planet.rot.y = rotation

    def calculate_orbit(self, radius, speed):
        time = self.app.time
        angle = speed * time

        x = radius * np.cos(angle)
        z = radius * np.sin(angle)
        return x, z

    def calculate_rotation(self, speed):
        time = self.app.time
        angle = speed * time
        return angle
