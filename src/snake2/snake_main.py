import pygame
import random
from turtle import width


size = 10    # size of the apple (same size as grid spot)
def start_screen(screen): 
    # initializing the constructor      
    print("start_screen()")     
    pygame.init()       
    not_playing_yet = True      
    light_green = (144, 238, 144)   
    white = (255, 255, 255)     
    black = (0, 0, 0)   
    screen.fill(light_green)    


    font = pygame.font.SysFont("monospace", 30)     
    label = font.render("Welcome to Our Game!", 1, white)   
    label1 = font.render("Click the mouse to continue", 2, white)   
    screen.blit(label, (250, 250))  
    screen.blit(label1, (200, 400))     
    pygame.display.update()     

    while not_playing_yet:  
        for event in pygame.event.get():   
            if event.type == pygame.MOUSEBUTTONDOWN:  
                not_playing_yet = False  
    pygame.display.update()  

 
 

def end_screen(screen, score):  

    black = (0, 0, 0)   
    red = (255, 0, 0)   
    pygame.init()   
    screen.fill(black)      
    font = pygame.font.SysFont("monospace", 30)     
    label = font.render("You Lost!", 1, red)    
    label1 = font.render("Click the mouse to continue", 1, red)     
    show_score = font.render("Score: " + str(score), 1, red)    
    screen.blit(label, (325, 250))      
    screen.blit(label1, (180, 300))     
    screen.blit(show_score, (325, 350))     
    font = pygame.font.Font('freesansbold.ttf', 32)     
    pygame.display.update()     


    not_playing_yet = True  
    while not_playing_yet:      
        for event in pygame.event.get():      
            if event.type == pygame.MOUSEBUTTONDOWN:    
                run()   

    pygame.display.update() 

class Apple:
    def __init__(self, screen):                                   # constructor for the apple object
        self.image = pygame.image.load("../../apple.png").convert()     # loads the apple image
        self.screen = screen                                      # screen that the apple will be drawn on
        self.x = size*20                                           # x coordinate of the apple
        self.y = size*20                                           # y coordinate of the apple

    def draw(self):                                               # function to draw the apple
        self.screen.blit(self.image, (self.x, self.y))            # blit is used to draw an image on top of another (in this case apple on top of the grid)
        pygame.display.flip()                                     # updates the contents drawn to the screen

    def move_random(self):                                        # function to move apple to a random spot
        self.x = random.randint(50, 750)
        self.y = random.randint(50, 750)



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
    start_screen(screen)
    pygame.display.update() 
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

    entire_snake = []
    snake_size = 1
    direction = ""

    def draw_snake(size, entire_snake):
        for pos in entire_snake:
            pygame.draw.rect(screen, othergreen, (pos[0], pos[1], size, size))

    while game_in_progress:        
        screen.fill(green)
        entire_snake.append([Sprite.x, Sprite.y])
        # print(entire_snake)
        
        if len(entire_snake) > snake_size:
            entire_snake = entire_snake[1:]

        draw_snake(20, entire_snake)

        controlled = pygame.draw.rect(screen, othergreen, (Sprite.x, Sprite.y, Sprite.width, Sprite.height))
        food = pygame.draw.circle(screen, red, (apple.x, apple.y), size)

        font = pygame.font.SysFont(None, 30)
        score_txt = 'SCORE: ' + str(score)

        score_img = font.render(score_txt, True, (0, 0, 255))
        screen.blit(score_img, (2, 2))
   
        

        
        if controlled.colliderect(food):
            print("collided with apple")
            apple.move_random()
            pygame.draw.circle(screen, red, (apple.x, apple.y), size)
            snake_size += 1
            score += 1

         
        if Sprite.x < 0 or Sprite.x > w or Sprite.y < 0 or Sprite.y > h:
            break

        for event in pygame.event.get(): 
            if event.type == pygame.KEYDOWN: 
                if event.key == pygame.K_LEFT or event.key == ord('a'): 
                    if direction != "RIGHT":
                        # break
                        #Sprite.x -= speed
                        direction = "LEFT"
                        print("D")

                if event.key == pygame.K_RIGHT or event.key == ord('d'):
                    if direction != "LEFT":
                        # break
                        #Sprite.x += speed 
                        direction = "RIGHT"
                    

                if event.key == pygame.K_UP or event.key == ord('w'): 
                    if direction != "DOWN":
                        #Sprite.y -= speed
                        direction = "UP"
                    


                if event.key == pygame.K_DOWN or event.key == ord('s'):
                    if direction != "UP":
                        # break 
                        #Sprite.y += speed
                        direction = "DOWN"
                   

            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT or event.key == ord('a'): 
                    if direction != "RIGHT":
                        # break
                        #Sprite.x -= speed
                        direction = "LEFT"
                        print("D")             

                if event.key == pygame.K_RIGHT or event.key == ord('d'):
                    if direction != "LEFT":
                        # break
                       # Sprite.x += speed 
                        direction = "RIGHT"
        

                if event.key == pygame.K_UP or event.key == ord('w'): 
                    if direction != "DOWN":
                        #Sprite.y -= speed
                        direction = "UP"
            

                if event.key == pygame.K_DOWN or event.key == ord('s'): 
                    if direction != "UP":
                        # break 
                        #Sprite.y += speed
                        direction = "DOWN"

        if direction =="UP":
            Sprite.y -= speed
        if direction == "DOWN":
            Sprite.y += speed
        if direction == "LEFT":
            Sprite.x -= speed
        if direction == "RIGHT":
            Sprite.x += speed



        pygame.display.update()  # move?
        clock.tick(60)   
    end_screen(screen,score)
    pygame.display.quit() 

    return 
 

if __name__ == '__main__': #if the user runs "snake_main.py" from terminal 

    run()