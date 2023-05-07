import pygame

ALVO ='Projeto---Equipe-5/assets/imgs/sport-recife.png'
LARGURA = 1280
ALTURA = 720
pygame.init()
screen = pygame.display.set_mode((LARGURA,ALTURA))
class Alvo(pygame.sprite.Sprite):
    def __init__(self,image, rect, pos_x, pos_y):
        super().__init__()
        self.image = image
        self.rect = rect
        self.rect.center = [pos_x, pos_y]


testando1 = pygame.image.load(ALVO).convert_alpha()
testando1 = pygame.transform.scale(testando1, (100,100))
testando2 = testando1.get_rect()