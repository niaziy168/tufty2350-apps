import time

screen.font = rom_font.nope

action = "menu"

stopwatch = 0
stopwatchms = 0
stopwatchs = 0
stopwatchm = 0

timeraction = 0
timer = 0
timers = 0
timerm = 0
timerh = 0

def update():# clear the framebuffer
    
    global action, stopwatch, stopwatchms, stopwatchs, stopwatchm, timer, timers, timerm, timerh, timeraction
    
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
            
    if action == "timer":
        screen.pen = color.rgb(255, 255, 255)
        
        screen.text("C/U/D Set, B reset, A start", 0,10)
        
        if badge.pressed(BUTTON_C):
            timeraction = timeraction+1
            if timeraction == 3:
                timeraction = 0
        if badge.pressed(BUTTON_B):
            timerh = 0
            timerm = 0
            timers = 0
        
        if timeraction < 3:
            if badge.pressed(BUTTON_A):
                timeraction = 3
        else:
            if badge.pressed(BUTTON_A):
                timeraction = 0
            
        if badge.pressed(BUTTON_UP):
            if timeraction == 0:
                timerh = timerh+1
            elif timeraction == 1:
                timerm = timerm+1
            else:
                timers = timers+1
                
        if badge.pressed(BUTTON_DOWN):
            if timeraction == 0:
                timerh = timerh+-1
            elif timeraction == 1:
                timerm = timerm+-1
            else:
                timers = timers+-1
        
        if timeraction == 0:
            screen.text("^", 55,70)
        elif timeraction == 1:
            screen.text("^", 75,70)
        else:
            screen.text("^", 95,70)
            
        screen.text(str(timerh), 55, 60)
        screen.text(str(timerm), 75, 60)
        screen.text(str(timers), 95, 60)
        
        if timeraction == 3:
            
            badge.caselights(1)
            
            timers = timers-1
            
            if timers == -1:
                timers = 59
                timerm = timerm-1
            if timerm == -1:
                timerm = 59
                timerh = timerh-1
            if timerh < 0:
                badge.caselights(0)
                time.sleep(0.25)
                badge.caselights(1)
                time.sleep(0.25)
                badge.caselights(0)
                time.sleep(0.25)
                screen.pen = color.rgb(255,0,0)
                screen.clear()
            time.sleep(0.98)
        
            
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
