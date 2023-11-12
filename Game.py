
#coding=utf-8
import pygame

#Inicializo Pygame
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

#Balon
#Variables de Movimiento
velocidadPelota = 15
Pelota = pygame.image.load("segundoTpGrupalPython/Img/pelota.png").convert()

#Personaje 1 
#Variables de Movimiento
posicionX_Init = 200  #posición en x
posicionY_Init = 325  #posición en y
velocidad = 10
Personaje1 = pygame.image.load("segundoTpGrupalPython/Img/jugador1.png").convert()

#Personaje 2
#Variable de Moviento
posicionX_Init2 = 800 #posición en x
posicionY_Init2 = 325  #posición en y
velocidad = 10
Personaje2 = pygame.image.load("segundoTpGrupalPython/Img/jugador2.png").convert()


class Jugador_Uno(pygame.sprite.Sprite):
    def __init__(self):
	    # Heredamos el init de la clase Sprite de Pygame
        super().__init__()
        self.image = Personaje1
        self.rect = self.image.get_rect()
        self.rect.center = (posicionX_Init,posicionY_Init)
        BLACK= (0,0,0)
        self.image.set_colorkey(BLACK)


    def update(self):
        # Opción tecla pulsada
        keys = pygame.key.get_pressed()

        # Tecla A - Moviemiento a la izquierda
        if keys[pygame.K_a] and self.rect.left > 0:
            self.rect.x -= velocidad 

        # Tecla D - Moviemiento a la derecha
        elif keys[pygame.K_d] and self.rect.right < ANCHO :
            self.rect.x += velocidad
           
        # Tecla S - Moviemiento hacia abajo
        if keys[pygame.K_s] and self.rect.bottom < ALTO:	
            self.rect.y += velocidad
		
        # Tecla W - Moviemiento hacia abajo
        if keys[pygame.K_w] and self.rect.top > 0:	
            self.rect.y -= velocidad

class Jugador_Dos(pygame.sprite.Sprite):
    def __init__(self):
	    # Heredamos el init de la clase Sprite de Pygame
        super().__init__()
        self.image = Personaje2
        self.rect = self.image.get_rect()
        self.rect.center = (posicionX_Init2,posicionY_Init2)
        BLACK= (0,0,0)
        self.image.set_colorkey(BLACK)
    
    def update(self):
        # Opción tecla pulsada
        keys = pygame.key.get_pressed()

        # Tecla A - Moviemiento a la izquierda
        if keys[pygame.K_LEFT] and self.rect.left > 0:
            self.rect.x -= velocidad 

        # Tecla D - Moviemiento a la derecha
        elif keys[pygame.K_RIGHT] and self.rect.right < ANCHO :
            self.rect.x += velocidad
           
        # Tecla S - Moviemiento hacia abajo
        if keys[pygame.K_DOWN] and self.rect.bottom < ALTO:	
            self.rect.y += velocidad
		
        # Tecla W - Moviemiento hacia arriba
        if keys[pygame.K_UP] and self.rect.top > 0:	
            self.rect.y -= velocidad

class balonObjeto(pygame.sprite.Sprite):
    def __init__(self):
	    # Heredamos el init de la clase Sprite de Pygame
        super().__init__()
        self.image = Pelota
        self.rect = self.image.get_rect()
        self.rect.center = (ANCHO // 2,ALTO // 2)
        self.velocidad_x = 0 # Velocidad inicial en x
        self.velocidad_y = 0 # Velocidad inicial en y
        BLACK= (0,0,0)
        self.image.set_colorkey(BLACK)
    
    def update(self):
        # Colision de jugador 1 con el balon
        if self.rect.colliderect(Jugador_1.rect):
            intersection = self.rect.clip(Jugador_1.rect)

            # Verifica la cara de colisión con el jugador
            if intersection.width > intersection.height:
                # Colisión vertical
                if self.rect.centery < Jugador_1.rect.centery:
                    self.rect.bottom = Jugador_1.rect.top
                    self.velocidad_y = -velocidadPelota
                else:
                    self.rect.top = Jugador_1.rect.bottom
                    self.velocidad_y = velocidadPelota
            else:
                # Colisión horizontal
                if self.rect.centerx < Jugador_1.rect.centerx:
                    self.rect.right = Jugador_1.rect.left
                    self.velocidad_x = -velocidadPelota
                else:
                    self.rect.left = Jugador_1.rect.right
                    self.velocidad_x = velocidadPelota
                    
            if self.velocidad_x > 0:
                self.velocidad_x = velocidadPelota  # Colisión desde la derecha, cambia a la izquierda
            elif self.velocidad_x <=0:
                self.velocidad_x = -velocidadPelota  # Colisión desde la izquierda, cambia a la derecha
            
            if self.velocidad_y > 0:
                self.velocidad_y = velocidadPelota  # Colisión desde abajo, cambia a arriba
            elif self.velocidad_y <= 0:
                self.velocidad_y = -velocidadPelota  # Colisión desde arriba, cambia a abajo
                     
         # Colision de jugador 2 con el balon
        
        # Colision de jugador 2 con el balon
        if self.rect.colliderect(Jugador_2.rect):
            intersection2 = self.rect.clip(Jugador_2.rect)
           
            # Verifica la cara de colisión con el jugador
            if intersection2.width > intersection2.height:
                # Colisión vertical
                if self.rect.centery < Jugador_2.rect.centery:
                    self.rect.bottom = Jugador_2.rect.top
                    self.velocidad_y = -velocidadPelota
                else:
                    self.rect.top = Jugador_2.rect.bottom
                    self.velocidad_y = velocidadPelota
            else:
                # Colisión horizontal
                if self.rect.centerx < Jugador_2.rect.centerx:
                    self.rect.right = Jugador_2.rect.left
                    self.velocidad_x = -velocidadPelota
                else:
                    self.rect.left = Jugador_2.rect.right
                    self.velocidad_x = velocidadPelota
                
            if self.velocidad_x > 0:
                self.velocidad_x = velocidadPelota  # Colisión desde la derecha, cambia a la izquierda
            elif self.velocidad_x <=0:
                self.velocidad_x = -velocidadPelota  # Colisión desde la izquierda, cambia a la derecha
            
            if self.velocidad_y > 0:
                self.velocidad_y = velocidadPelota  # Colisión desde abajo, cambia a arriba
            elif self.velocidad_y <= 0:
                self.velocidad_y = -velocidadPelota  # Colisión desde arriba, cambia a abajo
        

        # Verifica si ha alcanzado el límite derecho o izquierdo y revierte la dirección si es necesario
        if self.rect.right >= ANCHO:
            self.velocidad_x = -abs(self.velocidad_x)  # Invierte la dirección (positiva a negativa) al tocar el límite derecho
        elif self.rect.left <= 0:
            self.velocidad_x = abs(self.velocidad_x)  # Invierte la dirección (negativa a positiva) al tocar el límite izquierdo

        if self.rect.top >= ALTO-50:
            self.velocidad_y = -abs(self.velocidad_y)  # Invierte la dirección (positiva a negativa) al tocar el límite inferior
        elif self.rect.bottom <= 30:
            self.velocidad_y = abs(self.velocidad_y)  # Invierte la dirección (negativa a positiva) al tocar el límite superior
        
        self.rect.x += self.velocidad_x       
        self.rect.y += self.velocidad_y
        
            
# Grupo de sprites y balon
sprites = pygame.sprite.Group()
balon_objeto = pygame.sprite.Group()

#instanciacion del Balon
Balon = balonObjeto()
balon_objeto.add(Balon)

#instanciacion de Jugador 1
Jugador_1 = Jugador_Uno()
sprites.add(Jugador_1)

#instanciacion de Jugador 2
Jugador_2 = Jugador_Dos()
sprites.add(Jugador_2)

#Bucle del Juego y Controles 
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
    balon_objeto.update()
    sprites.update()
    
    #Dibujo Sprites y Balon
    sprites.draw(PANTALLA)
    balon_objeto.draw(PANTALLA)

    pygame.display.update()
   
pygame.quit()

