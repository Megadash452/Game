import pygame
from Network import Network

# import menus

win_width = 500
win_height = 500
win = pygame.display.set_mode((win_width, win_height))
pygame.display.set_caption("Client")


# ---  ---

# --- ---


def redrawWindow(surface, player, player2):
    win.fill((0, 50, 50))
    player.draw_hitbox(surface)
    player.draw_img(surface)

    player2.draw_hitbox(surface)
    player.draw_img(surface)
    pygame.display.update()


def main(run_bool):
    run = run_bool
    n = Network()

    p = n.get_p()

    clock = pygame.time.Clock()

    while run:
        clock.tick(60)
        p2 = n.send(p)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                # --- Save User's last position, state, and looking direction ---
                run = False
                pygame.quit()

        p.move()
        redrawWindow(win, p, p2)


main(True)
