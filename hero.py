import pygame
import random
pygame.init()

WIDTH = 640
HEIGHT = 480
screen = pygame.display.set_mode((WIDTH, HEIGHT))

# Set up the hero
hero = pygame.sprite.Sprite()
# Load sound
munch_sound = pygame.mixer.Sound('crunch.wav')
# Add image and rectangle properties to the hero
hero.image = pygame.image.load('hero.gif')
hero.rect = hero.image.get_rect()

TILE_SIZE = hero.rect.width
NUM_TILES_WIDTH = WIDTH / TILE_SIZE
NUM_TILES_HEIGHT = HEIGHT / TILE_SIZE
hero_group = pygame.sprite.GroupSingle(hero)

candies = pygame.sprite.OrderedUpdates()

def add_candy(candies):
    candy = pygame.sprite.Sprite()
    #Load up the image of it:
    candy.image = pygame.image.load('candy.png')
    #Make a rectangle property for it:
    candy.rect = candy.image.get_rect()
    #Put it in a location - here I’ll just choose to put it three tiles to the right and two tiles down:
    candy.rect.left = random.randint(0, NUM_TILES_WIDTH - 1) * TILE_SIZE
    candy.rect.top = random.randint(0, NUM_TILES_HEIGHT - 1) * TILE_SIZE
    candies.add(candy)

#Add candies to the list
for i in range(10):
# add the candy!
    add_candy(candies)
   
finish = False
win = False
pygame.time.set_timer(pygame.USEREVENT, 4000)
while finish != True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finish = True
        if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
            finish = True
        if event.type == pygame.KEYDOWN:
            # Move the hero around the screen
            if event.key == pygame.K_UP:
                hero.rect.top -= TILE_SIZE
            elif event.key == pygame.K_DOWN:
                hero.rect.top += TILE_SIZE
            elif event.key == pygame.K_RIGHT:
                hero.rect.right += TILE_SIZE
            elif event.key == pygame.K_LEFT:
                hero.rect.right -= TILE_SIZE
        if event.type == pygame.USEREVENT:
            if win == False:
                add_candy(candies)                
        # Paint the background black (the three
        # values represent red, green and blue:
        # 255 for all of them makes it black)
        screen.fill((255, 255, 255))
        if win:
            font = pygame.font.Font(None, 36)
            text_image = font.render("You Win!", True, (0, 0, 0))
            text_rect = text_image.get_rect(centerx=WIDTH/2, centery=100)
            screen.blit(text_image, text_rect)       
        # add these lines at the end of the main loop
        candies.draw(screen)
        hero_group.draw(screen)
        pygame.display.update()
    
    #collision
        collides = pygame.sprite.groupcollide(hero_group, candies, False, True)
        if len(candies) == 0:
            win = True

        if len(collides) > 0:
            munch_sound.play()

pygame.quit()



