x = 10
y = 10
size = 3
colorvar = 0
nope_font = rom_font.nope
screen.font = nope_font

while True:
    
    if badge.held(BUTTON_A):
        if not badge.held(BUTTON_C):
            x=x-1
        else:
            if badge.pressed(BUTTON_UP):
                colorvar = colorvar + 1
                if colorvar == 11:
                    colorvar = 0
            elif badge.pressed(BUTTON_DOWN):
                colorvar = colorvar -1
                if colorvar == -1:
                    colorvar = 10
                    
    elif badge.held(BUTTON_C):
        x=x+1
    
    if badge.held(BUTTON_DOWN):
        if not badge.held(BUTTON_UP):
            y=y+1
        else:
            if badge.pressed(BUTTON_A):
                size = size + 1
            elif badge.pressed(BUTTON_C):
                if size > 1:
                    size = size - 1
    elif badge.held(BUTTON_UP):
        y=y-1
    
    if not badge.held(BUTTON_B):
        screen.pen = color.black
        eraser = shape.rectangle(x-1, y-1, size+2, size+2)
        screen.shape(eraser)
        
    cursor = shape.rectangle(x, y, size, size)
    if colorvar == 0:
        screen.pen = color.red
    if colorvar == 1:
        screen.pen = color.orange
    if colorvar == 2:
        screen.pen = color.yellow
    if colorvar == 3:
        screen.pen = color.green
    if colorvar == 4:
        screen.pen = color.blue
    if colorvar == 5:
        screen.pen = color.rgb(255,0,255)
    if colorvar == 6:
        screen.pen = color.brown
    if colorvar == 7:
        screen.pen = color.rgb(0,0,0)
    if colorvar == 8:
        screen.pen = color.white
    if colorvar == 9:
        screen.pen = color.lime
    if colorvar == 10:
        screen.pen = color.cyan
    screen.shape(cursor)
    
    badge.default_clear = None
    
    badge.update()