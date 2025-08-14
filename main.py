import pygame

# Propriedades da janela
largura_tela = 500
altura_tela = 400

# Propriedades do quadrado (bolinha)
pos_x_bola = largura_tela/2
pos_y_bola = altura_tela/2
raio_bola = 10

# Propriedade para verificar em qual direção ele deve se mexer, valores: 1 e -1, vel de velocidade
vel_x = 1
vel_y = 1

# Propriedade para o tamanho da caixa que vai rebater a bolinha
largura_ret = 30
altura_ret = 100

# Propriedade para iniciação da primeira caixa, points se refere a pontuação do jogador
pontos_raq1 = 0
pos_x_raq1 = 10
pos_y_raq1 = altura_tela/2 - altura_ret/2

# E da segunda caixa
pontos_raq2 = 0
pos_x_raq2 = largura_tela - largura_ret - 10
pos_y_raq2 = altura_tela/2 - altura_ret/2

# Necessário para que o jogo rode
pygame.init()

tela = pygame.display.set_mode((largura_tela, altura_tela))
pygame.display.set_caption("Pong Game")
relogio = pygame.time.Clock()

# A fonte do texto
fonte = pygame.font.Font(None, 40)

sair = False

while not sair:
    primeira_raquete = pygame.Rect(pos_x_raq1, pos_y_raq1, largura_ret, altura_ret)
    segunda_raquete = pygame.Rect(pos_x_raq2, pos_y_raq2, largura_ret, altura_ret)
    bola = pygame.Rect(pos_x_bola, pos_y_bola, 2*raio_bola, 2*raio_bola)

    # Para carregar o texto (mas ainda não aparece)
    

    # O background da janela fica preto
    tela.fill("black")

    # Checa se ele apertou algum evento da janela
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            sair = True

    # Pega as teclas que o jogador apertou
    keys = pygame.key.get_pressed()

    # Teclas do jogador 1
    if keys[pygame.K_w]:
        pos_y_raq1 -= 1
    elif keys[pygame.K_s]:
        pos_y_raq1 += 1

    # Teclas do jogador 2
    if keys[pygame.K_UP]:
        pos_y_raq2 -= 1
    elif keys[pygame.K_DOWN]:
        pos_y_raq2 += 1
    
    # Faz a bolinha andar
    pos_x_bola += vel_x
    pos_y_bola += vel_y

    # Checagem de colisão com o tamanho da janela, a bolinha

    # Primeiro com o eixo X
    if bola.right > largura_tela:
        pos_x_bola = largura_tela/2
        pos_y_bola = altura_tela/2

        if vel_x > 0:
            vel_x = -1
        else:
            vel_x = 1

        pontos_raq1 += 1
    elif bola.left < 0:
        pos_x_bola = largura_tela/2
        pos_y_bola = altura_tela/2

        if vel_x > 0:
            vel_x = -1
        
        if vel_x > 0:
            vel_x = -1
        else:
            vel_x = 1

        pontos_raq2 += 1

    # Depois com o eixo Y
    if bola.bottom > altura_tela:
        pos_y_bola = altura_tela - 2*raio_bola
        vel_y = -vel_y
    elif bola.top < 0:
        pos_y_bola = 0
        vel_y = -vel_y

    # Checagem de colisão dos quadrados com a janela
    # Jogador 1
    if primeira_raquete.bottom > altura_tela:
        pos_y_raq1 = altura_tela - altura_ret
    elif primeira_raquete.top < 0:
        pos_y_raq1 = 0
    
    # Jogador 2
    if segunda_raquete.bottom > altura_tela:
        pos_y_raq2 = altura_tela - altura_ret
    elif segunda_raquete.top < 0:
        pos_y_raq2 = 0

    # Checagem de colisão da bolinha com o quadrado
    if primeira_raquete.colliderect(bola):
        if primeira_raquete.right < bola.right: # Colisão pela esquerda ou direita
            vel_x = -vel_x

            pos_x_bola = primeira_raquete.right

            vel_x += 0.1
        elif primeira_raquete.top > bola.top: # Colisão pelo topo
            vel_y = -vel_y

            pos_y_bola = primeira_raquete.top - 2*raio_bola
        else: # Colisão por baixo
            vel_y = -vel_y

            pos_y_bola = primeira_raquete.bottom + 2*raio_bola
    
    if segunda_raquete.colliderect(bola):
        if segunda_raquete.midtop[1] > bola.midtop[1]: # Colisão pelo topo
            vel_y = -vel_y

            bola.bottom = segunda_raquete.top
            pos_y_bola = bola.y - 1
        elif segunda_raquete.midleft[0] > bola.midleft[0] or segunda_raquete.midright[0] < bola.midright[0]: # Colisão pela esquerda ou direita
            vel_x = -vel_x

            bola.right = segunda_raquete.left
            pos_x_bola = bola.x

            vel_x -= 0.1
        else: # Colisão por baixo
            vel_y = -vel_y

            bola.top = segunda_raquete.bottom
            pos_y_bola = bola.y + 1

    texto_pontos_1 = fonte.render(str(pontos_raq1), True, (255, 255, 255))
    texto_pontos_2 = fonte.render(str(pontos_raq2), True, (255, 255, 255))
    
    # Para mostrar o texto, o calculo serve para colocar eles espaçadamente iguais
    tela.blit(texto_pontos_1, (largura_tela * 1/3, 5))
    tela.blit(texto_pontos_2, (largura_tela * 2/3, 5))
        
    # Desenha as formas para o jogo
    pygame.draw.rect(tela, (255, 255, 255), primeira_raquete)
    pygame.draw.rect(tela, (255, 255, 255), segunda_raquete)

    pygame.draw.circle(tela, (255, 0, 0), (bola.centerx, bola.centery), raio_bola)

    # Faz o update na tela
    pygame.display.update()

    # Tick do jogo para que não seja infinitamente rápido
    relogio.tick(100)