#!/bin/bash

DATE=$(date +"%Y-%m-%d_%H%M%S")
fswebcam --no-banner -r 640x480 --crop 320x390,160x80 --scale 224x224 /home/pi/snacks-photos/$DATE.jpg 
