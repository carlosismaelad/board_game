import pygame

pygame.init()

# Configurações da tela
screen_width = 1520
screen_height = 1760
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Board game")
background = pygame.image.load("assets/space_resized.png")
clock = pygame.time.Clock()
fps = 60

# Carregar imagens dos personagens e redimensioná-las
alien_imagem = pygame.image.load("assets/persons/alien.jpg").convert_alpha()
alien_imagem = pygame.transform.scale(alien_imagem, (70, 90))

alien2_imagem = pygame.image.load("assets/persons/alien2.jpg").convert_alpha()
alien2_imagem = pygame.transform.scale(alien2_imagem, (70, 90))

disco_imagem = pygame.image.load("assets/persons/disco.png").convert_alpha()
disco_imagem = pygame.transform.scale(disco_imagem, (70, 90))

disco2_imagem = pygame.image.load("assets/persons/disco2.png").convert_alpha()
disco2_imagem = pygame.transform.scale(disco2_imagem, (70, 90))

foguete_imagem = pygame.image.load("assets/persons/foguete.png").convert_alpha()
foguete_imagem = pygame.transform.scale(foguete_imagem, (70, 90))

# Definição dos personagens
personagens = [
    {"imagem": alien_imagem, "posicao": (60, 840), "selecionado": False},
    {"imagem": alien2_imagem, "posicao": (140, 740), "selecionado": False},
    {"imagem": disco_imagem, "posicao": (60, 740), "selecionado": False},
    {"imagem": disco2_imagem, "posicao": (300, 740), "selecionado": False},
    {"imagem": foguete_imagem, "posicao": (220, 740), "selecionado": False}
]

personagem_atual = None

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:  # Botão esquerdo do mouse
                mouse_position = pygame.mouse.get_pos()
                for personagem in personagens:
                    imagem = personagem["imagem"]
                    posicao = personagem["posicao"]
                    personagem_rect = imagem.get_rect(topleft=posicao)
                    if personagem_rect.collidepoint(mouse_position):
                        if personagem_atual is None:
                            personagem_atual = personagem
                            personagem_atual["selecionado"] = True
                        elif personagem_atual == personagem:
                            personagem_atual = None
                            personagem["selecionado"] = False
                        else:
                            personagem_atual["selecionado"] = False
                            personagem_atual = personagem
                            personagem_atual["selecionado"] = True
                    elif personagem["selecionado"]:
                        personagem["posicao"] = mouse_position
                        personagem["selecionado"] = False

    screen.blit(background, (0, 0))  # Limpar a tela

    for personagem in personagens:
        imagem = personagem["imagem"]
        posicao = personagem["posicao"]
        selecionado = personagem["selecionado"]
        screen.blit(imagem, posicao)
        if selecionado:
            pygame.draw.rect(
                screen,
                (255, 0, 0),
                (posicao[0], posicao[1], imagem.get_width(), imagem.get_height()),
                2,
            )

    pygame.display.flip()
    clock.tick(fps)

pygame.quit()
