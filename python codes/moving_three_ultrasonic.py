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
Trig_M= 26
Echo_M = 19

Trig_R = 13
Echo_R = 6

Trig_L = 21
Echo_L = 20



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



#Ultrasonic Pins Setup
GPIO.setup(Trig_M, GPIO.OUT)
GPIO.setup(Echo_M, GPIO.IN)

GPIO.setup(Trig_L, GPIO.OUT)
GPIO.setup(Echo_L, GPIO.IN)

GPIO.setup(Trig_R, GPIO.OUT)
GPIO.setup(Echo_R, GPIO.IN)


while True:
    try:


        dist_m = ultrasonic.echo (Trig_M, Echo_M)
        dist_l = ultrasonic.echo (Trig_L, Echo_L)
        dist_r = ultrasonic.echo (Trig_R, Echo_R)

        if dist_m>40:
            car.Motor_A_Forward(100)
            car.Motor_B_Forward(100)

        elif dist_r<30 and dist_m>40:

            car.Motor_A_Stop()
            car.Motor_B_Stop()

            time.sleep(0.5)

            car.Motor_A_Forward(100)
            car.Motor_B_Backward(100)

            time.sleep(0.5)


        elif dist_l<30 and dist_m>40:

            car.Motor_A_Stop()
            car.Motor_B_Stop()

            time.sleep(0.5)

            car.Motor_A_Backward(100)
            car.Motor_B_Forward(100)

            time.sleep(0.5)



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
