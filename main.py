import pygame

# Propriedades da janela
width = 500
height = 400

# Propriedades do quadrado (bolinha)
pos_x = width/2
pos_y = height/2
size_square = 20

# Propriedade para verificar em qual direção ele deve se mexer, valores: 1 e -1
value_x = 1
value_y = 1

# Propriedade para o tamanho da caixa que vai rebater a bolinha
width_rect = 30
height_rect = 100

# Propriedade para iniciação da primeira caixa, points se refere a pontuação do jogador
points_rect1 = 0
pos_x_rect1 = 10
pos_y_rect1 = height/2 - height_rect/2

# E da segunda caixa
points_rect2 = 0
pos_x_rect2 = width - width_rect - 10
pos_y_rect2 = height/2 - height_rect/2

# Necessário para que o jogo rode
pygame.init()

canva = pygame.display.set_mode((width, height))
pygame.display.set_caption("Pong Game")
clock = pygame.time.Clock()

# A fonte do texto
font = pygame.font.Font(None, 40)

exit = False

while not exit:
    first_raq = pygame.Rect(pos_x_rect1, pos_y_rect1, width_rect, height_rect)
    second_raq = pygame.Rect(pos_x_rect2, pos_y_rect2, width_rect, height_rect)
    ball = pygame.Rect(pos_x, pos_y, size_square, size_square)

    # Para carregar o texto (mas ainda não aparece)
    text1 = font.render(str(points_rect1), True, (255, 255, 255))
    text2 = font.render(str(points_rect2), True, (255, 255, 255))

    # O background da janela fica preto
    canva.fill("black")

    # Checa se ele apertou algum evento da janela
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit = True

    # Pega as teclas que o jogador apertou
    keys = pygame.key.get_pressed()

    # Teclas do jogador 1
    if keys[pygame.K_w]:
        pos_y_rect1 -= 1
    elif keys[pygame.K_s]:
        pos_y_rect1 += 1

    # Teclas do jogador 2
    if keys[pygame.K_UP]:
        pos_y_rect2 -= 1
    elif keys[pygame.K_DOWN]:
        pos_y_rect2 += 1
    
    # Faz a bolinha andar
    pos_x += value_x
    pos_y += value_y

    # Checagem de colisão com o tamanho da janela, a bolinha

    # Primeiro com o eixo X
    if ball.right > width:
        pos_x = width/2
        pos_y = height/2

        if value_x > 0:
            value_x = -1
        else:
            value_x = 1

        points_rect1 += 1
    elif ball.left < 0:
        pos_x = width/2
        pos_y = height/2

        if value_x > 0:
            value_x = -1
        
        if value_x > 0:
            value_x = -1
        else:
            value_x = 1

        points_rect2 += 1

    # Depois com o eixo Y
    if ball.bottom > height:
        pos_y = height - size_square
        value_y = -value_y
    elif ball.top < 0:
        pos_y = 0
        value_y = -value_y

    # Checagem de colisão dos quadrados com a janela
    # Jogador 1
    if first_raq.bottom > height:
        pos_y_rect1 = height - height_rect
    elif first_raq.top < 0:
        pos_y_rect1 = 0
    
    # Jogador 2
    if second_raq.bottom > height:
        pos_y_rect2 = height - height_rect
    elif second_raq.top < 0:
        pos_y_rect2 = 0

    # Checagem de colisão da bolinha com o quadrado
    if first_raq.colliderect(ball):
        if first_raq.midtop[1] > ball.midtop[1]: # Colisão pelo topo
            value_y = -value_y

            ball.bottom = first_raq.top
            pos_y = ball.y - 1
        elif first_raq.midleft[0] > ball.midleft[0] or first_raq.midright[0] < ball.midright[0]: # Colisão pela esquerda ou direita
            value_x = -value_x

            ball.left = first_raq.right
            pos_x = ball.x

            value_x += 0.1
        else: # Colisão por baixo
            value_y = -value_y

            ball.top = first_raq.bottom
            pos_y = ball.y + 1
    
    if second_raq.colliderect(ball):
        if second_raq.midtop[1] > ball.midtop[1]: # Colisão pelo topo
            value_y = -value_y

            ball.bottom = second_raq.top
            pos_y = ball.y - 1
        elif second_raq.midleft[0] > ball.midleft[0] or second_raq.midright[0] < ball.midright[0]: # Colisão pela esquerda ou direita
            value_x = -value_x

            ball.right = second_raq.left
            pos_x = ball.x

            value_x -= 0.1
        else: # Colisão por baixo
            value_y = -value_y

            ball.top = second_raq.bottom
            pos_y = ball.y + 1

    # Para mostrar o texto
    canva.blit(text1, (width * 1/3, 5))
    canva.blit(text2, (width * 2/3, 5))
        
    # Desenha as formas para o jogo
    pygame.draw.rect(canva, (255, 255, 255), first_raq)
    pygame.draw.rect(canva, (255, 255, 255), second_raq)

    pygame.draw.circle(canva, (255, 0, 0), (ball.centerx, ball.centery), size_square // 2)

    # Faz o update na tela
    pygame.display.update()

    # Tick do jogo para que não seja infinitamente rápido
    clock.tick(100)