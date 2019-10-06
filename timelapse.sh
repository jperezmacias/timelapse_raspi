#!/bin/bash

DATE=$(date +"%Y_%m_%d_%H_%M_%S")
sudo raspistill -t 999999999 -n -w 1920 -h 1080 -q 85 -tl 30000 -o image_%04d.jpg

