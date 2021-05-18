import pygame
from rainbowfy import colour_spread


class Player:
    def __init__(self, x, y, radius, speed, fade, jumpval, jumping):
        self.x = x
        self.y = y
        self.radius = radius

        self.speed = speed
        self.jumpval = jumpval
        self.fade = fade
        self.color_rotation = colour_spread(fade)
        self.current_color = 0

        self.jumping = jumping
        self.jumpval = jumpval

    def draw_player(self, window):
        pygame.draw.circle(window, self.color_rotation[self.current_color], (self.x, self.y), self.radius)

        # Bubble blower
        pygame.draw.circle(window, (0, 0, 0), (self.x, self.y), 0.7*self.radius)

        # move on to next color
        self.current_color += 1
        if self.current_color >= self.fade:
            self.current_color = 0
