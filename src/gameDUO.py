import pygame as pg
from src.settings import *
from src.snake import Snake
from src.food import Food

class DuoGame:
    def __init__(self):
        pg.init()
        self.screen = pg.display.set_mode((0, 0), pg.FULLSCREEN)
        pg.display.set_caption('Змейка на 2оих')
        self.clock = pg.time.Clock()
        
    def run(self):
        snakes = [
            p1 := Snake(self.screen, 20, color['green'], control['p1']),
            p2 := Snake(self.screen, 20, color['blue'], control['p2'])  
        ]
        p1.direction = 'left'
        p2.direction = 'right'
        
        food = Food(self.screen, p1.size, color['red'])
        
        
        while True:
            self.screen.fill(color['black'])
            for event in pg.event.get():
                if event.type == pg.QUIT:
                    return False
                
                if event.type == pg.KEYDOWN:
                    if event.key == pg.K_ESCAPE:
                        pg.mixer.music.play()
                        return False
                        
                         
            for snake in snakes:
                food.draw()
                if snake.check_сollision() == True:
                    return False
                if snake.check_eat_pos(food.position):
                    snake.grow()
                    food.new_position()
                snake.change_direction()
                snake.move()
                snake.draw()
                
            if p1.body[0] in p2.body:
                return False
            if p2.body[0] in p1.body:
                return False
            
            
            pg.display.flip()
            self.clock.tick(FPS)
            

# if __name__ == '__main__':
#     duogmae = DuoGame()
#     duogmae.run()