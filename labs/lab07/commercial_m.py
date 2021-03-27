"""
lab07 : Эффективность рекламы

Created on Fri Mar 26 13:34:42 2021

@author: kirilldi
"""

import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt

N0 = 7 # количество людей, знающих о товаре в начальный момент времени

N = 1505 # общее число платежеспособных покупателей

t = np.arange(0, 0.1, 0.001) # временной промежуток

# функции, отвечающие за платную рекламу (а1)

def k1(t):          #случай 1
    g = 0.68
    return g

def k2(t):          #случай 2
    g = 0.00001
    return g

def k3(t):          #случай 3
    g = 0.1*np.sin(5*t)
    return g

# функции, описывающие сарафанное радио (a2)

def p1(t):          #случай 1
    v = 0.00009
    return v

def p2(t):          #случай 2
    v = 0.28
    return v

def p3(t):          #случай 3
    v = 0.4*np.cos(3*t)
    return v

def p4(t):          #сравнительный коэффициент для задания
    v = 0.005
    return v

# функции, описывающие уравнения распространения рекламы

def f1(x, t):           #Случай 1
    xd1 = ( k1(t) + p1(t)*x )*( N - x )
    return xd1

def f2(x, t):           # Случай 2
    xd2 = ( k2(t) + p2(t)*x )*( N - x )
    return xd2

def f3(x, t):           #Cлучай 3
    xd3 = ( k3(t) + p3(t)*x )*( N - x )
    return xd3

def f4(x, t):           # a1 = 0
    xd4 = ( p4(t)*x )*( N - x )
    return xd4

def f5(x, t):           # a2 = 0
    xd5 = p4(t) *( N - x )
    return xd5

# решение ОДУ
x1 = odeint(f1, N0, t)
x2 = odeint(f2, N0, t)
x3 = odeint(f3, N0, t)
x4 = odeint(f4, N0, t)
x5 = odeint(f5, N0, t)

plt.plot(t, x1, label='a1 > a2') # случай 1
plt.plot(t, x2, label='a1 < a2') # случай 2

plt.plot(t, x3, label='случай 3') # случай 3
plt.legend()

plt.plot(t, x4, label='Только сарафанное радио') 
plt.plot(t, x5, label='Только платная реклама') 
plt.legend()
