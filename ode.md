# Ordinary Differential Equations

Edit `ode.py` and implement the following functions handling ordinary differential equations (ODEs).

## Hints and Requirements

The file will be used as a module; a runner code `ode_runner.py` will import the file and use it.
Therefore, `ode.py` should not have a "main" block or the "main" block must be enclosed in an `if __name__ == "__main__":` block.

You may write your test-code in `ode_runner.py` so that you can test your code by executing `python ode_runner.py`.

**Do not** use NumPy or SciPy in these tasks.

## How to Set-up the problem

Consider the following ODE: `y' = -y + x + 1` with the initial condition `y(1) = 2`. We know the solution is `y = x + exp(1-x)`.

In Python, this set-up can be given in the following way:

```python
def f(x, y):
    return -y + x + 1

target_function = f
x0 = 1
y0 = 2
solve_ode(target_function, x0, y0, ...)  # ... are other arguments, if needed.
```

The output of `solve_ode` will be, for example, a list of tuples `[(x0, y0), (x1, y1), ...]` where `(xi, yi)` is the estimated value at `xi`.
Or, we may tell the function the values of `x` we need:

```python
points_to_return = [x/2 for x in range(3, 9)]  # this means [1.5, 2, 2.5, 3, 3.5, 4]
solve_ode(target_function, x0, y0, points_to_return, ...)
```

Even in this case, the output should be a list of tuples `[(x0, y0), (x1, y1), ...]`.
If you are interested only in the value at `x=10` (for example), then it could be

```python
solve_ode(target_function, x0, y0, 10, ...)
```

and the output can be a single tuple `(10, y_at_10)`, but it is also fine to return a list of tuples as long as the list has the answer for `x=10`.

In the following tasks, the return value will be one of the above choices, depending on the task. Meanwhile, the input will be `(target_funtion, x0, y0, ...)`, where the specification of `target_function` is given as the first code-snippet above.

## Task 1: Euler Method

Section 21.1 of Kreyszig discusses basic algorithms to solve ODEs. It first introduces the Euler method, and then the improved Euler method in Table 21.1

### Subtask 1a

Implement the Euler method in the function `euler(target_function, x0, y0, h, n)` that solves the ODE `y' = f(x, y)` with the initial condition `y(x0) = y0` using the Euler method.

The input will be

- `target_function` is a function such as `f(x, y)` above. (Check the order ! It should not be `f(y, x)`.)
- `x0` and `y0` specify the initial value.
- `h` is the step size and `n` is the number of steps.

It will estimate the values of `y(x)` at `x0 + h`, `x0 + 2h`, ..., `x0 + nh`. Therefore, the output list will have length `n`.

- Input: `target_function`, `x0`, `y0`, `h`, and `n`. You can assume `h` as well as `n` is positive, i.e., we only calculate `x > x0`.
- Output: a list of tuples `[(x1, y1), ..., (xn, yn)]`. Length must be `n`.

For example,

```python
def f(x, y):
    return -y + x + 1

euler(f, 1, 2, 0.1, 4)  # -> [(1.1, 2), (1.2, 2.01), (1.3, 2.029), (1.4, 2.0561)]
```

The result is not good; we know the exact value at 1.4 is 2.070.
You can improve the precision with using smaller `h`, but then we need larger `n` such as `euler(f, 1, 2, 0.001, 400)` and it will take much more time (x100 in this case); it is not a good idea.

### Subtask 1b

Using the improved Euler method, you can obtain the same precision with fewer steps.

Implement the improved Euler method in the function `improved_euler(target_function, x0, y0, h, n)`. Table 21.1 in the textbook will help you.

The input and output should be the same as in the previous Subtask. Check how the result is improved.

## Task 2: Runge-Kutta Method

In practice, the Runge-Kutta method of fourth order (RK4) is the best method for most situations.
It is introduced in Section 21.2 of the textbook.

### Subtask 2a

Based on the implementation in Table 21.3 of the textbook, implement the function for RK4, `rk4(target_function, x0, y0, h, n)` that solves the ODE `y' = f(x, y)` with the initial condition `y(x0) = y0` using the method.

See Task 1 for the input and output specification. The input will be

- `target_function` is a function such as `f(x, y)` above. (Check the order ! It should not be `f(y, x)`.)
- `x0` and `y0` specify the initial value.
- `h` is the step size and `n` is the number of steps.

It will estimate the values of `y(x)` at `x0 + h`, `x0 + 2h`, ..., `x0 + nh`. Therefore, the output list will have length `n`.

- Input: `target_function`, `x0`, `y0`, `h`, and `n`. You can assume `h` as well as `n` is positive, i.e., we only calculate `x > x0`.
- Output: a list of tuples `[(x1, y1), ..., (xn, yn)]`. Length must be `n`.

### Subtask 2b

Theoretically, the Euler method (Subtask 1a) is equivalent to the Runge-Kutta of first order and the improved Euler method (Subtask 1b) is to the Runge-Kutta of second order.
As you may expect, there is also the third-order version (RK3), which is introduced in Problem 21.1.18.

Implement the function `rk3(target_function, x0, y0, h, n)` that solves the ODE `y' = f(x, y)` with the initial condition `y(x0) = y0` using the Runge-Kutta of *third* order.
The input and output specification is the same as the previous subtasks.

You may check the RK3 is better than the improved Euler, but worse than RK4.
