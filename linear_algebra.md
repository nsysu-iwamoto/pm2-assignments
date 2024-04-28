# Linear Algebra

Edit `linear_algebra.py` and implement the following functions.

## Hints and Requirements

The file will be used as a module; a runner code `linear_algebra_runner.py` will import the file and use it.
Therefore, `linear_algebra.py` should not have a "main" block or the "main" block must be enclosed in an `if __name__ == "__main__":` block.

You may write your test-code in `linear_algebra_runner.py` so that you can test your code by executing `python linear_algebra_runner.py`.

In general, **we should not** implement matrix handling by ourselves.
Use functions in packages (NumPy, SciPy, LAPACK, ...) as much as possible.
For example, read [the manual of numpy.linalg](https://numpy.org/doc/stable/reference/routines.linalg.html) very carefully.

## Task 1: Linear Systems of Equations

### Subtask 1a

In Kreyszig Section 7.5, we have learned how we can classify linear systems of equations (Theorem 1).
Let's make a code for this test.

As a linear system of equations is equivalent to an augmented matrix (See Section 7.3), we can use it as the input.
The output can just be a string: `"unique", "many", "none"` to represent how many solutions we have.

Complete the function `classify_linear_system(aug)`.

- Input: `aug` is the augmented matrix of a linear system of equations. It is a 2d NumPy array with real elements.
- Output: a string: `"unique"`, `"many"`, or `"none"`.

### Subtask 1b

Complete the function `solve_linear_system(mat, vec)`, which finds a solution `x` of a linear system of equations `(mat)(x) = (vec)`.
Here, `mat` is an (m,n) matrix, `x` is a (m,1) vector, and `vec` is a (n,1) vector. Notice that both `x` and `vec` are column vectors, but we use 1d NumPy arrays to represent them.

- Input: `mat` is a 2d NumPy array. `vec` is a 1d NumPy array. Their elements are real numbers.
- Output: If the system has a unique solution, return the solution as a 1d NumPy array. Otherwise, return `None`.

### Subtask 1c

Complete the function `find_solutions_of_linear_system(mat, vec)`, which finds a solution `x` of a linear system of equations `(mat)(x) = (vec)`.

The set-up is the same as the previous task, but here, if the system has infinitely many solutions, return one solution.

You are encouraged to reuse the previous functions.

- Input: `mat` is a 2d NumPy array. `vec` is a 1d NumPy array. Their elements are real numbers.
- Output: If the system has a solution, return it as a 1d NumPy array. Otherwise, return `None`.

## Task 2: Matrix Decomposition

### Subtask 2a

Following the Python-Starter-2 Task 07, implement the following functions. Here, `m` are complex matrices.

- `is_upper_triangular(m)` to check if `m` is (square and) upper-triangular.
- `is_diagonal(m, only_square=True)` to check if `m` is diagonal. Here, if `only_square` is `True`, the function should check if it is square and should return `False` for non-square matrices. If `only_square` is `False`, it should return `True` for any matrix satisfying `m[i, j] == 0` for all `i != j`.

### Subtask 2b

Similarly, implement the following functions. Here, `m` are complex matrices. However, do not calculate their inverse matrices. In principle, we should avoid the calculation of the inverse matrix because it is relatively slow.

- `is_orthogonal(m, tol=1e-6)` to check if `m` is real and orthogonal, where you need to consider some tolerance `tol`.
- `is_unitary(m, tol=1e-6)` to check if `m` is unitary with some tolerance `tol`.
- `is_hermitian(m, tol=1e-6)` to check if `m` is hermitian with some tolerance `tol`.

### Subtask 2c

Any (complex) matrix `m` can be decomposed into a unitary matrix `Q` and an upper-triangular matrix `R` as `m = Q R`, which is called QR decomposition.

Write a function `qr_decomposition(m)` that returns `Q` and `R` as a tuple.

- Input: `m` is a 2d NumPy array, whose elements are complex.
- Output: A tuple `(q, r)` of two 2d NumPy arrays. They satisfy `q@r == m`, `q` is unitary, and `r` is upper-triangular.

It is recommended to check the results by using the previous functions, such as

```python
def qr_decomposition(m):
    # (your code here, and then)
    assert is_unitary(q)
    assert is_upper_triangular(r)
    return (q, r)
```

### Subtask 2d

Any (complex) matrix `m` can be decomposed into as `m = U D V-dagger`, where `U` and `V` are unitary and `D` is a (possibly non-square) "diagonal" matrix.

Write a function `qr_decomposition(m)` that returns a tuple `(U, D, V)`.

- Input: `m` is a 2d NumPy array, whose elements are complex.
- Output: A tuple `(u, d, v)` of three 2d NumPy arrays. They satisfy `u @ d @ v.H == m`, `d` is diagonal but can be non-square, and `u` and `v` are unitary.

It is recommended to check the results by using the previous functions.

## Task 3: Matrix Diagonalization

### Subtask 3a

Write a function `unitary_diagonalize(m)` that diagonalizes a (complex) square matrix `m` by an unitary matrix.
Recall that `m` can be unitary diagonalized if and only if `m` is normal.

- Input: `m` is a 2d NumPy array, whose elements are complex.
- Output: `None` if `m` is not normal. Otherwise, return a tuple `(u, d)` with two 2d NumPy arrays. They satisfy `u @ d @ u.H == m`, `d` is diagonal, and `u` is unitary.

### Subtask 3b

Write a function `diagonalize(m)` that diagonalizes a (complex) square matrix `m`.
Here, you need to check whether `m` can be diagonalized or not.

- Input: `m` is a 2d NumPy array, whose elements are complex.
- Output: `None` if `m` is not diagonalzable. Otherwise, return a tuple `(p, d)` with two 2d NumPy arrays. They satisfy `p @ d @ np.linalg.inv(p) == m`, `d` is diagonal, and `u` is invertible.

Notice you can reuse the previous functions.
