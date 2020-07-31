import pygame

win_width = 500
win_height = 500
win = pygame.display.set_mode((win_width, win_height))
pygame.display.set_caption("Client")

client_number = 0


class Player():
    def __init__(self, x_pos, y_pos, width, height, color):
        self.x_pos = x_pos
        self.y_pos = y_pos
        self.width = width
        self.height = height
        self.color = color
        self.rect = (x_pos, y_pos, width, height)
        self.vel = 3

    def draw(self, surface):
        pygame.draw.rect(surface, self.color, self.rect)

    def move(self):
        keys = pygame.key.get_pressed()

        if keys[pygame.K_LEFT]:
            self.x_pos -= self.vel

        if keys[pygame.K_RIGHT]:
            self.x_pos += self.vel

        if keys[pygame.K_UP]:
            self.y_pos -= self.vel

        if keys[pygame.K_DOWN]:
            self.y_pos += self.vel

        self.rect = (self.x_pos, self.y_pos, self.width, self.height)


def redrawWindow(surface, player):
    surface.fill((0, 50, 50))
    player.draw(win)
    pygame.display.update()


def main():
    run = True
    p = Player(50, 50, 100, 100, (255, 255, 255))
    clock = pygame.time.Clock()

    while run:
        clock.tick(60)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                pygame.quit()

        p.move()
        redrawWindow(win, p)


main()
