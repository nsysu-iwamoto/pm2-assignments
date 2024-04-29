# Monte Carlo

"""
You may use/edit this file to test the functions in monte_carlo.py.
"""

import math
import monte_carlo as mc


def test_task_1():
    n = 100000
    print(mc.estimate_pi_by_monte_carlo(n))
    print(mc.integration_abs_sin_cos(0, 0, n))  # zero
    print(mc.integration_abs_sin_cos(0, math.pi, n))  # 1.79
    print(mc.integration_sin_cos(0, math.pi, n))  # zero


def test_task_2():
    lifetime = 12.0
    speed = 0.5
    detector_length = 5
    detector_position = 10
    prob = mc.detect_probability(lifetime, speed, detector_length, detector_position)

    max_angle = 0.25
    prob = mc.detect_probability_angled(
        lifetime, speed, max_angle, detector_length, detector_position
    )
    print(prob)


def test_task_3():
    for i in range(10):
        print(mc.random_direction())

    print(mc.angle_probability_three(0.0))  # one
    print(mc.angle_probability_three(3.15))  # zero
    print(mc.angle_probability_three(math.pi / 6))  # zero


if __name__ == "__main__":
    print("Input which task to test (1, 2, or 3): ", end="")
    task = int(input() or 0)
    if task == 1:
        test_task_1()
    elif task == 2:
        test_task_2()
    elif task == 3:
        test_task_3()
