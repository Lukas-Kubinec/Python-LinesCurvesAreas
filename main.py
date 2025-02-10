import pygame

pygame.init()

viewport = pygame.display.set_mode((640, 480))
pygame.display.set_caption('Lines, curves and areas/blobs')
viewport.fill((0, 0, 0))


while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()


        # BEGIN
        viewport.fill((0, 0, 0))

        # EVENTS

        # DRAW

        # UPDATE
        pygame.display.update()
