#!/bin/bash

#DATE=$(date +"%Y-%m-%d_%H%M%S")
fswebcam --no-banner -r 1920x1080 --crop 840x840,550x220 /home/pi/hack-29-snack/devbox_backend/image.jpg 
curl -X POST -F 'file=@/home/pi/hack-29-snack/devbox_backend/image.jpg' 172.30.166.220:5000/images
