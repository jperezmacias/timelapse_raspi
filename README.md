# TimeLapse Nano-Project

This repository contains a simple nano-project for creating a timelapse using a Raspberry Pi 2. The project consists of two files: `timelapse.sh` and `calculations.py`.

## `timelapse.sh`

The `timelapse.sh` script is a Bash script that captures images at regular intervals using the Raspberry Pi camera module. The images are saved with a filename format of `image_XXXX.jpg`, where `XXXX` represents the sequential number of the image. The key parameters used in the script are as follows:

- `DATE=$(date +"%Y_%m_%d_%H_%M_%S")`: This line sets the variable `DATE` to the current date and time in the format `YYYY_MM_DD_HH_MM_SS`. This variable is not used in the script, but it might have been intended to include the date in the filenames of the captured images.

- `sudo raspistill -t 999999999 -n -w 1920 -h 1080 -q 85 -tl 30000 -o image_%04d.jpg`: This command uses the `raspistill` utility to capture images. The parameters used are:
  - `-t 999999999`: The time (in milliseconds) the script will run, effectively setting it to run indefinitely.
  - `-n`: Disables the preview window during image capture.
  - `-w 1920`: Sets the width of the captured images to 1920 pixels.
  - `-h 1080`: Sets the height of the captured images to 1080 pixels.
  - `-q 85`: Sets the image quality to 85 (out of 100).
  - `-tl 30000`: Sets the time interval between consecutive image captures to 30000 milliseconds (30 seconds).
  - `-o image_%04d.jpg`: Defines the output filename pattern. The `%04d` will be replaced by the sequential number of the image.

## `calculations.py`

The `calculations.py` script performs some calculations related to the timelapse. The calculated values are:

- `t=30`: This variable stores the time interval (in seconds) between consecutive image captures.

- `size=1.4`: This variable represents the size (in MB) of an individual image.

- `npic_size=3600/t*24*size`: This variable calculates the total size (in MB) of all the images captured in a day (24 hours) based on the given time interval and image size.

- `npic=3600/t*24`: This variable calculates the total number of images captured in a day (24 hours) based on the given time interval.

- `minutes=npic/(30*60)`: This variable calculates the total duration (in minutes) of the timelapse based on the number of images captured and the given time interval.

The script then prints the calculated values for the size, number of pictures, and total minutes of the timelapse.

## Result

The timelapse project has been completed, and the result can be viewed on YouTube at the following link: [Timelapse Result](https://www.youtube.com/watch?v=oeSyCpV7Wuc&t=4s).

It's worth noting that the README.md currently contains a comment that mentions missing the time information. It seems like the `DATE` variable in `timelapse.sh` was supposed to address this, but it is not used in the script. If you wish to include the date in the image filenames, you can modify the `raspistill` command to use the `DATE` variable in the filename pattern.

The nano-project appears to have been a fun and successful endeavor, capturing the gym's activity over time. If there are any further improvements or updates to the project, feel free to add them to this README or the code itself.
