# -*- coding: utf-8 -*-c
import sys
from Dynamixel import dynamixel
import time

ID = 1

# Control table address
ADDR_TORQUE_ENABLE          = 24
ADDR_LED                    = 25
ADDR_GOAL_POSITION          = 30
ADDR_MOVING_SPEED           = 32
ADDR_TORQUE_LIMIT           = 34
ADDR_PRESENT_POSITION       = 36
ADDR_PRESENT_SPEED          = 38
ADDR_PRESENT_LOAD           = 40
ADDR_PRESENT_VOLT           = 42
ADDR_PRESENT_TEMP           = 43

# Protocol version
PROTOCOL_VERSION            = 1                             # See which protocol version is used in the Dynamixel
# Servo
#DXL_ID                      = 1                            # Dynamixel ID: 1
BAUDRATE                    = 1000000                       # Baud Rate
#COM                         = ''                            # Check which port is being used on your controller
TORQUE_ENABLE               = 1                             # Value for enabling the torque
TORQUE_DISABLE              = 0                             # Value for disabling the torque
DXL_MINIMUM_POSITION_VALUE  = 400                           # Dynamixel will rotate between this value
DXL_MAXIMUM_POSITION_VALUE  = 800                           # and this value (note that the Dynamixel would not move when the position value is out of movable range. Check e-manual about the range of the Dynamixel you use.)
DXL_MOVING_STATUS_THRESHOLD = 20                            # Dynamixel moving status threshold
COMM_SUCCESS                = 0                             # Communication Success result value
COMM_TX_FAIL                = -1001                         # Communication Tx Failed
ax12 = dynamixel()


def dec2bit(percent):
    return int(percent*1023/100)

def setTorqueLimit(dyna_id, limit):
    """Torque limit:
    Params Dynamixel ID
    Torque limit [0 - 100]%"""
    tor = dec2bit(limit)
    ax12.set_ax_reg(dyna_id, ADDR_TORQUE_LIMIT, ([(tor%256),(tor>>8)]))
    
def setSpeedLimit(dyna_id, limit):
    """Speed limit:
    Params Dynamixel ID
    Torque limit [0 - 100]%"""
    vel = dec2bit(limit)
    ax12.set_ax_reg(dyna_id, ADDR_MOVING_SPEED, ([(vel%256),(vel>>8)]))
    

def ang2bit(angle):
    return int(angle*1023/300)

def bit2ang(bit):
    return int(bit*300/1023)

def moveCenter(dyna_id):
    moveDyna(dyna_id, 512)

def moveDyna(dyna_id, goal_pos):
    """Position between 0 and 1023"""
    ax12.set_ax_reg(dyna_id, ADDR_GOAL_POSITION, ([(goal_pos%256),(goal_pos>>8)]))
    
def moveToAngle(dyna_id, angle):
    """Position between 0Â° and 300Â°"""
    goal_pos = ang2bit(angle)
    moveDyna(dyna_id, goal_pos)

def closeMotor1():
    moveToAngle(1, 60)

def openMotor1():
    moveToAngle(1, 150)

def closeMotor2():
    moveToAngle(2, 150)

def openMotor2():
    moveToAngle(2, 60)

if __name__ == '__main__':
    motor = 2
    setTorqueLimit(motor, 100)
    setSpeedLimit(motor, 50)
    #moveCenter(2)
    moveToAngle(motor, 200)
