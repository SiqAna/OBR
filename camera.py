import RPi.GPIO as GPIO
from picamera.array import PiRGBArray
from picamera import PiCamera
import cv2
import time
import numpy as np #números fofuchos, o time sleep tá aqui
from adafruit_motorkit import MotorKit #biblioteca que reconhece os motores
kit = MotorKit()

GPIO.setmode(GPIO.BCM)

GPIO.setup(dirF, GPIO.OUT)
GPIO.setup(dirT, GPIO.OUT)
GPIO.setup(esqF, GPIO.OUT)
GPIO.setup(esqT, GPIO.OUT)

def direita():
    
    parar()
    time.sleep(1)

    kit.motor1.throttle = 0.5  # M1: Frente Esquerda
    kit.motor2.throttle = -0.5  # M2: Trás Esquerda
    kit.motor3.throttle = 0.5  # M3: Trás Direita
    kit.motor4.throttle = -0.5  # M4: Frente Direita

def esquerda():

    parar()
    time.sleep(1)

    kit.motor1.throttle = -0.5  # M1: Frente Esquerda
    kit.motor2.throttle = 0.5  # M2: Trás Esquerda
    kit.motor3.throttle = -0.5  # M3: Trás Direita
    kit.motor4.throttle = 0.5  # M4: Frente Direita
    
    time.sleep(2)


def virar180():

    parar()
    time.sleep(1)

    kit.motor1.throttle = -0.5  # M1: Frente Esquerda
    kit.motor2.throttle = 0.5  # M2: Trás Esquerda
    kit.motor3.throttle = -0.5  # M3: Trás Direita
    kit.motor4.throttle = 0.5  # M4: Frente Direita

    time.sleep(4)

def intersecao():

    parar()
    time.sleep(1.5)

    frente()


def frente():
    
    kit.motor1.throttle = 0.5  # M1: Frente Esquerda
    kit.motor2.throttle = 0.5  # M2: Trás Esquerda
    kit.motor3.throttle = 0.5  # M3: Trás Direita
    kit.motor4.throttle = 0.5  # M4: Frente Direita

def arena():
    
    parar()
    time.sleep(1)

    código

def parar():
    
    kit.motor1.throttle = 0  # M1: Frente Esquerda
    kit.motor2.throttle = 0  # M2: Trás Esquerda
    kit.motor3.throttle = 0  # M3: Trás Direita
    kit.motor4.throttle = 0  # M4: Frente Direita

def camerasegue():

pretoDireita = PiCamera.cor.pretoDireita
pretoEsquerda = PiCamera.cor.pretoEsquerda    
pretoFrente = PiCamera.cor.pretoFrente   
verdeDireita = PiCamera.cor.verdeDireita
verdeEsquerda = PiCamera.cor.verdeEsquerda
verde180 = PiCamera.cor.verde180
cameraIntersecao = PiCamera.intersecao

DistanciaUltrassom1 = GPIO.input(23)
DistanciaUltrassom2 = GPIO.input(24)

def seguelinha(): 

    if verdeDireita == True:
        direita()
        time.sleep(2)

    elif verdeEsquerda == True:
        esquerda()
        time.sleep(2)

    elif verde180 == True:
        virar180()

    elif cameraIntersecao == True:
        intersecao()
    elif pretoFrente == True:
        frente()
    elif pretoDireita == True:
        direita()
        time.sleep(0.5)
    elif pretoEsquerda == True:
        esquerda()
        time.sleep(0.5)

    elif DistanciaUltrassom1 < 10 and DistanciaUltrassom2 < 20:
        arena()
        
    else: 
        frente()

seguelinha()
