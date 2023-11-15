# -*- coding: utf-8 -*-

import pygame
pygame.init()

#Tamaño de la Pantalla
ANCHO=1000
ALTO=650
PANTALLA = pygame.display.set_mode((ANCHO, ALTO))
pygame.display.set_caption("Pygame Test")

#Cancha de Futbol
CanchaFutbol=pygame.image.load("segundoTpGrupalPython/Img/Background.png").convert()
PANTALLA.blit(CanchaFutbol,(0,0))

#Control de Velocidad
reloj = pygame.time.Clock()
FPS=60

class Personaje1(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()  # Llamada al constructor de la clase base
        self.sheet = pygame.image.load("segundoTpGrupalPython/Img/kate.png")
        self.sheet.set_clip(pygame.Rect(0, 0, 52, 76))
        self.image = self.sheet.subsurface(self.sheet.get_clip())
        self.rect = self.image.get_rect()
        self.rect.topleft = position
        self.frame = 0
        self.left_states = { 0: (0, 76, 52, 76), 1: (52, 76, 52, 76), 2: (156, 76, 52, 76) }
        self.right_states = { 0: (0, 152, 52, 76), 1: (52, 152, 52, 76), 2: (156, 152, 52, 76) }
        self.up_states = { 0: (0, 228, 52, 76), 1: (52, 228, 52, 76), 2: (156, 228, 52, 76) }
        self.down_states = { 0: (0, 0, 52, 76), 1: (52, 0, 52, 76), 2: (156, 0, 52, 76) }

    def get_frame(self, frame_set):
        self.frame += 1
        if self.frame > (len(frame_set) - 1):
            self.frame = 0
        return frame_set[self.frame]

    def clip(self, clipped_rect):
        if type(clipped_rect) is dict:
            self.sheet.set_clip(pygame.Rect(self.get_frame(clipped_rect)))
        else:
            self.sheet.set_clip(pygame.Rect(clipped_rect))
        return clipped_rect

    def update(self, direction):
        if direction == 'left':
            self.clip(self.left_states)
            self.rect.x -= 5
        if direction == 'right':
            self.clip(self.right_states)
            self.rect.x += 5
        if direction == 'up':
            self.clip(self.up_states)
            self.rect.y -= 5
        if direction == 'down':
            self.clip(self.down_states)
            self.rect.y += 5
            print("entro")
        self.image = self.sheet.subsurface(self.sheet.get_clip())
    '''
        if direction == 'stand_left':
            self.clip(self.left_states[0])
        if direction == 'stand_right':
            self.clip(self.right_states[0])
        if direction == 'stand_up':
            self.clip(self.up_states[0])
        if direction == 'stand_down':
            self.clip(self.down_states[0])
    '''
   

    def handle_event(self, event):
        if event.type == pygame.QUIT:
            game_over = True

        if event.type == pygame.KEYDOWN:

            if event.key == pygame.K_LEFT:
                self.update('left')
            if event.key == pygame.K_RIGHT:
                self.update('right')
            if event.key == pygame.K_UP:
                self.update('up')
            if event.key == pygame.K_DOWN:
                self.update('down')
                print("entro")
'''
        if event.type == pygame.KEYUP:

            if event.key == pygame.K_LEFT:
                self.update('stand_left')
            if event.key == pygame.K_RIGHT:
                self.update('stand_right')
            if event.key == pygame.K_UP:
                self.update('stand_up')
            if event.key == pygame.K_DOWN:
                self.update('stand_down')'''

# Grupo de sprites
sprites = pygame.sprite.Group()

#instanciacion de Jugador 1
Jugador_1 = Personaje1((ANCHO // 2, ALTO // 2))
sprites.add(Jugador_1)

running = True
while running:
    # FPS
    reloj.tick(FPS)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if pygame.key.get_pressed()[pygame.K_ESCAPE]:
            running = False          

    
    #Recargo la Pantalla (Evito la superoposicion)
    PANTALLA.blit(CanchaFutbol, (0, 0))

    #Actualizacion de Sprites
    sprites.update("down")
    
    #Dibujo Sprites y Balon
    sprites.draw(PANTALLA)
   

    pygame.display.update()
   
pygame.quit()

