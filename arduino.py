#!/usr/bin/env python
# coding: utf-8

# In[2]:


import serial

ser = serial.Serial(port = "COM8", baudrate = 9600 , bytesize = 8 )

f = open(r"C:\Users\boscu\Code\Data\Arduino text.txt",'a')

try:
    while 1 :
        f.write(ser.readline().decode("utf-8"))
        ser.flushInput()
        ser.flushOutput()
        f.close()
        f = open(r"C:\Users\boscu\Code\Data\Arduino text.txt",'a')
except KeyboardInterrupt:
    print("done")


# In[ ]:




