
#%%
import time
import datetime as dt
import random 
#import serial
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

xs = []
ys = []

#plt.style.use('fivethirtyeight')

def animate(i):
    # Add x and y data to lists
    xs.append(dt.datetime.now().strftime('%H:%M:%S.%f'))
    ys.append(random.random())
    
    # Limit x and y axes to 10 values
    if len(xs) > 10:
        xs.pop(0)
    
    if len(ys) > 10:
        ys.pop(0)
    
    # Draw x and y lists
    plt.cla()
    plt.plot(xs, ys)

    # Format plot
    plt.xticks(rotation=45, ha='right')
    plt.subplots_adjust(bottom=0.30)
    plt.title('Voltage over Time')
    plt.ylabel('Voltage (mV)')
    
# Set up plot to call animate() function periodically
ani = animation.FuncAnimation(plt.gcf(), animate, interval=1000)

plt.tight_layout()
plt.show()

'''
def init():
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
'''
# %%
