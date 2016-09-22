import time
import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BCM) # I prefer this way


#Pins corresponding to the different direcitons of movement.
PinDirections = {"Ra+" : 17 , "Ra-" : 18, "Dec+" : 23 , "Dec-" : 24 }

#Init to False for pins
GPIO.setup(PinDirections["Dec+"], GPIO.OUT)
GPIO.output(PinDirections["Dec+"], False)

GPIO.setup(PinDirections["Dec-"], GPIO.OUT)
GPIO.output(PinDirections["Dec-"], False)

GPIO.setup(PinDirections["Ra+"], GPIO.OUT)
GPIO.output(PinDirections["Ra+"], False)

GPIO.setup(PinDirections["Ra-"], GPIO.OUT)
GPIO.output(PinDirections["Ra-"], False)


def Move(Direction,step):
    # 100 steps = tout l'ecran visible. Attention : 1 step en DEC est moins grand qu'un step en RA (ecran rectangle)
    
    ValidDirections = ["Dec+", "Dec-", "Ra+", "Ra-"]
    if Direction in ValidDirections :
        GPIO.output(PinDirections[Direction], GPIO.HIGH)
        #Duration est fonction de la direction...
        if Direction = "Dec+" || Direction = "Dec-"
            Duration = 30*Step*0.2729/100 #1/30 est 8 fois la vitesse sidérale (mode fast) en deg/sec. 0.2729 est l'angle vu par le capteur en deg
        else
		    Duration = 30*Step*0.3638/100 # comme plus haut avec un angle plus gros car le capteur est plus large selon la direction RA
        time.sleep(Duration)
        GPIO.output(PinDirections[Direction], GPIO.LOW)
    else:
        print("Direction not among : Dec+, Dec-, Ra+, Ra-")
    time.sleep(Duration)



