import pyttsx3
import RPi.GPIO as GPIO
import time


GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)

class Drive():
    def __init__(self, pins=[40,38,37,31,29,32], frequency=500): #pins=[pwmA,Ai1,Ai2,Bi1,Bi2,pwmB]
        
        self.pins = pins
        for pin in self.pins: #set pins as output
            GPIO.setup(pin, GPIO.OUT) 
        for pin in self.pins[1:-1]: #set motor pins to 0 initially
            GPIO.output(pin, 0)
        self.pwmA = GPIO.PWM(self.pins[0],frequency) #setup pwmA
        self.pwmB = GPIO.PWM(self.pins[5],frequency) #setup pwmB
        
    def run_motor(self, motor, speed, direction=1, runtime=None):
        #general DC run code
        if motor == "A":
            pin1 = self.pins[1]
            pin2 = self.pins[2]
            pwm = self.pwmA
        elif motor == 'B':
            pin2 = self.pins[3]
            pin1 = self.pins[4]
            pwm = self.pwmB
        if direction:
            GPIO.output(pin1,1) #direction 1
            GPIO.output(pin2,0)
        else:
            GPIO.output(pin1,0) #direction 2
            GPIO.output(pin2,1) 
        pwm.start(speed)
        if runtime is not None:
            time.sleep(runtime)
            pwm.stop()

    def stop_motor(self, motor):
        if motor == "A":
            self.pwmA.stop()
        elif motor == 'B':
            self.pwmB.stop()
    
    def stop_motors(self):
        self.stopMotor("A")
        self.stopMotor("B")

    def forward(self, speed, runtime=None):
        print('drive forward speed '+str(speed))
        self.runMotor("A", speed, 1)
        self.runMotor("B", speed, 1)
        if runtime is not None:
            time.sleep(runtime)
            self.stopMotors()

    def backward(self, speed, runtime=None):
        print('drive back speed '+str(speed))
        self.runMotor("A", speed, 0)
        self.runMotor("B", speed, 0)
        if runtime != None:
            time.sleep(runtime)
            self.stopMotors()

    def left(self, angle=None):
        print('drive left angle '+str(angle))
        self.runMotor("A", 50, 1)
        self.runMotor("B", 50, 0)
        if angle != None:
            runtime = angle/90
            time.sleep(runtime)
            self.stopMotors()
        
    def right(self, angle=None):
        print('drive right angle '+str(angle))
        self.runMotor("A", 50, 0)
        self.runMotor("B", 50, 1)
        if angle != None:
            runtime = angle/180
            time.sleep(runtime)
            self.stopMotors()

class Light():
    def __init__(self):
        GPIO.setup(3, GPIO.OUT)
        GPIO.setup(5, GPIO.OUT)
        GPIO.setup(7, GPIO.OUT)
        self.RED = GPIO.PWM(3, 100)
        self.GREEN = GPIO.PWM(5, 100)
        self.BLUE = GPIO.PWM(7, 100)
        self.RED.start(1)
        self.GREEN.start(1)
        self.BLUE.start(1)

    def set_colour(self, colour):
        if colour == "red":
            self.RED.ChangeDutyCycle(100)
            self.GREEN.ChangeDutyCycle(1)
            self.BLUE.ChangeDutyCycle(1)

        elif colour == "green":
            self.RED.ChangeDutyCycle(1)
            self.GREEN.ChangeDutyCycle(100)
            self.BLUE.ChangeDutyCycle(1)

        elif colour == "blue":
            self.RED.ChangeDutyCycle(1)
            self.GREEN.ChangeDutyCycle(1)
            self.BLUE.ChangeDutyCycle(100)

        elif colour == "yellow":
            self.RED.ChangeDutyCycle(100)
            self.GREEN.ChangeDutyCycle(100)
            self.BLUE.ChangeDutyCycle(1)

        elif colour == "orange":
            self.RED.ChangeDutyCycle(100)
            self.GREEN.ChangeDutyCycle(60)
            self.BLUE.ChangeDutyCycle(1)

        elif colour == "purple":
            self.RED.ChangeDutyCycle(100)
            self.GREEN.ChangeDutyCycle(1)
            self.BLUE.ChangeDutyCycle(100)

        elif colour == "pink":
            self.RED.ChangeDutyCycle(100)
            self.GREEN.ChangeDutyCycle(50)
            self.BLUE.ChangeDutyCycle(100)


    def custom_colour(self, r, g, b):
        self.RED.ChangeDutyCycle(r/2.55)
        self.GREEN.ChangeDutyCycle(g/2.55)
        self.BLUE.ChangeDutyCycle(b/2.55)

    def off(self):
        self.RED.ChangeDutyCycle(1)
        self.GREEN.ChangeDutyCycle(1)
        self.BLUE.ChangeDutyCycle(1)


class Sense():
    def __init__(self):
        GPIO.setup(13,IO.IN) #GPIO 13 -> IR sensor as input
        GPIO.setup(15,IO.IN) #GPIO 13 -> IR sensor as input

    def left(self):
        if(GPIO.input(13)): #object is far away
            return False

        else:
            return True

    def right(self):
        if(GPIO.input(15)): #object is far away
            return False

        else:
            return True


class Sound():
    def __init__(self):
        self.engine = pyttsx3.init() 
        print('TTS System Initialised')

    def say(self, text):
        self.engine.setProperty('rate', 150)     # setting up new voice rate
        self.engine.setProperty('volume',9)    # setting up volume level  between 0 and 1
        self.engine.say(text)
        self.engine.runAndWait()
        self.engine.stop()