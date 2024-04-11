def first_derivative(x, y):
    h = abs(x[1] - x[0])
    k = (1/(6*h))
    df1 = k * (-11 * y[0] + 18 * y[1] - 9 * y[2] + 2 * y[3])
    df2 = k * (-2 * y[0] - 3 * y[1] + 6 * y[2] - 1 * y[3])
    df3 = k * (1 * y[0] - 6 * y[1] + 3 * y[2] + 2 * y[3])
    df4 = k * (-2 * y[0] + 9 * y[1] - 18 * y[2] + 11 * y[3])

    return df1, df2, df3, df4


xi = [0, 1, 2, 3, 4]
f_x = [2.0, 3.0, 5.0, 4.0, 6.0]
df_in_x = first_derivative(xi, f_x)
print(df_in_x)