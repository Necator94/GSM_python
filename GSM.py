import Adafruit_BBIO.UART as UART
import serial
import time 
import io

UART.setup("UART4")
ser = serial.Serial(port = "/dev/ttyO4", baudrate=9600, timeout = 2)


def readMsg():
	ser.close()
	ser.open()
	if ser.isOpen():
		ser.write("at\r")
   		answ = ser.readline() 
  		answ = ser.readline()[:-2]
	ser.close()
	return answ

def sendComm(command):
	data = []
	ser.close()
	ser.open()
	if ser.isOpen():
		ser.write(command + "\r")
   		data.append(ser.readline()) 
  		data.append(ser.readline())
  		data.append(ser.readline()) 
	ser.close()
	return data



print sendComm("at")


