import numpy as np
import matplotlib.pyplot as plt


class Equation:
    A = []
    b = []

    def solve(self, precision, max_iterations):
        pass


# Implement non-linear equations class
class NonLinearEquation(Equation):
    pass


class LinearEquation(Equation):
    A = []
    b = []

    def __init__(self, A, b):
        """
        initializes equation as a state of two matrices
        :param A: coefficient matrix as numpy array
        :param b: free members column vector
        """
        self.A = A
        self.b = b

    def solve(self, precision=1e-6, max_iterations=1000):
        """
        overridden method that randomly choose which method use to solve linear system of equations
        :param precision: desired precision
        :param max_iterations: maximum number of iterations
        :return: solution vector
        """
        random_method = np.random.randint(0, 2)
        if random_method == 0:
            print('Fixed-point method:')
            return self.fixed_point_solve(precision, max_iterations)
        else:
            print('Gauss-Seidel method:')
            return self.gauss_seidel_solve(precision, max_iterations)

    def fixed_point_solve(self, precision, max_iterations):
        """
        solves the equation by fixed-point iteration method and returns the solution vector
        :param precision: desired precision
        :param max_iterations: maximum number of iterations
        :return: solution vector
        """
        A = self.A.copy()
        b = self.b.copy()

        n = A.shape[0]
        x = np.zeros(n)

        for _ in range(max_iterations):
            x_new = np.zeros(n)
            for i in range(n):
                sum_term = 0
                for j in range(n):
                    if j != i:
                        sum_term += A[i, j] * x[j]
                x_new[i] = (b[i] - sum_term) / A[i, i]

            if np.linalg.norm(x - x_new) < precision:
                return x_new
            x = x_new

    def gauss_seidel_solve(self, precision, max_iterations):
        """
        solves the equation by Gauss-Seidel iteration method and returns the solution vector
        :param precision: desired precision
        :param max_iterations: maximum number of iterations
        :return: solution vector
        """
        A = self.A.copy()
        b = self.b.copy()

        n = A.shape[0]
        x = np.zeros(n)

        for _ in range(max_iterations):
            x_new = np.zeros(n)
            for i in range(n):
                sum_term = 0
                for j in range(n):
                    if j != i:
                        sum_term += A[i, j] * x_new[j]
                x_new[i] = (b[i] - sum_term) / A[i, i]

            if np.linalg.norm(x - x_new) < precision:
                return x_new
            x = x_new


A = np.array([[20.9, 1.2, 2.1, 0.9],
              [1.2, 21.2, 1.5, 2.5],
              [2.1, 1.5, 19.8, 1.3],
              [0.9, 2.5, 1.3, 32.1]])
b = np.array([21.70, 27.46, 28.78, 49.72])

linear = LinearEquation(A, b)
x = linear.solve()

print(x)




