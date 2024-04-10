import math

import matplotlib.pyplot as plt


def interpolate(x, y, a):
    """
    using Lagrange polynom to approximate a
    :param x: params in func
    :param y: result of func(x)
    :param a: point to approximate
    :return: approximated a
    """
    def calculate_lagrange_coefficient(i):
        numerator = 1
        denominator = 1

        for k in range(len(x)):
            if k != i:
                numerator *= (a - x[k])
                denominator *= (x[i] - x[k])

        lagrange_coefficient = y[i] * (numerator/denominator)
        return lagrange_coefficient

    approximation = 0
    for L in range(len(x)):
        approximation += calculate_lagrange_coefficient(L)

    return approximation


# interpolated function
def f(x):
    square = lambda i: i * i
    #return math.pow(math.log(x, math.e), 13/4)
    return square(x)


x = [-90, -60, -30, 30, 60, 90]
y = [f(xi) for xi in x]

a = 0
y_a = interpolate(x, y, a)

x_interpolated = x.copy()
x_interpolated.append(a)

y_interpolated = y.copy()
y_interpolated.append(y_a)

x_interpolated_sorted, y_interpolated_sorted = zip(*sorted(zip(x_interpolated, y_interpolated)))


print(f'f in {a} = {y_a}')

fig, ax = plt.subplots(1, 2)

ax[0].plot(x, y)
ax[1].plot(x_interpolated_sorted, y_interpolated_sorted, c='g')

plt.show()
