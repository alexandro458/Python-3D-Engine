#version 330 core

layout (location = 0) out vec4 fragColor;

in vec2 uv_0;
in vec3 normal;

uniform sampler2D u_texture_0;


void main() {
    vec3 color = texture(u_texture_0, uv_0).rgb;
    float normal = min(1, normal.x + 1.0); //using normal so OpenGL doesn't remove unused variable
    fragColor = vec4(color, normal);
}