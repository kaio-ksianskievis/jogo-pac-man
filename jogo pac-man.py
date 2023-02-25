import pygame
from pygame.locals import * 
pygame.init()
janela = pygame.display.set_mode((700,600))
pygame.display.set_caption('pacman')
fonte = pygame.font.Font('freesansbold.ttf',24)
text = fonte.render('Você perdeu, aperte R para jogar novamente',True,(0,0,255))
textrect = text.get_rect()
textrect.center = 350,280
class Fantasma():
    def __init__(self,img1,img2,img3,img4,img5,img6,img7,img8,x,y):
        self.lista = []
        self.lista.append(pygame.image.load(img1))
        self.lista.append(pygame.image.load(img2))
        self.lista.append(pygame.image.load(img3))
        self.lista.append(pygame.image.load(img4))
        self.lista.append(pygame.image.load(img5))
        self.lista.append(pygame.image.load(img6))
        self.lista.append(pygame.image.load(img7))
        self.lista.append(pygame.image.load(img8))
        self.atual = 0
        self.imagem = self.lista[self.atual]
        self.rect = self.imagem.get_rect()
        self.rect.size = 20,33
        self.rect.x = x
        self.rect.y = y
        self.aumentar_x = True
        self.diminuir_x = False
        self.aumentar_y = False
        self.diminuir_y = False
    def printar(self):
        janela.blit(self.imagem,self.rect)
    def atualizar(self):
        self.atual = self.atual+0.5
        if self.atual>=8:
            self.atual=0
        self.imagem = self.lista[int(self.atual)]
    def movimento_horario(self):
        if self.rect.x>600:
            self.aumentar_x = False
            self.aumentar_y = True
            self.diminuir_x = False
            self.diminuir_y = False
        if self.aumentar_y:
            self.rect.y = self.rect.y+15
        if self.rect.y>500:
            self.aumentar_x = False
            self.aumentar_y = False
            self.diminuir_x = True
            self.diminuir_y = False
        if self.diminuir_x:
            self.rect.x = self.rect.x-15
        if self.rect.x<130:
            self.aumentar_x = False
            self.aumentar_y = False
            self.diminuir_x = False
            self.diminuir_y = True
        if self.diminuir_y:
            self.rect.y = self.rect.y-15
        if self.rect.y<130:
            self.diminuir_x = False
            self.aumentar_y = False
            self.diminuir_y = False
            self.aumentar_x = True
        if self.aumentar_x:
            self.rect.x = self.rect.x +15
    def movimento_antihorario(self):
        if self.rect.x<130:
            self.aumentar_x = False
            self.aumentar_y = True
            self.diminuir_x = False
            self.diminuir_y = False
        if self.aumentar_y:
            self.rect.y = self.rect.y+15
        if self.rect.y>500:
            self.aumentar_x = True
            self.aumentar_y = False
            self.diminuir_x = False
            self.diminuir_y = False
        if self.aumentar_x:
            self.rect.x = self.rect.x+15
        if self.rect.x>600:
            self.aumentar_x = False
            self.aumentar_y = False
            self.diminuir_x = False
            self.diminuir_y = True
        if self.diminuir_y:
            self.rect.y = self.rect.y-15
        if self.rect.y<130:
            self.diminuir_x = True
            self.aumentar_y = False
            self.diminuir_y = False
            self.aumentar_x = False
        if self.diminuir_x:
            self.rect.x = self.rect.x -15
    def movimento_curto(self):
        if self.rect.x>350:
            self.aumentar_x = False
            self.aumentar_y = True
            self.diminuir_x = False
            self.diminuir_y = False
        if self.aumentar_y:
            self.rect.y = self.rect.y+15
        if self.rect.y>450:
            self.aumentar_x = False
            self.aumentar_y = False
            self.diminuir_x = True
            self.diminuir_y = False
        if self.diminuir_x:
            self.rect.x = self.rect.x-15
        if self.rect.x<230:
            self.aumentar_x = False
            self.aumentar_y = False
            self.diminuir_x = False
            self.diminuir_y = True
        if self.diminuir_y:
            self.rect.y = self.rect.y-15
        if self.rect.y<130:
            self.diminuir_x = False
            self.aumentar_y = False
            self.diminuir_y = False
            self.aumentar_x = True
        if self.aumentar_x:
            self.rect.x = self.rect.x +15
    def movimento_alongado(self):
        if self.rect.x>600:
            self.aumentar_x = False
            self.diminuir_x = True
        if self.diminuir_x:
            self.rect.x = self.rect.x-15
        if self.rect.x<150:
            self.diminuir_x = False
            self.aumentar_x = True
        if self.aumentar_x:
            self.rect.x = self.rect.x+15
    def movimento_facil(self):
        if self.rect.y>500:
            self.aumentar_y = False
            self.diminuir_y = True
        if self.diminuir_y:
            self.rect.y = self.rect.y-15
        if self.rect.y<200:
            self.diminuir_y = False
            self.aumentar_y = True
        if self.aumentar_y:
            self.rect.y = self.rect.y+15
class Principal():
    def __init__(self,img1,img2,img3,x,y):
        self.lista= []
        self.lista.append(pygame.image.load(img1))
        self.lista.append(pygame.image.load(img2))
        self.lista.append(pygame.image.load(img3))
        self.atual = 0
        self.imagem = self.lista[self.atual]
        self.rect = self.imagem.get_rect()
        self.rect.size = 36,37
        self.rect.x = x
        self.rect.y = y
    def printar(self):
        janela.blit(self.imagem,self.rect)
    def atualizar(self):
        self.atual = self.atual+0.5
        if self.atual>=3:
            self.atual = 0
        self.imagem=self.lista[int(self.atual)]
    def movimentar(self):
        if pygame.key.get_pressed()[K_d]:
            self.rect.x =+ self.rect.x+15
            self.lista[0] = pygame.image.load('img\pac_esquerda_2.png')
            self.lista[1] = pygame.image.load('img\pac_esquerda_1.png')
        if pygame.key.get_pressed()[K_a]:
            self.rect.x =+ self.rect.x-15
            self.lista[0] = pygame.image.load('img\pac_direita_2.png')
            self.lista[1] = pygame.image.load('img\pac_direita_1.png')
        if pygame.key.get_pressed()[K_s]:
            self.rect.y =+ self.rect.y+15
        if pygame.key.get_pressed()[K_w]:
            self.rect.y =+ self.rect.y-15
        if self.rect.x>700:
            self.rect.x = 0
        if self.rect.x<0:
            self.rect.x = 700
        if self.rect.y>600:
            self.rect.y = 0
        if self.rect.y<0:
            self.rect.y = 600
vermelho = Fantasma('img/v_1.png','img/v_2.png','img/v_3.png','img/v_4.png','img/v_5.png','img/v_6.png','img/v_7.png','img/v_8.png',150,160)
azul = Fantasma('img/a_1.png','img/a_2.png','img/a_3.png','img/a_4.png','img/a_5.png','img/a_6.png','img/a_7.png','img/a_8.png',610,400)
pac = Principal('img\pac_direita_2.png','img\pac_direita_1.png','img\pac_centro.png',350,280)
laranja = Fantasma('img/l_1.png','img/l_2.png','img/l_3.png','img/l_4.png','img/l_5.png','img/l_6.png','img/l_7.png','img/l_8.png',130,300)
amarelo = Fantasma('img/y_1.png','img/y_2.png','img/y_3.png','img/y_4.png','img/y_5.png','img/y_6.png','img/y_7.png','img/y_8.png',300,400)
red = Fantasma('img/v_1.png','img/v_2.png','img/v_3.png','img/v_4.png','img/v_5.png','img/v_6.png','img/v_7.png','img/v_8.png',180,550)
fundo = pygame.image.load('img/fundo.jpg')
fundo = pygame.transform.scale(fundo,(167*4.1,192*3.1))
while True:

    morreu = False
    pygame.time.Clock().tick(10)
    janela.fill((0,0,0))
    janela.blit(fundo,(0,0))
    amarelo.printar()
    vermelho.printar()
    pac.printar()
    azul.printar()
    laranja.printar()
    red.printar()
    vermelho.movimento_horario()
    azul.movimento_antihorario()
    amarelo.movimento_curto()
    laranja.movimento_alongado()
    red.movimento_facil()
    pac.movimentar()
    pac.atualizar()
    vermelho.atualizar()
    azul.atualizar()
    red.atualizar()
    laranja.atualizar()
    amarelo.atualizar()
    def reiniciar():
        vermelho.rect.x = 150
        vermelho.rect.y = 160
        azul.rect.x = 610
        azul.rect.y = 400
        amarelo.rect.x = 300
        amarelo.rect.y = 400
        laranja.rect.x = 130
        laranja.rect.y = 300
        red.rect.x = 180
        red.rect.y = 550
        pac.rect.x = 350
        pac.rect.y = 280
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            exit()
    if pac.rect.colliderect(vermelho.rect):
        morreu = True
        janela.fill((255,255,255))
        janela.blit(text,textrect)
        pygame.display.flip()
    if pac.rect.colliderect(azul.rect):
        morreu = True
        janela.fill((255,255,255))
        janela.blit(text,textrect)
        pygame.display.flip()
    if pac.rect.colliderect(amarelo.rect):
        morreu = True
        janela.fill((255,255,255))
        janela.blit(text,textrect)
        pygame.display.flip()
    if pac.rect.colliderect(laranja.rect):
        morreu = True
        janela.fill((255,255,255))
        janela.blit(text,textrect)
        pygame.display.flip()

    if pac.rect.colliderect(red.rect):
        morreu = True
        janela.fill((255,255,255))
        janela.blit(text,textrect)
        pygame.display.flip()
    while morreu:
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                exit()
            if event.type == KEYDOWN:
                if event.key == K_r:
                    morreu = False
                    reiniciar()
                    break

            

    pygame.display.flip()