import glm


class Light:
    def __init__(self, position=glm.vec3(3, 3, -3), color=(1, 1, 1)):
        self.position = position
        self.color = glm.vec3(color)
        # intensities
        self.Ia = 0.04 * self.color  # ambient
        self.Id = 0.8 * self.color  # diffuse
        self.Is = 1.0 * self.color  # specular
