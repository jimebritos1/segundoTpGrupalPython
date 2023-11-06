import pygame,sys
pygame.init()

#Definir Colores

BLACK = (0,    0,   0)
WHITE = (255, 255, 255)
GREEN = (0,   255,  0)
RED   = (255 ,  0,  0)
BLUE  = (0,    0, 255)

size = (800,500)

#Crear Ventana
screen = pygame.display.set_mode(size)

# Controlar FPS
# Se usa para gestionar cuan rápido se actualiza la pantalla
clock = pygame.time.Clock()

# Coordenadas del cuadrado 
cord_x = 400
cord_y = 200

# Velocidad a la que se movera el cuadrado
speed_x = 3
speed_y = 3

# TODOS LOS EVENTOS DE PROCESAMIENTO DEBERÍAN IR DEBAJO DE ESTE COMENTARIO
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
# TODOS LOS EVENTOS DE PROCESAMIENTO DEBERÍAN IR ENCIMA DE ESTE COMENTARIO    
    # Hacemos que rebote 
           
# TODA LA LÓGICA DEL JUEGO DEBERÍA IR DEBAJO DE ESTE COMENTARIO          
    if (cord_x >720 or cord_x <0):
        speed_x *= -1
        
    cord_x += speed_x
    
# TODA LA LÓGICA DEL JUEGO DEBERÍA IR ENCIMA DE ESTE COMENTARIO  
    
    
#EL CÓDIGO DE DIBUJO DEBERÍA IR DEBAJO DE ESTE COMENTARIO
    
    # Limpia la ventana y establece el color del fondo
    screen.fill(WHITE)
    ### ---- ZONA DE DIBUJO
    
    pygame.draw.rect(screen,RED,(cord_x,cord_y,80,80))
    pygame.draw.line(screen, GREEN, [0,100], [100,100],5)
    
    ### --- ZONA DE DIBUJO 
# EL CÓDIGO DE DIBUJO DEBERÍA IR ENCIMA DE ESTE COMENTARIO

    # Actualizar pantalla
    pygame.display.flip()
    clock.tick(60)
