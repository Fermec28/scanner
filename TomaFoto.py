#!/usr/bin/python
import sys
import subprocess
import os
import time
import  LibraryDynamixel as motor
### IMPORTANTE
# MOTOR 1 SE MUEVE ENTRE 190 Y 80, DONDE 150 ES EL CERO DEL MOTOR, POSICION SUPERIOR
# MOTOR 2 SE MUEVE ENTRE 200 Y 70, DONDE 150 ES EL CERO DEL MOTOR, POSICION LATERAL

#motor.setTorqueLimit(1,60)
#motor.setTorqueLimit(2,60)
#motor.setSpeedLimit(3,100)
#motor.setSpeedLimit(4,100)

#motor.openMotor1()
#motor.closeMotor2()
time.sleep(1)
#setear y mover motor1 y 2 a condiciones iniciales
if(len(sys.argv)==3):
        Nombre=sys.argv[1]
        Documentos= int(sys.argv[2])+1 
        for x in range(1,Documentos):
                #motor.closeMotor1()
                #print("MOTOR 1 - POS 1")
                time.sleep(1)
                bash= "fswebcam -r 1920x1080 -d /dev/video0 --no-banner -s 80 /home/pi/Desktop/ScannerServer/public/"+Nombre+"%d-0.jpeg "%(x)
                #bash1= "fswebcam -r 1920x1080 -d /dev/video1 --no-banner -s 80 /home/pi/Desktop/ScannerServer/public/"+Nombre+"%d-1.jpeg "%(x)
                os.system(bash)                
                #os.system(bash1)                               
                #motor.openMotor2()                
                #motor.openMotor1()                
                #motor.time.sleep(1)
                #motor.closeMotor2()                
                time.sleep(2)
                print {'x':2, 'y':2, 'z':4}
else:
        print "Error argumentos no validos"


#falta integrar luces, integrar el movimiento y tiempo de las luces
