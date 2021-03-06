---
## Front matter
lang: ru-RU
title: Лабораторная работа №5
author: Дидусь К.В.
		Группа НКНбд-01-18
date: 12.03.2021

## Formatting
toc: false
slide_level: 2
theme: metropolis
header-includes: 
 - \metroset{progressbar=frametitle,sectionpage=progressbar,numbering=fraction}
 - '\makeatletter'
 - '\beamer@ignorenonframefalse'
 - '\makeatother'
aspectratio: 43
section-titles: true
---

# Прагматика выполнения лабораторной работы (Зачем)

## Прагматика выполнения лабораторной работы (Зачем)

- Модель Лотки-Вольтерры положила начало для изучения популяционных волн и более сложных процессов в природе и не только; 

- Используя эту модель как базу, можно создавать и более сложные модели, учитывая такие переменные как старение, шанс катаклизма и другие

- Модель Хищник-Жертва принима и в экономике;

# Цель выполнения лабораторной работы

## Цель выполнения лабораторной работы

Рассмотреть простейшую модель "хищник-жертва" — модель Лотки-Вольтерры. 

# Задачи выполнения лабораторной работы

## Задачи выполнения лабораторной работы

1. Построить график зависимости численности хищников от численности жертв и графики изменения численности хищников и численности жертв при следующих начальных условиях: $x_{0}=9, y_{0}=29$.
2. Найти стационарное состояние системы.

# Результаты выполнения лабораторной работы

## Модель Лотки-Вольтерры

$$
\begin{cases}
    \frac{\partial x}{\partial t} = ax(t)+bx(t)y(t)
    \\
    \frac{\partial y}{\partial t} = -cy(t)-dx(t)y(t)
\end{cases}
$$

a — коэффициент естественной смертности хищников

b — коэффициент увеличения числа хищников

c — коэффициент естественного прироста жертв

d — коэффициент смертности жертв


## Стационарное состояние

Стационарное состояние системы будет в точке: 
$$x_0 = \frac{c}{d}, y_0 = \frac{a}{b}$$

## Графики

![Зависимость x от y и стационарное состояние](images/2.png){ #fig:001 width=70% }

## Графики

![Зависимость x(t) и y(t)](images/1.png){ #fig:002 width=70% }

## {.standout}

Рассмотрел простейшую модель "хищник-жертва" — модель Лотки-Вольтерры. 