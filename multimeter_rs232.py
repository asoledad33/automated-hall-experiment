#%% matplotlib notebook
import time
import datetime as dt
import random
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import serial.py

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
  
def animate(i, df):
    
    df.loc[len(df.index)] = [dt.datetime.now().strftime('%H:%M:%S.%f'), random.random()] 
    
    # Draw x and y axes, limiting to 10 values in the graph 
    plt.cla()
    plt.plot(df['datetime'][-10:],df['voltage'][-10:]) 
    
    # Save data
    store.append('name_of_frame', df.loc[len(df.index)], format='t',  data_columns=True)

    # Format plot
    plt.xticks(rotation=45, ha='right')
    plt.subplots_adjust(bottom=0.30)
    plt.title('Voltage over Time')
    plt.ylabel('Voltage (mV)')

def main():
  xs = []
  ys = []

  df = pd.DataFrame({
      'datetime': [],
      'voltage': []
  })
  
store = pd.HDFStore('test.h5')
  
# Set up plot to call animate() function periodically
ani = animation.FuncAnimation(plt.gcf(), animate, fargs=(df), interval=1000)

plt.tight_layout()
plt.show()

# Testing 
# Second Test
# Third Test
