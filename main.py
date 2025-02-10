import pygame
import numpy as np
pygame.init()

# Window settings
viewport = pygame.display.set_mode((640, 480))
pygame.display.set_caption('Lines, curves and areas/blobs')
viewport.fill((0, 0, 0))

# FPS clock
clock = pygame.time.Clock()

# Line position
line_a,line_b = [150,150] , [200,200]

# Star attributes


# Functions
# Move
def move_by(a,b,xy):
    result = [a[0]+xy[0] , a[1]+xy[1] , b[0]+xy[0] , b[1]+xy[1]]
    print(result)
    return result

# Scale
def scale_by(a, b, scalar):
    a_orig = a

    a[0] = a[0] - b[0]
    a[1] = a[1] - b[1]
    b[0] = b[0] - a[0]
    b[1] = b[1] - a[1]

    scalar = [[scalar[0],0],[0,scalar[1]]]
    scaled_a = [np.transpose(np.dot(scalar[0], np.transpose(a[0]))),np.transpose(np.dot(scalar[0], np.transpose(a[1])))]
    scaled_b = [np.transpose(np.dot(scalar[1], np.transpose(b[0]))),np.transpose(np.dot(scalar[1], np.transpose(b[1])))]
    scaled_a = np.transpose(scaled_a)
    scaled_b = np.transpose(scaled_b)
    result = [scaled_a[0]+a_orig[0], scaled_a[1]+a_orig[1], scaled_b[0], scaled_b[1]]
    print("A: " + str(result[0]) + " B: " + str(result[1]))
    return result

# Rotate
def rotate_by(a,b,angle):
    rads = angle * np.pi / 180

    a[0] = a[0] - b[0]
    a[1] = a[1] - b[1]

    new_x = a[0] * np.cos(rads) - a[1] * np.sin(rads)
    new_y = a[0] * np.sin(rads) + a[1] * np.cos(rads)

    result = [new_x+b[0],new_y+b[1]]

    print(result)
    return result

while True:
    for event in pygame.event.get():
        # BEGIN
        viewport.fill((0, 0, 0))

        # EVENTS
        if event.type == pygame.QUIT:
            pygame.quit()

        # Mouse events
        if pygame.mouse.get_pressed()[0]:
            line_scalar = scale_by(line_a, line_b, [1.1, 1.1])
            line_a = line_scalar[0]
            line_b = line_scalar[1]
            line_a[0],line_a[1] = int(line_a[0]),int(line_a[1])
            line_b[0],line_b[1] = int(line_b[0]),int(line_b[1])

        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 5:
                line_b = rotate_by(line_b, line_a, 5)

        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 4:
                line_b = rotate_by(line_b, line_a, -5)

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
                movement = move_by(line_b,line_a,[10,0])
                line_a = [movement[0],movement[1]]
                line_b = [movement[2],movement[3]]

            if event.key == pygame.K_LEFT:
                movement = move_by(line_a,line_b,[-10,0])
                line_a = [movement[0],movement[1]]
                line_b = [movement[2],movement[3]]


        # DRAW
        pygame.draw.line(viewport, (255,255,255), line_a, line_b)

    # UPDATE
    pygame.display.flip()
    clock.tick(60)
    pygame.display.set_caption('Lines, curves and areas/blobs | FPS:' + str(clock.get_fps()))
