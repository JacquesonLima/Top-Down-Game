from pgzero.actor import Actor

class Obstacle:
  def __init__(self, pos, sprite="obstacle/obstacle"):
    self.actor = Actor(sprite, topleft=pos)

  def draw(self):
    self.actor.draw()
