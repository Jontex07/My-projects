from pokemon_class import *
import  pygame

class Pokapics(pygame.sprite.Sprite):
    def __init__(self,width,height,pos_x,pos_y,color):
        super().__init__()
        self.image = pygame.Surface([width,height])

# general setup
pygame.init()
clock = pygame.time.Clock()

#game screen
screen_width = 1090
screen_height = 720
screen = pygame.display.set_mode((screen_width,screen_height))
background = pygame.image.load("pokemon_photos//battle_backround.png")
pokemon1 = pygame.image.load("back sprits//6.png")
pokemon1 = pygame.transform.scale(pokemon1,(300,300))
pokemon2 = pygame.image.load("pokemon_photos//150.png")
pokemon2 = pygame.transform.scale(pokemon2,(300,300))
postion_pokemon1 = (100,200)
postion_pokemon2 = (640,0)
pygame.display.set_caption("Pokemon J&A")
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()


    pygame.display.flip()
    screen.blit(background,(0,0))
    screen.blit(pokemon1,postion_pokemon1)
    screen.blit(pokemon2,postion_pokemon2)
    clock.tick(60)

