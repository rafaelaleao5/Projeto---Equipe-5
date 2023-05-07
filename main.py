import pygame
import random
import sys
from mira import Mira
from alvo import Alvo


 



#TAMANHO DA TELA
LARGURA = 1280
ALTURA = 720

#ARQUIVOS
BG = 'Projeto---Equipe-5/assets/imgs/fundo.jpg'
FONTE = 'Projeto---Equipe-5/assets/fonts/PixelGameFont.ttf'
ALVO ='Projeto---Equipe-5/assets/imgs/sport-recife.png'
MIRA = 'Projeto---Equipe-5/assets/imgs/dedo.png'
DISPARO = 'Projeto---Equipe-5/assets/audio/clique.mp3'

#PONTUAÇÃO
PONTOS = 0
RECORDE = 0

#TEMPORIZADOR
TIMER = 8000  #1800/60 = 30 SEGUNDOS

#pause & fechar
GAME_PAUSED = False
FINALIZAR = False



pygame.init() #sempre em cima para evitar bugs
screen = pygame.display.set_mode((LARGURA,ALTURA))
teste1 = pygame.image.load(MIRA).convert_alpha()
teste1 = pygame.transform.scale(teste1, (50, 50))
teste2 = teste1.get_rect()
teste3 = pygame.mixer.Sound(DISPARO)
testando1 = pygame.image.load(ALVO).convert_alpha()
testando1 = pygame.transform.scale(testando1, (100,100))
testando2 = testando1.get_rect()



bg =  pygame.image.load(BG).convert() #convert ajuda na adqueção da imagem
bg = pygame.transform.scale(bg, (LARGURA,ALTURA))

clock = pygame.time.Clock()

font = pygame.font.Font(FONTE, 30)

pygame.display.set_caption('Tiro ao alvo')


grupo_de_alvos = pygame.sprite.Group()

for i in range(1):
    alvo = Alvo(testando1, testando2, random.randrange(0,LARGURA),random.randrange(0,ALTURA)) #só pode desenhar em grupos (conjunto)
    grupo_de_alvos.add(alvo)
    
mira = Mira(teste1, teste2, teste3)
mira_group = pygame.sprite.Group()
mira_group.add(mira)


while not FINALIZAR:
    
    
    if not GAME_PAUSED:
        
        pygame.mouse.set_visible(False)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
                
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE: #esc
                    GAME_PAUSED = not GAME_PAUSED
                    
            if event.type == pygame.MOUSEBUTTONDOWN:
                mira.shoot()
                
        screen.blit(bg, (0,0))
        grupo_de_alvos.draw(screen)
            
        mira_group.draw(screen)
            
        mira_group.update()
            
        score = font.render(f' Pontos: {int(PONTOS)} ', True, (0,0,0))
        screen.blit(score, (50,50))
            
        tempo = font.render(f'Tempo: {TIMER/60:.1f} s',True, (0,0,0))
        screen.blit(tempo, (50,100))
            
        TIMER -=1
            
        if TIMER < 0:
            TIMER = 600
            
            if PONTOS > RECORDE:
                RECORDE = PONTOS
                PONTOS = 0
            GAME_PAUSED = not GAME_PAUSED
            
    else:
        screen.fill((252, 132, 3))
        pygame.mouse.set_visible(True)
        for event in pygame.event.get():
    
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE: #esc
                    GAME_PAUSED = not GAME_PAUSED

            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
                
        pause = font.render(f"PRESSIONE ESC PARA INICIAR   ",True, (255,255,255))
        points = font.render(f"RECORDE: {RECORDE} ",True, (255,255,255))
        
        pause_rect = pause.get_rect(center = (LARGURA/2, ALTURA/2))
        points_rect = points.get_rect(center = (LARGURA/2, ALTURA/2-50))
        
        screen.blit(pause, pause_rect)
        screen.blit(points,points_rect)

            
    pygame.display.flip()
    clock.tick(60)
                
