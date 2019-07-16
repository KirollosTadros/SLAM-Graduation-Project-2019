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

#ultrasonic pins
Trig = 26
Echo = 19



#Motor Pins setup
GPIO.setup(car.enA, GPIO.OUT)
GPIO.setup(car.enB, GPIO.OUT)
GPIO.setup(car.IN1, GPIO.OUT)
GPIO.setup(car.IN2, GPIO.OUT)
GPIO.setup(car.IN3, GPIO.OUT)
GPIO.setup(car.IN4, GPIO.OUT)

#PWM pins frequency
enA_PWM=GPIO.PWM(car.enA,500)
enB_PWM=GPIO.PWM(car.enB,500)

#Ultrasonic Pins Setup
GPIO.setup(Trig, GPIO.OUT)
GPIO.setup(Echo, GPIO.IN)



while True:
    try:

        dist = ultrasonic.echo (Trig, Echo)


        if dist >30:
            car.Motor_A_Forward(100)
            car.Motor_B_Forward(100)




        else:
            car.Motor_A_Stop()
            car.Motor_B_Stop()

            time.sleep(0.5)

            car.Motor_A_Forward(100)
            car.Motor_B_Backward(100)

            time.sleep(0.7)


        

    
    except KeyboardInterrupt:
        GPIO.cleanup()




'''
    Ain Shams University
    Faculty of Engineering
    SLAM Graduation Project 2019
'''
