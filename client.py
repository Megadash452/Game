import pygame
from Network import Network

win_width = 500
win_height = 500
win = pygame.display.set_mode((win_width, win_height))
pygame.display.set_caption("Client")

client_number = 0


class Player:
    def __init__(self, x_pos, y_pos, width, height, color):
        self.x_pos = x_pos
        self.y_pos = y_pos
        self.width = width
        self.height = height
        self.color = color
        self.hitbox = (x_pos, y_pos, width, height)
        self.vel = 3

    def draw_hitbox(self, surface):
        pygame.draw.rect(surface, self.color, self.hitbox)

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

        self.update()

    def update(self):
        self.hitbox = (self.x_pos, self.y_pos, self.width, self.height)


def read_pos(string):
    string = string.split(",")
    return int(string[0]), int(string[1])


def make_pos(tup):
    return str(tup[0]) + "," + str(tup[1])


def redrawWindow(surface, player, player2):
    win.fill((0, 50, 50))
    player.draw_hitbox(surface)
    player2.draw_hitbox(surface)
    pygame.display.update()


def main():
    run = True

    n = Network()
    start_pos = read_pos(n.get_pos())

    p = Player(start_pos[0], start_pos[1], 100, 100, (0, 255, 0))
    p2 = Player(0, 0, 100, 100, (255, 0, 0))

    clock = pygame.time.Clock()

    while run:
        clock.tick(60)
        p2_pos = read_pos(n.send(make_pos((p.x_pos, p.y_pos))))
        p2.x_pos = p2_pos[0]
        p2.y_pos = p2_pos[1]
        p2.update()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                # --- Save User's last position, state, and looking direction ---
                run = False
                pygame.quit()

        p.move()
        redrawWindow(win, p, p2)


main()
