from pgzero.actor import Actor
from knife import Knife

class Player:
  def __init__(self):
    self.idle_frames = ["player/player_idle"]
    self.walk_frames = [
      "player/player_walk",
      "player/player_idle"
    ]

    self.actor = Actor(self.idle_frames[0], center=(300, 300))
    self.velocity = 5

    self.current_animation = self.idle_frames
    self.actual_frame = 0
    self.time = 0
    self.switch_frame = 10

  def update(self, keyboard, obstacles):
    dx = dy = 0
    walking = False

    if keyboard.a:
      dx = -self.velocity
      walking = True
    if keyboard.d:
      dx = self.velocity
      walking = True
    if keyboard.w:
      dy = -self.velocity
      walking = True
    if keyboard.s:
      dy = self.velocity
      walking = True

    if walking:
      if self.current_animation != self.walk_frames:
        self.current_animation = self.walk_frames
        self.actual_frame = 0
    else:
      if self.current_animation != self.idle_frames:
        self.current_animation = self.idle_frames
        self.actual_frame = 0

    self.actor.x += dx
    for obs in obstacles:
      if self.actor.colliderect(obs.actor):
        self.actor.x -= dx
        break

    self.actor.y += dy
    for obs in obstacles:
      if self.actor.colliderect(obs.actor):
        self.actor.y -= dy
        break
      
    self.time += 1
    if self.time >= self.switch_frame:
      self.time = 0
      self.actual_frame = (self.actual_frame + 1) % len(self.current_animation)
      self.actor.image = self.current_animation[self.actual_frame]

    self.keep_inside_screen(800, 600)

  def keep_inside_screen(self, width, height):
    self.actor.left = max(0, self.actor.left)
    self.actor.right = min(width, self.actor.right)
    self.actor.top = max(0, self.actor.top)
    self.actor.bottom = min(height, self.actor.bottom)

  def draw(self):
    self.actor.draw()

  def throw_knife(self, knives, target_pos):
    knife = Knife(self.actor.center, target_pos)
    knives.append(knife)

  def reset_position(self):
    self.actor.center = (300, 300)
