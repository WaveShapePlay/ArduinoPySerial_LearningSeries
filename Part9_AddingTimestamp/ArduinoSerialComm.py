import serial
import time
from ini_read import getINI

iniData = getINI()
numRowsCollect = int(iniData['numRowsCollect'])
numPoints = int(iniData['numPoints'])

ser = serial.Serial('COM3', baudrate = 9600, timeout = 1)
time.sleep(3)

dataFile = open('dataFile.txt', 'w')
dataList = [0]*numPoints

def getValues(timeStamp):
    
    if timeStamp == 'false':
        ser.write(b'g')
        arduinoData = ser.readline().decode().split('\r\n')
        arduinoOutput = arduinoData[0]
    
    if timeStamp == 'true':
        ser.write(b'c')
        arduinoOutput = ser.readline().decode().split('-')
        
    return arduinoOutput

def printToFile(data,index):
    
    dataFile.write(data)
    if index != (numPoints - 1):
        dataFile.write(',')
    else:
        dataFile.write('\n')

def getAverage(dataSet,row):

    dataAvg = sum(dataSet) / len(dataSet)
    print('Average for ' + str(row) + ' is: ' + str(dataAvg))
    
    
while(1):

    userInput = input('Get data points?')

    if userInput == 'y':
        timeStamp = 'false'
        for row in range(0,numRowsCollect):
            for i in range(0,numPoints):
                data = getValues(timeStamp)
                printToFile(data,i)
                dataInt = int(data)
                dataList[i] = dataInt
            
            getAverage(dataList,row)
   
    if userInput == 'c':
        timeStamp = 'true'
        data = getValues(timeStamp)
        dataPoint = data[0]
        timeCollected = data[1]
        timeCollected = timeCollected.strip()
        unitTime = timeCollected[-2:]
        deltaTime = timeCollected[:-2]

        if unitTime == 'ms':
            timeValue = int(deltaTime)
            timeValue = timeValue/1000

        if unitTime == 'us':
            timeValue = int(deltaTime)
            timeValue = timeValue/1000000

        print('Data Point: ' + dataPoint + 
        '  Time from last point: ' + str(timeValue) + 's')

    if userInput == 'n':
        dataFile.close()
