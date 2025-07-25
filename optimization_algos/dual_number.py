# -*- coding: utf-8 -*-
"""
Consider the dual number code introduced in the slides. Define sine and cosine such that the given code works. Do NOT use Taylor series expansion of sine and cosine since we do not want to incur any truncation errors.
"""

from math import sin, cos
class Dual:
    def __init__(self, a, b=0):
        if isinstance(a, Dual):
            self.a, self.b = a.a, a.b
        else:
            self.a, self.b = a, b

    def __str__(self):
        return f"Dual({self.a}, {self.b})"

    def __add__(self, other):
        other = Dual(other)
        new_a = self.a + other.a
        new_b = self.b + other.b
        return Dual(new_a, new_b)

    def __sub__(self, other):
        other = Dual(other)
        new_a = self.a - other.a
        new_b = self.b - other.b
        return Dual(new_a, new_b)

    def __mul__(self, other):
        other = Dual(other)
        new_a = self.a * other.a
        new_b = self.b * other.a + self.a * other.b
        return Dual(new_a, new_b)

    def __truediv__(self, other):
        other = Dual(other)
        if other.a == 0:
            raise ZeroDivisionError("Division by zero")
        new_a = self.a / other.a
        new_b = (self.b * other.a - self.a * other.b) / (other.a ** 2)
        return Dual(new_a, new_b)

def cube(x):
    return x * x * x

def sine(x):
  return Dual(sin(x.a), cos(x.a))

def cosine(x):
  return Dual(cos(x.a), -sin(x.a))

def sqrt(x):
    t = x
    for _ in range(10):
        t = (t + x / t) / 2
    return t

f = lambda x: cosine(sqrt(x)) + sine(cube(x))

df = f(Dual(2.0,1))

print('f(x) = ',df.a,'f\'(x) =',df.b)