#/dev/ttyACM0
# export ROS_PACKAGE_PATH=~/PycharmProjects/RoboSys:$ROS_PACKAGE_PATH

import serial
a = 1
while a:
    ser = serial.Serial('/dev/ttyACM0', 9600)
    # ser.write(b'1')
    print(ser.readline())     #  //выводит b''

file = open("base.txt")
onstring = file.read().split("\n")[:-1]
user = dict()
for item in onstring:
    key = item.split(" ")[0]
    value = item.split(" ")[1:]
    user[key] = value
file.close()



import sys
print('Using version:', sys.version[:5])