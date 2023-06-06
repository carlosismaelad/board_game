
import pygame

class Figure:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.width = 50
        self.height = 50
        self.selected = False
    
    def select_position(self, x, y):
        self.x = x
        self.y = y
    
    def get_rect(self):
        return pygame.Rect(self.x - self.width/2, self.y - self.height/2, self.width, self.height)
    