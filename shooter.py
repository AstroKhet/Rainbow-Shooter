import pygame
from player import Player
from projectile import Projectile
from rainbowfy import colour_spread

pygame.init()
fps = pygame.time.Clock()

ww, wh = 1200, 700
window = pygame.display.set_mode((ww, wh))


# rainbow palette
rainbow = colour_spread(ww)


def draw_platform():
    pygame.draw.rect(window, (125, 125, 125), (0, 550, 1200, 150))


# Main event loop

ball = Player(
    x=500,
    y=525,
    radius=25,
    speed=4,
    fade=750,
    jumpval=20,
    jumping=False
)

projectiles = []
cooldown = 1

running = True
while running:
    fps.tick(64)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            continue

    mouse_pos = pygame.mouse.get_pos()
    mouse = pygame.mouse.get_pressed()

    if mouse[0] and cooldown <= 0:  # Right click
        projectiles.append(Projectile(ball.x, ball.y, 17, mouse_pos, 191))
        projectiles[-1].initialize()
        cooldown = 1

    cooldown -= 1

    key = pygame.key.get_pressed()
    if key[pygame.K_d] and ball.x < ww - ball.radius:
        ball.x += ball.speed
        left = False
        right = True
    if key[pygame.K_a] and ball.x > ball.radius:
        ball.x -= ball.speed
        left = True
        right = False
    if key[pygame.K_a] == key[pygame.K_d]:
        left = False
        right = False
        ball.walk_count = 0  # reset

    if not ball.jumping:
        if key[pygame.K_UP] or key[pygame.K_w]:
            ball.jumping = True
    elif ball.jumping:
        if ball.jumpval >= -20:
            neg = -1 if ball.jumpval < 0 else 1
            ball.y -= round((ball.jumpval ** 2) / 20) * neg
            ball.jumpval -= 1
        else:
            ball.jumping = False
            ball.jumpval = 20

    window.fill((0, 0, 0))  # refresh from last window
    ball.draw_player(window)

    for proj_big in projectiles:
        proj_big.draw_projectile(window, rainbow)

    draw_platform()

    projectiles = list(filter(lambda o: o.frames >= 0, projectiles))
    pygame.display.update()
