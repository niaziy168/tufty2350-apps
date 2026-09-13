import random
import time

# High score sits outside the game loop so it remembers it after you die!
high_score = 0
ICONS = "/system/apps/clones/rpg.ppf"

# Outer loop to let the game restart on death
while True:
    money = 100
    hp = 10
    cursorx = 80
    cursory = 60
    menu = False

    placing_item = None
    cursor_icon = "Z"

    towers = [] 
    bombs = []  
    stickmen = [] 
    dispensers = []
    zappers = []

    spawn_delay = 80.0  
    spawn_timer = spawn_delay
    dots_per_spawn_float = 1.0 # Controls how many dots spawn at once!

    dots = [[0, 60]]
    
    score = 0
    frames_survived = 0

    # Inner loop - the actual gameplay
    while True:
        screen.pen = color.rgb(0, 100, 0)
        screen.clear()

        # --- TOWER TIMERS & DRAWING ---
        screen.pen = color.rgb(255, 255, 255)
        screen.font = font.load(ICONS)
        
        for tower in towers:
            tower[2] -= 1
            
            if tower[2] <= 0:
                tower[2] = 30  
                tower[3] = False 
                
            draw_y = tower[1]
            if tower[2] > 25:
                draw_y -= 8
                
            screen.text("a", tower[0], draw_y)

        # --- BOMB LOGIC & DRAWING ---
        surviving_bombs = []
        for bomb in bombs:
            bx = bomb[0]
            by = bomb[1]
            cx = bx + 6
            cy = by + 6
            
            if bomb[3] == 0:  
                bomb[2] -= 1
                screen.pen = color.rgb(255, 255, 255)
                screen.font = font.load(ICONS)
                screen.text("Q", bx, by)
                
                if bomb[2] <= 0:
                    bomb[3] = 1 
                    bomb[2] = 5 
                    
                    killed_count = 0
                    surviving_dots_after_boom = []
                    for dot in dots:
                        if killed_count < 10:
                            dist_sq = (cx - dot[0])**2 + (cy - dot[1])**2
                            if dist_sq <= 400: 
                                killed_count += 1
                                money += 1
                                continue 
                        surviving_dots_after_boom.append(dot)
                    dots = surviving_dots_after_boom
                surviving_bombs.append(bomb)
                
            elif bomb[3] == 1:  
                bomb[2] -= 1
                screen.pen = color.rgb(255, 165, 0) 
                circle = shape.circle(cx, cy, 20)
                screen.shape(circle)
                if bomb[2] > 0:
                    surviving_bombs.append(bomb)
        bombs = surviving_bombs

        # --- DISPENSER LOGIC & DRAWING ---
        for d in dispensers:
            d[2] -= 1
            screen.pen = color.rgb(255, 255, 255)
            screen.font = font.load(ICONS)
            screen.text("¯", d[0], d[1])
            
            cx = d[0] + 6
            cy = d[1] + 6
            
            if d[2] <= 0 and d[3] == 0:
                d[3] = 5    
                d[2] = 120  
                
                killed_count = 0
                surviving_dots_after_boom = []
                for dot in dots:
                    if killed_count < 7:
                        dist_sq = (cx - dot[0])**2 + (cy - dot[1])**2
                        if dist_sq <= 225:
                            killed_count += 1
                            money += 1
                            continue
                    surviving_dots_after_boom.append(dot)
                dots = surviving_dots_after_boom
                
            if d[3] > 0:
                d[3] -= 1
                screen.pen = color.rgb(255, 165, 0)
                circle = shape.circle(cx, cy, 15)
                screen.shape(circle)

        # --- ZAPPER LOGIC & DRAWING ---
        for zapper in zappers:
            zx = zapper[0]
            zy = zapper[1]
            cx = zx + 6
            cy = zy + 6
            
            screen.pen = color.rgb(255, 255, 255)
            screen.font = font.load(ICONS)
            screen.text("_", zx, zy)
            
            if zapper[2] > 0:
                zapper[2] -= 1
                
            if zapper[2] <= 0:
                nearest_dot = None
                min_dist_sq = 401 
                
                for dot in dots:
                    dist_sq = (cx - dot[0])**2 + (cy - dot[1])**2
                    if dist_sq <= 400 and dist_sq < min_dist_sq:
                        min_dist_sq = dist_sq
                        nearest_dot = dot
                        
                if nearest_dot:
                    zapper[4] = nearest_dot[0]
                    zapper[5] = nearest_dot[1]
                    zapper[3] = 5   
                    zapper[2] = 90  
                    
                    money += 1
                    if nearest_dot in dots:
                        dots.remove(nearest_dot)
                        
            if zapper[3] > 0:
                zapper[3] -= 1
                screen.pen = color.rgb(255, 255, 0)
                line = shape.line(cx, cy, zapper[4], zapper[5], 2)
                screen.shape(line)

        # --- STICKMAN LOGIC & DRAWING ---
        screen.pen = color.rgb(255, 255, 255)
        screen.font = font.load(ICONS)
        for sm in stickmen:
            sm_cx = sm[0] + 6
            sm_cy = sm[1] + 6
            
            if sm[2] == 1: 
                # Decrement the 1-second cooldown timer
                if sm[3] > 0:
                    sm[3] -= 1
                    
                orig_x = sm[4]
                orig_y = sm[5]
                
                # Walk back home
                if sm[0] < orig_x: sm[0] += 1
                elif sm[0] > orig_x: sm[0] -= 1
                
                if sm[1] < orig_y: sm[1] += 1
                elif sm[1] > orig_y: sm[1] -= 1
                
                # Only return to attack state if at origin AND cooldown is done!
                if sm[0] == orig_x and sm[1] == orig_y and sm[3] <= 0:
                    sm[2] = 0 
            
            elif sm[2] == 0 and len(dots) > 0: 
                min_dist = 999999
                nearest_dot = None
                for dot in dots:
                    dist_sq = (sm_cx - dot[0])**2 + (sm_cy - dot[1])**2
                    if dist_sq < min_dist:
                        min_dist = dist_sq
                        nearest_dot = dot
                        
                if nearest_dot:
                    if sm_cx < nearest_dot[0]: sm[0] += 1
                    elif sm_cx > nearest_dot[0]: sm[0] -= 1
                    
                    if sm_cy < nearest_dot[1]: sm[1] += 1
                    elif sm_cy > nearest_dot[1]: sm[1] -= 1
                    
            screen.text("'", sm[0], sm[1])

        # --- UI & SCORE SYSTEM ---
        frames_survived += 1
        if frames_survived >= 30:
            score += 1
            frames_survived = 0

        screen.pen = color.rgb(255, 255, 255)
        screen.font = font.load(ICONS)
        screen.text(")", 0, 105) 
        
        screen.font = font.nope 
        screen.text(str(money), 15, 106)
        # Moved to 70 to allow up to 4 digits comfortably!
        screen.text("Score:" + str(score), 70, 106) 

        # --- ENEMY MOVEMENT, COMBAT & SPAWNING ---
        surviving_dots = []

        for dot in dots:
            clone = shape.rectangle(dot[0], dot[1], 1, 1)
            screen.shape(clone)

            direction = rnd(0, 2)

            if direction == 0: dot[1] -= 1
            elif direction == 1: dot[0] += 1
            elif direction == 2: dot[1] += 1
            else: dot[0] -= 1
                
            if dot[0] >= 160:
                hp -= 1
                continue  
                
            killed_by_tower = False
            for tower in towers:
                is_swinging = tower[2] > 25
                attack_y = tower[1] - 8 if is_swinging else tower[1]
                if is_swinging and not tower[3]:
                    if tower[0] - 2 <= dot[0] <= tower[0] + 12 and attack_y - 2 <= dot[1] <= attack_y + 12:
                        killed_by_tower = True
                        tower[3] = True  
                        money += 1       
                        break            
            if killed_by_tower:
                continue
                
            killed_by_stickman = False
            for sm in stickmen:
                if sm[2] == 0:
                    sm_cx = sm[0] + 6
                    sm_cy = sm[1] + 6
                    dist_sq = (sm_cx - dot[0])**2 + (sm_cy - dot[1])**2
                    if dist_sq <= 100:
                        killed_by_stickman = True
                        sm[2] = 1   
                        sm[3] = 30 # Start 1-second cooldown when a dot is killed
                        money += 1
                        break
            if killed_by_stickman:
                continue
                
            surviving_dots.append(dot)

        dots = surviving_dots

        spawn_timer -= 1
        if spawn_timer <= 0:
            spawn_delay *= 0.995 # Changed from 0.99 for a smoother initial difficulty curve
            
            # If we hit the speed limit, start spawning MORE dots instead of faster
            if spawn_delay < 5.0:
                spawn_delay = 5.0
                dots_per_spawn_float += 0.005 # Dropped from 0.05 to make the extra spawns happen gradually
                
            # Spawn the guaranteed number of dots
            num_spawns = int(dots_per_spawn_float)
            for _ in range(num_spawns):
                dots.append([0, 60])
                
            # Handle the decimal / fractional chance for an extra dot
            fractional_chance = int((dots_per_spawn_float - num_spawns) * 100)
            if random.randint(1, 100) <= fractional_chance:
                dots.append([0, 60])
                
            spawn_timer = spawn_delay

        # --- UI (Hearts) ---
        screen.pen = color.rgb(255, 0, 0)
        screen.font = font.load(ICONS)
        for i in range(hp):
            screen.text("³", i * 15, 0)

        # --- GAME OVER SCREEN ---
        if hp <= 0:
            if score > high_score:
                high_score = score
                
            screen.pen = color.rgb(0, 0, 0)
            screen.clear()
            screen.pen = color.rgb(255, 255, 255)
            screen.font = font.nope
            screen.text("GAME OVER", 45, 40)
            screen.text("Score: " + str(score), 45, 60)
            screen.text("High Score: " + str(high_score), 45, 75)
            badge.update()
            time.sleep(4)
            break 
        
        # --- MENU RENDERING ---
        if menu == True:
            screen.pen = color.rgb(0, 0, 0)
            screen.shape(shape.rectangle(15, 15, 130, 90))
            screen.font = font.nope
            screen.pen = color.rgb(255, 255, 255)
            screen.text("Menu", 16, 16)
            screen.text("45", 41, 27) 
            screen.text("25", 45, 41)
            screen.text("200", 40, 56) 
            screen.text("50", 41, 71) 
            screen.text("35", 41, 86)
            screen.font = font.load(ICONS)
            screen.text("a", 16, 26) 
            screen.text(")", 27, 26)  
            screen.text("Q", 18, 40)  
            screen.text(")", 31, 40)
            screen.text("'", 15, 55) 
            screen.text(")", 25, 55)  
            screen.text("¯", 16, 70)
            screen.text(")", 28, 70)
            screen.text("_", 16, 85)
            screen.text(")", 28, 85)

        # --- CURSOR MOVEMENT ---
        if badge.held(BUTTON_A): cursorx -= 4
        elif badge.held(BUTTON_C): cursorx += 4
        if badge.held(BUTTON_UP): cursory -= 4
        elif badge.held(BUTTON_DOWN): cursory += 4
         
        screen.pen = color.rgb(0, 0, 255) 
        screen.font = font.load(ICONS) 
        screen.text(cursor_icon, cursorx, cursory)
        
        # --- BUTTON LOGIC ---
        if badge.pressed(BUTTON_B):
            if placing_item is not None:
                overlap = False
                for t in towers:
                    if abs(cursorx - t[0]) < 10 and abs(cursory - t[1]) < 10: overlap = True
                for sm in stickmen:
                    if abs(cursorx - sm[4]) < 10 and abs(cursory - sm[5]) < 10: overlap = True
                for d in dispensers:
                    if abs(cursorx - d[0]) < 10 and abs(cursory - d[1]) < 10: overlap = True
                for z in zappers:
                    if abs(cursorx - z[0]) < 10 and abs(cursory - z[1]) < 10: overlap = True
                    
                if not overlap:
                    if placing_item == "sword":
                        towers.append([cursorx, cursory, 30, False])
                    elif placing_item == "bomb":
                        bombs.append([cursorx, cursory, 30, 0]) 
                    elif placing_item == "stickman":
                        stickmen.append([cursorx, cursory, 0, 0, cursorx, cursory])
                    elif placing_item == "dispenser":
                        dispensers.append([cursorx, cursory, 120, 0])
                    elif placing_item == "zapper":
                        zappers.append([cursorx, cursory, 90, 0, 0, 0])
                        
                    placing_item = None
                    cursor_icon = "Z"
                time.sleep(0.3)

            elif menu == True:
                if 10 <= cursorx <= 25 and 20 <= cursory <= 35 and money >= 45: 
                    money -= 45
                    menu = False
                    placing_item = "sword"
                    cursor_icon = "a" 
                elif 14 <= cursorx <= 28 and 36 <= cursory <= 50 and money >= 25:
                    money -= 25
                    menu = False
                    placing_item = "bomb"
                    cursor_icon = "Q" 
                elif 11 <= cursorx <= 25 and 51 <= cursory <= 65 and money >= 200:
                    money -= 200
                    menu = False
                    placing_item = "stickman"
                    cursor_icon = "'" 
                elif 12 <= cursorx <= 28 and 66 <= cursory <= 80 and money >= 50: 
                    money -= 50
                    menu = False
                    placing_item = "dispenser"
                    cursor_icon = "¯"
                elif 12 <= cursorx <= 28 and 81 <= cursory <= 95 and money >= 35:
                    money -= 35
                    menu = False
                    placing_item = "zapper"
                    cursor_icon = "_"
                else:
                    menu = False
                time.sleep(0.3)
                    
            else:
                sold_something = False
                for i, t in enumerate(towers):
                    if abs(cursorx - t[0]) < 10 and abs(cursory - t[1]) < 10:
                        money += 22 
                        towers.pop(i)
                        sold_something = True
                        break
                
                if not sold_something:
                    for i, sm in enumerate(stickmen):
                        if abs(cursorx - sm[4]) < 10 and abs(cursory - sm[5]) < 10:
                            money += 100
                            stickmen.pop(i)
                            sold_something = True
                            break
                            
                if not sold_something:
                    for i, d in enumerate(dispensers):
                        if abs(cursorx - d[0]) < 10 and abs(cursory - d[1]) < 10:
                            money += 25 
                            dispensers.pop(i)
                            sold_something = True
                            break
                            
                if not sold_something:
                    for i, z in enumerate(zappers):
                        if abs(cursorx - z[0]) < 10 and abs(cursory - z[1]) < 10:
                            money += 17 
                            zappers.pop(i)
                            sold_something = True
                            break
                
                if not sold_something:
                    menu = True
                    
                time.sleep(0.3)

        badge.update()