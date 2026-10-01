import RPi.GPIO as GPIO
from picamera.array import PiRGBArray
from picamera import PiCamera
import cv2
import time
import numpy as np 

dirFF, dirFT = 1, 2
dirTF, dirTT = 3, 4
esqFF, esqFT = 5, 6
esqTF, esqTT = 7, 8

GPIO.setup(dirFF, GPIO.OUT)
GPIO.setup(dirFT, GPIO.OUT)
GPIO.setup(dirTF, GPIO.OUT)
GPIO.setup(dirTT, GPIO.OUT)
GPIO.setup(esqFF, GPIO.OUT)
GPIO.setup(esqFT, GPIO.OUT)
GPIO.setup(esqTF, GPIO.OUT)
GPIO.setup(esqTT, GPIO.OUT)

pwm_dirFF = GPIO.PWM(dirFF, 100)
pwm_dirFT = GPIO.PWM(dirFT, 100)
pwm_dirTF = GPIO.PWM(dirTF, 100)
pwm_dirTT = GPIO.PWM(dirTT, 100)
pwm_esqFF = GPIO.PWM(esqFF, 100)
pwm_esqFT = GPIO.PWM(esqFT, 100)
pwm_esqTF = GPIO.PWM(esqTF, 100)
pwm_esqTT = GPIO.PWM(esqTT, 100)

pwms = [pwm_dirFF, pwm_dirFT, pwm_dirTF, pwm_dirTT, pwm_esqFF, pwm_esqFT, pwm_esqTF, pwm_esqTT]

vel = 0

for pwm in pwms:
    pwm.start(20)

def parar(): #feito
    for pwm in pwms: 
        pwm.ChangeDutyCycle(0)

def frente(vel = 50): #feito
    pwm_dirFF.ChangeDutyCycle(vel)
    pwm_dirFT.ChangeDutyCycle(0)
    pwm_dirTF.ChangeDutyCycle(vel)
    pwm_dirTT.ChangeDutyCycle(0)
    
    pwm_esqFF.ChangeDutyCycle(vel)
    pwm_esqFT.ChangeDutyCycle(0)
    pwm_esqTF.ChangeDutyCycle(vel)
    pwm_esqTT.ChangeDutyCycle(0)
    
def direita(vel = 50): #feito
    pwm_dirFF.ChangeDutyCycle(0)
    pwm_dirFT.ChangeDutyCycle(vel)
    pwm_dirTF.ChangeDutyCycle(0)
    pwm_dirTT.ChangeDutyCycle(vel)
    
    pwm_esqFF.ChangeDutyCycle(vel)
    pwm_esqFT.ChangeDutyCycle(0)
    pwm_esqTF.ChangeDutyCycle(vel)
    pwm_esqTT.ChangeDutyCycle(0)

def esquerda(vel = 50): #feito

    pwm_dirFF.ChangeDutyCycle(vel)
    pwm_dirFT.ChangeDutyCycle(0)
    pwm_dirTF.ChangeDutyCycle(vel)
    pwm_dirTT.ChangeDutyCycle(0)
    
    pwm_esqFF.ChangeDutyCycle(0)
    pwm_esqFT.ChangeDutyCycle(vel)
    pwm_esqTF.ChangeDutyCycle(0)
    pwm_esqTT.ChangeDutyCycle(vel)

def virar180(vel = 50): #feito
    pwm_dirFF.ChangeDutyCycle(vel)
    pwm_dirFT.ChangeDutyCycle(0)
    pwm_dirTF.ChangeDutyCycle(vel)
    pwm_dirTT.ChangeDutyCycle(0)
    
    pwm_esqFF.ChangeDutyCycle(0)
    pwm_esqFT.ChangeDutyCycle(vel)
    pwm_esqTF.ChangeDutyCycle(0)
    pwm_esqTT.ChangeDutyCycle(vel)
    
    time.sleep(4)

def intersecao(): #feito
    parar()
    time.sleep(1.5)
    frente(vel = 50)

def arena(): #não feito
    
    parar()
    time.sleep(1)

    código

def camerasegue(): #não feito

pretoDireita = PiCamera.cor.pretoDireita
pretoEsquerda = PiCamera.cor.pretoEsquerda    
pretoFrente = PiCamera.cor.pretoFrente   
verdeDireita = PiCamera.cor.verdeDireita
verdeEsquerda = PiCamera.cor.verdeEsquerda
verde180 = PiCamera.cor.verde180
cameraIntersecao = PiCamera.intersecao

DistanciaUltrassom1 = GPIO.input(23)
DistanciaUltrassom2 = GPIO.input(24)

def seguelinha(): #não feito

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
