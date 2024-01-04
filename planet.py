class Planet:
    def __init__(self, name, scale, orbit_radius, orbit_speed):
        self.name = name
        self.scale = scale
        self.orbit_radius = orbit_radius
        self.orbit_speed = orbit_speed
        self.orbit_angle = 0


class PlanetSettings:
    def __init__(self):
        self.mercury = Planet("mercury", 0.38, 57.9, 47.87)
        self.venus = Planet("venus", 0.949, 108.2, 35.02)
        self.earth = Planet("earth", 1.0, 149.6, 29.78)
        self.mars = Planet("mars", 0.532, 227.9, 24.07)
        self.jupiter = Planet("jupiter", 11.209, 778.5, 13.07)
        self.saturn = Planet("saturn", 9.449, 1433.5, 9.69)
        self.uranus = Planet("uranus", 4.007, 2872.5, 6.81)
        self.neptune = Planet("neptune", 3.883, 4495.1, 5.43)
        self.planets = [self.mercury, self.venus, self.earth, self.mars,
                        self.jupiter, self.saturn, self.uranus, self.neptune]
