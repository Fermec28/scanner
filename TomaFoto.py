#!/usr/bin/python
import sys
import subprocess
import os
import time
import  LibraryDynamixel as motor
### IMPORTANTE
# MOTOR 1 SE MUEVE ENTRE 300 Y 100, DONDE 150 ES EL CERO DEL MOTOR, POSICION SUPERIOR
# MOTOR 2 SE MUEVE ENTRE 300 Y 0, DONDE 150 ES EL CERO DEL MOTOR, POSICION LATERAL

motor.setTorqueLimit(1,100)
motor.setTorqueLimit(2,100)
motor.setSpeedLimit(3,20)
motor.setSpeedLimit(4,20)
motor.initialState()

#setear y mover motor1 y 2 a condiciones iniciales
if(len(sys.argv)==3):
        Nombre=sys.argv[1]
        Documentos= int(sys.argv[2])+1
        setupcam0= "v4l2-ctl -d /dev/video0 --set-ctrl focus_auto=0"
        os.system(setupcam0)
        setupcam1= "v4l2-ctl -d /dev/video1 --set-ctrl focus_auto=0"
        os.system(setupcam1)
        setupcam01= "v4l2-ctl -d /dev/video0 --set-ctrl focus_absolute=20"
        os.system(setupcam01)
        setupcam11= "v4l2-ctl -d /dev/video1 --set-ctrl focus_absolute=20"
        os.system(setupcam11)
        for x in range(1,Documentos):
                motor.openMotor1()
                #print("MOTOR 1 - POS 1")
                time.sleep(1)
                bash= "fswebcam -r 1920x1080 -d /dev/video0 --no-banner -s 80 /home/pi/Desktop/ScannerServer/public/"+Nombre+"%d-0.jpeg "%(x)                
                bash1= "fswebcam -r 1920x1080 -d /dev/video1 --no-banner -s 80 /home/pi/Desktop/ScannerServer/public/"+Nombre+"%d-1.jpeg "%(x)                
                os.system(bash)
                time.sleep(1)
                os.system(bash1)                               
                motor.openMotor2()
                time.sleep(1.5)
                motor.closeMotor2()                
                #motor.time.sleep(1)
                motor.closeMotor1()                
                
                
else:
        print "Error argumentos no validos"


#falta integrar luces, integrar el movimiento y tiempo de las luces
