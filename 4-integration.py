import matplotlib.pyplot as plt


def newton_cotes(x, y):
    a = x[0]
    b = x[len(x) - 1]

    c0_4 = c4_4 = 7*(b-a)/90
    c1_4 = c3_4 = 16*(b-a)/45
    c2_4 = 2*(b-a)/15
    cotes_coefficients = [c0_4, c1_4, c2_4, c3_4, c4_4]

    area = 0
    for i in range(len(y)):
        area += cotes_coefficients[i] * y[i]

    return area


def rectangle(x, y):
    h = x[1] - x[0]
    area = 0
    for i in y:
        area += h * i

    return area


def trapezoidal(x, y):
    h = x[1] - x[0]
    area = 0
    for i in range(len(y)-2):
        area += h * (y[i] + y[i + 1])/2

    return area


def simpson(x, y):
    h = (x[1] - x[0])/3
    area = y[0] + y[-1]
    for i in range(1, len(y)-1):
        area += 2 * (i % 2 + 1) * y[i]

    return h * area


xi = [i for i in range(0, 5)]
f_x = [2 * i for i in xi]

print('Analytically we calculate area under line as Newton-Leibniz integral')
print('But for line with slope 2 we can use simple formula:')
print('We calculate area as right`s triangle area with sides max(x) and max(y)')
print(f'Area of right triangle = ({max(xi)} * {max(f_x)}) / 2 = {max(xi) * max(f_x) * 0.5}')

print(f'Newton-Cotes method: area = {newton_cotes(xi, f_x)}')
print(f'Rectangles method: area = {rectangle(xi, f_x)}')
print(f'Trapezoidal method: area = {trapezoidal(xi, f_x)}')
print(f'Simpson`s method: area = {simpson(xi, f_x)}')

plt.plot(xi, f_x)
plt.show()
