import sys
import pygame
import numpy as np
pygame.init()

# Window settings
SCREEN_WIDTH, SCREEN_HEIGHT = 800, 600
viewport = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption('Lines, curves and areas/blobs')
viewport.fill((0, 0, 0))

# FPS clock
clock = pygame.time.Clock()

# SHAPES
# Moving circle
circle_diameter = 20
circle_x, circle_y = 50, 50
circle_hspeed = 3
circle_vspeed = 3
circle_color = (255, 0, 0)

# Line position
line_a,line_b = [150,150] , [200,200]

# Triangle position
triangle_a, triangle_b, triangle_c = [350,400] , [400,400] , [375,350]

# Rectangle position
rect_a, rect_b, rect_c, rect_d = [300,250] , [400,250] , [300,150] , [400,150]

# Functions
# Move
def move_by(a,b,xy):
    # Calculation of new position
    result = [a[0]+xy[0] , a[1]+xy[1] , b[0]+xy[0] , b[1]+xy[1]]
    return result

# Scale
def scale_by(a, b, scalar):
    # Storing a copy of original values
    default_a, default_b = a, b
    # Subtracts the position vectors
    a = np.subtract(a, default_a)
    b = np.subtract(b, default_a)
    # Scales the points, and adds back the default position values
    scaled_a = np.add(np.multiply(scalar, a), default_a)
    scaled_b = np.add(np.multiply(scalar, b), default_b)
    # Stores the new scaled vector positions, and returns them
    result = [[round(scaled_a[0], 2), round(scaled_a[1], 2)], [round(scaled_b[0], 2), round(scaled_b[1], 2)]]
    return result

# Rotate
def rotate_by(a,b,angle):
    # Converts degrees to radians
    rads = angle * np.pi / 180
    # Subtracts the position vectors
    a = np.subtract(a,b)
    # Calculation of new position
    new_x = a[0] * np.cos(rads) - a[1] * np.sin(rads)
    new_y = a[0] * np.sin(rads) + a[1] * np.cos(rads)
    # Stores new position and then returns it
    result = [new_x+b[0],new_y+b[1]]
    return result

# Random RGB
def random_rgb():
    return np.random.randint(0,255),np.random.randint(0,255),np.random.randint(0,255)

# Used to determine if the program should be running
program_running = True

# Main loop
while program_running:
    # BEGIN SECTION
    viewport.fill((0, 0, 0))

    # EVENTS SECTION
    # Movement of red circle
    circle_y += circle_vspeed
    if circle_y >= SCREEN_HEIGHT - circle_diameter:
        circle_vspeed = -3
        circle_color = random_rgb()
    elif circle_y <= 0 + circle_diameter:
        circle_vspeed = 3
        circle_color = random_rgb()

    circle_x += circle_hspeed
    if circle_x >= SCREEN_WIDTH - circle_diameter:
        circle_hspeed = -5
        circle_color = random_rgb()
    elif circle_x <= 0 + circle_diameter:
        circle_hspeed = 5
        circle_color = random_rgb()

    # INPUT EVENTS SECTION
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            program_running = False

        # Mouse events
        if pygame.mouse.get_pressed()[0]:
            # Scaling of line
            line_scalar = scale_by(line_a, line_b, [0.1,0.1])
            line_a = line_scalar[0]
            line_b = line_scalar[1]
            # Scaling of triangle
            triangle_c = scale_by(triangle_a, triangle_c, [0.1, 0.1])[1]
            triangle_b = scale_by(triangle_a, triangle_b, [0.1, 0.1])[1]
            # Scaling of rectangle
            rect_b = scale_by(rect_a, rect_b, [0.1, 0.1])[1]
            rect_c = scale_by(rect_a, rect_c, [0.1, 0.1])[1]
            rect_d = scale_by(rect_a, rect_d, [0.1, 0.1])[1]


        if pygame.mouse.get_pressed()[2]:
            # Scaling of line
            line_scalar = scale_by(line_a, line_b, [-0.1,-0.1])
            line_a = line_scalar[0]
            line_b = line_scalar[1]
            # Scaling of triangle
            triangle_c = scale_by(triangle_a, triangle_c, [-0.1, -0.1])[1]
            triangle_b = scale_by(triangle_a, triangle_b, [-0.1, -0.1])[1]
            # Scaling of rectangle
            rect_b = scale_by(rect_a, rect_b, [-0.1, -0.1])[1]
            rect_c = scale_by(rect_a, rect_c, [-0.1, -0.1])[1]
            rect_d = scale_by(rect_a, rect_d, [-0.1, -0.1])[1]

        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 5:
                # Rotation of line
                line_b = rotate_by(line_b, line_a, 5)
                # Rotation of triangle
                triangle_b = rotate_by(triangle_b, triangle_a, 5)
                triangle_c = rotate_by(triangle_c, triangle_a, 5)
                # Rotation of rectangle
                rect_b = rotate_by(rect_b, rect_a, 5)
                rect_c = rotate_by(rect_c, rect_a, 5)
                rect_d = rotate_by(rect_d, rect_a, 5)

        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 4:
                # Rotation of line
                line_b = rotate_by(line_b, line_a, -5)
                # Rotation of triangle
                triangle_b = rotate_by(triangle_b, triangle_a, -5)
                triangle_c = rotate_by(triangle_c, triangle_a, -5)
                # Rotation of rectangle
                rect_b = rotate_by(rect_b, rect_a, -5)
                rect_c = rotate_by(rect_c, rect_a, -5)
                rect_d = rotate_by(rect_d, rect_a, -5)

        # Keyboard events
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_DOWN:
                # Move line down
                movement = move_by(line_a,line_b,[0,10])
                line_a = [movement[0],movement[1]]
                line_b = [movement[2],movement[3]]

            if event.key == pygame.K_UP:
                movement = move_by(line_a,line_b,[0,-10])
                line_a = [movement[0],movement[1]]
                line_b = [movement[2],movement[3]]

            if event.key == pygame.K_RIGHT:
                movement = move_by(line_a,line_b,[10,0])
                line_a = [movement[0],movement[1]]
                line_b = [movement[2],movement[3]]

            if event.key == pygame.K_LEFT:
                movement = move_by(line_a,line_b,[-10,0])
                line_a = [movement[0],movement[1]]
                line_b = [movement[2],movement[3]]

    # DRAW SECTION
    # Draw circle
    pygame.draw.circle(viewport, circle_color, (circle_x, circle_y), circle_diameter)
    # Draw line
    pygame.draw.line(viewport, (255, 255, 255), line_a, line_b)
    # Draw triangle
    pygame.draw.polygon(viewport, (255, 255, 255), (triangle_a, triangle_b, triangle_c))
    # Draw rectangle
    pygame.draw.polygon(viewport, (255, 255, 255), (rect_a, rect_b, rect_d, rect_c))

    # UPDATE
    pygame.display.flip()
    clock.tick(60)
    pygame.display.set_caption('Lines, curves and areas/blobs | FPS:' + str(int(clock.get_fps())))

# Quits the game
pygame.quit()
sys.exit()