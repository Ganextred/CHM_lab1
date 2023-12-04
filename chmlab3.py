import math

from matplotlib import pyplot as plt

# y = C1*e^(-kx)+ys
# C1 = (y0-ys)/e^(-k*x0)


def dy_dx(y, k, ys):
    return -k * (y - ys)


def fun(y0, x0, xf, h, k, ys):
    h = (xf - x0) * abs(h) / abs(xf - x0)
    C1 = (y0-ys)/math.e**(-1*k*x0)

    num_points = int(abs((xf - x0) / h) + 1)
    x_values = [x0 + i * h for i in range(num_points)]
    y_values = [C1*(math.e**(-1*k*x_values[i]))+ys for i in range(num_points)]

    return x_values, y_values


def euler_method(y0, x0, xf, h, k, ys):
    h = (xf-x0)/abs(xf-x0)*abs(h)
    num_points = int(abs((xf - x0) / h) + 1)
    x_values = [x0 + i * h for i in range(num_points)]
    y_values = [y0]

    for i in range(1, num_points):
        y_next = y_values[-1] + h * dy_dx(y_values[-1], k, ys)
        y_values.append(y_next)

    return x_values, y_values


def runge_kutta(y0, x0, xf, h, k, ys):
    h = (xf - x0) * abs(h) / abs(xf - x0)
    num_points = int(abs((xf - x0) / h) + 1)
    x_values = [x0 + i * h for i in range(num_points)]
    y_values = [y0]

    for i in range(1, num_points):
        k1 = h * dy_dx(y_values[-1], k, ys)
        k2 = h * dy_dx(y_values[-1] + k1, k, ys)
        y_next = y_values[-1] + 0.5 * (k1 + k2)
        y_values.append(y_next)

    return x_values, y_values

def main():
    # User-defined constants
    k = 0.045
    ys = 22
    x0 = 0
    y0 = 87
    xf = complex(0, 1) # комплексне значення тчоки 0+1i
    h = 0.1 #модуль кроку

    # Solve using Euler method
    x_values1, y_values1 = euler_method(y0, x0, xf, h, k, ys)
    x_values2, y_values2 = runge_kutta(y0, x0, xf, h, k, ys)
    x_values_real, y_values_real = fun(y0, x0, xf, h, k, ys)

    # Plotting the results
    plt.plot(x_values_real, y_values_real, label='Real values')
    plt.plot(x_values1, y_values1, label='Euler Method')
    plt.plot(x_values2, y_values2, label='Runge-Kutta 2nd Order')
    plt.xlabel('x')
    plt.ylabel('y')
    plt.title('Solution of Cauchy Problem using Euler Method')
    plt.legend()
    plt.show()

    print("X value", x_values_real[-1])
    C1 = (y0 - ys) / math.e ** (-1 * k * x0)
    real_value = C1*(math.e**(-1*k*xf))+ys
    print('Real value', real_value)
    print('Euler Method', y_values1[-1])
    print('Runge-Kutta 2nd Order', y_values2[-1])
    print()
    print()
    print()
    print()

if __name__ == "__main__":
    main()

