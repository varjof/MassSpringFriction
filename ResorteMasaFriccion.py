# -*- coding: utf-8 -*-
"""
Created on Mon Oct  5 10:47:51 2020

@author: John
"""
import matplotlib.pyplot as plt

Lo=1
xo=1.7
vo=0
k=100
m=10
t=0
dt=0.001
x=xo
v=vo
Ax=[x]
At=[t]
d=x

ka=0.5

while t<50:

    x=v*dt+x
    v=(k/m*(Lo-d)-ka/m*v)*dt+v
    d=x
    t=t+dt
    Ax.append(x)
    At.append(t)

plt.plot(At,Ax)
plt.xlabel("tiempo")
plt.ylabel("x")  