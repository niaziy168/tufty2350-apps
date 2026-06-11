import time

screen.font = rom_font.nope

action = "menu"
stopwatch = 0
stopwatchms = 0
stopwatchs = 0
stopwatchm = 0

def update():# clear the framebuffer
    
    global action,stopwatch,stopwatchms,stopwatchs,stopwatchm
    
    screen.pen = color.rgb(20, 40, 60)
    screen.clear()
    
    if action == "menu":
        screen.pen = color.rgb(255, 255, 255)
        
        screen.text("Timer App",10,10)
        screen.text("A: Stopwatch", 10, 30)
        screen.text("B: Timer", 10, 40)
        
        if badge.pressed(BUTTON_A):
            action = "stopwatch"
            
        if badge.pressed(BUTTON_B):
            action = "timer"
            
    if action == "stopwatch":
        screen.pen = color.rgb(255, 255, 255)
        
        screen.text("A: start/stop B: reset",10,10)
        
        screen.text(str(stopwatchm), 10, 30)
        screen.text(str(stopwatchs), 30, 30)
        screen.text(str(stopwatchms), 50, 30)
        
        if stopwatch == 1:
            
            if badge.pressed(BUTTON_A):
                stopwatch = 0
                badge.caselights(0)
                
        else:
            
            if badge.pressed(BUTTON_A):
                stopwatch = 1
        
        if badge.pressed(BUTTON_B):
            
            stopwatchms = 0
            stopwatchs = 0
            stopwatchm = 0
        
        if badge.pressed(BUTTON_C):
            
            action = "menu"
            
            stopwatchms = 0
            stopwatchs = 0
            stopwatchm = 0
        
        if stopwatch == 1:
            
            badge.caselights(1)
            
            screen.text(str(stopwatchm), 10, 30)
            screen.text(str(stopwatchs), 30, 30)
            screen.text(str(stopwatchms), 50, 30)
            
            time.sleep(0.0725)
            
            stopwatchms = stopwatchms + 1
            
            if stopwatchms == 10:
                
                stopwatchms = 0
                stopwatchs = stopwatchs + 1
                
            if stopwatchs == 60:
                
                stopwatchs = 0
                stopwatchm = stopwatchm + 1
        
    


run(update)