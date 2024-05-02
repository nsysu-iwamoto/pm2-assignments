# Interpolation

Edit `interpolation.py` and implement the following functions.

## Hints and Requirements

The file will be used as a module; a runner code `interpolation_runner.py` will import the file and use it.
Therefore, `interpolation.py` should not have a "main" block or the "main" block must be enclosed in an `if __name__ == "__main__":` block.

You may write your test-code in `interpolation_runner.py` so that you can test your code by executing `python interpolation_runner.py`.

You **are recommended to** use NumPy and SciPy functions but do not use `Decimal` module for these tasks.

## Task 1: Lagrange Interpolation

### Subtask 1a

Section 19.3 of Kreyszig discusses interpolation of a function. Imagine there are `n` data points:

```python
x = [1, 2, 3]
y = [101, 104, 109]  # interpolated by x^2 + 100
```

Then, there is always a `n-1`-th order polynomial `f(x)` that passes all these points: `y[n] == f(x[n])`, as long as `x[i]` are all different.
We can estimate the value at a different `x` using the polynomial.
This is called a polynomial interpolation, or a Lagrange interpolation. The obtained polynomial is called Lagrange polynomial.

Now, data points are given by a list of two-tuples, and you are asked to write a function that returns the coefficients of the Lagrange polynomial. For example,

```python
data = [(1, 101), (2, 104), (4, 116)]
coefficients = lagrange_coefficients(data)
print(coefficients[0])  # -> 100
print(coefficients[1])  # -> 0
print(coefficients[2])  # -> 1
```

Write this function `lagrange_coefficients(data)`.

- Input: `data` is a list of tuples. It has `n` elements, each of which is a tuple `(xi, yi)`. The values of `xi` are all different.
- Output: a list of `n` numbers, which are the coefficients of the Lagrange polynomial. The first element is the coefficient of the constant term, so that the function is given by the sum of`a[k] * (x**k)` as in mathematics, where `a` is the output of this function.

### Subtask 1b

Using the above result, we can estimate the value at a different `x` using the above result.
 Write a function `lagrange_interpolation(coefficients, x)` that returns the value of the Lagrange polynomial at `x`. Namely,

```python
data = [(1, 101), (2, 104), (4, 116)]
coefficients = lagrange_coefficients(data)
print(lagrange_interpolation(coefficients, 3))  # -> 109
print(lagrange_interpolation(coefficients, 2))  # -> 104
```

- Input: `coefficients` are the output of `lagrange_coefficients(data)`. `x` is a number.
- Output: a number.

### Subtask 1c

This interpolation  is theoretically nice but useless in practice. You can check how it is useless by running the following code:

```python
data1 = [(0, 0), (2, 0), (3, 1), (4, 3), (5, 3)]
data2 = [(0, 0), (2, 0), (3, 3), (4, 3), (5, 3)]
print(lagrange_interpolation(lagrange_coefficients(data1), 1))  # -> 0.4
print(lagrange_interpolation(lagrange_coefficients(data2), 1))  # -> ???
```

I suppose you get an unexpected value.

We therefore usually use the spline interpolation or other method, but also the linear interpolation: connecting the adjacent points with a straight line and interpolating the value according to the line, is also useful in spite of its simplicity.

Try to implement the linear interpolation in the function `linear_interpolation(data, x)`, where

- Input: `data` is a list of tuples and `x` is the point to be estimated. `data` It has `n` elements, each of which is a tuple `(xi, yi)` and *they are sorted* by `xi`; i.e., `data[i][0] < data[j][0]` if `i < j`.
- Output: a number.

For example,

```python
data1 = [(0, 0), (2, 0), (3, 1), (4, 3), (5, 3)]
data2 = [(0, 0), (2, 0), (3, 3), (4, 3), (5, 3)]
print(linear_interpolation(data1, 1))  # -> 0
print(linear_interpolation(data2, 1))  # -> 0
print(linear_interpolation(data1, 2.5))  # -> 0.5
print(linear_interpolation(data2, 2.5))  # -> 1.5
```

## Task 2: Spline Interpolation

### Subtask 2a

Here, we are going to compare the linear interpolation and the cubic spline interpolation, which is more accurate than the linear interpolation.

First, implement `linear_interpolation(data, x)` that calculate the linear interpolation. This is the same task as Subtask 1c, so you can skip this subtask if you have this function.

- Input: `data` is a list of tuples and `x` is the point to be estimated. `data` It has `n` elements, each of which is a tuple `(xi, yi)` and *they are sorted* by `xi`; i.e., `data[i][0] < data[j][0]` if `i < j`. See Subtask 1c for the details.
- Output: a number.

### Subtask 2b

Implement `cubic_spline_interpolation(data, x)` that estimates the value of `x` with using the cubic spline interpolation of `data`. The specification for input and output is the same as `linear_interpolation(data, x)`.
