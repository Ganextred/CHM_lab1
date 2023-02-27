import random
def funct(x):
    return x**3 - 3*x**2 - 17*x + 22

def function_for_simple_itterarion(x):
    return -22/(x**2 - 3*x - 17)


def dih_method(f, a, b, eps):
    # print(a, b)
    if f(a) * f(b) > 0:
        print("The function has the same sign at points a and b. Bisection method cannot be applied.")
        return None
    x0 = (a+b)*1.0/2
    # print(x0, f(x0))
    if abs(f(x0)) <= eps:
        return x0
    else:
        # print (a, x0, a*x0)
        if f(a)*f(x0) < 0:
            return dih_method(f, a, x0, eps)
        else:
            return dih_method(f, x0, b, eps)

# def dih_method2(f, a, b, eps):
#     if f(a) * f(b) > 0:
#         print("The function has the same sign at points a and b. Bisection method cannot be applied.")
#         return None
#     x0 = (a+b)*1.0 /2
#     while abs(f(x0)) > eps:
#         if f(a)*f(x0) < 0:
#             b = x0
#         else:
#             a = x0
#         x0 = (a+b)*1.0/2
#     return x0

def relaxation_method(f, x, tau, eps):
    x_next = x + tau * f(x)
    while abs(x_next - x) > eps*tau:
        x = x_next
        x_next = x + tau * f(x)
    return x_next

def simple_iteration_method(g, x, eps):
    x_next =g(x)
    while abs(x_next - x) > eps:
        x = x_next
        x_next = g(x_next)
    return x_next

def main():
    print("Метод дихотомії: ", dih_method(funct, -1, 2, 0.0001))
    print("Метод релаксації: ", relaxation_method(funct, 1, 0.05, 0.0001))
    print("Метод простої ітерації: ", simple_iteration_method(function_for_simple_itterarion, 100, 0.0000001))

if __name__ == "__main__":
    main()

