import pygame as pg

class Text:
    def __init__(self, screen, x, y, text, text_color, text_size=None, font=None):
        self.screen = screen
        self.x = x
        self.y = y
        self.text = str(text)
        self.Tcolor = text_color
        self.colorSP = None
        self.size = 36
        if text_size:
            self.size = text_size
        self.font = None
        if font:
            self.font = font
            
    def draw(self):
        font = pg.font.Font(None, self.size)
        text_width, _  = font.size(self.text)
        text_surf = font.render(self.text, True, self.Tcolor)
        text_surf2 = font.render(self.text, True, (0, 0, 0))
        text_rect = (self.x-text_width/2, self.y)
        text_rect2 = (self.x-text_width/2+10, self.y)
        self.screen.blit(text_surf2, text_rect2)
        self.screen.blit(text_surf, text_rect)
            
        