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
        
        #self.x = random.randint(0, 60)*size                       # random x coordinate
        #self.y = random.randint(0, 60)*size                       # random y coordinate
        x = random.randint(0, 80)*size
        if x > 800 or x < 0:
            if x > 800:
                x = 750
                self.x = x
            else: # x < 0
                x = 10
                self.x = x

        else: # x <= 800 and x >= 0
            self.x = x


        y = random.randint(0, 80)*size
        if y > 800 or y < 0:
            if y > 800:
                y = 750
                self.y = y
            else: # y < 0
                y = 10
                self.y = y

        else: # y <= 800 and y >= 0
            self.y = y




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
        controlled = pygame.draw.rect(screen, othergreen, (Sprite.x, Sprite.y, Sprite.width, Sprite.height))
        food = pygame.draw.circle(screen, red, (apple.x, apple.y), size)
        if controlled.colliderect(food):
            print("COLLISION")
        # myfont = pygame.font.SysFont("monospace", 15)
        # label = myfont.render(score, 1, (255, 255, 0))

        # screen.blit(label, (100, 100))

        for event in pygame.event.get(): 
            speed = 5
        
        if controlled.colliderect(food):
            print("collided with apple")
            apple.move_random()
            pygame.draw.circle(screen, red, (apple.x, apple.y), size)
        
        if Sprite.x < 0 or Sprite.x > w or Sprite.y < 0 or Sprite.y > h:
            break
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