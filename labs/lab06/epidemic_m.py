#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Mar 18 18:56:15 2021
@author: kirilldi
"""

import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt

a = 0.7 #коэфф заболеваемости
b = 0.2 #коэфф выздоровления
N = 4973 #кол-во жителей
I0 = 49 #кол-во зараженных
R0 = 19 #кол-во с иммунитетом
S0 = N - I0 - R0 #кол-во восприимчивых

x0 = [S0, I0, R0] # начальные значения

#Случай 1 : I0 <= I*
def syst(x, t):
    dx0 = 0
    dx1 = -b*x[1]
    dx2 = b*x[1]
    return dx0, dx1, dx2

t = np.arange(0, 20, 0.01) # шаг по времени
"""
y1 = odeint(syst, x0, t) 

plt.plot(t,y1[:,0], label='S(t)')
plt.plot(t,y1[:,1], label='I(t)')
plt.plot(t,y1[:,2], label='R(t)')
plt.legend()
plt.title('Случай 1: I0 <= I*',fontsize=14)

"""

#Случай 2 : I0 > I*

def syst(x, t):
    dx0 = -a*x[0]
    dx1 = a*x[0]-b*x[1]
    dx2 = b*x[1]
    return dx0, dx1, dx2

y2 = odeint(syst, x0, t) 

plt.plot(t,y2[:,0], label='S(t)')
plt.plot(t,y2[:,1], label='I(t)')
plt.plot(t,y2[:,2], label='R(t)')
plt.legend()
plt.title('a > b',fontsize=14)
