this is a prototype project operating a vehicle with gesture control. Eventually the vehicle will be semi-autonomous.


Download and extract https://github.com/DFRobot/DFRobot_HuskylensV2/tree/master

Make sure you have smbus and pyserial installed on raspberry pi
sudo apt install python3-smbus
sudo apt install python3-serial

### Wiring Diagram
Raspberry Pi 5
```
|              pin 3 (SDA)|-----|SDA
| Pi5 (Master)       +5 v |-----|+5    HuskyLens2
|              pin 5 (SCL)|-----|SCL
|                         |-----|GND
```

Raspberry Pi 4
```
|              Pin 11 / GPIO 17|-----|1N1                      OUT 1|-------|Motor 1 +
| Pi4 (Slave)  Pin 13 / GPIO 27|-----|1N2  L298N Motor Driver  OUT 2|-------|Motor 1 -
|              Pin 15 / GPIO 22|-----|1N3                      OUT 3|-------|Motor 2 +
|              Pin 16 / GPIO 23|-----|1N4                      OUT 4|-------|Motor 2 -
|                          GND |-----|GND                        GND|-------|GND  9 volt battery  |
|                                    |VCC                        VCC|-------|+9                   |
```
