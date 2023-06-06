import pygame
from gamers import Gamers
from dado import Dado

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

circle1 = Gamers(90, 800)
circle2 = Gamers(100, 850)
dado = Dado()

current_circle = None

class Button:
    def __init__(self, x, y, width, height, text, callback):
        self.rect = pygame.Rect(x, y, width, height)
        self.color = pygame.Color("purple")
        self.text = text
        self.callback = callback

    def handle_event(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            if self.rect.collidepoint(event.pos):
                self.callback()

    def draw(self, surface):
        pygame.draw.rect(surface, self.color, self.rect)
        font = pygame.font.Font(None, 24)
        text = font.render(self.text, True, pygame.Color("white"))
        text_rect = text.get_rect(center=self.rect.center)
        surface.blit(text, text_rect)

jogar_dado_button = Button(20, 20, 150, 50, "Jogar Dado", dado.roll)


while running:
  pygame.time.delay(50)

  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      running = False
    elif event.type == pygame.MOUSEBUTTONDOWN:
      if event.button == 1:  # Botão esquerdo do mouse
        mouse_position = pygame.mouse.get_pos()
        if circle1.selected:
            circle1.move_to_position(mouse_position[0], mouse_position[1])
            circle1.selected = False
            current_circle = None
        elif circle2.selected:
            circle2.move_to_position(mouse_position[0], mouse_position[1])
            circle2.selected = False
            current_circle = None
        else:
            if circle1.get_rect().collidepoint(mouse_position):
                circle1.selected = True
                circle2.selected = False
                current_circle = circle1
            elif circle2.get_rect().collidepoint(mouse_position):
                circle2.selected = True
                circle1.selected = False
                current_circle = circle2

    jogar_dado_button.handle_event(event)

  if circle1.selected:
        pygame.draw.circle(screen, (255, 0, 0), (circle1.x, circle1.y), 55)
  else:
        pygame.draw.circle(screen, (0, 255, 0), (circle1.x, circle1.y), 50)

  if circle2.selected:
        pygame.draw.circle(screen, (255, 0, 0), (circle2.x, circle2.y), 55)
  else:
        pygame.draw.circle(screen, (0, 0, 255), (circle2.x, circle2.y), 50)

  dado.update()
  dado.draw(screen)

  screen.blit(background, (0,0))
  jogar_dado_button.draw(screen)
  pygame.display.flip()

  clock.tick(fps)

pygame.quit()