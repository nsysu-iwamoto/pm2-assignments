# Newton Method

Edit `newton_method.py` and implement the following functions.

## Hints and Requirements

The file will be used as a module; a runner code `newton_method_runner.py` will import the file and use it.
Therefore, `newton_method.py` should not have a "main" block or the "main" block must be enclosed in an `if __name__ == "__main__":` block.

You may write your test-code in `newton_method_runner.py` so that you can test your code by executing `python newton_method_runner.py`.

Do not use `Decimal` module for these tasks.

## Task 1: Newton Method

### Subtask 1a

Example 1 in Section 19.2 of the textbook demonstrates an iterative method for calculating solutions of $x^2 - 3x + 1 = 0$.

The textbook says that this equation can be solved by Eq. (4a) and shows a sequence `1.0, 0.667, 0.481, 0.411, 0.390, ...`.
So, let us reproduce this sequence.

Implement the fixed-point iteration algorithm in the function `fixed_point_iteration(g, x0, n)` and reproduce the sequences in Example 1.
Namely, the following code should print-out `[1.0, 0.6666666666666666, 0.48148148148148145]`.

```python
def g(x):
    return (x * x + 1) / 3

print(fixed_point_iteration(g, 1.0, 2))
```

- Input:
  - `g` is a function that receives a float and returns a float. *Yes, we can assign not only a number but also a function to a variable!*
  - `x0` is the initial value (float).
  - `n` is the number of iterations (int).
- Output: a list of n+1 floats. The first element is x0. The last element is xn.

### Subtask 1b

Table 19.1 summarizes the Newton method. According to the table, the method should receive the following inputs:

- a function `f`,
- its derivative `fp` (standing for f prime),
- the initial value `x0`,
- the error tolerance `eps`, and
- the maximum number of iterations `n`.

and return x_(n+1) if the method converges. If it does not converge, it should stop.

*(Notice again that we can assign a function to a variable `f` and pass it to another function `newton`.)*

Now, let us implement the Newton method, starting from the skeleton `newton(f, fp, x0, eps=1e-7, n=100000)` in the file.
Our function should return the solution (if converges) or `None` (if it stops).

Namely, according to Example 3, the following code should print out the square-root of 5.

```python
def f0(x):
    return x * x - 5

def f1(x):
    return 2 * x

x0 = 2.0
solution = newton(f0, f1, x0)
print(solution)
```

Implement the Newton-method algorithm in the function `newton(f, fp, x0, eps=1e-7, n=100000)`, where you need to follow the specification.

- Input: aforementioned `f`, `fp`, `x0` (int/float), `eps` (float), and `n` (int).
- Output: a floating-point number or `None`.

## Task 2: Secant Method and Bisection Method

These methods are less powerful than the Newton method but are more robust and easy to implement, especially when the derivative is not available.

### Subtask 2a

Secant method is introduced in the end of Section 19.2 of the textbook. It is written as the function `secant(f, x0, x1, eps=1e-7, n=100000)` with the inputs

- a function `f`,
- the initial values `x0` and `x1`,
- the error goal `eps`, and
- the maximum number of iterations `n`.

It should return the estimated solution if the difference is converged to `eps` or smaller. Otherwise, it should stop after `n` iteration.

*(Notice we assign a function to a variable `f` and pass it to another function.)*

Namely, according to Example 8, the following code should print out 1.8955 or a closer number.

```python
import math

def f(x):
    return x - 2 * math.sin(x)


x0, x1 = 2.0, 1.9
solution = secant(f, x0, x1, 0.0000001, 1000000)
print(solution)
```

Implement the secant method in the function `secant(f, x0, x1, eps=1e-7, n=100000)`, where

- Input: aforementioned `f`, `x0` and `x1` (int/float), `eps` (float), and `n` (int).
- Output: a floating-point number or `None`.

Also, try to solve Problems 26–29 in Section 19.2.

### Subtask 2b

Do the similar thing with Bisection Method (Problem 25 in Section 19.2). Namely, implement the bisection method as the function `bisection(f, a, b, eps=1e-7, n=100000)`.
