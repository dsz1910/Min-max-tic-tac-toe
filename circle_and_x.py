import pygame


class Figure:

    def __init__(self, window, cell, box_width, box_height):
        self.window = window
        self.cell = cell
        self.box_width = box_width
        self.box_height = box_height
    
    @property
    def window(self):
        return self._window
    
    @window.setter
    def window(self, val):
        if isinstance(val, pygame.surface.Surface):
            self._window = val

    @property
    def cell(self):
        return self._cell
    
    @cell.setter
    def cell(self, val):
        assert isinstance(val, tuple) and len(val) == 2 and all(0 <= x < 3 for x in val), 'Niepoprawny atrybut cell'
        self._cell = val
        

    @property
    def box_width(self):
        return self._box_width
    
    @box_width.setter
    def box_width(self, val):
        if isinstance(val, int) and val > 0:
            self._box_width = val

    @property
    def box_height(self):
        return self._box_height
    
    @box_height.setter
    def box_height(self, val):
        if isinstance(val, int) and val > 0:
            self._box_height = val

class Circle(Figure):

    color = (16, 215, 222)

    def __init__(self, window, cell, box_width, box_height):
        super().__init__(window, cell, box_width, box_height)
        self.center = (self.cell[1] * self.box_width + 0.5 * self.box_width, self.cell[0] * self.box_height + 0.5 * self.box_height)

    def draw(self):
        pygame.draw.circle(self.window, Circle.color, self.center, 100, width=10)

class X(Figure):

    color = (252, 3, 23)

    def __init__(self, window, cell, box_width, box_height):
        super().__init__(window, cell, box_width, box_height)

    def draw(self):
        pygame.draw.line(self.window, X.color, (self.cell[1] * self.box_width + 30, self.cell[0] * self.box_height + 30), (self.cell[1] * self.box_width + 284, self.cell[0] * self.box_height + 214), 10)
        pygame.draw.line(self.window, X.color, (self.cell[1] * self.box_width + 30, self.cell[0] * self.box_height + 214), (self.cell[1] * self.box_width + 284, self.cell[0] * self.box_height + 30), 10)