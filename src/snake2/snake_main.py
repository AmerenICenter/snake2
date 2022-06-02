import pygame
import random
from turtle import width


size = 10    # size of the apple (same size as grid spot)

class Apple:
    def __init__(self, screen):                                   # constructor for the apple object
        self.image = pygame.image.load("../../apple.png").convert()     # loads the apple image
        self.screen = screen                                      # screen that the apple will be drawn on
        self.x = size*3                                           # x coordinate of the apple
        self.y = size*3                                           # y coordinate of the apple

    def draw(self):                                               # function to draw the apple
        self.screen.blit(self.image, (self.x, self.y))            # blit is used to draw an image on top of another (in this case apple on top of the grid)
        pygame.display.flip()                                     # updates the contents drawn to the screen

    def move_random(self):                                        # function to move apple to a random spot
        self.x = random.randint(0, 50)*size                       # random x coordinate
        self.y = random.randint(0, 50)*size                       # random y coordinate


# FUNCTION FOR COLLISION W/ APPLE
def check_collision(x1, y1, x2, y2):
    if x1 >= x2 and x1 < x2 + size:
        if y1 >= y2 and y1 < y2 + size:
            return True         # returns True if there is a collision
    return False        # returns False if there is no collision


class Sprite:
    x = 100
    y = 100
    width = 20
    height = 20

def run(): 
    global w, h 

    pygame.init() 
    pygame.display.init() 
    pygame.display.set_caption('snake')
    print(pygame.display.get_init()) 
    green = (34,139,34) 
    red = (220, 20, 60)
    othergreen = (0,255,0) 
    w = 800
    h = 800
    screen = pygame.display.set_mode((w, h)) 
    screen.fill(green) 
    pygame.display.update() 
    game_in_progress = 1 
    speed = 5
    square = pygame.Surface((20, 20))
    square.fill((255, 0, 0))
    clock = pygame.time.Clock()
    score = 0

    apple = Apple(screen)
    apple.draw()

    while game_in_progress:        
        screen.fill(green) 
        pygame.draw.rect(screen, othergreen, (Sprite.x, Sprite.y, Sprite.width, Sprite.height))
        pygame.draw.circle(screen, red, (apple.x, apple.y), size)

        # myfont = pygame.font.SysFont("monospace", 15)
        # label = myfont.render(score, 1, (255, 255, 0))

        # screen.blit(label, (100, 100))

        for event in pygame.event.get(): 
            speed = 5
        
        if check_collision(Sprite.x, Sprite.y, apple.x, apple.y):
            print("collided with apple")
            apple.move_random()
            pygame.draw.circle(screen, red, (apple.x, apple.y), size)
         
        
        # print(Sprite.x)
        # print(Sprite.y)

        if event.type == pygame.KEYDOWN: 
            if event.key == pygame.K_LEFT or event.key == ord('a'): 
                Sprite.x -= speed                    

            if event.key == pygame.K_RIGHT or event.key == ord('d'):
                Sprite.x += speed 

            if event.key == pygame.K_UP or event.key == ord('w'): 
                Sprite.y -= speed


            if event.key == pygame.K_DOWN or event.key == ord('s'): 
                Sprite.y += speed

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == ord('a'): 
                Sprite.x -= speed                    

            if event.key == pygame.K_RIGHT or event.key == ord('d'):
                Sprite.x += speed 

            if event.key == pygame.K_UP or event.key == ord('w'): 
                Sprite.y -= speed

            if event.key == pygame.K_DOWN or event.key == ord('s'): 
                Sprite.y += speed
   
        
        pygame.display.update() 
        clock.tick(60)   

    pygame.display.quit() 

    return 
 

if __name__ == '__main__': #if the user runs "snake_main.py" from terminal 

    run()