# Integration

Edit `integration.py` and implement the following functions.

## Hints and Requirements

The file will be used as a module; a runner code `integration_runner.py` will import the file and use it.
Therefore, `integration.py` should not have a "main" block or the "main" block must be enclosed in an `if __name__ == "__main__":` block.

You may write your test-code in `integration_runner.py` so that you can test your code by executing `python integration_runner.py`.

Do not use SciPy functions or `Decimal` module for these tasks.

## Task 1: Trapezoidal Integration

### Subtask 1a

In practice, the trapezoidal-integration method is sufficient for many purposes, which is introduced in Kreyszig's Section 19.5.

Begin with the simplest version, `trapezoidal(f, a, b, n=100)`, which calculate the integral of a function `f` over the interval `[a, b]` with the trapezoidal rule with `n` separation.

Namely, according to Example 1,

```python
import math

def f(x):
    return math.exp(-x*x)

print(trapezoidal(f, 0, 1, 10))
```

should print-out 0.746 or a closer number. **Notice that `trapezoidal(f, 1, 0, 10)` should not return the same value!** Its output must be -0.746.

Implement the trapezoidal integration algorithm in the function `trapezoidal(f, a, b, n=100)`, where

- Input: `f` is a function, `a` and `b` are floats specifying the integration range, and `n` is the number of separation. `b` may be smaller than or equal to `a`.
- Output: a number.

### Subtask 1b

We need to estimate the error of `trapezoidal`.  A simple method is to use rectangles instead of trapezoids. 

Assume we are considering the trapezoid between `x1` and `x2 = x1 + delta`. If `f(x1) < f(x2)`, the area of the trapezoid will **usually** be larger than `f(x1) * delta` and smaller than for `f(x2) * delta`. We can use them as an lower and upper bounds of the true value of the integral between `x1` and `x2`.  (It is just an estimation, and there is no guarantee that the true value is between them.)

Implement this algorithm in the function `trapezoidal_with_bounds(f, a, b, n=100)`, where

- Input: `f` is a function, `a` and `b` are floats specifying the integration range, and `n` is the number of separation. `b` may be smaller than or equal to `a`.
- Output: a tuple of three numbers `(integral, lower, upper)`, where `lower` is an estimation of the lower bound and `upper` is an estimation of the upper bound. While `integral` is guaranteed to be between `lower` and `upper, the true result may be out of this range.

## Task 2: Simpson's Rule

### Subtask 2a

The above **Subtask 1b** can be improved by using Simpson's rule, which is more accurate than the trapezoidal rule, so do that.

Simpson's rule splits the integration range into `n` segments and approximates each segment by a quadratic function.
Effectively, Simpson's rule with `n` segments corresponds to trapezoidal rule with `2n` segments, but it usually gives better result due to the use of quadratic functions.

Implement the Simpson's rule in the function `simpson_with_bounds(f, a, b, n=100)`, where

- Input: `f` is a function, `a` and `b` are floats specifying the integration range, and `n` is the number of separation. `b` may be smaller than or equal to `a`.
- Output: a tuple of three numbers `(integral, lower, upper)`, where `lower` is an estimation of the lower bound and `upper` is an estimation of the upper bound.

(This Task 2 has only one Subtask.)
