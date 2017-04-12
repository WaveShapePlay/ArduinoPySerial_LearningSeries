import serial
import time

ser = serial.Serial('COM3', baudrate = 9600, timeout = 1)
time.sleep(3)
numPoints = 5
dataList = [0]*numPoints

def getValues():
    
    ser.write(b'g')
    arduinoData = ser.readline().decode('ascii')

    return arduinoData


while(1):

    userInput = input('Get data points?')

    if userInput == 'y':
        for i in range(0,numPoints):
            data = getValues()
            dataList[i] = data
       
        print(dataList)

    
