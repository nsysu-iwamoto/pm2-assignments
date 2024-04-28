# Integration

"""
You may use/edit this file to test the functions in integration.py.
"""

import math
import integration


def f(x):
    return math.exp(-x * x)


def test_task_1():
    print(integration.trapezoidal(f, 0, 1, 100))
    print(integration.trapezoidal_with_bounds(f, 0, 1, 100))


def test_task_2():
    print(integration.simpson_with_bounds(f, 0, 1, 100))


if __name__ == "__main__":
    print("Input which task to test (1 or 2): ", end="")
    task = int(input() or 0)
    if task == 1:
        test_task_1()
    elif task == 2:
        test_task_2()
