import math
import matplotlib.pyplot as plt


def bisection(func, accuracy, abs_range):
    interval = range(-abs_range, abs_range + 1)
    x = [i for i in interval]

    x0 = min(x)
    x1 = max(x)

    while abs(x1 - x0) >= accuracy:
        x_bisection = (x1 + x0) / 2
        if func(x_bisection) == 0:
            return x_bisection
        elif func(x_bisection) < 0:
            x0 = x_bisection
        else:
            x1 = x_bisection

    return (x1 + x0) / 2


def newtons_method(func, der_func, accuracy, abs_range):
    root = 5
    interval = range(-abs_range, abs_range + 1)
    for x_0 in interval:
        x_prev = x_0
        iter_count = 0
        while True:
            x_next = x_prev - func(x_prev) / der_func(x_prev)
            if abs(x_next - x_prev) < accuracy or iter_count > 1000:
                root = x_next
                break
            x_prev = x_next
            iter_count += 1
    return root


def secants_method(func, accuracy, abs_range):
    root = -500
    interval = range(-abs_range, abs_range + 1)
    for x_0 in interval:
        x_prev = x_0
        x_curr = x_0 + 0.1
        iter_count = 0
        while True:
            if abs(x_curr - x_prev) < accuracy or iter_count > 1000:
                root = x_curr
                break
            try:
                x_next = x_curr - ((x_curr - x_prev) / (func(x_curr) - func(x_prev))) * func(x_curr)
            except ZeroDivisionError:
                break
            x_prev = x_curr
            x_curr = x_next
            iter_count += 1
    return root


# y = 2x - 3
# analytical solution for this equation where y = 0, therefore 2x - 3 = 0, where x = 3/2
f = lambda x: 2*x - 3
acc = 0.0001
rng = 10
root_bisection = bisection(f, acc, rng)

# Newtons method(simple variation) needs first derivative of f(x)
# (2x - 3)' = 2
f_der = lambda x: 2
root_newton = newtons_method(f, f_der, acc, rng)

# Secant`s method uses no derivative in computation but costs a bit more time
root_secant = secants_method(f, acc, rng)

print(f'Bisection: x = {root_bisection}, f(x)={f(root_bisection)}')
print(f'Newton`s method: x = {root_newton}, f(x)={f(root_newton)}')
print(f'Secant`s method: x = {root_secant}, f(x)={f(root_secant)}')

xi = [i for i in range(-rng, rng+1)]
yi = [f(i) for i in xi]

plt.plot(xi, yi)
plt.scatter(root_bisection, f(root_bisection), color='red')

plt.axhline(0, color='black')
plt.axvline(0, color='black')

plt.show()
