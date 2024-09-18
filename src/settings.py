import pygame as pg

FPS = 15

color = {
    "black":(0, 0, 0),
    "white":(255, 255, 255),
    "red":(255, 0, 0),
    "green":(0, 255, 0),
    "blue":(0, 0, 255)
}


control = {
    'p1':{
        'right':pg.K_d,
        'left':pg.K_a,
        'up':pg.K_w,
        'down':pg.K_s
        },

    'p2':{
        'right':pg.K_RIGHT,
        'left':pg.K_LEFT,
        'up':pg.K_UP,
        'down':pg.K_DOWN
        }   
}

