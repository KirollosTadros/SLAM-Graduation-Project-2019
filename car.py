'''
    Ain Shams University
    Faculty of Engineering
    SLAM Graduation Project 2019
'''



#Motor A pins
enA = 22
IN1 = 24
IN2 = 17

#Motor B Pins
enB = 23
IN3 = 27
IN4 = 18


#Pin Setup

GPIO.setup(enA, GPIO.OUT)
GPIO.setup(enB, GPIO.OUT)
GPIO.setup(IN1, GPIO.OUT)
GPIO.setup(IN2, GPIO.OUT)
GPIO.setup(IN3, GPIO.OUT)
GPIO.setup(IN4, GPIO.OUT)

#Frequency of PWM pins
enA_PWM=GPIO.PWM(enA,500)
enB_PWM=GPIO.PWM(enB,500)

#Moto Functions

def Motor_A_Forward(PWM):
    GPIO.output (IN1, True)
    GPIO.output (IN2, False)
    enA_PWM.start(PWM)

def Motor_A_Backward(PWM):
    GPIO.output (IN1, False)
    GPIO.output (IN2, True)
    enA_PWM.start(PWM)

def Motor_A_OFF():
    GPIO.output (IN1, False)
    GPIO.output (IN2, False)
    enA_PWM.start(100)

def Motor_A_Stop():
    GPIO.output (IN1, True)
    GPIO.output (IN2, True)
    enA_PWM.start(100)


def Motor_B_Forward(PWM):
    GPIO.output (IN3, True)
    GPIO.output (IN4, False)
    enB_PWM.start(PWM)

def Motor_B_Backward(PWM):
    GPIO.output (IN3, False)
    GPIO.output (IN4, True)
    enB_PWM.start(PWM)


def Motor_B_OFF():
    GPIO.output (IN3, False)
    GPIO.output (IN4, False)
    enB_PWM.start(100)

def Motor_B_Stop():
    GPIO.output (IN3, True)
    GPIO.output (IN4, True)
    enB_PWM.start(100)


'''
    Ain Shams University
    Faculty of Engineering
    SLAM Graduation Project 2019
'''
