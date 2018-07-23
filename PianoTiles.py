"""A simple implementation of Piano Tiles"""

import pygame
import random
import time

clock = pygame.time.Clock()

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

WINDOW_HEIGHT = 400
WINDOW_WIDTH = 300

TILE_HEIGHT = 100
TILE_WIDTH = WINDOW_WIDTH/4

LIST_LEFT = [int(_*TILE_WIDTH) for _ in range(4)]


class Tile:
    """A tile"""
    def __init__(self):
        self.height = TILE_HEIGHT
        self.width = TILE_WIDTH
        self.top = 0
        self.left = LIST_LEFT[random.randint(0, 3)]

    def render(self, screen):
        """Render this tile"""
        pygame.draw.rect(screen, WHITE, pygame.Rect(self.left, self.top, self.width, self.height))

    def move_down(self):
        """Move this tile down"""
        self.top += 4  # + amount (Becomes really too hard after some time)


class Game:
    """The game itself"""
    def __init__(self):
        self.height = WINDOW_HEIGHT
        self.width = WINDOW_WIDTH
        self.tile_list = [Tile()]
        self.done = False
        pygame.init()
        self.screen = pygame.display.set_mode((self.width, self.height))
        self.score = 0

    def add_tile(self):
        """Add a new tile at the beginning of self.tile_list"""
        new_tile = Tile()
        self.tile_list.insert(0, new_tile)
        # print('\n\nnew tile added\n\n')

    def remove_tile(self, tile_to_remove):
        """Remove tile_to_remove"""
        self.tile_list.remove(tile_to_remove)

    def increase_score(self):
        """Increment the score"""
        self.score += 1

    def run_game(self):
        """Run the game"""
        counter = 0
        time.clock()
        while not self.done:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.done = True

            to_add_tile = False
            first_tile = True
            self.screen.fill(BLACK)
            for tile in self.tile_list:
                tile.render(self.screen)
                tile.move_down() # counter/600

                if first_tile and tile.top >= TILE_HEIGHT:
                    # Use > to have little spaces
                    to_add_tile = True
                first_tile = False
                # print(tile.top, tile.left)

                left = tile.left
                right = left + tile.width
                top = tile.top
                bottom = top + tile.height
                pos = pygame.mouse.get_pos()

                if pygame.mouse.get_pressed()[0] and on_tile(pos, left, right, top, bottom):
                    self.remove_tile(tile)
                    self.increase_score()
                    print(self.score)

            if to_add_tile:
                self.add_tile()

            pygame.display.flip()

            clock.tick(60)
            counter += 1  # Counter is 60 x num seconds elapsed


def on_tile(pos, left, right, top, bottom) -> bool:
    """Return whether the current position is within the given boundaries"""

    horizontal_pos = pos[0]
    vertical_pos = pos[1]

    return left <= horizontal_pos <= right and top <= vertical_pos <= bottom

if __name__ == '__main__':
    g = Game()
    g.run_game()
