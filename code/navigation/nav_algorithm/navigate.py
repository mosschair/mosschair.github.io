#!/usr/bin/env python3
import sys
import time
from rplidar import RPLidar


PORT_NAME = '/dev/ttyUSB0'

def should_stop(state, distance, angle):
    if distance<610 and angle>=135 and angle<=225 and state == "forward": 
        return True
    else: 
        return False


def can_turn_right(state, distance, angle):
    if distance>1800 and angle>=180 and angle<=270 and state =="stopped":
        return True
    else:
        return False


def can_turn_left(state, distance, angle):
    if distance>1800 and angle>=45 and angle<=135 and state=="stopped":
        return True
    else:
        return False



def run():
    '''Main function'''
    lidar = RPLidar(PORT_NAME)
    try:
        lidar.start_motor()
        iterator = lidar.iter_measures()
        state = "forward"
        for new_scan, quality, angle, distance in iterator:
            if distance > 0:
               if should_stop(state, distance, angle):
                   print("stopping...")
                   state = "stopped"
               if can_turn_right(state, distance, angle):
                   print("turning right...")
                   state = "turning right"
               elif can_turn_left(state, distance, angle):
                   print("turning left...")
                   state = "turning left"


    except KeyboardInterrupt:
        print('Stopping.')
    lidar.clean_input()
    lidar.stop()
    lidar.disconnect()

if __name__ == '__main__':
    run()
