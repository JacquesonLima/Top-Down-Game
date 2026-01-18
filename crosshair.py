from pgzero.actor import Actor

class Crosshair:
  def __init__(self):
    self.actor = Actor("crosshair/crosshair")

  def update(self, pos):
    self.actor.pos = pos

  def draw(self):
    self.actor.draw()
