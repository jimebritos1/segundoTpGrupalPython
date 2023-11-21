#coding=utf-8
import pygame

#Inicializo Pygame y Mixer de Musica
pygame.init()
pygame.mixer.init()

#Colores constantes
BLACK = (0,0,0)
WHITE = (255,255,255)

#Tamaño de la Pantalla
ANCHO=1000
ALTO=650
PANTALLA = pygame.display.set_mode((ANCHO, ALTO))
pygame.display.set_caption("Pygame Test")

#Cancha de Futbol
CanchaFutbol=pygame.image.load("Img/Background.png").convert()
PANTALLA.blit(CanchaFutbol,(0,0))

#Control de Velocidad
reloj = pygame.time.Clock()
FPS=60

#Balon
#Variables de Movimiento
velocidadPelota = 8
Pelota = pygame.image.load("Img/pelota.png")

#Personaje 1 
#Variables de Movimiento
posicionX_Init = 200  #posición en x
posicionY_Init = 325  #posición en y
velocidad = 6
Personaje1 = pygame.image.load("Img/archie.png")

#Personaje 2
#Variable de Moviento
posicionX_Init2 = 800 #posición en x
posicionY_Init2 = 325  #posición en y
velocidad = 6
Personaje2 = pygame.image.load('Img/lucas.png')

# Cargar la imagen de fondo para el ingreso de nombres
fondo_ingreso_nombres = pygame.image.load("Img/estadio.jpg") 
fondo_ingreso_nombres = pygame.transform.scale(fondo_ingreso_nombres, (ANCHO, ALTO))  

# Nombres de los jugadores
nombre_jugador_1 = ""
nombre_jugador_2 = ""

# Pantalla de ingreso de nombres
ingresando_nombres = True
jugador_actual = 1  # Jugador 1 empieza ingresando su nombre

#Sonidos
SoundBalon = pygame.mixer.Sound("Sounds/Ball-Football-Kick.mp3")
SoundGol = pygame.mixer.Sound("Sounds/GolConversion.mp3")
pygame.mixer.music.load("Sounds/EstadioSonidoFondo.mp3")
pygame.mixer.music.set_volume(0.5)
pygame.mixer.music.play(loops=-1)

'''Bucle para Ingresar los nombres'''
while ingresando_nombres:
    for event in pygame.event.get():
    
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RETURN:
                # Si se presiona Enter, cambiamos al siguiente jugador o salimos del bucle
                if jugador_actual == 1:
                    jugador_actual = 2
                else:
                    ingresando_nombres = False
            elif event.key == pygame.K_BACKSPACE:
                # Si se presiona Retroceso, borramos el último carácter del nombre actual
                if jugador_actual == 1:
                    nombre_jugador_1 = nombre_jugador_1[:-1]
                else:
                    nombre_jugador_2 = nombre_jugador_2[:-1]
            elif event.unicode.isalnum():
                # Si se presiona una tecla alfanumérica, la agregamos al nombre actual
                if jugador_actual == 1:
                    nombre_jugador_1 += event.unicode
                else:
                    nombre_jugador_2 += event.unicode

    # Llenar la pantalla con negro antes de blit de la imagen de fondo
    PANTALLA.fill(BLACK)
    
    # Blit de la imagen de fondo
    PANTALLA.blit(fondo_ingreso_nombres, (0, 0))

    # Texto de instrucciones
    font_instrucciones = pygame.font.Font(None, 36)
    texto_instrucciones = font_instrucciones.render("Ingrese su nombre y presione Enter", True, WHITE)
    PANTALLA.blit(texto_instrucciones, (ANCHO // 2 - texto_instrucciones.get_width() // 2, ALTO // 4))

    # Ingreso de nombre del Jugador 1
    font_nombre = pygame.font.Font(None, 48)
    texto_nombre_1 = font_nombre.render("Nombre Jugador 1: " + nombre_jugador_1, True, WHITE)
    PANTALLA.blit(texto_nombre_1, (ANCHO // 4, ALTO // 2))

    # Ingreso de nombre del Jugador 2
    texto_nombre_2 = font_nombre.render("Nombre Jugador 2: " + nombre_jugador_2, True, WHITE)
    PANTALLA.blit(texto_nombre_2, (ANCHO // 4, ALTO // 2 + 60))

    pygame.display.update()

class Jugador_Uno(pygame.sprite.Sprite):
    def __init__(self, nombre):
	    # Heredamos el init de la clase Sprite de Pygame
        super().__init__()
        self.goles = 0
        self.nombre = nombre
        self.sheet = Personaje1
        self.sheet.set_clip(pygame.Rect(0, 0, 52, 76))
        self.image = self.sheet.subsurface(self.sheet.get_clip())
        self.rect = self.image.get_rect()
        self.rect.center = (posicionX_Init,posicionY_Init)
        self.frame = 0
        self.left_states = { 0: (0, 76, 52, 76), 1: (52, 76, 52, 76), 2: (156, 76, 52, 76) }
        self.right_states = { 0: (0, 152, 52, 76), 1: (52, 152, 52, 76), 2: (156, 152, 52, 76) }
        self.up_states = { 0: (0, 228, 52, 76), 1: (52, 228, 52, 76), 2: (156, 228, 52, 76) }
        self.down_states = { 0: (0, 0, 52, 76), 1: (52, 0, 52, 76), 2: (156, 0, 52, 76) }
        self.image.set_colorkey(BLACK)
        self.image.set_colorkey(WHITE)

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


    def update(self):
        # Opción tecla pulsada
        keys = pygame.key.get_pressed()

        # Tecla A - Moviemiento a la izquierda
        if keys[pygame.K_a] and self.rect.left > 0:
            self.clip(self.left_states)
            self.rect.x -= velocidad 

        # Tecla D - Moviemiento a la derecha
        elif keys[pygame.K_d] and self.rect.right < ANCHO :
            self.clip(self.right_states)
            self.rect.x += velocidad
           
        # Tecla S - Moviemiento hacia abajo
        if keys[pygame.K_s] and self.rect.bottom < ALTO:
            self.clip(self.down_states)
            self.rect.y += velocidad
		
        # Tecla W - Moviemiento hacia arriba
        if keys[pygame.K_w] and self.rect.top > 0:	
            self.clip(self.up_states)
            self.rect.y -= velocidad
        self.image = self.sheet.subsurface(self.sheet.get_clip())

class Jugador_Dos(pygame.sprite.Sprite):
    def __init__(self, nombre):
	    # Heredamos el init de la clase Sprite de Pygame
        super().__init__()
        self.sheet = Personaje2
        self.sheet.set_clip(pygame.Rect(0, 0, 52, 76))
        self.image = self.sheet.subsurface(self.sheet.get_clip())
        self.rect = self.image.get_rect()
        self.rect.center = (posicionX_Init2,posicionY_Init2)
        self.frame = 0
        self.left_states = { 0: (0, 76, 52, 76), 1: (52, 76, 52, 76), 2: (156, 76, 52, 76) }
        self.right_states = { 0: (0, 152, 52, 76), 1: (52, 152, 52, 76), 2: (156, 152, 52, 76) }
        self.up_states = { 0: (0, 228, 52, 76), 1: (52, 228, 52, 76), 2: (156, 228, 52, 76) }
        self.down_states = { 0: (0, 0, 52, 76), 1: (52, 0, 52, 76), 2: (156, 0, 52, 76) }
        self.goles = 0
        self.nombre = nombre

        
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
    
    def update(self):
        # Opción tecla pulsada
        keys = pygame.key.get_pressed()

        # Tecla A - Moviemiento a la izquierda
        if keys[pygame.K_LEFT] and self.rect.left > 0:
            self.clip(self.left_states)
            self.rect.x -= velocidad 

        # Tecla D - Moviemiento a la derecha
        elif keys[pygame.K_RIGHT] and self.rect.right < ANCHO :
            self.clip(self.right_states)
            self.rect.x += velocidad
           
        # Tecla S - Moviemiento hacia abajo
        if keys[pygame.K_DOWN] and self.rect.bottom < ALTO:
            self.clip(self.down_states)	
            self.rect.y += velocidad
		
        # Tecla W - Moviemiento hacia arriba
        if keys[pygame.K_UP] and self.rect.top > 0:	
            self.clip(self.up_states)
            self.rect.y -= velocidad
        self.image = self.sheet.subsurface(self.sheet.get_clip())

class balonObjeto(pygame.sprite.Sprite):
    def __init__(self):
	    # Heredamos el init de la clase Sprite de Pygame
        super().__init__()
        self.image = Pelota
        self.rect = self.image.get_rect()
        self.rect.center = (ANCHO // 2,ALTO // 2)
        self.velocidad_x = 0 # Velocidad inicial en x
        self.velocidad_y = 0 # Velocidad inicial en y
    
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
                    SoundBalon.play()
                else:
                    self.rect.top = Jugador_1.rect.bottom
                    self.velocidad_y = velocidadPelota
                    SoundBalon.play()
            else:
                # Colisión horizontal
                if self.rect.centerx < Jugador_1.rect.centerx:
                    self.rect.right = Jugador_1.rect.left
                    self.velocidad_x = -velocidadPelota
                    SoundBalon.play()
                else:
                    self.rect.left = Jugador_1.rect.right
                    self.velocidad_x = velocidadPelota
                    SoundBalon.play()
                    
            if self.velocidad_x > 0:
                self.velocidad_x = velocidadPelota  # Colisión desde la derecha, cambia a la izquierda
            elif self.velocidad_x <=0:
                self.velocidad_x = -velocidadPelota  # Colisión desde la izquierda, cambia a la derecha
            if self.velocidad_y > 0:
                self.velocidad_y = velocidadPelota  # Colisión desde abajo, cambia a arriba
            elif self.velocidad_y <= 0:
                self.velocidad_y = -velocidadPelota  # Colisión desde arriba, cambia a abajo
                     
        # Colision de jugador 2 con el balon
        if self.rect.colliderect(Jugador_2.rect):
            intersection2 = self.rect.clip(Jugador_2.rect)
           
            # Verifica la cara de colisión con el jugador
            if intersection2.width > intersection2.height:
                # Colisión vertical
                if self.rect.centery < Jugador_2.rect.centery:
                    self.rect.bottom = Jugador_2.rect.top
                    self.velocidad_y = -velocidadPelota
                    SoundBalon.play()
                else:
                    self.rect.top = Jugador_2.rect.bottom
                    self.velocidad_y = velocidadPelota
                    SoundBalon.play()
            else:
                # Colisión horizontal
                if self.rect.centerx < Jugador_2.rect.centerx:
                    self.rect.right = Jugador_2.rect.left
                    self.velocidad_x = -velocidadPelota
                    SoundBalon.play()
                else:
                    self.rect.left = Jugador_2.rect.right
                    self.velocidad_x = velocidadPelota
                    SoundBalon.play()
                
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
Objetos = pygame.sprite.Group()

#instanciacion del Balon
Balon = balonObjeto()
Objetos.add(Balon)

#instanciacion de Jugador 1 con nombre
Jugador_1 = Jugador_Uno(nombre_jugador_1)
sprites.add(Jugador_1)

#instanciacion de Jugador 2 con nombre
Jugador_2 = Jugador_Dos(nombre_jugador_2)
sprites.add(Jugador_2)

'''VARIABLES Y FUNCIONES DEL ARCO'''
# Dimensiones del arco
ancho_del_arco = 100
alto_del_arco = 200

# Coordenadas del centro de la cancha
centro_x = ANCHO // 2
centro_y = ALTO // 2

# Coordenadas de los arcos
arco_derecho_x = centro_x + ANCHO // 2   # Ajustado para que el arco derecho esté en el extremo derecho de la pantalla
arco_izquierdo_x = centro_x - ANCHO // 2  # Ajustado para que el arco izquierdo esté en el extremo izquierdo de la pantalla
arco_y = centro_y - alto_del_arco // 2

# Fuente y tamaño del texto
font = pygame.font.Font(None, 36)

def mostrar_puntaje():
    # Renderizar el puntaje de los jugadores
    puntaje_jugador_1 = font.render(f"{Jugador_1.nombre}: {Jugador_1.goles}", True, WHITE)
    puntaje_jugador_2 = font.render(f"{Jugador_2.nombre}: {Jugador_2.goles}", True, WHITE)

    # Posicionamiento en la pantalla
    PANTALLA.blit(puntaje_jugador_1, (10, 10))
    PANTALLA.blit(puntaje_jugador_2, (ANCHO - puntaje_jugador_2.get_width() - 10, 10))

def Verif_Gol():
    if (
    arco_izquierdo_x <= Balon.rect.centerx <= arco_izquierdo_x + ancho_del_arco
    and arco_y <= Balon.rect.centery <= arco_y + alto_del_arco
    ):
        # Gol del Jugador 2
        Jugador_2.goles += 1
        SoundGol.play()
        # Reiniciar posiciones
        Jugador_1.rect.center = (posicionX_Init, posicionY_Init)
        Jugador_2.rect.center = (posicionX_Init2, posicionY_Init2)
        Balon.rect.center = (ANCHO // 2, ALTO // 2)

    elif (
    arco_derecho_x - ancho_del_arco <= Balon.rect.centerx <= arco_derecho_x
    and arco_y <= Balon.rect.centery <= arco_y + alto_del_arco
    ):
        # Gol del Jugador 1
        Jugador_1.goles += 1
        SoundGol.play()
        # Reiniciar posiciones
        Jugador_1.rect.center = (posicionX_Init, posicionY_Init)
        Jugador_2.rect.center = (posicionX_Init2, posicionY_Init2)
        Balon.rect.center = (ANCHO // 2, ALTO // 2)
        
        # Detener el movimiento de la pelota
        Balon.velocidad_x = 0
        Balon.velocidad_y = 0

'''BUCLE DE JUEGO '''
running = True
while running:
    # FPS
    reloj.tick(FPS)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Verificar si la tecla Escape está presionada
    keys = pygame.key.get_pressed()
    if keys[pygame.K_ESCAPE]:
        running = False

    # Actualizar Sprites y Balón
    Objetos.update()
    sprites.update()

    # Verificar si se ha marcado un gol
    Verif_Gol()

    #Recargo la Pantalla (Evito la superoposicion)
    PANTALLA.blit(CanchaFutbol, (0, 0))

    #Actualizacion de Sprites
    Objetos.update()
    sprites.update()
    
    #Dibujo Sprites y Balon
    PANTALLA.blit(CanchaFutbol, (0, 0))
    sprites.draw(PANTALLA)
    Objetos.draw(PANTALLA)
    mostrar_puntaje()
    
    pygame.display.update()
   
pygame.quit()

