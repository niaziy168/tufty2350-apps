# tufty2350-apps
Any apps I make for the tufty 2350 will be placed in here.
Note that due to major changes introduced with each update, make sure you are on BadgeOS V3.0.0

# Thermometer
A thermometer
Uses the RP2350's built in thermometer to measure the temperature without needing external sensors.
Note that both the RP2350 and Tufty's screen, battery, and USB port all create heat and therefore will cause the readings to be skewed.
Use A and B buttons to switch between Celsius and Fahrenheit

Current Version(1.1)
Now works on BadgeOS V3.0.0

Previous Version(1.0)
Nothing fancy
# Paint
A basic drawing app.
Controls:
1. A/C/U/D to move cursor
2. B to draw
3. To erase, just don't press B
4. Hold U+D, then use A/C to change pen size
5. Hold A+C, then use U/D to change color

Current Version(1.0)
It works and you can draw :)
# Video Player
This allows you to play videos on your Tufty. 
PLEASE COMPLETLY READ THE FOLLOWING INSTRUCTIONS!

1. First, record your video and if you want shrink the resolution to 160x 120 or below at
   https://www.onlineconverter.com/resize-video (this will greatly upgrade fps)
3. Convert your video to png images at https://ezgif.com/video-to-png
4. select the resolution to be below 320x240
5. Download them as a .zip file
6. extract all, then upload the unnzipped folder to /apps/video_player/
7. rename the folder you just moved to "images"
8. confirm all files are named "ezgif-frame-001", "ezgif-frame-002", etc
9. go back to /apps/video_player
10. open __init__.py
11. at line 9, change image_count to equal the number of images in your video
12. if your video is below 160 x 120, change the line "res = "high"" to "res = "low""
13. additional customization can be done within this file, however they are not required.
14. eject the TUFTY drive and open the video_player app, the video should start playing

Current Version(1.3):
Now works on BadgeOS V3.0.0
FPS is greatly improved

Previous Version(1.2):
Now the text "Paused" and "Rewind" will show when doing the corresponding action.
When rewinding you now have to hold down C, and therefore you can choose how much to rewind.

Old version(1.1):
You can now press B to pause, A to unpause, and C to restart video

Old version(1.0):
It now works but you can't pause the video. You can only have one video at a time.
# Timer
This is a basic tool which has a stopwatch and timer.
Note that this is not extremely accurate and will drift by a few seconds if you run it for long enough.

Current Version(1.2):
Now works on BadgeOS V3.0.0

Previous version(1.1):
Timer is now functioning, needs UI improvements

Old verison(1.0):
Stopwatch is now fully functional, timer still shows blank screen
