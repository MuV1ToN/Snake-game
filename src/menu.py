import pygame as pg
from src.settings import *
from src.btns import ColorButton, ImageButton
from src.game import Game
from src.gameDUO import DuoGame
from src.text import Text


class Menu:
    def __init__(self):
        pg.init()
        self.screen = pg.display.set_mode((0, 0), pg.FULLSCREEN)
        pg.display.set_caption('Меню')
        self.clock = pg.time.Clock()
        self.background = pg.image.load('src\images\\background.jpg')
        pg.mixer.music.load('src\sounds\\background_sound.mp3')
        
    def run(self):
        btns = [
            # Кнопки
            play := ColorButton(x=self.screen.get_width()/2-125, y = self.screen.get_height()/2-100, 
                                width=250, height=70, 
                                text='Играть', size_text=40, 
                                not_active_color=(81, 158, 117), 
                                active_color=(158, 81, 81), 
                                sound_path='src/sounds/click.mp3'),
            
            play_duo := ColorButton(x=self.screen.get_width()/2-125, y = self.screen.get_height()/2, 
                                    width=250, height=70, 
                                    size_text=40,text='Играть дуо', 
                                    not_active_color=(81, 158, 117),active_color=(158, 81, 81), 
                                    sound_path='src/sounds/click.mp3'),
            
            exit := ColorButton(x=self.screen.get_width()/2-125, y = self.screen.get_height()/2+100, 
                                width=250, height=70, 
                                text='Выход', size_text=40,
                                not_active_color=(81, 158, 117),  
                                active_color=(158, 81, 81), 
                                sound_path='src/sounds/click.mp3'),
        ]
        pg.mixer.music.play()
        pg.mixer.music.set_volume(0.025)
        
        while True:
            
            self.screen.fill(color['black'])
            self.screen.blit(self.background, ((0, 0)))
            for event in pg.event.get():
                if event.type == pg.QUIT:
                    return False
                
                if event.type == pg.USEREVENT and event.button == play:
                    pg.mixer.music.stop()
                    game = Game()
                    game.run()
                
                if event.type == pg.USEREVENT and event.button == play_duo:
                    pg.mixer.music.stop()
                    gameDUO = DuoGame()
                    gameDUO.run()
                  
                if event.type == pg.USEREVENT and event.button == exit:
                    return False
                
                for btn in btns:
                    btn.update(pg.mouse.get_pos(), event)
            
            for btn in btns:
                btn.draw(self.screen)
                
            title = Text(screen=self.screen, x=self.screen.get_width()/2, y=30, text='Зеленый змей',text_color=(81, 158, 117), text_size=300)
            title.draw()
            pg.display.update()
            
                    
