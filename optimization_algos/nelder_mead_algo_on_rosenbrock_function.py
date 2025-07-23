# -*- coding: utf-8 -*-
"""
Implement the Nelder-mead algorithm on the function $f(x,y) = (x-1)^2 + (y-x^2)^2$ starting at initial point $(-1,-1)$.
"""

from numpy import arange, meshgrid
from matplotlib import pyplot as plt
import numpy as np
import copy

# objective function
def f(x):
  # Rosenbrock function
  return (x[0]-1)**2 + 1*(x[1]-x[0]**2)**2

xinit = [-1.0,-1.0]    # initialization

maxiter = 100

# Implement Nelder mead
n = len(xinit)
prev_best = f(xinit)
no_impr = 0   # count iterations without improvement
res = [[xinit, prev_best]]

for i in range(n):
  u = xinit.copy()
  u[i] = u[i] + 1
  res.append([u, f(u)])


for iter in range(maxiter):
  res.sort(key=lambda x: x[1])
  best = res[0][1]

  print('...best so far:', best)

  if best < prev_best - 1e-6:
      no_impr = 0
      prev_best = best
  else:
      no_impr += 1

  if no_impr >= 10:
    print(res[0])
    break

  x0 = np.mean([t[0] for t in res[:-1]], axis=0)

  # reflection
  xr = 2 * x0 - res[2][0]
  rscore = f(xr)
  if res[0][1] <= rscore < res[-2][1]:
    res[-1] = [xr, rscore]
    print('reflection')
    continue

  # expansion
  if rscore < res[0][1]:
    xe = 2 * xr - x0
    escore = f(xe)
    res[-1] = [xe, escore] if escore < rscore else [xr, rscore]
    print('expansion')
    continue

  # contraction
  if rscore > res[-1][1]: ##made correction - it was 'if rscore < res[-1][1]' but should be 'if rscore > res[-1][1]'
    xc = (res[-1][0] + x0)/2
    cscore = f(xc)
    if cscore < rscore: ##should be ideally compared with res[-1][1] i.e. the worst point(xw)
      res[-1] = [xc, cscore]
      print('contraction (out)')
      continue
  else:
    xc = (x0 + xr)/2
    cscore = f(xc)
    if cscore < res[-1][1]:
      res[-1] = [xc, cscore]
      print('contraction (in)')
      continue

  # reduction
  res = [((t[0] + res[0][0])/2, f(t[0])) for t in res[1:]]
  print('reduction')