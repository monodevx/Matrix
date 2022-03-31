import pygame, random

pygame.init() #Init pygame screen

### Virables
FPS = 60

clock = pygame.time.Clock()

WIDTH = 1200
HEIGHT = 800

window = pygame.display.set_mode((WIDTH, HEIGHT))

flag = False

### Virables

def update():
    window.fill((0, 0, 0))
    run()
    pygame.draw.circle(window, "green", a, 2)
    pygame.draw.circle(window, "green", b, 2)
    pygame.draw.circle(window, "green", c, 2)
    pygame.draw.circle(window, "white", d, 2)

def init():
    global d

    rnd = random.randint(1, 6)
    
    if rnd == 1 or rnd == 2:
        drx = (d[0] + a[0]) / 2
        dry = (d[1] + a[1]) / 2

        d = drx, dry 

    elif rnd == 3 or rnd == 4:
            drx = (d[0] + b[0]) / 2
            dry = (d[1] + b[1]) / 2
    
            d = drx, dry 

    elif rnd == 5 or rnd == 6:
            drx = (d[0] + c[0]) / 2
            dry = (d[1] + c[1]) / 2
    
            d = drx, dry
             
    pygame.draw.circle(window, "white", d, 1)
    
def run():
    global a, b, c, d
    ### Randomize
    arx = random.randint(0, WIDTH)
    ary = random.randint(0, HEIGHT)
    
    brx = random.randint(0, WIDTH)
    bry = random.randint(0, HEIGHT)
    
    crx = random.randint(0, WIDTH)
    cry = random.randint(0, HEIGHT)

    drx = random.randint(0, WIDTH)
    dry = random.randint(0, HEIGHT)
    ### Randomize

    a = (arx, ary)
    b = (brx, bry)
    c = (crx, cry)
    d = (drx, dry)
    
while True:
    keystate = pygame.key.get_pressed()
    for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit()
                
    if keystate[pygame.K_SPACE]:                  
        update()
        
    if keystate[pygame.K_RETURN]:
        flag = True
        
    if flag == True:
        init()
     
    pygame.display.update()   
    clock.tick(FPS)
