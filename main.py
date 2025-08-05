import pygame

# Propriedades da janela
width = 500
height = 400

# Propriedades do quadrado (bolinha)
pos_x = width/2
pos_y = height/2
size_square = 50

# Propriedade para verificar em qual direção ele deve se mexer, valores: 1 e -1
value_x = 1
value_y = 1

# Propriedade para o tamanho da caixa que vai rebater a bolinha
width_rect = 50
height_rect = 100

# Propriedade para iniciação da primeira caixa, points se refere a pontuação do jogador
points_rect1 = 0
pos_x_rect1 = 0
pos_y_rect1 = 0

# E da segunda caixa
points_rect2 = 0
pos_x_rect2 = width - width_rect
pos_y_rect2 = 0

# Necessário para que o jogo rode
pygame.init()

canva = pygame.display.set_mode((width, height))
pygame.display.set_caption("Pong Game")
clock = pygame.time.Clock()

exit = False

while not exit:
    first_raq = pygame.Rect(pos_x_rect1, pos_y_rect1, width_rect, height_rect)
    second_raq = pygame.Rect(pos_x_rect2, pos_y_rect2, width_rect, height_rect)
    ball = pygame.Rect(pos_x, pos_y, size_square, size_square)

    # O background da janela fica preto
    canva.fill("black")

    # Checa se ele apertou algum evento da janela
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit = True

    # Pega as teclas que o jogador apertou
    keys = pygame.key.get_pressed()

    # Teclas do jogador 1
    if keys[pygame.K_UP]:
        pos_y_rect1 -= 1
    elif keys[pygame.K_DOWN]:
        pos_y_rect1 += 1

    # Teclas do jogador 2
    if keys[pygame.K_w]:
        pos_y_rect2 -= 1
    elif keys[pygame.K_s]:
        pos_y_rect2 += 1
    
    # Faz a bolinha andar
    pos_x += value_x
    pos_y += value_y

    # Checagem de colisão com o tamanho da janela, a bolinha

    # Primeiro com o eixo X
    if pos_x + size_square > width:
        pos_x = width/2
        pos_y = height/2

        value_x = -value_x

        points_rect1 += 1
    elif pos_x < 0:
        pos_x = width/2
        pos_y = height/2

        value_x = -value_x

        points_rect2 += 1

    # Depois com o eixo Y
    if pos_y + 50 > height:
        pos_y = height - 50
        value_y = -value_y
    elif pos_y < 0:
        pos_y = 0
        value_y = -value_y

    # Checagem de colisão dos quadrados com a janela
    # Jogador 1
    if pos_y_rect1 + height_rect > height:
        pos_y_rect1 = height - height_rect
    elif pos_y_rect1 < 0:
        pos_y_rect1 = 0
    
    # Jogador 2
    if pos_y_rect2 + height_rect > height:
        pos_y_rect2 = height - height_rect
    elif pos_y_rect2 < 0:
        pos_y_rect2 = 0

    # Checagem de colisão da bolinha com o quadrado
    collideObject = ball
    collideObject.x = collideObject.x + 1*value_x
    collideObject.y = collideObject.y + 1*value_y
    
    if first_raq.colliderect(collideObject) or second_raq.colliderect(collideObject):
        value_x = -value_x

        if pos_y + size_square + 1*value_y >= pos_y_rect1:
            value_y = -value_y
            value_x = -value_x
        
    # Desenha as formas para o jogo
    pygame.draw.rect(canva, (255, 255, 255), first_raq)
    pygame.draw.rect(canva, (255, 255, 255), second_raq)

    pygame.draw.rect(canva, (255, 0, 0), ball)

    # Faz o update na tela
    pygame.display.update()

    # Tick do jogo para que não seja infinitamente rápido
    clock.tick(100)