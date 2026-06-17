# tufty2350-apps
Any apps I make for the tufty 2350 will be placed in here.

# Video Player
This allows you to play videos on your Tufty. 
PLEASE COMPLETLY READ THE FOLLOWING INSTRUCTIONS!

1. First, record your video and convert it to png images at https://ezgif.com/video-to-png
2. select the resolution to be below 320x240
3. Download them as a .zip file
4. extract all, then upload the unnzipped folder to /apps/video_player/
5. rename the folder you just moved to "images"
6. confirm all files are named "ezgif-frame-001", "ezgif-frame-002", etc
7. go back to /apps/video_player
8. open __init__.py
9. at line 9, change image_count to equal the number of images in your video
10. additional customization can be done within this file, such as resolution changing and fps, however they are not required.
11. eject the TUFTY drive and open the video_player app, the video should start playing

Current version(1.1):
You can now press B to pause, A to unpause, and C to restart video

Previous version(1.0):
It now works but you can't pause the video. You can only have one video at a time.
# Timer
This is a basic tool which has a stopwatch and timer.

Current version(1.1):
Timer is now functioning, needs UI improvements

Preivous verison(1.0):
Stopwatch is now fully functional, timer still shows blank screen
