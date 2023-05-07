import pygame
import random
import sys 

#TAMANHO DA TELA
LARGURA = 1280
ALTURA = 720

#ARQUIVOS
BG = 'Projeto---Equipe-5/assets/imgs/fundo.jpg'
FONTE = 'Projeto---Equipe-5/assets/fonts/PixelGameFont.ttf'
ALVO_SPORT ='Projeto---Equipe-5/assets/imgs/sport-recife.png'
ALVO_NAUTICO ='Projeto---Equipe-5/assets/imgs/nautico.png'
ALVO_SANTA ='Projeto---Equipe-5/assets/imgs/santa.png'
MIRA = 'Projeto---Equipe-5/assets/imgs/dedo.png'
DISPARO = 'Projeto---Equipe-5/assets/audio/clique.mp3'

#PONTUAÇÃO
PONTOS_SPORT = 0
PONTOS_NAUTICO = 0
PONTOS_SANTA = 0
RECORDE = 0

#TEMPORIZADOR
TIMER = 1800  #1800/60 = 30 SEGUNDOS

#pause & fechar
GAME_PAUSED = False
FINALIZAR = False

class AlvoSport(pygame.sprite.Sprite):
    def __init__(self, pos_x, pos_y):
        super().__init__()
        self.image = pygame.image.load(ALVO_SPORT).convert_alpha()
        self.image = pygame.transform.scale(self.image, (100,100))
        self.rect = self.image.get_rect()
        self.rect.center = [pos_x, pos_y]

class AlvoNautico(pygame.sprite.Sprite):
    def __init__(self, pos_x, pos_y):
        super().__init__()
        self.image = pygame.image.load(ALVO_NAUTICO).convert_alpha()
        self.image = pygame.transform.scale(self.image, (100,100))
        self.rect = self.image.get_rect()
        self.rect.center = [pos_x, pos_y]

class AlvoSanta(pygame.sprite.Sprite):
    def __init__(self, pos_x, pos_y):
        super().__init__()
        self.image = pygame.image.load(ALVO_SANTA).convert_alpha()
        self.image = pygame.transform.scale(self.image, (100,100))
        self.rect = self.image.get_rect()
        self.rect.center = [pos_x, pos_y]
        
class Mira(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load(MIRA).convert_alpha()
        self.image = pygame.transform.scale(self.image, (50,50))
        self.rect = self.image.get_rect()
        self.sound = pygame.mixer.Sound(DISPARO)
    
    def update(self):   #predefinido pela Sprite
        self.rect.center = pygame.mouse.get_pos()
    
    def shoot(self):
        global PONTOS_SPORT
        global PONTOS_NAUTICO
        global PONTOS_SANTA
        self.sound.play()
        
        colisions_sport = pygame.sprite.spritecollide(mira,grupo_de_alvos_sport, False)
        colisions_nautico = pygame.sprite.spritecollide(mira,grupo_de_alvos_nautico, False)
        colisions_santa = pygame.sprite.spritecollide(mira,grupo_de_alvos_santa, False)

        for colision in colisions_sport:
            PONTOS_SPORT +=1
            colision.kill()
            alvo_sport = AlvoSport(random.randrange(0,LARGURA),random.randrange(0,ALTURA)) #só pode desenhar em grupos (conjunto)
            grupo_de_alvos_sport.add(alvo_sport)

        for colision in colisions_nautico:
            PONTOS_NAUTICO +=1
            colision.kill()
            alvo_nautico = AlvoNautico(random.randrange(0,LARGURA),random.randrange(0,ALTURA)) #só pode desenhar em grupos (conjunto)
            grupo_de_alvos_nautico.add(alvo_nautico)

        for colision in colisions_santa:
            PONTOS_SANTA +=1
            colision.kill()
            alvo_santa = AlvoSanta(random.randrange(0,LARGURA),random.randrange(0,ALTURA)) #só pode desenhar em grupos (conjunto)
            grupo_de_alvos_santa.add(alvo_santa)

        



pygame.init() #sempre em cima para evitar bugs

screen = pygame.display.set_mode((LARGURA,ALTURA))

bg =  pygame.image.load(BG).convert() #convert ajuda na adqueção da imagem
bg = pygame.transform.scale(bg, (LARGURA,ALTURA))

clock = pygame.time.Clock()

font = pygame.font.Font(FONTE, 30)

pygame.display.set_caption('Tiro ao alvo')


grupo_de_alvos_sport = pygame.sprite.Group()
grupo_de_alvos_nautico = pygame.sprite.Group()
grupo_de_alvos_santa = pygame.sprite.Group()


for i in range(1):
    alvo = AlvoSport(random.randrange(0,LARGURA),random.randrange(0,ALTURA)) #só pode desenhar em grupos (conjunto)
    grupo_de_alvos_sport.add(alvo)

for i in range(1):
    alvo = AlvoNautico(random.randrange(0,LARGURA),random.randrange(0,ALTURA)) #só pode desenhar em grupos (conjunto)
    grupo_de_alvos_nautico.add(alvo)

for i in range(1):
    alvo = AlvoSanta(random.randrange(0,LARGURA),random.randrange(0,ALTURA)) #só pode desenhar em grupos (conjunto)
    grupo_de_alvos_santa.add(alvo)
    
mira = Mira()
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
        grupo_de_alvos_sport.draw(screen)
        grupo_de_alvos_nautico.draw(screen)
        grupo_de_alvos_santa.draw(screen)
            
        mira_group.draw(screen)
            
        mira_group.update()
            
        score_sport = font.render(f'Sport: {int(PONTOS_SPORT)} ', True, (0,0,0))
        score_nautico = font.render(f'Nautico: {int(PONTOS_NAUTICO)} ', True, (0,0,0))
        score_santa = font.render(f'Santa Cruz: {int(PONTOS_SANTA)} ', True, (0,0,0))
        
        screen.blit(score_sport, (50,50))
        screen.blit(score_nautico, (50,100))
        screen.blit(score_santa, (50,150))
            
        tempo = font.render(f'Tempo: {TIMER/60:.1f} s',True, (0,0,0))
        screen.blit(tempo, (50,200))
            
        TIMER -=1
            
        if TIMER < 0:
            TIMER = 600
            GAME_PAUSED = not GAME_PAUSED
            
            
    else:
        screen.fill((252, 132, 3))
        pygame.mouse.set_visible(True)
        for event in pygame.event.get():
    
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE: #esc
                    GAME_PAUSED = not GAME_PAUSED
                    PONTOS_SPORT = 0
                    PONTOS_NAUTICO = 0
                    PONTOS_SANTA = 0

            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
                
        pause = font.render(f"PRESSIONE ESC PARA INICIAR   ",True, (255,255,255))
        points_sport = font.render(f"PONTUACAO SPORT: {PONTOS_SPORT} ",True, (255,255,255))
        points_nautico = font.render(f"PONTUACAO NAUTICO: {PONTOS_NAUTICO} ",True, (255,255,255))
        points_santa = font.render(f"PONTUACAO SANTA: {PONTOS_SANTA} ",True, (255,255,255))
        
        pause_rect = pause.get_rect(center = (LARGURA/2, ALTURA/2))
        points_rect_sport = points_sport.get_rect(center = (LARGURA/2, ALTURA/2-50))
        points_rect_nautico = points_nautico.get_rect(center = (LARGURA/2, ALTURA/2-100))
        points_rect_santa = points_santa.get_rect(center = (LARGURA/2, ALTURA/2-150))
        
        screen.blit(pause, pause_rect)
        screen.blit(points_sport,points_rect_sport)
        screen.blit(points_nautico,points_rect_nautico)
        screen.blit(points_santa,points_rect_santa)


            
    pygame.display.flip()
    clock.tick(60)
                
