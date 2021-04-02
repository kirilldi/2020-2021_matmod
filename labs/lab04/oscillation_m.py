#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Apr  2 20:01:52 2021

@author: kirilldi
"""

import math
import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt

t = np.arange(0, 54, 0.05)

#Вектор начальных условий
x0 = np.array([-0.7, 0.8])

# Первый случай : без затухания и внешней силы
w1 = math.sqrt(10.5) #частота
g1 = 0.00            #затухание

# Второй случай : с затуханием и без внешней силы
w2 = math.sqrt(5);
g2 = 7;

# Правая часть уравнения для 1 и 2 случая
def f(t):
    f = 0
    return f

# Третий случай : с затуханием и внешней силой
w3 = math.sqrt(5.5);
g3 = 0.4;

#Правая часть уравнения для 3 случая
def f3(t):
    f3 = 8*np.sin(3*t)
    return f3

#Вектор-функции f(t, x) для решения системы дифференциальных уравнений x' = y(t, x)
def y1(x, t):
    dx1 = x[1]
    dx2 = - w1*w1*x[0] - 2*g1*x[1] - f(t)
    return dx1, dx2

def y2(x, t):
    dx1 = x[1]
    dx2 = - w2*w2*x[0] - 2*g2*x[1] - f(t)
    return dx1, dx2

def y3(x, t):
    dx1 = x[1]
    dx2 = - w3*w3*x[0] - 2*g3*x[1] - f3(t)
    return dx1, dx2

#Решаем дифференциальные уравнения с начальным условием x(t0) = x0 
#на интервале t с правой частью, заданной y и записываем решение в матрицу x
x = odeint(y1, x0, t)

#Переписываем отдельно
axis_1 = x[:,0]
axis_2 = x[:,1]
#Строим фазовую траекторию для 1 случая
plt.plot(axis_1,axis_2)      
plt.grid(axis='both')
plt.legend(['g = 0'])


#Строим фазовую траекторию для 2 случая
x = odeint(y2, x0, t)
axis_1 = x[:,0]
axis_2 = x[:,1]
plt.plot(axis_1,axis_2)      
plt.grid(axis='both')
plt.legend(['g = 7'])

#Строим фазовую траекторию для 3 случая
x = odeint(y3, x0, t)
axis_1 = x[:,0]
axis_2 = x[:,1]
plt.plot(axis_1,axis_2)     
plt.grid(axis='both')
plt.legend(['g = 0.4, F'])
