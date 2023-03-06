from math import log, floor


def funct(x):
    return x**3 - 3*x**2 - 17*x + 22

def function_for_simple_itterarion(x):
    return -22/(x**2 - 3*x - 17)


def dih_method(f, a, b, eps, i):
    if f(a) * f(b) > 0:
        print("The function has the same sign at points a and b. Bisection method cannot be applied.")
        return None
    x0 = (a+b)*1.0/2
    if abs(f(x0)) < eps:
        return x0, i
    else:
        print("Ітреація та значення кореня:", i, x0, "апостеріорна оцінка: ", round(log((b - a * 1.0) / eps, 2) + 1))
        if f(a)*f(x0) < 0:
            return dih_method(f, a, x0, eps, i+1)
        else:
            return dih_method(f, x0, b, eps, i+1)

# def dih_method2(f, a, b, eps):
#     if f(a) * f(b) > 0:
#         print("The function has the same sign at points a and b. Bisection method cannot be applied.")
#         return None
#     x0 = (a+b)*1.0 /2
#     i = 0
#     while abs(f(x0)) > eps:
#         i+=1
#         if f(a)*f(x0) < 0:
#             b = x0
#         else:
#             a = x0
#         x0 = (a+b)*1.0/2
#     return x0, i

def relaxation_method(f, x, tau, eps, q):
    x_next = x - tau * f(x)
    i = 1
    print("Ітреація та значення кореня:", i, x_next,
          "апостеріорна оцінка: ", floor(log((abs(x_next-x)) / eps)/log(1 / q) + 1))
    while abs(x_next - x) > (1-q)/q*eps:
        x = x_next
        x_next = x + tau * f(x)
        i+=1
        print("Ітреація та значення кореня:", i, x_next,
              "апостеріорна оцінка: ", round(log((abs(x_next-x*1.0)) / eps)/log(1.0 / q) + 1))
    return x_next, i

def simple_iteration_method(g, x, eps, q):
    x_next =g(x)
    i = 1
    print("Ітреація та значення кореня:", i, x_next)
    while abs(x_next - x) > eps*(1-q)/q:
        x = x_next
        x_next = g(x_next)
        i+=1
        print("Ітреація та значення кореня:", i, x_next)
    return x_next, i

def main():
    print("Метод дихотомії: ", dih_method(funct, -1, 2, 0.0001, 0))
    print("Метод релаксації: ", relaxation_method(funct, 1, 0.054, 0.0001, 0.081))
    print("Метод простої ітерації: ", simple_iteration_method(function_for_simple_itterarion, 100, 0.0001,0.081))




if __name__ == "__main__":
    main()

