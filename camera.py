# Importação de bibliotecas para o reconhecimento dos pinos GPIO

import RPi.GPIO as GPIO
from picamera.array import PiRGBArray
from picamera import PiCamera
import cv2
import numpy as np #números fofuchos, o time sleep tá aqui
from adafruit_motorkit import MotorKit #biblioteca que reconhece os motores
kit = MotorKit()

GPIO.setmode(GPIO.BCM)

dirF, dirT = 26, 6
esqF, esqT = 5, 19

GPIO.setup(dirF, GPIO.OUT)
GPIO.setup(dirT, GPIO.OUT)
GPIO.setup(esqF, GPIO.OUT)
GPIO.setup(esqT, GPIO.OUT)

velDirF = GPIO.PWM(dirF, 100)
velDirT = GPIO.PWM(dirT, 100)
velEsqF = GPIO.PWM(esqF, 100)
velEsqT = GPIO.PWM(esqT, 100)

def cameraDetectouVerdeDireita():
    changeDutyCycle(velDirF, 100)
    changeDutyCycle(velDirT, 0)
    changeDutyCycle(velEsqF, 0)
    changeDutyCycle(velEsqT, 100)

def cameraDetectouVerdeEsquerda():
    código

def cameraDetectouVerde180():
    código

def cameraDetectouIntersecao():
    código

def frente():
    kit.motor1.throttle = 1.0  # M1: Frente Esquerda
    kit.motor2.throttle = 1.0  # M2: Trás Esquerda
    kit.motor3.throttle = 1.0  # M3: Trás Direita
    kit.motor4.throttle = 1.0  # M4: Frente Direita

DistanciaUltrassom1 = GPIO.input(23)
DistanciaUltrassom2 = GPIO.input(24)

def segue.linha(): 

    if (cameraDetectouVerdeDireita = true):
        vel = 0
        time.sleep(1.0)
        vel = 15
        virarDireita()

    elif (cameraDetectouVerdeEsquerda = true):
        vel = 0
        time.sleep(1.0)
        vel = 15
        virarEsquerda()

    elif (cameraDetectouVerde180 = true):
        vel = 0
        time.sleep(1.0)
        vel = 15
        verde180()

    elif (cameraDetectouIntersecao = true):
        vel = 15

    elif (DistanciaUltrassom1 < 10 and DistanciaUltrassom2 < 20):
        vel = 0
        time.sleep(1.0)
        vel = 15
        arena()
        
    else: 
        Frente()
