#upload your images to the "images" folder, they must be named ezgif-frame001.png, etc
#convert your video to this format at https://ezgif.com/video-to-png/
#currently the images can be up to 320 x 240 resolution
#to reduce resolution below 320, go to https://www.onlineconverter.com/resize-video BEFORE uploading video to ezgif

import time

res = 'high'#change this to low if your video is less than 160x120, to get WAY better fps

if res == 'high':
    badge.mode(HIRES)
else:
    badge.mode(LORES)

image_number = 1
image_count = 25 #change this to how many images are in your video
pause = 0
blinkeffectcounter = 0

if res == 'high':
    font = rom_font.ignore
else:
    font = rom_font.nope

image = image.load(f"/system/apps/video_player/images/ezgif-frame-{image_number:03d}.png")

def update():
    global image_number, image, image_count, pause, blinkeffectcounter
    

    # Try to load the current image
    image = image.load(f"/system/apps/video_player/images/ezgif-frame-{image_number:03d}.png")
        
    screen.blit(image, vec2(0, 0))# if the video is not centered on the screen change these numbers (default is 0,0)
        
    time.sleep(0) #change this to slow the fps, however the Tufty update speed is not very fast anyways
    

    if badge.pressed(BUTTON_A):
        pause = 0
    
    if pause == 0:
        image_number = image_number+1
    else:
        if blinkeffectcounter == 0:
            screen.text('PAUSED', 10, 10)
            blinkeffectcounter = 1
        else:
            blinkeffectcounter = 0

    
    if badge.pressed(BUTTON_B):
        pause = 1
        screen.pen = color.white
        screen.font = font
        screen.text('PAUSED', 10, 10)
    
    if badge.held(BUTTON_C):
        image_number = image_number - 5
        if res == 'high':
            screen.text('REWIND', 220, 10)
        else:
            screen.text('REWIND', 105, 10)
        if image_number < 1:
            image_number = 1
    
    if image_number > image_count:
        image_number = 1


run(update)
