#! /usr/bin/env python3

import RPi.GPIO as GPIO
import serial


ENABLE_PIN  = 18              # The BCM pin number corresponding to GPIO1

SERIAL_PORT = '/dev/ttyAMA0'  # Location of serial port.  
# This might be different depending on Operating System and version of Pi. 

                              
def validate_rfid(code):
    # The code being read is 12 characters long with the first character 
	# being a line feed and the last character being a carriage return.
    
	s = code.decode("ascii")
       
    if (len(s) == 12):
      	# return True
	
	return s[1:11] # return RFID code

    
def main():
    # Initialize the Raspberry Pi by suppressing warnings 
    GPIO.setwarnings(False)
	# Use the BCM pin numbering scheme
    GPIO.setmode(GPIO.BCM)

    # GPIO1 pin to be used to turn the RFID reader on/off
    GPIO.setup(ENABLE_PIN, GPIO.OUT)

    # Setting the pin to LOW will turn the reader on.  You should notice
    # the green LED light on the reader turn red if successfully enabled.
    print("Enabling RFID reader and reading from serial port: " + SERIAL_PORT)
    GPIO.output(ENABLE_PIN, GPIO.LOW)

    # Set up the serial port as per the Parallax reader's datasheet.
    ser = serial.Serial(baudrate = 2400,
                        bytesize = serial.EIGHTBITS,
                        parity   = serial.PARITY_NONE,
                        port     = SERIAL_PORT,
                        stopbits = serial.STOPBITS_ONE,
                        timeout  = 3)
    
	#ser = serial.Serial("/dev/ttyAMA0",baudrate=2400, timeout=5)
    
	# Wrap everything in a try block to catch any exceptions.
    try:
       var = 1
        # Loop forever, or until CTRL-C is pressed.
       while var:
            #Read in 12 byte data from serial port
            print("Reading tag...")
            data = ser.read(12)
            #print(data)
            
	        #Validate read data
            code = validate_rfid(data)
            #print(code)
            
	    #If validate_rfid() code, then check if registered or not
            if code:
                print("Read RFID code: " + code); 
		# Print message based on Tag being read
		if ("415D7D42C" in code):
			print("Welcome User1")
			var = 0
	        	GPIO.output(ENABLE_PIN, GPIO.HIGH)
		elif ("415EA0D36" in code):
			print("Welcome User2")
			var = 0
	        	GPIO.output(ENABLE_PIN, GPIO.HIGH)
		else:
			print("Please contact admin to register first")
			var = 0
	        	GPIO.output(ENABLE_PIN, GPIO.HIGH)
		
    except Exception as e:
	print (e)
        # If an exception caught, disable the reader 
		# this is done by setting the pin to HIGH
		# exit the program
        print("Disabling RFID reader...")
        GPIO.output(ENABLE_PIN, GPIO.HIGH)

        
if __name__ == "__main__":
    main()