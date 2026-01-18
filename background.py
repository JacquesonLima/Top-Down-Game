class Background:
    def __init__(self, tile_name, tile_size, width, height):
        self.tile = tile_name
        self.tile_size = tile_size
        self.width = width
        self.height = height

    def draw(self, screen):
        for x in range(0, self.width, self.tile_size):
            for y in range(0, self.height, self.tile_size):
                screen.blit(self.tile, (x, y))