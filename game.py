from player import Player
from enemy import Enemy
from crosshair import Crosshair
from background import Background
from obstacle import Obstacle
import random
import math

WIDTH = 800
HEIGHT = 600

player = Player()
crosshair = Crosshair()
background = Background("background/background", 16, WIDTH, HEIGHT)

ENEMY_TYPES = [
    {"type": "rabbit", "speed": 2, "life": 3},
    {"type": "bee", "speed": 4, "life": 2},
    {"type": "worm", "speed": 1, "life": 5},
]

obstacles = [
    Obstacle((150, 100)),
    Obstacle((150, 150)),
    Obstacle((150, 200)),
    Obstacle((150, 250)),
    Obstacle((500, 120)),
    Obstacle((550, 120)),
    Obstacle((600, 120)),
    Obstacle((600, 170)),
    Obstacle((600, 220)),
    Obstacle((250, 400)),
    Obstacle((300, 400)),
    Obstacle((350, 400)),
    Obstacle((400, 400)),
]

knives = []
enemies = []

game_started = False
game_over = False
score = 0

SPAWN_TIMER = 0
SPAWN_DELAY = 60
SAFE_DISTANCE = 200

music.play("music")
music.set_volume(0.1)

current_mouse_pos = (0, 0)

def update():
  global SPAWN_TIMER, game_over, score

  if not game_started or game_over:
    return

  player.update(keyboard, obstacles)
  crosshair.update(current_mouse_pos)

  SPAWN_TIMER += 1
  if SPAWN_TIMER >= SPAWN_DELAY:
    spawn_enemy()
    SPAWN_TIMER = 0

  for enemy in enemies[:]:
    enemy.update(player, obstacles)

    if enemy.hits_player(player):
      sounds.lose.play()
      music.stop()
      game_over = True
      return

  for knife in knives[:]:
    knife.update()

    if knife.is_off_screen(WIDTH, HEIGHT):
      knives.remove(knife)
      continue

    for enemy in enemies[:]:
      if knife.hits(enemy):
        sounds.hit.play()
        knives.remove(knife)

        if enemy.hit():
          enemies.remove(enemy)
          score += 10

        break

def on_mouse_move(pos, rel, buttons):
  global current_mouse_pos
  current_mouse_pos = pos

def on_mouse_down(pos, button):
  if button == mouse.LEFT and game_started and not game_over:
    player.throw_knife(knives, pos)

def spawn_enemy():
  data = random.choice(ENEMY_TYPES)

  while True:
    x = random.randint(0, WIDTH)
    y = random.randint(0, HEIGHT)

    dx = x - player.actor.x
    dy = y - player.actor.y

    if math.hypot(dx, dy) >= SAFE_DISTANCE:
      enemies.append(
        Enemy(
          (x, y),
          data["type"],
          data["speed"],
          data["life"]
        )
      )
      break

def on_key_down(key):
  global game_started, game_over

  if key == keys.SPACE:
    if not game_started:
      game_started = True
      return

    if game_over:
      reset_game()

def reset_game():
  global enemies, knives, score, game_over, SPAWN_TIMER, game_started

  enemies.clear()
  knives.clear()

  score = 0
  SPAWN_TIMER = 0
  game_over = False
  game_started = True

  player.reset_position()

  music.play("music")
  music.set_volume(0.1)

def draw():
  screen.clear()
  background.draw(screen)

  for obs in obstacles:
    obs.draw()

  for enemy in enemies:
    enemy.draw()

  for knife in knives:
    knife.draw()

  if not game_started:
    screen.draw.text(
      "Press SPACE for start",
      center=(WIDTH // 2, HEIGHT // 2),
      fontsize=48,
      color="white"
    )
    return

  if game_over:
    screen.draw.text(
      "GAME OVER",
      center=(WIDTH // 2, HEIGHT // 2 - 40),
      fontsize=60,
      color="red"
    )
    screen.draw.text(
      "Press SPACE for restart",
      center=(WIDTH // 2, HEIGHT // 2),
      fontsize=30,
      color="white"
    )
    screen.draw.text(
      f"Score: {score}",
      center=(WIDTH // 2, HEIGHT // 2 + 40),
      fontsize=40,
      color="white"
    )
    return

  player.draw()
  crosshair.draw()

  screen.draw.text(
    f"Score: {score}",
    (10, 10),
    fontsize=32,
    color="white"
  )
