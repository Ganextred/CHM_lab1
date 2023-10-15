from math import log, floor, sin

from mpmath import ln


def funct(x):
    return ln(x)*sin(x)/(x*x*x*x +1)

def funct2(x):
    return ln(1/x)*sin(1/x)/(1/(x*x)+x*x)


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


def main():
    #print(middle_rectangles(funct(1,100,)))
    print("Метод обрізання границі: ", calculate_with_precision(funct, 1, 100, 0.00005))
    print("Метод заміни змінної: ", calculate_with_precision(funct2, 0, 1, 0.0001))



if __name__ == "__main__":
    main()

