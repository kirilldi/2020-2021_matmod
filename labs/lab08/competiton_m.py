#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Mar 26 13:35:01 2021

@author: kirilldi
"""
import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt

p_cr = 45 # критическая стоимость продукта

tau1 = 30 # длительность производственного цикла фирмы 1

p1 = 9 # себестоимость продукта у фирмы 1

tau2 = 25 # длительность производственного цикла фирмы 2

p2 = 11 # себестоимость продукта у фирмы 2

N = 55 # число потребителей производимого продукта

q = 1 #потребность человека в единицу времени

# Начальное значение объема оборотных средств x1 и х2
x0 = [7.5, 9.5]

# Время симуляции
t = np.arange(0, 15, 0.001)

# Вычисление коэффициентов
a1 = p_cr/(tau1*tau1*p1*p1*N*q)

a2 = p_cr/(tau2*tau2*p2*p2*N*q)

b = p_cr/(tau1*tau1*tau2*tau2*p1*p1*p2*p2*N*q)

c1 = (p_cr-p1)/(tau1*p1)

c2 = (p_cr-p2)/(tau2*p2)

# Стационарные состояния для первого случая
s1 = (a2*c1-b*c2)/(a1*a2-b*b)
s2 = (a1*c2-b*c1)/(a1*a2-b*b)

# Первый случай

def syst(x, t):
    dx1 = x[0] - (b/c1)*x[0]*x[1] - (a1/c1)*x[0]*x[0]
    dx2 = (c2/c1)*x[1] - (b/c1)*x[0]*x[1] - (a2/c1)*x[1]*x[1] 
    return dx1, dx2

# Второй случай

def syst2(x, t):
    dx1 = x[0] - (b/c1 + 0.00046)*x[0]*x[1] - (a1/c1)*x[0]*x[0]
    dx2 = (c2/c1)*x[1] - (b/c1)*x[0]*x[1] - (a2/c1)*x[1]*x[1]
    return dx1, dx2

y = odeint(syst, x0, t)
y2 = odeint(syst2, x0, t)

# Построение динамики изменения оборотных средств фирмы 1 и фирмы 2
# в первом случае

plt.plot(t, y[:,0], label='Фирма 1')
plt.plot(t, y[:,1], label='Фирма 2')
plt.hlines(s1, 0, 20, colors="darkgrey", linestyles='dashed', label='s1')
plt.hlines(s2, 0, 20, colors="dimgrey", linestyles='dashed', label='s2')
plt.legend(loc=4)
plt.grid()


# Построение динамики изменения оборотных средств фирмы 1 и фирмы 2
# во втором случае

plt.plot(t, y2[:,0], label='Фирма 1')
plt.plot(t, y2[:,1], label='Фирма 2')
plt.legend()
plt.grid()
