---
# Front matter
lang: ru-RU
title: "Лабораторная работа №5"
subtitle: "Модель хищник-жертва"
author: "Кирилл Валерьевич Дидусь"

# Formatting
toc-title: "Содержание"
toc: true # Table of contents
toc_depth: 2
lof: true # List of figures
lot: true # List of tables
fontsize: 12pt
linestretch: 1.5
papersize: a4paper
documentclass: scrreprt
polyglossia-lang: russian
polyglossia-otherlangs: english
mainfont: PT Serif
romanfont: PT Serif
sansfont: PT Sans
monofont: PT Mono
mainfontoptions: Ligatures=TeX
romanfontoptions: Ligatures=TeX
sansfontoptions: Ligatures=TeX,Scale=MatchLowercase
monofontoptions: Scale=MatchLowercase
indent: true
pdf-engine: lualatex
header-includes:
  - \linepenalty=10 # the penalty added to the badness of each line within a paragraph (no associated penalty node) Increasing the value makes tex try to have fewer lines in the paragraph.
  - \interlinepenalty=0 # value of the penalty (node) added after each line of a paragraph.
  - \hyphenpenalty=50 # the penalty for line breaking at an automatically inserted hyphen
  - \exhyphenpenalty=50 # the penalty for line breaking at an explicit hyphen
  - \binoppenalty=700 # the penalty for breaking a line at a binary operator
  - \relpenalty=500 # the penalty for breaking a line at a relation
  - \clubpenalty=150 # extra penalty for breaking after first line of a paragraph
  - \widowpenalty=150 # extra penalty for breaking before last line of a paragraph
  - \displaywidowpenalty=50 # extra penalty for breaking before last line before a display math
  - \brokenpenalty=100 # extra penalty for page breaking after a hyphenated line
  - \predisplaypenalty=10000 # penalty for breaking before a display
  - \postdisplaypenalty=0 # penalty for breaking after a display
  - \floatingpenalty = 20000 # penalty for splitting an insertion (can only be split footnote in standard LaTeX)
  - \raggedbottom # or \flushbottom
  - \usepackage{float} # keep figures where there are in the text
  - \floatplacement{figure}{H} # keep figures where there are in the text
---

# Цель работы

Ознакомление с простейшей моделью взаимодействия двух видов типа «хищник — жертва» - моделью Лотки-Вольтерры  и ее построение с помощью языка программирования Modelica.

# Задание

1. Построить график зависимости численности хищников от численности жертв.
2. Построить графики изменения численности хищников и численности жертв.
3. Найти стационарное состояние системы.

# Выполнение лабораторной работы

Уравнение модели "хищник-жертва" имеет следующий вид:
	$$ 
                \begin{cases}
                    \frac{dx}{dt} = -0.15x(t)+0.035x(t)y(t)
                    \\
                    \frac{dy}{dt} = 0.26y(t)-0.035x(t)y(t)
                 \end{cases}
        $$
Начальные условия: x_0 = 9 и y_0 = 29.
1. Ниже приведен код программы, реализованный на языке программирования Python (рис 1. -@fig:001)  

![Код программы для решения задачи](images/1.png){ #fig:001 width=70% }

Также ниже приведен график зависимости численности популяции хищников от численности популяции жертв. (рис 2. -@fig:001)  

![График зависимости численности хищников от численности жертв](images/2.png){ #fig:001 width=70% }

2. Построим графики изменения численности популяции хищников и численности популяции жертв с течением времени (рис 3. -@fig:001)  

![Графики изменения численности хищников и численности жертв с течением времени](images/3.png){ #fig:001 width=70% }

3. Для того, чтобы найти стационарное состояние системы, необходимо приравнять производные каждой из функций x и y к нулю и выразить значения y и x соответственно.  

Получим следующие значения:
$$ x_0 = \frac{a}{c} = \frac{0.15}{0.035} \approx 4.29  $$
$$ y_0 = \frac{b}{d} = \frac{0.26}{0.035} \approx 7.43  $$
При стационарном состоянии значения числа жертв и хищников не меняется во времени. (рис 4. -@fig:001)  

![Стационарное состояние системы](images/4.png){ #fig:001 width=70% }

## Код программы

Приведу полный код программы (Python):    

import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt

a = 0.15 #коэффициент смертности хищников
b = 0.26 #коэффициент прироста жертв
c = 0.035 #коэффициент прироста хищников
d = 0.035 #коэффициент смертности жертв

st1 = a/c # cтационарное состояние хищников
st2 = b/d # стационарное состояние жертв


def y(x,t):                       # вектор-функция представляющая 
    dx1 = -a*x[0] + c*x[0]*x[1]   # дифф. уравнения 
    dx2 = b*x[1] - d*x[0]*x[1]
    return dx1,dx2

"""начальные условия задачи
x0 = np.array([9.0, 29.0])"""

x0 = np.array([st2, st1]) # условие равновесия


t = np.arange(0,400,0.1) # интервал отображения решения

x = odeint(y, x0, t) # решения дифф. уравнения


y1 = x[:,0] # разбивка по осям
y2 = x[:,1]


plt.plot(t,y1)  # построение графика
plt.grid(axis='both')

plt.plot(t,y2)
plt.grid(axis='both')

## Выводы

Ознакомился c основами модели хищник-жертва. Построил графики зависимости и нашел стационарную точку системы.