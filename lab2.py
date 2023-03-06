import numpy as np

def gauss(A, b):
    n = len(A)
    Ab = np.concatenate((A, b), 1)

    for i in range(n):
        max_row = i
        for j in range(i + 1, n):
            if abs(Ab[j, i]) > abs(Ab[max_row, i]):
                max_row = j
        print(i + 1, "- ітерація", max_row, "- головний рядок")
        Ab[[i, max_row]] = Ab[[max_row, i]]

        for j in range(i + 1, n):
            k = (Ab[j, i] / Ab[i, i])
            row = Ab[i]*k
            Ab[j] = (Ab[j] - row)
        print(Ab)

    x = np.zeros(n)
    for i in range(n - 1, -1, -1):
        x[i] = (Ab[i, n] - np.dot(Ab[i, i+1:n], x[i+1:n])) / Ab[i, i]

    return x


# noinspection PyPep8Naming
def jacobi(A, b, x, eps):
    n = len(A)

    D = np.diag(np.diag(A))
    D_inv = np.diag([1/D[i, i] for i in range(n)])
    # x = Bx + c
    B = np.matmul(D_inv, (D-A))
    c = np.dot(D_inv, b)

    x_next = np.dot(B, x)+c
    i = 1
    print("Ітреація 1, вектор x_next - x та його норма:", x_next-x, np.max(np.abs(x_next - x)))
    while np.max((np.abs(x_next - x))) > eps:
        x = x_next
        x_next = np.dot(B, x)+c
        i += 1
        print("Ітреація та значення кореня:", i, x_next)
        np.max((np.abs(x_next - x)))
    print("Ітреація, ", i, ", вектор x_next - x та його норма:", x_next-x, (np.abs(x_next - x)))
    return x_next


def main():
    A1 = np.array([[1.0, 2, 3],
                  [4, 5, 6],
                  [7, 8, 10]])
    b1 = np.array([[3], [6], [9]])
    x1 = gauss(A1, b1)
    print("Розв'язок:", x1)
    print("//////////////////////////////////////////////////")
    A2 = np.array([[3, -1, 1],
                  [-1, 2, 0.5],
                  [1, 0.5, 3]])
    b2 = np.array([3.0, 6, 9])
    x2 = jacobi(A2, b2, np.ones(len(b2)), 0.0001)
    print("Розв'язок:", x2)


if __name__ == '__main__':
    main()

