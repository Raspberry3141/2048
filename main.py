import random
import pygame


class Game(object):
    def __init__(self):
        pygame.init()
        self.width, self.height = 440, 440
        self.clock = pygame.time.Clock()
        self.window = pygame.display.set_mode((self.width, self.height))
        self.running = True
        self.tiles = [[0 for _ in range(4)] for _ in range(4)]
        self.temp_tiles = None
        self.tile_colors = {0: "grey",
                            2: (107, 107, 106),
                            4: (250, 240, 217),
                            8: (237, 208, 140),
                            16: (245, 150, 34),
                            32: (237, 89, 36),
                            64: "red",
                            128: "yellow",
                            256: "black",
                            512: "purple",
                            1024: "green",
                            2048: "blue"}
        self.init_values = [2, 4]
        for _ in range(2):
            self.row = random.randint(0, 3)
            self.column = random.randint(0, 3)
            self.init_value = random.choice(self.init_values)
            self.tiles[self.row][self.column] = self.init_value
        self.main()

    def main(self):
        while self.running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False

                if event.type == pygame.KEYDOWN:
                    self.temp_tiles = self.tiles
                    if event.key == pygame.K_LEFT:
                        self.temp_tiles = self.tiles
                        self.temp_tiles = self.move_tiles()
                        if self.temp_tiles != self.tiles:
                            self.tiles = self.temp_tiles
                            self.spawn_tiles()
                        self.temp_tiles = self.tiles

                    if event.key == pygame.K_RIGHT:
                        self.temp_tiles = self.tiles
                        for _ in range(2): self.temp_tiles = self.rotate_arr()
                        self.temp_tiles = self.move_tiles()
                        for _ in range(2): self.temp_tiles = self.rotate_arr()
                        if self.temp_tiles != self.tiles:
                            self.tiles = self.temp_tiles
                            self.spawn_tiles()
                        self.temp_tiles = self.tiles

                    if event.key == pygame.K_UP:
                        self.tiles = self.tiles
                        self.temp_tiles = self.tiles
                        self.temp_tiles = self.rotate_arr()
                        self.temp_tiles = self.move_tiles()
                        for _ in range(3): self.temp_tiles = self.rotate_arr()
                        if self.temp_tiles != self.tiles:
                            self.tiles = self.temp_tiles
                            self.spawn_tiles()
                        self.temp_tiles = self.tiles

                    if event.key == pygame.K_DOWN:
                        self.temp_tiles = self.tiles
                        for _ in range(3): self.temp_tiles = self.rotate_arr()
                        self.temp_tiles = self.move_tiles()
                        self.temp_tiles = self.rotate_arr()
                        if self.temp_tiles != self.tiles:
                            self.tiles = self.temp_tiles
                            self.spawn_tiles()
                        self.temp_tiles = self.tiles

            self.window.fill((235, 220, 178))

            # draw the border around the boxes in orange
            line_coords = [(0, 0), (440, 0), (440, 440), (0, 440)]
            self.surface = self.window
            for i in range(3):
                pygame.draw.line(self.surface, "orange", line_coords[i], line_coords[i + 1], 10)
            pygame.draw.line(self.surface, "orange", line_coords[3], line_coords[0], 10)

            # draw the tiles and display numbers
            font = pygame.font.Font(None, 60)
            for i in range(4):
                for j in range(4):
                    self.tile_colors = self.tile_colors
                    pygame.draw.rect(self.surface, self.tile_colors.get(self.tiles[i][j]),
                                     (5 + (j * 110), 5 + (i * 110), 100, 100))
                    text_surface = font.render(str(self.tiles[i][j]), True, "white")
                    if self.tiles[i][j] != 0:
                        self.surface.blit(text_surface, (5 + (j * 110), 5 + (i * 110) + 25))

            if self.game_over_check():
                self.game_over()

            pygame.display.update()
            self.clock.tick(20)

    def spawn_tiles(self):
        openings = []
        choices = [2, 2, 2, 4]
        try:
            for i in range(len(self.tiles)):
                for j in range(len(self.tiles)):
                    if self.tiles[i][j] == 0:
                        openings.append(list([i, j]))
            chosen = random.choice(openings)
            self.tiles[chosen[0]][chosen[1]] = random.choice(choices)
        except:
            self.game_over()

    def game_over(self):
        print("game over!")
        self.tiles = [[0 for _ in range(4)] for _ in range(4)]
        pygame.quit()

    def rotate_arr(self):
        rotated_arr = [[self.temp_tiles[i][j] for i in range(len(self.temp_tiles))] for j in range(3, -1, -1)]
        return rotated_arr

    def move_tiles(self):
        result = []
        for k in range(len(self.temp_tiles)):
            self.temp_tiles[k] = [num for num in self.temp_tiles[k] if num != 0]
            for _ in range(4 - len(self.temp_tiles[k])):
                self.temp_tiles[k].append(0)
            for i in range(len(self.temp_tiles[k]) - 1):
                if self.temp_tiles[k][i] == self.temp_tiles[k][i + 1]:
                    self.temp_tiles[k][i] *= 2
                    self.temp_tiles[k][i + 1] = 0
                elif self.temp_tiles[k][i] == 0:
                    self.temp_tiles[k][i] = self.temp_tiles[k][i + 1]
                    self.temp_tiles[k][i + 1] = 0
            result.append(self.temp_tiles[k])
        return result

    def game_over_check(self):
        pass


if __name__ == '__main__':
    game = Game()
    pygame.quit()
