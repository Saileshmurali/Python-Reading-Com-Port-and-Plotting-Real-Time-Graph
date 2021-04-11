import serial
import matplotlib.pyplot as plt
import numpy as np
import time
from scipy.fft import fft
import matplotlib.animation as animation
import datetime as dt
fig = plt.figure()
ser = serial.Serial('COM8',9600)
ser.close()
ser.open()
i=0
x=[]
y=[]
def animate(i):
    while True:
        data=ser.readline()
        data=str(data.decode())
        p=data.split()
        a=p[0]
        a=float(a)
        b=p[1]
        #c=a+b
        ct = dt.datetime.now()
        #data=int(data)
        #print(type(data))
        print(ct,a)
        i=i+1
        #print(i)
        x.append(i)
        y.append(a)
        #line, = plt.plot(x,y)
        #return line,
ani = animation.FuncAnimation(fig,animate, interval=1)
plt.show()
