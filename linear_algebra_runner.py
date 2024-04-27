# Linear Algebra

"""
You may use/edit this file to test the functions in linear_algebra.py.
"""

import numpy as np
import linear_algebra as la


def test_task_1():
    aug = np.array([[1, 2, 3], [4, 5, 6]])
    print(la.classify_linear_system(aug))


def test_task_2():
    m = np.array([[1, 2, 3], [0, 4, 5], [0, 0, 6]])
    print(la.is_upper_triangular(m))


def test_task_3():
    m = np.array([[1, 2], [2, 3]])
    print(la.unitary_diagonalize(m))


if __name__ == "__main__":
    print("Input which task to test (1 or 2 or 3): ", end="")
    task = int(input())
    if task == 1:
        test_task_1()
    elif task == 2:
        test_task_2()
    elif task == 3:
        test_task_3()
