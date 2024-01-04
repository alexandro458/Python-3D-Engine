#version 330 core

layout (location = 0) out vec4 fragColor;

in vec2 uv_0;
in vec3 normal;
in vec3 fragPos;

struct Light{
    vec3 position;
    vec3 Ia;
    vec3 Id;
    vec3 Is;
};

uniform Light light;
uniform sampler2D u_texture_0;
uniform vec3 camPos;

vec3 getLight(vec3 color){
    vec3 Normal = normalize(normal);

    //ambient light
    vec3 ambient = light.Ia;

    //diffuse light
    vec3 lightDir = normalize(light.position - fragPos);
    float diff = max(0, dot(lightDir, Normal));
    vec3 diffuse = diff * light.Id;

    //specular light
    vec3 viewDir = normalize(camPos - fragPos);
    vec3 reflectDir = reflect(-lightDir, Normal);
    float spec = pow(max(dot(viewDir, reflectDir), 0), 10);
    vec3 specular = spec * light.Is;


    return color * (ambient + diffuse + specular);
}

vec3 applyFog(vec3 color, vec3 fragPos, vec3 camPos, vec3 fogColor, float fogDensity, float fogStart, float fogEnd) {
    // Calcular la distancia desde la cámara al fragmento
    float distance = length(camPos - fragPos);

    // Calcular el factor de niebla
    float fogFactor = clamp((distance - fogStart) / (fogEnd - fogStart), 0.0, 1.0);

    // Mezclar el color del objeto con el color de la niebla
    vec3 finalColor = mix(color, fogColor, fogFactor);

    return finalColor;
}

void main() {
    float gamma = 2.2;
    vec3 color = texture(u_texture_0, uv_0).rgb;
    color = pow(color, vec3(gamma));

    color = getLight(color);

    color = pow(color, 1 / vec3(gamma));

    vec3 fogColor = vec3(0.05, 0.05, 0.05);
    float fogDensity = 0.1;
    float fogStart = 300.0;
    float fogEnd = 1500.0;

    color = applyFog(color, fragPos, camPos, fogColor, fogDensity, fogStart, fogEnd);

    fragColor = vec4(color, 1.0);
}