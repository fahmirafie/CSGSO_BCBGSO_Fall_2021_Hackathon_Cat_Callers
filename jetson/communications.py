import time
import serial
import struct
import random
import math
from enum import Enum

# Change this to the virtual port of your arduino
SERIAL_PORT = '/dev/ttyUSB0'

# Add more commands here
class CommandType(Enum):
    UP=1
    RIGHT=2
    DOWN=3
    LEFT=4

# Class to contain command info
class Command():
    def __init__(self,command_type,command_param):
        self.command_type = command_type
        self.command_param = command_param

    def __str__(self):
        return CommandType(command_type).name+" "+str(command_param)

# write to serial port in binary
def send_command(command):
    port.write(b'^'+struct.pack('<h', command.command_type.value)+struct.pack('<f', command.command_param))

# read from serial port into variables
def read_info():
    info = port.readline()
    if(info[0] == 94 and len(info[1:-1])==14):
        data = struct.unpack('<hfff', info[1:-1])
        sensor_info = Info(data)
        return sensor_info
    else:
        print(info, info[0])
        return None

# Called every 30 milliseconds (roughly 33 times a second)
def main(i):
    if (port.in_waiting >= 14):
        command_to_send = Command(CommandType.MOVE, angle)
        send_command(command_to_send)

if __name__ == '__main__':
    with serial.Serial(SERIAL_PORT, 9600, timeout=0.5) as port:
        # 5s timeout to wait for reset sequence and diagnostics on arduino
        time.sleep(5)
        while True:
            start_time = time.clock()
            main(1)
            # 30 millisecond loop
            while (time.clock()-start_time)<0.03:
                pass
        