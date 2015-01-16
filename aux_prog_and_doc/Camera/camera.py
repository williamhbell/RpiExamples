#!/usr/bin/python
import io
import time
import picamera
import SimpleCV

camera = picamera.PiCamera()

camera.resolution = (1280, 1024)
camera.awb_mode = 'fluorescent'

try:
    camera.start_preview()
    time.sleep(2)
    camera.capture('/home/pi/Desktop/image.jpg')
    camera.stop_preview()
finally:
    camera.close()

img = SimpleCV.Image('/home/pi/Desktop/image.jpg')

img.show()
time.sleep(2)

img = img.edges()    
img.show()    
time.sleep(5)

img = img.binarize()  
img.show()  
time.sleep(5)    
