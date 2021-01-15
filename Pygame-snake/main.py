import pygame

# Inicializando o Pygame e criando uma janela
pygame.init()
display = pygame.display.set_mode([840, 480]) 
pygame.display.set_caption("Meu jogo")


def draw():
    display.fill([82, 8, 128])


gameLoop = True
if __name__== "__main__":
    while gameLoop:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                gameLoop = False

        draw()
        pygame.display.update()
