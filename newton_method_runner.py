# Newton Method

"""
You may use/edit this file to test the functions in newton_method.py.
"""

import math
import newton_method


def test_task_1():
    def g(x):
        return (x * x + 1) / 3

    def f0(x):
        return x * x - 5

    def f1(x):
        return 2 * x

    print(newton_method.fixed_point_iteration(g, 1.0, 2))
    print(newton_method.newton(f0, f1, 2.0))


def test_task_2():
    def f(x):
        return x - 2 * math.sin(x)

    print(newton_method.secant(f, 2.0, 1.9))


if __name__ == "__main__":
    print("Input which task to test (1 or 2): ", end="")
    task = int(input() or 0)
    if task == 1:
        test_task_1()
    elif task == 2:
        test_task_2()
