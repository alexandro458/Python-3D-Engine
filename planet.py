class Planet:
    def __init__(self, name, scale, orbit_radius, orbit_speed, rotation_speed):
        self.name = name
        self.scale = scale
        self.orbit_radius = orbit_radius
        self.orbit_speed = orbit_speed
        self.rotation_speed = rotation_speed


class PlanetSettings:
    def __init__(self):
        self.mercury = Planet("mercury", 0.38, 70, 47.87, 7)
        self.venus = Planet("venus", 0.949, 120, 35.02, -3)
        self.earth = Planet("earth", 1.0, 170, 29.78, 3)
        self.mars = Planet("mars", 0.532, 230, 24.07, 5)
        self.jupiter = Planet("jupiter", 11.209, 778.5, 13.07, 25)
        self.saturn = Planet("saturn", 9.449, 1200, 9.69, 25)
        self.uranus = Planet("uranus", 4.007, 1500, 6.81, -10)
        self.neptune = Planet("neptune", 3.883, 2000, 5.43, 10)

        # planet list
        self.planets = [self.mercury, self.venus, self.earth, self.mars,
                        self.jupiter, self.saturn, self.uranus, self.neptune]

        self.sun = Planet("sun", 13, 0, 0, 0)
