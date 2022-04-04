# -*- coding: utf-8 -*-
"""
Created on Tue Oct  6 14:53:16 2020

@author: John
"""

import matplotlib.pyplot as plt

Lo=1
xo=0.5
vo=0
k=50
m=10
t=0
dt=0.1
x=xo
v=vo
d=x
cuadro,=plt.plot(x,1,'sb',markersize=20)
linea,=plt.plot([0,x],[1,1],'b')
plt.axis([0,2,0,1.5])
plt.xlabel("x")
plt.grid()
ka=0.6

for i in range(150):
    v=(k/m*(Lo-d)-ka/m*v)*dt+v
    x=v*dt+x
    d=x
    t=t+dt
    cuadro.set_xdata(x)
    linea.set_xdata([0,x])
    plt.pause(0.1)
