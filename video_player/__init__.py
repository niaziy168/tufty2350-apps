#upload your images to the "images" folder, they must be named ezgif-frame001.png, etc
#convert your video to this format at https://ezgif.com/video-to-png/
#currently the images can be up to 320 x 240 resolution
import time

badge.mode(HIRES)#change this to lores if your video is less than 160x120, to get better fps

image_number = 1
image_count = 25 #change this to how many images are in your video

image = image.load(f"/system/apps/video_player/images/ezgif-frame-{image_number:03d}.png")

def update():
    global image_number, image, image_count
    

    # Try to load the current image
    image = image.load(f"/system/apps/video_player/images/ezgif-frame-{image_number:03d}.png")
        
    screen.blit(image, vec2(0, 0))
        
    time.sleep(0) #change this to slow the fps, however the Tufty update speed is not very fast anyways
    
    image_number = image_number+1
    
    if image_number > image_count:
        image_number = 1


run(update)
