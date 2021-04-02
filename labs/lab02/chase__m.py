#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Apr  2 17:55:12 2021

@author: kirilldi
"""

import math
import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt

t = np.arange(0, 15, 1)

k = 17.9 # Растояние между катером и лодкой
fi = 3*math.pi/4 # Направление лодки
tang_vel = 5.2**2-1 # Тангенциальная скорость

# Движение катера
def dr(r, tetha): 
    dr = r/math.sqrt(tang_vel)
    return dr

#
def tetha(v, tetha0):
    r0 = k/v
    tetha = np.arange(tetha0, 2*math.pi, 0.01)
    r = odeint(dr, r0, tetha)
    return r0, tetha, r

# Движение лодки
def f2(t): 
    xt=math.tan(fi)*t
    return xt

def plot(tetha, r, tetha2, r2):
    plt.figure(1)
    plt.polar(tetha, r, 'g')
    plt.polar(tetha2, r2, 'b')
    plt.legend(['Катер', 'Лодка'])


ll = t*t + f2(t)*f2(t)
r2 = np.sqrt(ll)
tetha2 = (np.tan(f2(t)/t))**(-1)

r0, tetha, r = tetha(6.2, 0)
plot(tetha, r, tetha2, r2)