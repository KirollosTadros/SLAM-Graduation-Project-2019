'''
    Ain Shams University
    Faculty of Engineering
    SLAM Graduation Project 2019
'''


import RPi.GPIO as GPIO
import sys, tty, termios, time
import car
import ultrasonic

GPIO.setmode(GPIO.BCM)

def getch():
    fd = sys.stdin.fileno()
    old_settings = termios.tcgetattr(fd)
    try:
        tty.setraw(sys.stdin.fileno())
        ch = sys.stdin.read(1)
    finally:
        termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)
    return ch




#Car Pin Setup
GPIO.setup(car.enA, GPIO.OUT)
GPIO.setup(car.enB, GPIO.OUT)
GPIO.setup(car.IN1, GPIO.OUT)
GPIO.setup(car.IN2, GPIO.OUT)
GPIO.setup(car.IN3, GPIO.OUT)
GPIO.setup(car.IN4, GPIO.OUT)

#Frequency of PWM pins
enA_PWM=GPIO.PWM(car.enA,500)
enB_PWM=GPIO.PWM(car.enB,500)



while True:
    c= getch()


    if(c=="w"):
        car.Motor_A_Forward(100)
        car.Motor_B_Forward(100)


    elif (c== "a"):
        car.Motor_A_Forward(85)
        car.Motor_B_Stop()


    elif (c == "d"):
        car.Motor_A_Stop()
        car.Motor_B_Forward(85)

    elif(c=="s"):
        car.Motor_A_Backward(100)
        car.Motor_B_Backward(100)


    elif(c==" "):
        car.Motor_A_Stop()
        car.Motor_B_Stop()

    elif (c=="q"):
        break



'''
    Ain Shams University
    Faculty of Engineering
    SLAM Graduation Project 2019
'''
