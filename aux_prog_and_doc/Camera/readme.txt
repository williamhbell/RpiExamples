Using the Camera

Basic use of the camera from the
 terminal:

Photographs using raspistill

For example, raspistill -n -awb fluorescent -w 640 -h 480 -o image.bmp

Videos using raspivid - see the help

Progammatic control of the camera

We can use the picamera library, and then process the resulting image with SimpleCV. Try it with:

python camera.py

You can extend how you analyze the image, and also take multiple images. For example:

http://tutorial.simplecv.org/en/latest/examples/image-math.html

from SimpleCV import *

cam = Camera()
threshold = 5.0 # if mean exceeds this amount do something

while True:
        previous = cam.getImage() #grab a frame
        time.sleep(0.5) #wait for half a second
        current = cam.getImage() #grab another frame
        diff = current - previous
        matrix = diff.getNumpy()
        mean = matrix.mean()

        diff.show()

        if mean >= threshold:
                print "Motion Detected"

Initial Setup

sudo apt-get install ipython python-opencv python-scipy python-numpy python-setuptools python-pip

Next download and install SimpleCV itself

sudo pip install https://github.com/sightmachine/SimpleCV/zipball/master

sudo pip install svgwrite

References

https://github.com/OpenLabTools/OpenLabTools/wiki/Using-the-Raspberry-Pi-camera-module-with-SimpleCV

http://picamera.readthedocs.org/en/release-1.9/index.html

