from pgzero.actor import Actor
import math

class Enemy:
    def __init__(self, pos, enemy_type, speed, life=3):
      self.type = enemy_type
      self.speed = speed
      self.life = life

      self.animations = {
          "idle": [
              f"enemies/{self.type}/{self.type}_idle",
          ],
          "walk": [
              f"enemies/{self.type}/{self.type}_walk",
              f"enemies/{self.type}/{self.type}_idle",
          ],
          "dead": [
              f"enemies/{self.type}/{self.type}_dead",
          ]
      }

      self.state = "walk"
      self.frame_index = 0
      self.frame_timer = 0
      self.frame_delay = 10

      self.actor = Actor(self.animations[self.state][0], center=pos)

    def update(self, player, obstacles):
      if self.state == "dead":
        return

      dx = player.actor.x - self.actor.x
      dy = player.actor.y - self.actor.y

      distance = math.hypot(dx, dy)
      if distance == 0:
        self.state = "idle"
        self.animate()
        return

      move_x = (dx / distance) * self.speed
      move_y = (dy / distance) * self.speed

      if self.type == "bee":
        self.actor.x += move_x
        self.actor.y += move_y
      else:
        self.actor.x += move_x
        for obs in obstacles:
          if self.actor.colliderect(obs.actor):
            self.actor.x -= move_x
            break

        self.actor.y += move_y
        for obs in obstacles:
          if self.actor.colliderect(obs.actor):
            self.actor.y -= move_y
            break

      self.state = "walk"
      self.animate()

      self.actor.left = max(0, self.actor.left)
      self.actor.right = min(800, self.actor.right)
      self.actor.top = max(0, self.actor.top)
      self.actor.bottom = min(600, self.actor.bottom)

    def animate(self):
      frames = self.animations[self.state]

      self.frame_timer += 1
      if self.frame_timer >= self.frame_delay:
        self.frame_timer = 0
        self.frame_index = (self.frame_index + 1) % len(frames)
        self.actor.image = frames[self.frame_index]

    def hit(self):
      self.life -= 1

      if self.life <= 0:
        self.state = "dead"
        self.actor.image = self.animations["dead"][0]
        return True

      return False

    def hits_player(self, player):
      return self.actor.colliderect(player.actor)

    def draw(self):
      self.actor.draw()
