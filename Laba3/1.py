screen.fill((255,255,255))

circle(screen, (255, 255, 0), (500,500), 300, 0) #face
circle(screen, (255, 0, 0), (350, 400), 80, 0) #eye1
circle(screen, (255, 0, 0), (650, 400), 60, 0) #eye2
circle(screen, (0, 0, 0), (350, 400), 20, 0) #micro eye1
circle(screen, (0, 0, 0), (650, 400), 15, 0) #micro eye2
polygon(screen, (0, 0, 0), [(600,700),(600,680),(400,680),(400,700)]) #mouse
polygon(screen, (0, 0, 0), [(200,230),(220,210),(520,400),(500,430)]) #brov1
polygon(screen, (0, 0, 0), [(540,410),(540,440),(800,230),(800,200)]) #brov2


pygame.display.update()
clock = pygame.time.Clock()
finished = False

while not finished:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True

pygame.quit()