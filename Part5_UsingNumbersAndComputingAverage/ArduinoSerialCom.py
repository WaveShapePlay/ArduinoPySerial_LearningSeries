import serial
import time

ser = serial.Serial('COM3', baudrate = 9600, timeout = 1)
time.sleep(3)
numPoints = 10
dataList = [0]*numPoints

def getValues():
    
    ser.write(b'g')
    arduinoData = ser.readline().decode().split('\r\n')
    
    return arduinoData[0]

    
while(1):

    userInput = input('Get data points?')

    if userInput == 'y':
        for i in range(0,numPoints):
            data = getValues()
            data = int(data)
            dataList[i] = data
            
        dataAvg = sum(dataList)/numPoints
        print(dataAvg)
        print(dataList)
        

    
