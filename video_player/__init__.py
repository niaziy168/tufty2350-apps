#upload your images to the "images" folder, they must be named ezgif-frame001.png, etc
#convert your video to this format at https://ezgif.com/video-to-png/
#currently the images can be up to 320 x 240 resolution
import time

badge.mode(HIRES)#change this to lores if your video is less than 160x120, to get better fps

image_number = 1
image_count = 45 #change this to how many images are in your video
pause = 0
blinkeffectcounter = 0

ignore_font = rom_font.ignore
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
        screen.font = ignore_font
        screen.text('PAUSED', 10, 10)
    
    if badge.held(BUTTON_C):
        image_number = image_number - 5
        screen.text('REWIND', 220, 10)
        if image_number < 1:
            image_number = 1
    
    if image_number > image_count:
        image_number = 1


run(update)
