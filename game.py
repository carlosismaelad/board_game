import pygame
from circle import Figure

pygame.init()

x = 90
y = 800
velocidade = 20
fps = 60

screen = pygame.display.set_mode((1520, 1760))
pygame.display.set_caption("Board game")
clock = pygame.time.Clock()
background = pygame.image.load("assets/space_resized.png")
running = True

circle1 = Figure(90, 800)
circle2 = Figure(100, 850)

current_circle = circle1

while running:
  pygame.time.delay(50)

  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      running = False
    elif event.type == pygame.MOUSEBUTTONDOWN:
      if event.button == 1:  # Botão esquerdo do mouse
        mouse_position = pygame.mouse.get_pos()
        if circle1.get_rect().collidepoint(mouse_position):
          circle1.selected = True
          circle2.selected = False
        elif circle2.get_rect().collidepoint(mouse_position):
          circle2.selected = True
          circle1.selected = False


  
  moviments = pygame.key.get_pressed()
  if circle1.selected:
        if moviments[pygame.K_UP]:
            circle1.y -= velocidade
        if moviments[pygame.K_DOWN]:
            circle1.y += velocidade
        if moviments[pygame.K_RIGHT]:
            circle1.x += velocidade
        if moviments[pygame.K_LEFT]:
            circle1.x -= velocidade
  elif circle2.selected:
        if moviments[pygame.K_UP]:
            circle2.y -= velocidade
        if moviments[pygame.K_DOWN]:
            circle2.y += velocidade
        if moviments[pygame.K_RIGHT]:
            circle2.x += velocidade
        if moviments[pygame.K_LEFT]:
            circle2.x -= velocidade


  if circle1.selected:
        pygame.draw.circle(screen, (255, 0, 0), (circle1.x, circle1.y), 55)
  else:
        pygame.draw.circle(screen, (0, 255, 0), (circle1.x, circle1.y), 50)

  if circle2.selected:
        pygame.draw.circle(screen, (255, 0, 0), (circle2.x, circle2.y), 55)
  else:
        pygame.draw.circle(screen, (0, 0, 255), (circle2.x, circle2.y), 50)

  pygame.display.flip()

  clock.tick(fps)

  screen.blit(background, (0,0))

  clock.tick(fps)

pygame.quit()