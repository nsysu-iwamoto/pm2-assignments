# Monte Carlo

Edit `monte_carlo.py` and implement the following functions.

## Hints and Requirements

The file will be used as a module; a runner code `monte_carlo_runner.py` will import the file and use it.
Therefore, `monte_carlo.py` should not have a "main" block or the "main" block must be enclosed in an `if __name__ == "__main__":` block.

You may write your test-code in `monte_carlo_runner.py` so that you can test your code by executing `python monte_carlo_runner.py`.

Do not use `Decimal` module for these tasks.

## Task 1: Monte Carlo Integration

### Subtask 1a

We can calculate the value of pi = 3.14.... by Monte Carlo method.
Implement the calculation in the function `estimate_pi_by_monte_carlo(n)`.

- Input: `n` is the number of Monte Carlo trials.
- Output: a number.

### Subtask 1b

We can interpret the previous Subtask as an integral of `sqrt(1 - x*x)` over [0, 1], which is pi/4.
In other words, we can do integration by Monte Carlo method.

Let's begin with a simple example: `f(x) = abs(sin(cos(x)))`.

Integration of this function is analytically difficult, but very easy with Monte Carlo method because it is always positive and smaller than 1. These conditions allow us just to repeat Subtask 1a.

Implement the Monte Carlo integration of this f(x) in the function `integration_abs_sin_cos(a, b, n=10000000)`, which calculate the integral of f(x) over [a, b].

- Input: `a` and `b` are the lower and upper limits of the integral. `n` is the number of Monte Carlo trials.
- Output: a number.

### Subtask 1c

The next step is `g(x) = sin(cos(x))`. Do the same thing, but notice that the function can be negative, and implement the function `integration_sin_cos(a, b, n=10000000)`.

- Input: `a` and `b` are the lower and upper limits of the integral. `n` is the number of Monte Carlo trials.
- Output: a number.

## Task 2: Monte Carlo Simulation

For this task, you need to understand the exponential distribution and how to generate a random number from the exponential distribution.
Look for resource in Wikipedia, or see documents of `random.expovariate()` or `numpy.random.exponential()`.

The following code may help you understand the exponential distribution.

```python
import random
import matplotlib.pyplot as plt

samples = []
for i in range(10000):
    samples.append(random.expovariate(1 / 2.5))
# or samples = [random.expovariate(1 / 2.5) for i in range(10000)]

plt.hist(samples, bins=30, density=True)
print(sum(samples) / len(samples))  # the average
plt.show()
```

### Subtask 2a

Consider an unstable particle, whose **average** lifetime is `tau`. According to quantum mechanics, its lifetime is `t` with a probability `math.exp(-t / tau) / tau`.

In other words, its lifetime is given by `random.expovariate(1 / tau)`; for example, if we prepare 100 samples of the particle, their lifetime is given by

```python
[random.expovariate(1 / tau) for i in range(100)]
```

Now, assume there is a machine emitting the particle at the origin (0, 0, 0). The **average** lifetime of the particle is `lifetime`, its speed is `speed`, and the direction is fixed to the positive-x direction.

We have a spherical detector with radius `detector_radius`.
The detector is not sensitive to the particle itself, but if the particle decays inside the detector, it can detect the particle.

We place it at (x, y, z) = (`detector_position`, 0, 0).
Namely, if the particle lifetime is between `(detector_position - detector_radius) / speed` and `(detector_position + detector_radius) / speed`, we can detect the particle.

Write a function `detect_probability(lifetime, speed, detector_radius, detector_position)` to calculate the probability that we can detect the particle.

- Input: `lifetime`, `speed`, `detector_radius`, and `detector_position`, as described above. These physical quantity have units, which we can ignore for now; `detector_radius < detector_position` is guaranteed.
- Output: a number between zero and one.

### Subtask 2b

What happens if the emitter is angled? Imagine the particle velocity is (`speed * math.cos(theta)`, `speed * math.sin(theta)`, 0) with `theta = random.uniform(-0.25, +0.25)`, i.e., random and uniformly distributed between -0.25 and +0.25 (radian), or ±14.3 degree.

The spherical detector is located as before; its center is at (x, y, z) = (`detector_position`, 0, 0).

Write a function `detect_probability_angled(lifetime, speed, max_angle, detector_radius, detector_position)` to calculate the probability that we can detect the particle.

- Input: `lifetime`, `speed`, `max_angle`, `detector_radius`, and `detector_position`, as described above, but you will call the function always with `max_angle = 0.25`.
- Output: a number between zero and one.

Hint: Calculate the decay location and check if it is inside the detector or not.

## Task 3: Spherically Symmetric Distribution

### Subtask 3a

See the previous Task 2. In the real-world experiments, the particle is often emitted isotropically, i.e., uniformly distributed in the solid angle. To simulate this, we need to generate a random direction, or in other words, we need to specify a point on the surface of the Earth randomly.

A point on the Earth surface is specified by `(longitude, latitude)`, where `longitude` is the angle from the Greenwich meridian (-pi to pi) and `latitude` is the angle from the equator (-pi/2 to pi/2).

Write a function `random_direction()` to generate a pair of `(longitude, latitude)` randomly.

- Input: None.
- Output: a `tuple` of two numbers, `(longitude, latitude)`, where `-math.pi <= longitude < math.pi` and `-math.pi/2 <= latitude <= math.pi/2`. Notice that, if `abs(latitude) == math.pi/2`, it is specifying the north or south pole and `longitude` can be any number.

Hint: The following code is totally incorrect. Find why.

```python
import math
import random

def random_direction():
    longitude = random.uniform(-math.pi, +math.pi)
    latitude = random.uniform(-math.pi / 2, +math.pi / 2)
    return (longitude, latitude)
```

### Subtask 3b

We can generate a (randomly directed) unit vector using `random_direction()` as follows:

```python
import math

def random_unit_vector():
    longitude, latitude = random_direction()
    x = math.cos(longitude) * math.cos(latitude)
    y = math.sin(longitude) * math.cos(latitude)
    z = math.sin(latitude)
    return (x, y, z)
```

Generate three unit vectors, and calculate the angles between each two. Now, find the probability that all of those three angles are larger than `theta`. Write a function `angle_probability_three(theta)` to calculate the probability.

- Input: `theta` is a number between 0 and pi.
- Output: a number between zero and one.

(You may extend the function to `angle_probability_n(theta, n)` so that it can handle two, four, five, or more unit vectors.)
