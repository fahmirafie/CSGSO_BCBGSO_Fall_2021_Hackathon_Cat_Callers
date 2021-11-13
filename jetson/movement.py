#! /usr/bin/env python3

import serial
import time
    
ON = bytes("on","utf8")
OFF = bytes("off","utf8")

def main():
    led_state = True
    with serial.Serial('/dev/ttyUSB0',9600,timeout=3.) as port:
        time.sleep(1.6)
        while(True):
            # get postion of cat
            # send position translated to arduino
            next_led_state = ON if led_state else OFF
            print("asking led to switch on" if led_state else "asking led to switch off")
            port.write(next_led_state)
            port.flush()
            response = port.readline()
            print(response)
            led_state = not led_state
            time.sleep(.1)

if __name__=="__main__":
    main()
    
