import pygame as pg
import random

class Food:
    def __init__(self, screen, size, color):
        self.screen = screen
        self.size = size
        self.position = (
            random.randint(0, self.screen.get_width() - self.size) // self.size*self.size,
            random.randint(0, self.screen.get_height() - self.size) // self.size*self.size
            )
        self.color = color
        
    def draw(self):
        pg.draw.rect(self.screen, self.color, 
                     [self.position[0], 
                      self.position[1], 
                      self.size, self.size])
        
    def new_position(self): 
        self.position = (
            random.randint(0, self.screen.get_width() - self.size) // self.size*self.size,
            random.randint(0, self.screen.get_height() - self.size) // self.size*self.size
            )
        
    # def cheak_eat(self, snake):
    #     if self.position == snake[0]:
    #         self.new_position()
    #         return True
    #     return False
    