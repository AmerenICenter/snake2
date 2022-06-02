import pygame
import random

#def run():
 #   global w, h
    
    # print ('Running the main script!')
    #pygame.init()
    #pygame.display.init()
    #print(pygame.display.get_init())
    #green = (34,139,34)
    #othergreen = (0,255,0)
    #w = 800
    #h = 800
    #screen = pygame.display.set_mode((w, h))
    #snake = pygame.surface(20,20)
    #screen.fill(green)
    #pygame.display.update()
    #game_in_progress = 1
    #speed = 0
    #snakewidth = 20
    #snakeheight = 20
    
    #while game_in_progress:
#        snakewidth += speed
#        snakeheight += speed
#        screen.blit(snake, (snakewidth,snakeheight))
#        pygame.display.update()
#        for event in pygame.event.get():
#            speed = 1
#
#        if event.type == pygame.KEYDOWN:
#            if event.key == pygame.K_LEFT:
#                print('left')
#            if event.key == pygame.K_RIGHT:
#                print('right')
#            if event.key == pygame.K_UP:
#                print('up')
#            if event.key == pygame.K_DOWN:
#                print('down')
#
#            if event.key == ord('q'):
#                game_in_progress = False    
#    pygame.display.quit()
#    pygame.quit()
#    return
#    
#    
#
#if __name__ == '__main__': #if the user runs "snake_main.py" from terminal
#    run()

size = 10    # size of the apple (same size as grid spot)

class Apple:
    def __init__(self, screen):                                   # constructor for the apple object
        self.image = pygame.image.load("apple.png").convert()     # loads the apple image
        self.screen = screen                                      # screen that the apple will be drawn on
        self.x = size*3                                           # x coordinate of the apple
        self.y = size*3                                           # y coordinate of the apple

    def draw(self):                                               # function to draw the apple
        self.screen.blit(self.image, (self.x, self.y))            # blit is used to draw an image on top of another (in this case apple on top of the grid)
        pygame.display.flip()                                     # updates the contents drawn to the screen

    def move_random(self):                                        # function to move apple to a random spot
        self.x = random.randint(0, 50)*size                       # random x coordinate
        self.y = random.randint(0, 50)*size                       # random y coordinate

class Sprite:
    x = 100
    y = 100
    #topedge = 100
    #bottomedge = 100

# FUNCTION FOR COLLISION W/ APPLE
def check_collision(self, x1, y1, x2, y2):
    if x1 >= x2 and x1 < x2 + size:
        if y1 >= y2 and y1 < y2 + size:
            return True         # returns True if there is a collision
    return False        # returns False if there is no collision

def run(): 
    global w, h 

    pygame.init() 
    pygame.display.init() 
    print(pygame.display.get_init()) 
    green = (34,139,34) 
    othergreen = (0,255,0) 
    w = 800
    h = 800
    screen = pygame.display.set_mode((w, h)) 
    screen.fill(green) 
    pygame.display.update() 
    game_in_progress = 1 
    speed = 0
    square = pygame.Surface((20, 20))
    square.fill((255, 0, 0))
    clock = pygame.time.Clock()

    # initialize apple into the game
    apple = Apple(screen)
    apple.draw()

    while game_in_progress:        

        screen.blit(square, (Sprite.x, Sprite.y))
        # pygame.draw.circle(screen, othergreen, (100,100), 10) #sprite
        # pygame.display.update() 

        for event in pygame.event.get(): 
            speed = 1 

            if event.type == pygame.KEYDOWN: 
                if event.key == pygame.K_LEFT or event.key == ord('a'): 
                    Sprite.x -= 10
                    print('left')

                if event.key == pygame.K_RIGHT or event.key == ord('d'):
                    Sprite.x += 10 
                    print('right') 

                if event.key == pygame.K_UP or event.key == ord('w'): 
                    Sprite.y -= 10
                    print('up') 

                if event.key == pygame.K_DOWN or event.key == ord('s'): 
                    Sprite.y += 10
                    print('down') 

        pygame.display.update() 
        clock.tick(60)

            # if event.key == ord('q'):
            #     # break
                
            #     pygame.quit() 
            #     sys.exit() 
            #     game_in_progress = False     

    pygame.display.quit() 

    return 

     

     

 
 

if __name__ == '__main__': #if the user runs "snake_main.py" from terminal 

    run()