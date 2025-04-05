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
            
            if event.type == pygame.QUIT:
                return
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_w and ctrl_held:
                    return
                if event.key == pygame.K_F4 and alt_held:
                    return
                if event.key == pygame.K_ESCAPE:
                    return
            
                # Determine color based on keypress
                if event.key == pygame.K_r:
                    cmode = 'red'
                elif event.key == pygame.K_g:
                    cmode = 'green'
                elif event.key == pygame.K_b:
                    cmode = 'blue'

            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:  # Left click grows radius
                    radius = min(200, radius + 1)
                elif event.button == 3:  # Right click shrinks radius
                    radius = max(1, radius - 1)

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_f:
                    filled = not filled

                if event.key == pygame.K_r and pressed[pygame.K_LSHIFT]:
                    mode = "rect"
                if event.key == pygame.K_c and pressed[pygame.K_LSHIFT]:
                    mode = "circle"
                if event.key == pygame.K_l and pressed[pygame.K_LSHIFT]:
                    mode = "line"
                if event.key == pygame.K_e and pressed[pygame.K_LSHIFT]:
                    mode = "eraser"
                if event.key == pygame.K_s and pressed[pygame.K_LSHIFT]:
                    mode = "square"
                if event.key == pygame.K_t and pressed[pygame.K_LSHIFT]:
                    mode = "right_triangle"
                if event.key == pygame.K_h and pressed[pygame.K_LSHIFT]:
                    mode = "equilateral_triangle"
                if event.key == pygame.K_d and pressed[pygame.K_LSHIFT]:
                    mode = "rhombus"
                
            if event.type == pygame.MOUSEMOTION:
                position = event.pos
                points = points + [position]
                points = points[-256:]

        screen.fill((0, 0, 0))
        
        i = 0
        if mode == "line":
            while i < len(points) - 1:
                drawLineBetween(background, i, points[i], points[i + 1], radius, cmode)
                i += 1

        if mode == "circle":
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    radius += 10
                if event.key == pygame.K_DOWN:
                    radius -= 10
            
            if event.type == pygame.MOUSEMOTION:
                x, y = event.pos
                
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    drawCircle(background, cmode, (x, y), radius, filled)
                
        if mode == "eraser":
            if event.type == pygame.MOUSEMOTION:
                if pygame.mouse.get_pressed()[0]:  # If left mouse button is held down
                    if len(points) > 1:
                        eraser(background, points[-2], points[-1], radius)

        if mode == "rect":
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    width -= 5
                if event.key == pygame.K_RIGHT:
                    width += 5
                if event.key == pygame.K_UP:
                    height += 5
                if event.key == pygame.K_DOWN:
                    height -= 5

            if event.type == pygame.MOUSEMOTION:
                x, y = event.pos
                
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    pack = (background, (x, y, width, height), cmode, filled)
                    drawRect(pack)

        if mode == "square":
            if event.type == pygame.MOUSEMOTION:
                x, y = event.pos
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    drawSquare(background, cmode, (x, y), 50, filled)

        if mode == "right_triangle":
            if event.type == pygame.MOUSEMOTION:
                x, y = event.pos
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    drawRightTriangle(background, cmode, (x, y), 50, filled)

        if mode == "equilateral_triangle":
            if event.type == pygame.MOUSEMOTION:
                x, y = event.pos
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    drawEquilateralTriangle(background, cmode, (x, y), 50, filled)

        if mode == "rhombus":
            if event.type == pygame.MOUSEMOTION:
                x, y = event.pos
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    drawRhombus(background, cmode, (x, y), 50, filled)
        
        screen.blit(background, (0,0))
        pygame.display.flip()
        clock.tick(60)


# Function for eraser tool
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


# Draw rectangle
def drawRect(bigTuple):
    screen, startData, color_mode, filled = bigTuple
    color = getColorFromMode(color_mode)
    if filled:
        pygame.draw.rect(screen, color, startData)
    else:
        pygame.draw.rect(screen, color, startData, width=5)


# Draw circle
def drawCircle(screen, color_mode, cords, radius, filled):
    color = getColorFromMode(color_mode)
    if filled:
        pygame.draw.circle(screen, color, cords, radius)
    else:
        pygame.draw.circle(screen, color, cords, radius, width=5)


# Draw line
def drawLineBetween(screen, index, start, end, width, color_mode):
    c1 = max(0, min(255, 2 * index - 256))
    c2 = max(0, min(255, 2 * index))
    
    color = getColorFromMode(color_mode)
    
    dx = start[0] - end[0]
    dy = start[1] - end[1]
    iterations = max(abs(dx), abs(dy))
    
    for i in range(iterations):
        progress = 1.0 * i / iterations
        aprogress = 1 - progress
        x = int(aprogress * start[0] + progress * end[0])
        y = int(aprogress * start[1] + progress * end[1])
        pygame.draw.circle(screen, color, (x, y), width)


# Draw square function
def drawSquare(screen, color_mode, position, size, filled):
    color = getColorFromMode(color_mode)
    if filled:
        pygame.draw.rect(screen, color, pygame.Rect(position[0], position[1], size, size))
    else:
        pygame.draw.rect(screen, color, pygame.Rect(position[0], position[1], size, size), width=5)


# Draw right triangle function
def drawRightTriangle(screen, color_mode, position, size, filled):
    color = getColorFromMode(color_mode)
    points = [(position[0], position[1]), 
              (position[0] + size, position[1]),
              (position[0], position[1] + size)]
    if filled:
        pygame.draw.polygon(screen, color, points)
    else:
        pygame.draw.polygon(screen, color, points, width=5)


# Draw equilateral triangle function
def drawEquilateralTriangle(screen, color_mode, position, size, filled):
    color = getColorFromMode(color_mode)
    
    # Calculate the height of an equilateral triangle
    height = (size * (3**0.5)) / 2
    
    # Points of the equilateral triangle
    points = [
        (position[0], position[1] - height / 2),  # Top point
        (position[0] - size / 2, position[1] + height / 2),  # Left bottom point
        (position[0] + size / 2, position[1] + height / 2)   # Right bottom point
    ]
    
    if filled:
        pygame.draw.polygon(screen, color, points)
    else:
        pygame.draw.polygon(screen, color, points, width=5)


# Draw rhombus function
def drawRhombus(screen, color_mode, position, size, filled):
    color = getColorFromMode(color_mode)
    
    # Calculate the rhombus points based on the size
    points = [
        (position[0], position[1] - size),  # Top point
        (position[0] + size, position[1]),  # Right point
        (position[0], position[1] + size),  # Bottom point
        (position[0] - size, position[1])   # Left point
    ]
    
    if filled:
        pygame.draw.polygon(screen, color, points)
    else:
        pygame.draw.polygon(screen, color, points, width=5)


# Utility function to get color based on mode
def getColorFromMode(color_mode):
    if color_mode == 'blue':
        return (0, 0, 255)
    elif color_mode == 'red':
        return (255, 0, 0)
    elif color_mode == 'green':
        return (0, 255, 0)
    return (255, 255, 255)  # Default white if no color selected


main()
