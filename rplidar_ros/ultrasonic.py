'''
    Ain Shams University
    Faculty of Engineering
    SLAM Graduation Project 2019
'''

def echo(Trig, Echo):
    
    GPIO.output(Trig, True)
    time.sleep(0.00001)
    GPIO.output(Trig, False)


    while GPIO.input (Echo) == 0:
        StartTime = time.time()

    while GPIO.input (Echo) == 1:
        StopTime = time.time()


    TimeElapsed = StopTime -StartTime

    distance = (TimeElapsed * 34300)/2
    
    return distance


'''
    Ain Shams University
    Faculty of Engineering
    SLAM Graduation Project 2019
'''
