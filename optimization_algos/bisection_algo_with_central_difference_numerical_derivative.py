# -*- coding: utf-8 -*-
"""
Solve the following problem using the bisection algorithm. First implement a routine to calculate the numerical derivative of the function, and then use any root finding algorithm in order to minimize it.
$$
\min_{x} \|\mathbf{A}_0 + \mathbf{A}_1 x + \mathbf{A}_2 x^2 + \mathbf{A}_3 x^3\|_2
$$
Answer should be $x^\star$ up to a tolerance of $10^{-10}$.
"""

import numpy as np
import matplotlib.pyplot as plt

# Define the size of our square matrices to be 3x3.
matrix_size = 3

np.random.seed(3)

# Generate four random 3x3 matrices.
# np.random.randn generates samples from the "standard normal" distribution.
A_0 = np.random.randn(matrix_size, matrix_size)
A_1 = np.random.randn(matrix_size, matrix_size)
A_2 = np.random.randn(matrix_size, matrix_size)
A_3 = np.random.randn(matrix_size, matrix_size)

# Define a function f(x) that calculates the 2-norm of a matrix A(x).
# A(x) is a polynomial matrix function of x: A_0 + x*A_1 + x^2*A_2 + x^3*A_3.
def f(x):
    Ax = A_0 + x * A_1 + x**2 * A_2 + x**3 * A_3
    return np.linalg.norm(Ax, ord=2)

# Define a function to approximate the derivative of f at x using the central difference method.
def df(x, h=1e-10):
    # define here
    return (f(x+h) - f(x-h))/(2*h)

# Implement any of bisection method, secant method, or dekker method
def bisection_method(a, b, tol=1e-5, max_iter=1000):
  c=0
  iter_count = 0
  interval = np.abs(b-a)
  if (np.sign(df(a)) == np.sign(df(b))):
    print("invalid interval (a,b) = (" + a + "," + b + ")")
    return

  while(interval > tol and iter_count < max_iter):
    if (np.sign(df(a)) != np.sign(df(b))):
      c = (a+b)/2
      if np.sign(df(c)) == np.sign(df(b)):
        b=c
      else:
        a=c
      interval = np.abs(b-a)
      iter_count += 1
  return c



#def secant_method(x0, x1, tol=1e-5, max_iter=1000):
  #

#def dekker_method(a,b,tol=1e-5, max_iter=1000):
  #

# Define the interval
a = -2  # Start of interval
b = 2  # End of interval

# Find the root
root = bisection_method(a,b)
print("root:", root)