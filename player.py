import pygame


# add player images
Character_img = {
    'up': pygame.transform.scale(pygame.image.load('char1_up.png'), (100, 100)),
    'down': pygame.transform.scale(pygame.image.load('char1_down.png'), (100, 100)),
    'left': pygame.transform.scale(pygame.image.load('char1_left.png'), (100, 100)),
    'right': pygame.transform.scale(pygame.image.load('char1_right.png'), (100, 100))
}


class Object:
    def __init__(self, x_pos, y_pos, width, height, color):
        self.x_pos = x_pos
        self.y_pos = y_pos
        self.width = width
        self.height = height
        self.color = color
        self.hitbox = (self.x_pos, self.y_pos, self.width, self.height)

    def draw_hitbox(self, surface):
        pygame.draw.rect(surface, self.color, self.hitbox, 2)


class Player(Object):
    def __init__(self, x_pos, y_pos, width, height, color, direction):
        super().__init__(x_pos, y_pos, width, height, color)
        self.vel = 3
        self.direction = direction

    def draw_img(self, surface):
        surface.blit(Character_img[self.direction], (self.hitbox[0], self.hitbox[1]))

    def move(self):
        keys = pygame.key.get_pressed()

        if keys[pygame.K_LEFT]:
            self.x_pos -= self.vel
            self.change_direction('left')

        if keys[pygame.K_RIGHT]:
            self.x_pos += self.vel
            self.change_direction('right')

        if keys[pygame.K_UP]:
            self.y_pos -= self.vel
            self.change_direction('up')

        if keys[pygame.K_DOWN]:
            self.y_pos += self.vel
            self.change_direction('down')

        self.update()

    def change_direction(self, direction):
        self.direction = direction

    def update(self):
        self.hitbox = (self.x_pos, self.y_pos, self.width, self.height)
