import time
import serial
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

ser = serial.Serial(
   port= '/dev/tty.usbserial-1410',
   baudrate=4800,
   
) 


ser.close()
ser.open()
ser.isOpen()

while True :
  #\r\n is for device terminators set to CR LF
  ser.write(':FETCh?\r\n'.encode())
  #wait one second before reading output. 
  time.sleep(1)
  out=''
  while ser.inWaiting() > 0:
    out += ser.read(1).decode()
  if out != '':
      out=out.rstrip()
      print("%s %s"%(time.time(),out))
      
#Save the code above in a file Serial.py and running it from the command line produces the output.
