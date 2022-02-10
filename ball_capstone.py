import pygame
pygame.init()

screen = pygame.display.set_mode((400,300))
pygame.display.set_caption("Bouncing balls")

speed = 1;

y1 = 25;
y2 = 275;


while True:
    for e in pygame.event.get():
        if e.type == pygame.QUIT:
            pygame.quit()
    
    
    y1 = y1 + speed
    y2 = y2 - speed
    
    if y1 >= 280:
        speed = speed * -1
    if y1 <= 15:
        speed = speed * -1
        
    
        
    if y2 <= 15:
        speed = speed * -1
    if y2 >= 280:
        speed = speed * -1
    
        
    
    screen.fill("black")
    
    background = pygame.image.load("bg.jpg").convert()
    screen.blit(background,[0,0])
    
    pygame.draw.circle(screen,"green",[150,y1],20)
    pygame.draw.circle(screen,"blue",[250,y2],20)
    pygame.display.update()
    
    
    
    


