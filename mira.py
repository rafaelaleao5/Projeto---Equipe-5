import random
import pygame
from alvo import Alvo

MIRA = 'Projeto---Equipe-5/assets/imgs/dedo.png'
DISPARO = 'Projeto---Equipe-5/assets/audio/clique.mp3'

LARGURA = 1280
ALTURA = 720


pygame.init()
screen = pygame.display.set_mode((LARGURA,ALTURA))
teste1 = pygame.image.load(MIRA).convert_alpha()
teste1 = pygame.transform.scale(teste1, (50, 50))
teste2 = teste1.get_rect()
teste3 = pygame.mixer.Sound(DISPARO)

class Mira(pygame.sprite.Sprite):
    def __init__(self, image, rect, sound):
        super().__init__()
        self.image = image
        self.rect = rect
        self.sound = sound
    
    def update(self):  #predefinido pela Sprite
        self.rect.center = pygame.mouse.get_pos()
    
    def shoot(self):
        global PONTOS
        self.sound.play()
        
        colisions = pygame.sprite.spritecollide(mira,grupo_de_alvos, False)
        for colision in colisions:
            print("teste")
            PONTOS +=1
            colision.kill()
            alvo = Alvo(random.randrange(0,LARGURA),random.randrange(0,ALTURA)) #só pode desenhar em grupos (conjunto)
            grupo_de_alvos.add(alvo)

mira = Mira(teste1, teste2, teste3)
mira_group = pygame.sprite.Group()
mira_group.add(mira)
grupo_de_alvos = pygame.sprite.Group()
