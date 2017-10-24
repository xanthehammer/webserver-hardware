# This is lab done at IT College by Aleksandr Logvinenko in Lauri's class

[Lab details](https://wiki.itcollege.ee/index.php/Category:I600_Introduction_to_Computers_and_Informatics#Assignment:_Set_up_basic_IoT_scenario)
[Link to the blog](https://lauri.võsandi.com/2017/06/espressif.html)

# What you need
1. ESP32 or ESP8266 microcontroller
2. LED lamp
3. Jumper cables (Male to female)
4. Programs installed:
   1. [pip](https://pip.pypa.io/en/stable/)
   2. picocom
     * Ubuntu: `sudo apt-get install picocom`
     * OS X: Use [Homebrew](https://brew.sh/) `brew install picocom`
   3. wget
     * Ubuntu: `sudo apt-get install wget`
     * OS X: Use [Homebrew](https://brew.sh/) `brew install wget`
   4. esptool
     * `pip install esptool`
   5. ampy
     * `pip install adafruit-ampy`
   6. Skip this if you are using Ubuntu:
     * Download [Silabs VCP driver](https://www.silabs.com/products/development-tools/software/usb-to-uart-bridge-vcp-drivers) for OS X 


# Getting started
#### Flashing MicroPython
    wget http://micropython.org/resources/firmware/esp32-20171017-v1.9.2-279-g090b6b80.bin
    esptool.py -p /dev/ttyUSB0 -b 460800 erase_flash
    esptool.py -p /dev/ttyUSB0 -b 460800 write_flash --flash_mode dio 0x1000 esp32-*.bin
    
    Note: in OS X /dev/ttyUSB0 is replaced with /dev/tty.SLAB_USBtoUART.
#### Getting microcontoller ready
    ampy -p /dev/ttyUSB0 put boot.py && ampy -p /dev/ttyUSB0 put main.py
#### Connecting to microcontoller
Reboot microcontroller with the button
Open terminal `CTRL+ALT+T` and use picocom to connect to the microcontroller:

    picocom -b115200 /dev/ttyUSB0
#### Enter `https://<ip_address>:8080/` in browser
And check if it's working!


