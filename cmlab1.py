from math import log, floor, sin

import numpy as np
from matplotlib import pyplot as plt



def funct(x):
    return np.log(x)*np.sin(x)/(x*x*x*x +1)

def funct2(x):
    return np.log(1/x)*np.sin(1/x)/(1/(x*x)+x*x)


def middle_rectangles(f, a, b, n):
    h = (b - a) / n
    integral = 0
    for i in range(n):
        x_mid = a + (i + 0.5) * h
        integral += f(x_mid)
    integral *= h
    return integral


def estimated_error(int_n, int_2n):
    return abs(int_n - int_2n)/3


def calculate_with_precision(f, a, b, eps):
    n = 1
    int_n = middle_rectangles(f, a, b, n)
    n = 2
    int_2n = middle_rectangles(f, a, b, n)
    while (estimated_error(int_n, int_2n) > eps):
        int_n = int_2n
        n *= 2
        int_2n = middle_rectangles(f, a, b, n)
    print(n)
    return int_2n


def visualize_integral(f, a, b, n):
    # Calculate the width of each rectangle
    dx = (b - a) / n
    integral = 0

    x_values = []
    y_values = []

    for i in range(n):
        # Calculate the x-coordinate of the middle of the rectangle
        x = a + (i + 0.5) * dx
        # Calculate the height of the rectangle using the function f
        y = f(x)
        # Add the area of the rectangle to the integral
        integral += y * dx

        # Store the x and y values for visualization
        x_values.append(x)
        y_values.append(y)

    # Convert lists to NumPy arrays for plotting
    x_values = np.array(x_values)
    y_values = np.array(y_values)

    # Plot the function and rectangles
    x = np.linspace(a, b, 400)
    y = f(x)
    plt.plot(x, y, label="f(x)")
    plt.bar(x_values, y_values, width=dx, align="center", alpha=0.5, label="Rectangles")
    plt.xlabel("x")
    plt.ylabel("y")
    plt.legend()
    plt.title("Middle Rectangles Method")
    plt.show()

    return integral


def main():
    #print(middle_rectangles(funct(1,100,)))
    print("Метод обрізання границі: ", middle_rectangles(funct, 1, 100, 35609))
    print("Метод заміни змінної: ", calculate_with_precision(funct2, 0, 1, 0.0001))
    visualize_integral(funct, 1, 10, 35)
    visualize_integral(funct2, 0, 1, 12)



if __name__ == "__main__":
    main()

