import pygame as pg
from src.settings import *
from src.snake import Snake
from src.food import Food
from src.text import Text

class Game:
    def __init__(self):
        pg.init()
        self.screen = pg.display.set_mode((0, 0), pg.FULLSCREEN)
        pg.display.set_caption('Зеленый змей')
        self.clock = pg.time.Clock()
        
    def run(self):
        snake = Snake(self.screen, 20, color['green'], control['p1'])
        food = Food(self.screen, snake.size, color['red'])
        while True:
            # Фон игры
            self.screen.fill(color['black'])
            # Получение событий
            for event in pg.event.get():
                # Если нажата кнопка выход
                if event.type == pg.QUIT:
                    return False
                
                # Выхож по нажатие кнопки "ESC"
                if event.type == pg.KEYDOWN:    
                    if event.key == pg.K_ESCAPE:
                        pg.mixer.music.play()
                        return False
                    
            # Вывод еды и змеки, а также работа логики змейки
            food.draw()   
            if snake.check_сollision() == True:
                return False
            if snake.check_eat_pos(food.position):
                snake.grow()
                food.new_position()
            snake.change_direction()                      
            snake.move()
            snake.draw()
            
            # Вывыод счета
            score = Text(self.screen, snake.size*2, snake.size, score:=f'Счёт: {len(snake.body)-1}', color['white'], text_size=20)
            score.draw()
            # Обновление экрана
            pg.display.flip()
            self.clock.tick(FPS)
            
