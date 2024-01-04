from numba import njit
import numpy as np
import glm
import math

# resolution
WIN_RES = glm.vec2(1600, 900)

# colors
BG_COLOR = glm.vec3(0.1, 0.16, 0.25)

# camera
FOV = 50  # deg
NEAR = 0.1
FAR = 5000
SPEED = 0.1
SENSITIVITY = 0.07

# scene
RADIUS_MULTIPLIER = 0.3
ORBIT_SPEED_MULTIPLIER = 0.005
