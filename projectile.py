import pygame
import random


class Projectile:
    def __init__(self, x, y, radius, pos_stop, frames):
        self.x = x
        self.y = y
        self.radius = radius
        self.sx = pos_stop[0]
        self.sy = pos_stop[1]
        self.travel_pos = []  # 16 positions, 4 frames/pos, 64 frames/s
        self.frames = frames
        # Large bubble
        self.particles = []
        self.particle_count = random.randint(4, 10)

    def initialize(self):
        x_dist = self.sx - self.x
        y_dist = self.sy - self.y
        x_intervals = [self.x + (x_dist / 128) * i for i in range(128)]
        y_intervals = [self.y + (y_dist / 128) * i for i in range(128)]

        self.travel_pos = [(x, y) for x, y in zip(x_intervals, y_intervals)]

        for i in range(self.particle_count):  # Particles
            x_pos = random.randint(self.sx - 160, self.sx + 160)
            y_pos = random.randint(self.sy - 160, self.sy + 160)
            x_dist = x_pos - self.sx
            y_dist = y_pos - self.sy
            x_intervals = [self.travel_pos[-1][0] + (x_dist / 64) * i for i in range(64)]
            y_intervals = [self.travel_pos[-1][1] + (y_dist / 64) * i for i in range(64)]
            travel_pos = [(x, y) for x, y in zip(x_intervals, y_intervals)]
            self.particles.append(travel_pos)

    def draw_projectile(self, window, colors):  # Rainbow explosion!
        pos = 191 - self.frames
        if self.frames > 63:
            try:
                color = colors[round(self.travel_pos[pos][0])]
            except IndexError:
                color = (255, 0, 0)
            pygame.draw.circle(window, color, self.travel_pos[pos], self.radius)
        else:
            for i in range(self.particle_count):
                try:
                    color = colors[round(self.particles[i][63 - self.frames][0])]
                except IndexError:
                    color = (255, 0, 0)

                pygame.draw.circle(window, color, self.particles[i][63 - self.frames], 11)
        self.frames -= 1
