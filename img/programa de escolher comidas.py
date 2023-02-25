import pygame
from pygame.locals import *
pygame.init()
janela = pygame.display.set_mode((700,600))
pygame.display.set_caption('jogo sprites')

fantasma1 = pygame.image.load('packman.png')
fantasma1 = pygame.transform.scale(fantasma1,(193*3,193*3))
fantasma2 = pygame.image.load('packman.png')
fantasma2 = pygame.transform.scale(fantasma2,(193*3,193*3))
fantasma3 = pygame.image.load('packman.png')
fantasma3 = pygame.transform.scale(fantasma3,(193*3,193*3))
fantasma4 = pygame.image.load('packman.png')
fantasma4 = pygame.transform.scale(fantasma4,(193*3,193*3))
pac1 = pygame.image.load('pac-1.png')
fundo = pygame.image.load('fundo.jpg')
fundo = pygame.transform.scale(fundo,(167*4,192*4))

x_sprite = 0
y_sprite = 0
sprite2 = 0
sprite_movimento = 250
x_movimento =250
y_movimento = 200
pacx_sprite = 0
pacy_sprite = 0
pacx_movimento = 400
pacy_movimento = 400
diminuir =  False
aumentar = True
less = False
more = True
sprite3 = 0
sprite3_movimento = 50
m = True
l = False
sprite4 = 0
sprite4_movimento = 450
mais = True
menos = False
while True:
    pygame.time.Clock().tick(12)
    janela.fill(0)
    janela.blit(fundo,(0,0))
    janela.blit(fantasma1,(x_movimento,y_movimento),(x_sprite*48,y_sprite,48,48))
    janela.blit(fantasma2,(sprite_movimento,500),(sprite2*48,144,48,48))
    janela.blit(fantasma3,(50,sprite3_movimento),(sprite3*48,240,48,48))
    janela.blit(fantasma4,(600,sprite4_movimento),(sprite4*48,192,48,48))
    janela.blit(pac1,(pacx_movimento,pacy_movimento),(pacx_sprite*60,pacy_sprite,60,80))
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            exit()
    pacx_sprite = pacx_sprite +1
    if pacx_sprite >=2:
        pacx_sprite = 0
    if pygame.key.get_pressed()[K_d]:
        pacy_sprite =80
        pacx_movimento = pacx_movimento +15

    if pygame.key.get_pressed()[K_a]:
        pacy_sprite = 0
        pacx_movimento =pacx_movimento -15
    if pygame.key.get_pressed()[K_w]:
        pacy_movimento =pacy_movimento -15
    if pygame.key.get_pressed()[K_s]:
        pacy_movimento =pacy_movimento +15
    if pacx_movimento>700:
        pacx_movimento = 0
    if pacx_movimento<0:
        pacx_movimento = 700
    if pacy_movimento>600:
        pacy_movimento = 0
    if pacy_movimento<0:
        pacy_movimento = 600
    
    x_sprite = x_sprite+1
    if x_sprite>=7:
        x_sprite = 0
    if x_movimento>500:
        diminuir = True
        aumentar = False
    if diminuir:
        x_movimento = x_movimento-15
    if x_movimento <90:
        aumentar = True
        diminuir = False
    if aumentar:
        x_movimento = x_movimento+15
#2 fantasma
    sprite2 = sprite2+1
    if sprite2>=7:
        sprite2 = 0
    if sprite_movimento>500:
        less = True
        more = False
    if less:
        sprite_movimento = sprite_movimento-15
    if sprite_movimento <90:
        more = True
        less = False
    if aumentar:
        sprite_movimento = sprite_movimento+15
#3 fantasma
    sprite3 = sprite3+1
    if sprite3>=7:
        sprite3 = 0
    if sprite3_movimento>500:
        l = True
        m = False
    if l:
        sprite3_movimento = sprite3_movimento-15
    if sprite3_movimento <90:
        m = True
        l = False
    if m:
        sprite3_movimento = sprite3_movimento+15
#4 fantasma
    sprite4 = sprite4+1
    if sprite4>=7:
        sprite4 = 0
    if sprite4_movimento>500:
        menos = True
        mais = False
    if menos:
        sprite4_movimento = sprite4_movimento-15
    if sprite4_movimento <90:
        mais = True
        menos = False
    if mais:
        sprite4_movimento = sprite4_movimento+15
    #colisão

    pygame.display.flip()