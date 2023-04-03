import matplotlib.pyplot as plt
import numpy as np
from sympy import *
from numpy import sort

def f(x):
    return 3 * (x ** 2) - (np.cos(np.pi * x)) ** 2

def fa(x, v):
    return 3 * (x ** 2) - (np.cos(np.pi * x)) ** 2 - v

def dih_method(a, b, eps, v):
    #print(v, fa(a, v), fa(b, v), a, b)
    if fa(a, v) * fa(b, v) > 0:
        return None
    x0 = (a+b)*1.0/2
    if abs(fa(x0, v)) < eps:
        return x0
    else:
        if fa(a, v)*fa(x0, v) < 0:
            return dih_method(a, x0, eps, v)
        else:
            return dih_method(x0, b, eps, v)



def lagrange(x, nodes, values):
    n = len(nodes)
    s = 0
    for i in range(n):
        product = 1
        for j in range(n):
            if i != j:
                product *= (x - nodes[j]) / (nodes[i] - nodes[j])
        s += values[i] * product
    return s



def f_obr(v):
    return dih_method(-2, 0, 0.0001, v)

def visualise(a, b, fun, nodes, values):

    x = np.linspace(-1-0.1, 1/2+0.1, 10000)
    y = fun(x, values, nodes)

    x2 = np.linspace(-0.45, 0.37, 10000)

    plt.plot(y, x, label='Lagrange polynomial')
    plt.plot(x2, f(x2), label='Original function')
    plt.legend()
    plt.show()

def visualise2(a, b, fun, nodes, values):
    x = np.linspace(-1-0.2, 1/2+0.1, 10000)
    y = fun(x, values, nodes)

    x2 = np.linspace(-0.45, 0.37, 10000)

    plt.plot(y, x, label='Lagrange polynomial chebyshev roots')
    plt.plot(x2, f(x2), label='Original function')
    plt.legend()
    plt.show()

def visualise3(a, b, fun, nodes, values):
    s = fun(values, nodes)
    x = np.linspace(-1-0.2, 1/2+0.1, 10000)
    y = np.array([s(a) for a in x])

    x2 = np.linspace(-0.45, 0.37, 10000)

    plt.plot(y, x, label='Natural spline')
    plt.plot(x2, f(x2), label='Original function')
    plt.legend()
    plt.show()

def visualise4(a, b, fun, nodes, values):
    s = fun(values, nodes)
    x = np.linspace(-1-0.2, 1/2+0.1, 10000)
    y = np.array([s(a) for a in x])

    x2 = np.linspace(-0.45, 0.37, 10000)

    plt.plot(y, x, label='Natural spline chebyshev roots')
    plt.plot(x2, f(x2), label='Original function')
    plt.legend()
    plt.show()



def chebyshev_roots(a, b, n):
    nodes = []
    for k in range(n):
        nodes.append((a+b)/2+(b-a)/2*np.cos((2*k+1)*np.pi/(2*n)))
    return np.array(nodes)

def cubic_spline(x, y):
    n = len(x) - 1
    h = x[1:] - x[:-1]
    f = (y[1:] - y[:-1]) / h
    A = np.zeros((n-1, n-1))
    b = np.zeros(n-1)
    for i in range(n-1):
        if i > 0:
            A[i, i-1] = h[i-1]/6
        A[i, i] = (h[i-1] + h[i])/3
        if i < n-2:
            A[i, i+1] = h[i]/6
        b[i] = (f[i+1] - f[i])
    m = np.zeros(n+1)
    m[1:-1] = np.linalg.solve(A, b)

    a = np.zeros(n)
    b = np.zeros(n)
    for i in range(n):
        b[i] = y[i+1]-(m[i+1]*h[i]**2)/6
        a[i] = y[i] - (m[i]*h[i]**2)/6

    def s(x0):
        i = np.searchsorted(x, x0) - 1
        if i < 0:
            i = 0
        elif i >= n:
            i = n-1
        sym = symbols('x')
        return m[i]*(x[i+1]-x0)**3/(6*h[i])+m[i+1]*(x0-x[i])**3/(6*h[i])+a[i]*(x[i+1]-x0)/h[i] + b[i]*(x0-x[i])/h[i]
    return s


def main():
        a = 0
        b = -1/2
        #print(f(a), f(b))
        n = 10
        nodes =np.linspace(a, b, n)
        values = f(nodes)
        print("значеня у", values)
        print("значеня x", nodes)
        print(lagrange(0, values, nodes))



        values2 = sort(chebyshev_roots(f(b), f(a), n))
        nodes2 = np.array([f_obr(xv) for xv in values2])
        print("корні поліному чебешева для оберненої функції", values2)
        print("значеня x для цих коренів", nodes2)
        print(lagrange(0, values2, nodes2))



        x = symbols('x')
        #print(simplify(lagrange(x, values2, nodes2)))
        sp1 = cubic_spline(values, nodes)
        print("splaine 1", sp1(0))
        sp2 = cubic_spline(values2, nodes2)
        print("splaine 2", sp2(0))
        visualise(-1 / 2, 0, lagrange, nodes, values)
        visualise2(-1 / 2, 0, lagrange, nodes2, values2)
        visualise3(-1 / 2, 0, cubic_spline, nodes, values)
        visualise4(-1 / 2, 0, cubic_spline, nodes2, values2)






if __name__ == '__main__':
    main()

