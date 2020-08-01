import pygame


class Player:
    def __init__(self, x_pos, y_pos, width, height, color, direction):
        self.x_pos = x_pos
        self.y_pos = y_pos
        self.width = width
        self.height = height
        self.color = color
        self.hitbox = (x_pos, y_pos, width, height)
        self.vel = 3
        self.direction = direction

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
