
# Infrared Camera Streaming

## Hardware used

- Raspberry Pi 4
- TOPDON TC001 Thermal Imaging Camera

## Software
- Python
- OpenCV

## Description

This uses a thermal imaging camera such as the TOPDON TC001, and connects to the Raspberry Pi. It is then able to send stream data towards the Pi, where it is then able to image process and frame via OpenCV. After that the data is then sent via TCP connection to a computer, where the computer then receives the data and is able to display information

Some future work can be done to work on changing color settings and being able to detect movement and objects around it. Also being able to detect temperatures of each heat signature could be very valuable to the user. 

This software can also be used for greater use cases such as drone fire detection and Reconnaissance
## 


## Acknowledgements

 - [Thermal Imaging Processing](https://github.com/leswright1977/PyThermalCamera)
 - [TOPDON TC001](https://www.topdon.com/products/tc001)
 - [Raspberry Pi](https://www.raspberrypi.com/products/raspberry-pi-4-model-b/)

