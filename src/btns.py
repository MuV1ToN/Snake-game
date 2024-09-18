import pygame as pg

# Кнопка с цветом
class ColorButton:
    def __init__(self, x, y, width, height, text,  not_active_color, size_text=None, font_text=None,  active_color = None, sound_path = None):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.text = text
        self.size = 36
        if size_text:
            self.size = size_text
        self.font = None
        if font_text:
            self.font = font_text
        self.NAcolor = not_active_color
        self.Acolor = None
        if active_color:
            self.Acolor = active_color
        self.surf = pg.Surface((width, height))
        self.rect = self.surf.get_rect(topleft=(x, y))
        self.sound = None
        if sound_path:
            self.sound = pg.mixer.Sound(sound_path)
        self.is_hoverd = False
            
    def draw(self, screen):
        curent_color = self.Acolor if self.is_hoverd else self.NAcolor
        screen.blit(self.surf, (self.x, self.y))
        self.surf.fill(curent_color)
        font = pg.font.SysFont(self.font, self.size)
        text_surface = font.render(self.text, True, (255, 255, 255))
        text_rect = text_surface.get_rect(center=self.rect.center)
        screen.blit(text_surface, text_rect)
        
    def update(self, mouse_pos, event):
        self.is_hoverd = self.rect.collidepoint(mouse_pos)
        if event.type == pg.MOUSEBUTTONDOWN and event.button == 1 and self.is_hoverd:
            if self.sound:
                self.sound.play()
            pg.event.post(pg.event.Event(pg.USEREVENT, button=self))

# Кнопка с картинкой
class ImageButton:
    def __init__(self, x, y, width, height, text, image_path, hoever_image_path=None, sound_path=None):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.text = text
        
        self.image = pg.image.load(image_path)
        self.image = pg.transform.scale(self.image, (width, height))
        self.hover_image = self.image
        if hoever_image_path:
            self.hover_image = pg.image.load(hoever_image_path)
            self.hover_image = pg.transform.scale(self.hover_image, (width, height))
        self.rect = self.image.get_rect(topleft = (x, y))
        self.sound = None
        if sound_path:
            self.sound = pg.mixer.Sound(sound_path)
        self.is_hoverd = False
        
    def draw(self, screen):
        current_image = self.hover_image if self.is_hoverd else self.image
        screen.blit(current_image, self.rect.topleft)
        
        font = pg.font.Font(None, 36)
        text_surface = font.render(self.text, True, (255, 255, 255))
        text_rect = text_surface.get_rect(center=self.rect.center)
        screen.blit(text_surface, text_rect)
    
    def update(self, mouse_pos, event):
        self.is_hoverd = self.rect.collidepoint(mouse_pos)
        if event.type == pg.MOUSEBUTTONDOWN and event.button == 1 and self.is_hoverd:
            if self.sound:
                self.sound.play()
            pg.event.post(pg.event.Event(pg.USEREVENT, button=self))
    
        
        