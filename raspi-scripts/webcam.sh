#!/bin/bash

DATE=$(date +"%Y-%m-%d_%H%M%S")
fswebcam --no-banner -r 1920x1080 --crop 840x840,550x220 /home/pi/hack-29-snack/snack-photos/$DATE.jpg 
