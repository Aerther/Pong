import pygame

# Propriedades da tela
largura_tela = 500
altura_tela = 400

# Propriedades do pygame
pygame.init()

tela = pygame.display.set_mode((largura_tela, altura_tela))
pygame.display.set_caption("Pong Game")
relogio = pygame.time.Clock()

sair = False

# Propriedades da bola
pos_x_bola = largura_tela/2
pos_y_bola = altura_tela/2
raio_bola = 10

# Propriedades das raquetes
largura_raq = 30
altura_raq = 100

# Raquete 1
pos_x_raq1 = 0
pos_y_raq1 = altura_tela/2

# Raquete 2
pos_x_raq2 = largura_tela - largura_raq
pos_y_raq2 = altura_tela/2

# Pontuação
pontos_raq1 = 0
pontos_raq2 = 0

# Velocidade da bola
vel_x = 1
vel_y = 1

# Fonte para o placar
fonte = pygame.font.Font(None, 40)

while not sair:
    tela.fill("black")

    # Setando o FPS do jogo
    relogio.tick(100)

    # Checagem de eventos do jogo
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            sair = True

    # Criação dos objetos
    bola = pygame.Rect(pos_x_bola, pos_y_bola, 2*raio_bola, 2*raio_bola)
    
    raquete_1 = pygame.Rect(pos_x_raq1, pos_y_raq1, largura_raq, altura_raq)
    raquete_2 = pygame.Rect(pos_x_raq2, pos_y_raq2, largura_raq, altura_raq)

    # Movimento da bola
    pos_x_bola += vel_x
    pos_y_bola += vel_y

    # Movimento pela tecla
    keys = pygame.key.get_pressed()

    # Jogador 1
    if keys[pygame.K_w]:
        pos_y_raq1 -= 1 
    elif keys[pygame.K_s]:
        pos_y_raq1 += 1
    
    # Jogador 2
    if keys[pygame.K_UP]:
        pos_y_raq2 -= 1 
    elif keys[pygame.K_DOWN]:
        pos_y_raq2 += 1

    # Colisão das raquetes com a tela
    if raquete_1.bottom > altura_tela:
        pos_y_raq1 = altura_tela - altura_raq
    elif raquete_1.top < 0:
        pos_y_raq1 = 0
    
    if raquete_2.bottom > altura_tela:
        pos_y_raq2 = altura_tela - altura_raq
    elif raquete_2.top < 0:
        pos_y_raq2 = 0

    # Colisão da bola com a tela
    # Eixo X
    if bola.right > largura_tela:
        vel_x = -1

        pontos_raq1 += 1

        pos_x_bola = largura_tela/2
        pos_y_bola = altura_tela/2
    elif bola.left < 0:
        vel_x = 1

        pontos_raq2 += 1
        
        pos_x_bola = largura_tela/2
        pos_y_bola = altura_tela/2

    # Eixo Y
    if bola.bottom > altura_tela:
        vel_y = -vel_y

        pos_y_bola = altura_tela - 2*raio_bola
    elif bola.top < 0:
        vel_y = -vel_y

        pos_y_bola = 0

    # Colisão da primeira raquete com a bola
    if raquete_1.colliderect(bola):
        if raquete_1.right < bola.right:
            vel_x = -vel_x

            pos_x_bola = raquete_1.right

            vel_x = vel_x * 1.1
        elif raquete_1.top > bola.top:
            vel_y = -vel_y

            pos_y_bola = raquete_1.top - 2*raio_bola
        else:
            vel_y = -vel_y

            pos_y_bola = raquete_1.bottom
    
    # Colisão da segunda raquete com a bola
    if raquete_2.colliderect(bola):
        if raquete_2.left > bola.left:
            vel_x = -vel_x

            pos_x_bola = raquete_2.left - 2*raio_bola

            vel_x = vel_x * 1.1
        elif raquete_2.top > bola.top:
            vel_y = -vel_y

            pos_y_bola = raquete_2.top - 2*raio_bola
        else:
            vel_y = -vel_y

            pos_y_bola = raquete_2.bottom

    # Para renderizar o placar na tela
    texto_pontos_1 = fonte.render(str(pontos_raq1), True, (255, 255, 255))
    texto_pontos_2 = fonte.render(str(pontos_raq2), True, (255, 255, 255))
    
    tela.blit(texto_pontos_1, (largura_tela * 1/3, 5))
    tela.blit(texto_pontos_2, (largura_tela * 2/3, 5))
    
    # Para desenhar as formas na tela
    pygame.draw.circle(tela, (255, 0, 0), (bola.centerx, bola.centery), raio_bola)

    pygame.draw.rect(tela, (255, 255, 255), raquete_1)
    pygame.draw.rect(tela, (255, 255, 255), raquete_2)

    pygame.display.update()