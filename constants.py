import pygame
pygame.font.init()


# Screen dimensions
SCREEN_WIDTH = 1200
SCREEN_HEIGHT = 600

# Particles
PARTICLE_RADIUS = 20
PARTICLE_TRANSPARENCY = 255
PARTICLE_LIFESPAN = 2000
AGE_INC = 1
TRANSPARENCY_INC = 20

# emitter
EMIT_RATE = 10


# Paddle properties
PADDLE_RADIUS = 30
PADDLE_SPEED = 5
PADDLE_LEFT_COLOR = (255, 0, 0)  # Red
PADDLE_RIGHT_COLOR = (0, 0, 255)  # Blue

# Puck properties
PUCK_SIZE = 20
PUCK_SPEED = 9
WHITE = (255, 255, 255)
NAVY = (0, 0, 102)

# text color for visibility
DARK_BLUE = (0, 0, 139)
PALETTE = [
    (255, 255, 255),    # White
    (255, 246, 143),    # Light Yellow
    (255, 201, 102),    # Yellow Orange
    (255, 153, 51),     # Orange
    (255, 102, 0),      # Orange Red
    (255, 51, 0),       # Red
    (204, 0, 0),        # Dark Red
    (102, 0, 0)         # Darker Red
]

# Game settings
FPS = 60

# Key bindings
KEY_PADDLE_LEFT_UP = pygame.K_w
KEY_PADDLE_LEFT_DOWN = pygame.K_s
KEY_PADDLE_LEFT_LEFT = pygame.K_a
KEY_PADDLE_LEFT_RIGHT = pygame.K_d
KEY_PADDLE_RIGHT_UP = pygame.K_i
KEY_PADDLE_RIGHT_DOWN = pygame.K_k
KEY_PADDLE_RIGHT_LEFT = pygame.K_j
KEY_PADDLE_RIGHT_RIGHT = pygame.K_l
KEY_QUIT = pygame.K_ESCAPE
KEY_RESET = pygame.K_r
KEY_START = pygame.K_SPACE

# Key bindings for particle mode selection
KEY_NO_PARTICLES = pygame.K_0  # No particles
KEY_SIMPLE_PARTICLES = pygame.K_1  # Simple particle mode
KEY_COMPLEX_PARTICLES = pygame.K_2 # complex particle mode
KEY_SMOKE_PARTICLES = pygame.K_3 # additional one that is complex

# Colors for the ice rink background
OFF_WHITE = (240, 248, 255) 
DARK_RED = (200, 30, 30)
BLUE = (30, 30, 200)
LIGHT_BLUE = (173, 216, 230) # for the goal colors

# image for smoke particles
IMAGE = 'smoke.png'