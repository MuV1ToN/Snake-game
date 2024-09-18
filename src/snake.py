import pygame as  pg


class Snake:
    def __init__(self, screen, size , color, control):
        self.screen = screen
        self.size = size
        self.color = color
        self.control = control
        self.direction = None
        self.body = [(self.screen.get_width()/2,
                    self.screen.get_height()/2)]
    
    # Отображение змейки   
    def draw(self):
        for x, y in self.body:
            pg.draw.rect(self.screen, self.color, [x, y, self.size, self.size])
    
    # Движение
    def move(self):
        x, y = self.body[0]
        # Проверка куда двигается змейка
        if self.direction == 'right':
            x += self.size
        if self.direction == 'left':
            x -= self.size
        if self.direction == 'up':
            y -= self.size
        if self.direction == 'down':
            y += self.size
        # Проверка границы для перехода на паралельную сторону
        if x < 0:
            x = self.screen.get_width()
        if x > self.screen.get_width():
            x = 0
        if y < 0:
            y = self.screen.get_height()
        if y > self.screen.get_height():
            y = 0
        self.body.insert(0, (x,y))
        self.body.pop()
    
    # Смена направления змейки
    def change_direction(self):
        press = pg.key.get_pressed()
        if press[self.control['right']] and self.direction != 'left':
            self.direction = 'right'
        elif press[self.control['left']] and self.direction != 'right':
            self.direction = 'left'
        elif press[self.control['up']] and self.direction != 'down':
            self.direction = 'up'
        elif press[self.control['down']] and self.direction != 'up':
            self.direction = 'down'
    
    # Проверка на съедание еды 
    def check_eat_pos(self, food):
        if self.body[0] == food:
            return True
        return False
    
    # Рост змейки
    def grow(self):
        self.body.append(self.body[-1])
    
    # Проверка на врезание в саму себя 
    def check_сollision(self):
        for body in self.body[1:]:
            if self.body[0] == body:
                return True
        return False
    
    


