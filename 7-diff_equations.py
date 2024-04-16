import math

import matplotlib.pyplot as plt


def Euler(func, n=10, h=0.1, x0=1, y0=1):
    x, y = x0, y0
    for _ in range(n):
        y += h*func(x, y)
        x += h
    return x, y


# 4-th order variant
def Runge_Kutta(func, n=10, h=0.1, x0=0, y0=0):
    x, y = x0, y0
    xs = []
    ys = []
    for i in range(n):
        r1 = h * func(x, y)
        r2 = h * func(x + h / 2, y + r1 / 2)
        r3 = h * func(x + h / 2, y + r2 / 2)
        r4 = h * func(x + h, y + r3)

        y += (1/6)*(r1 + 2*r2 + 2*r3 + r4)
        x += h

        xs.append(x)
        ys.append(y)

    return xs, ys


def function(x, y):
    return x**2 - 2*y


xs_range = range(-5, 6)

xs = [i for i in xs_range]
ys = [function(i, i) for i in xs]

plt.plot(xs, ys, color='red')

for i in xs_range:
    runge_kutta = Runge_Kutta(function, 10, 0.1, i, i)
    print(runge_kutta)
    xs = runge_kutta[0]
    x = xs[len(xs) - 1]

    ys = runge_kutta[1]
    y = ys[len(ys) - 1]

    plt.scatter(x, y, color='green')

plt.show()
