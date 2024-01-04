from vbo import VBO
from shader_program import ShaderProgram


class VAO:
    def __init__(self, ctx):
        self.ctx = ctx
        self.vbo = VBO(ctx)
        self.program = ShaderProgram(ctx)
        self.vaos = {}

        # skybox vao
        self.vaos["skybox"] = self.get_vao(
            program=self.program.programs['skybox'],
            vbo=self.vbo.vbos['skybox'])

        # sun vao
        self.vaos["sun"] = self.get_vao(
            program=self.program.programs['default'],
            vbo=self.vbo.vbos['sun'])

        self.planet_setters()

    def get_vao(self, program, vbo):
        vao = self.ctx.vertex_array(program, [(vbo.vbo, vbo.format, *vbo.attribs)])
        return vao

    def destroy(self):
        self.vbo.destroy()
        self.program.destroy()

    def planet_setters(self):
        self.set_planet_vao()

    def set_planet_vao(self):
        planets = ["mercury", "earth", "venus", "mars", "jupiter", "saturn", "uranus", "neptune"]
        for planet in planets:
            self.vaos[planet] = self.get_vao(
                program=self.program.programs['default'],
                vbo=self.vbo.vbos[planet])
