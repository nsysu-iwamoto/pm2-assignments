# Interpolation

"""
You may use/edit this file to test the functions in interpolation.py.
"""

import interpolation


def test_task_1():
    data = [(1, 101), (2, 104), (4, 116)]
    coefficients = interpolation.lagrange_coefficients(data)
    print(coefficients[0])  # -> 100
    print(coefficients[1])  # -> 0
    print(coefficients[2])  # -> 1

    print(interpolation.lagrange_interpolation(coefficients, 3))  # -> 109
    print(interpolation.lagrange_interpolation(coefficients, 2))  # -> 104

    data1 = [(0, 0), (2, 0), (3, 1), (4, 3), (5, 3)]
    data2 = [(0, 0), (2, 0), (3, 3), (4, 3), (5, 3)]
    c1 = interpolation.lagrange_coefficients(data1)
    c2 = interpolation.lagrange_coefficients(data2)
    print(interpolation.lagrange_interpolation(c1, 1))  # -> 0.4
    print(interpolation.lagrange_interpolation(c2, 1))  # -> ???

    print(interpolation.linear_interpolation(data1, 1))  # -> 0
    print(interpolation.linear_interpolation(data2, 1))  # -> 0
    print(interpolation.linear_interpolation(data1, 2.5))  # -> 0.5
    print(interpolation.linear_interpolation(data2, 2.5))  # -> 1.5


def test_task_2():
    data1 = [(0, 0), (2, 0), (3, 1), (4, 3), (5, 3)]
    data2 = [(0, 0), (2, 0), (3, 3), (4, 3), (5, 3)]
    print(interpolation.linear_interpolation(data1, 1))  # -> 0
    print(interpolation.linear_interpolation(data2, 1))  # -> 0

    print(interpolation.cubic_spline_interpolation(data1, 1))
    print(interpolation.cubic_spline_interpolation(data2, 1))


if __name__ == "__main__":
    print("Input which task to test (1 or 2): ", end="")
    task = int(input() or 0)
    if task == 1:
        test_task_1()
    elif task == 2:
        test_task_2()
