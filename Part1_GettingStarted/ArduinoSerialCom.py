import serial

ser = serial.Serial('COM3', baudrate = 9600, timeout=1)

while 1:

    arduinoData = ser.readline().decode('ascii')
    print(arduinoData)
    
    



    
