
def main():
    run = True
    p = Player(50, 50, 100, 100, (0, 250, 0))
    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                pygame.quit()
        p.move()
        redrawWindow(win, p)
