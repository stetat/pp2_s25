import pygame

def main():
    pygame.init()
    screen = pygame.display.set_mode((640, 480))
    clock = pygame.time.Clock()
    background = pygame.Surface((640,480))
    background.fill((0,0,0))
    
    radius = 15
    x = 0
    y = 0
    width = 100
    height = 100
    radius = 30
    filled = True
    cmode = 'blue'
    mode = "rect"
    points = []
    rectangles = []
    
    while True:
        
        pressed = pygame.key.get_pressed()

        
       
        
        

        
        
        alt_held = pressed[pygame.K_LALT] or pressed[pygame.K_RALT]
        ctrl_held = pressed[pygame.K_LCTRL] or pressed[pygame.K_RCTRL]
        
        for event in pygame.event.get():
            
            # determin if X was clicked, or Ctrl+W or Alt+F4 was used
            if event.type == pygame.QUIT:
                return
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_w and ctrl_held:
                    return
                if event.key == pygame.K_F4 and alt_held:
                    return
                if event.key == pygame.K_ESCAPE:
                    return
            
                # determine if a letter key was pressed
                if event.key == pygame.K_r:
                    cmode = 'red'
                elif event.key == pygame.K_g:
                    cmode = 'green'
                elif event.key == pygame.K_b:
                    cmode = 'blue'

            
            
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1: # left click grows radius
                    radius = min(200, radius + 1)
                elif event.button == 3: # right click shrinks radius
                    radius = max(1, radius - 1)

            if event.type == pygame.KEYDOWN:

                if event.key == pygame.K_f:
                    if filled:
                        filled = False
                    else:
                        filled = True

                if event.key == pygame.K_r and pressed[pygame.K_LSHIFT]:
                        mode = "rect"

                if event.key == pygame.K_c and pressed[pygame.K_LSHIFT]:
                        mode = "circle"

                if event.key == pygame.K_l and pressed[pygame.K_LSHIFT]:
                        mode = "line"

                if event.key == pygame.K_e and pressed[pygame.K_LSHIFT]:
                        mode = "eraser"
                
            if event.type == pygame.MOUSEMOTION:
                    # if mouse moved, add point to list
                position = event.pos
                points = points + [position]
                points = points[-256:]
            
        screen.fill((0, 0, 0))
        
        # draw all points
        i = 0
        if mode == "line":
            while i < len(points) - 1:
                drawLineBetween(background, i, points[i], points[i + 1], radius, cmode)
                i += 1

        if mode == "circle":
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    radius+=10
                
                if event.key == pygame.K_DOWN:
                    radius-=10
            
            if event.type == pygame.MOUSEMOTION:
                x, y = event.pos
                
                cords = (x,y)

            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    
                    drawCircle(background, cmode, cords, radius, filled)
                
        if mode == "eraser":
            if event.type == pygame.MOUSEMOTION:
                if pygame.mouse.get_pressed()[0]:  # If left mouse button is held down
                    if len(points) > 1:
                        eraser(background, points[-2], points[-1], radius)

        if mode == "rect":
            
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    width-=5
                
                if event.key == pygame.K_RIGHT:
                    width+=5

                if event.key == pygame.K_UP:
                    height+=5

                if event.key == pygame.K_DOWN:
                    height-=5

            

            if event.type == pygame.MOUSEMOTION:
                x, y = event.pos
                
                startData = (x, y, width, height)

            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    pack = (background, startData, cmode, filled)
                    drawRect(pack)

      
            
        screen.blit(background, (0,0))
        pygame.display.flip()

     
        
        clock.tick(60)


def eraser(screen, start, end, width):
    dx = start[0] - end[0]
    dy = start[1] - end[1]
    iterations = max(abs(dx), abs(dy))
    
    for i in range(iterations):
        progress = i / iterations
        x = int((1 - progress) * start[0] + progress * end[0])
        y = int((1 - progress) * start[1] + progress * end[1])
        
        # Draw a black circle to "erase" (simulating eraser effect)
        pygame.draw.circle(screen, (0, 0, 0), (x, y), width)



def drawRect(bigTuple):
    screen, startData, color_mode, filled = bigTuple
    if color_mode == 'blue':
        color = (0, 0, 255)
    elif color_mode == 'red':
        color = (255, 0, 0)
    elif color_mode == 'green':
        color = (0, 255, 0)


    


   

    if filled:
        pygame.draw.rect(screen, color_mode, startData)
    
    else:
        pygame.draw.rect(screen, color_mode, startData, width=5)



def drawCircle(screen, color_mode, cords, radius, filled):
    if color_mode == 'blue':
        color = (0, 0, 255)
    elif color_mode == 'red':
        color = (255, 0, 0)
    elif color_mode == 'green':
        color = (0, 255, 0)

    if filled:
        pygame.draw.circle(screen, color_mode, cords, radius)
    
    else:
        pygame.draw.circle(screen, color_mode, cords, radius, width=5)



def drawLineBetween(screen, index, start, end, width, color_mode):
    c1 = max(0, min(255, 2 * index - 256))
    c2 = max(0, min(255, 2 * index))
    
    if color_mode == 'blue':
        color = (c1, c1, c2)
    elif color_mode == 'red':
        color = (c2, c1, c1)
    elif color_mode == 'green':
        color = (c1, c2, c1)
    
    dx = start[0] - end[0]
    dy = start[1] - end[1]
    iterations = max(abs(dx), abs(dy))
    
    for i in range(iterations):
        progress = 1.0 * i / iterations
        aprogress = 1 - progress
        x = int(aprogress * start[0] + progress * end[0])
        y = int(aprogress * start[1] + progress * end[1])
        pygame.draw.circle(screen, color, (x, y), width)

main()