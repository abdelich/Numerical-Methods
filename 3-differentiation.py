import matplotlib.pyplot as plt


def first_derivative(x, y):
    h = abs(x[1] - x[0])
    k = (1/(6*h))
    df1 = k * (-11 * y[0] + 18 * y[1] - 9 * y[2] + 2 * y[3])
    df2 = k * (-2 * y[0] - 3 * y[1] + 6 * y[2] - 1 * y[3])
    df3 = k * (1 * y[0] - 6 * y[1] + 3 * y[2] + 2 * y[3])
    df4 = k * (-2 * y[0] + 9 * y[1] - 18 * y[2] + 11 * y[3])

    return df1, df2, df3, df4


xi = [1.25, 1.27, 1.29, 1.31]
f_x = [4.82835, 4.84418, 4.85989, 4.87523]

df_in_x = list(first_derivative(xi, f_x))
print(df_in_x)

plt.plot(xi, f_x, c='g')
plt.plot(xi, df_in_x, c='r')

plt.show()
