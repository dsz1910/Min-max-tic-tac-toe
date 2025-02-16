import pygame
from circle_and_x import Circle, X


class GameBoard:

    height = 750
    width = 950
    box_height = height * 0.33
    box_width = width * 0.33

    def __init__(self, window) -> None:
        self.window = window
        self.background = (40, 40, 40)

    @property
    def window(self):
        return self._window
    
    @window.setter
    def window(self, val):
        if isinstance(val, pygame.surface.Surface):
            self._window = val

    @property
    def background(self):
        return self._background
    
    @background.setter
    def background(self, val):
        if isinstance(val, tuple) and len(val) == 3 and all(isinstance(x, int) for x in val):
            self._background = val

    def draw_board(self):
        self.window.fill(self.background)
        green = (60, 179, 113)
        for i in range(1, 3):
            y = GameBoard.box_height * i
            x = GameBoard.box_width * i
            pygame.draw.line(self.window, green, (0, y), (GameBoard.width, y), 5)
            pygame.draw.line(self.window, green, (x, 0), (x, GameBoard.height), 5)

    def draw_figures(self, table):
        for r, row in enumerate(table):
            for c, el in enumerate(row):
                if el == -1:
                    self.draw_x((r, c))
                elif el == 1:
                    self.draw_circle((r, c))

    def draw_text(self, size, text, location):
        font = pygame.font.Font(None, size)
        text_surface = font.render(text, True, (255, 255, 255))
        text_rect = text_surface.get_rect(center=location)
        self.window.blit(text_surface, text_rect)

    def draw_tie(self):
        self.draw_text(100, 'DRAW', (GameBoard.width // 2, GameBoard.height // 2))
    
    def draw_turn(self, turn):
        self.draw_text(40, f'turn: {turn}', (GameBoard.width * 0.90, GameBoard.height * 0.02))

    def draw_circle(self, cell):
        circle = Circle(self.window, cell, int(GameBoard.box_width), int(GameBoard.box_height))
        circle.draw()

    def draw_x(self, cell):
        x = X(self.window, cell, int(GameBoard.box_width), int(GameBoard.box_height))
        x.draw()

    def draw_how_to_start(self):
        self.draw_text(40, 'Press enter to start', (GameBoard.width // 2, GameBoard.height * 0.02))
