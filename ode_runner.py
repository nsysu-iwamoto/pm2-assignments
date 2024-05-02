# Ordinary Differential Equations

"""
You may use/edit this file to test the functions in ode.py.
"""

import ode
import math


def f(x, y):
    return -y + x + 1


def test_task_1():
    print(ode.euler(f, 1, 2, 0.1, 4))
    print(ode.improved_euler(f, 1, 2, 0.1, 4))

    # you can try Problem 21.1.1-10. For example,
    def problem01(x, y):
        return -0.2 * y

    def problem02(x, y):
        return 0.5 * math.pi * math.sqrt(1 - y * y)

    def problem03(x, y):
        return (y - x) ** 2

    print(ode.euler(problem01, 0, 5, 0.2, 10))
    print(ode.euler(problem02, 0, 0, 0.1, 10))
    print(ode.euler(problem03, 0, 0, 0.1, 10))


def test_task_2():
    # you can try Problem 21.1.11-17. For example,
    def problem11(x, y):
        return x * y * y

    def problem15(x, y):
        return math.sin(2 * x) - y * math.tan(x)

    print(ode.rk4(problem11, 0, 1, 0.1, 10))
    print(ode.rk4(problem15, 0, 1, 0.1, 10))


if __name__ == "__main__":
    print("Input which task to test (1 or 2): ", end="")
    task = int(input() or 0)
    if task == 1:
        test_task_1()
    elif task == 2:
        test_task_2()
