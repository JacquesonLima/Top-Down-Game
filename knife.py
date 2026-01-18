from pgzero.actor import Actor
import math

class Knife:
    def __init__(self, start_pos, target_pos):
        self.actor = Actor("weapons/knife", center=start_pos)

        dx = target_pos[0] - start_pos[0]
        dy = target_pos[1] - start_pos[1]

        distance = math.hypot(dx, dy)
        if distance == 0:
            distance = 1

        self.vx = dx / distance
        self.vy = dy / distance

        self.speed = 10
        self.rotation_speed = 20

    def update(self):
        self.actor.x += self.vx * self.speed
        self.actor.y += self.vy * self.speed
        self.actor.angle += self.rotation_speed

    def hits(self, enemy):
        return self.actor.colliderect(enemy.actor)

    def is_off_screen(self, width, height):
        return (
            self.actor.right < 0 or
            self.actor.left > width or
            self.actor.bottom < 0 or
            self.actor.top > height
        )

    def draw(self):
        self.actor.draw()
