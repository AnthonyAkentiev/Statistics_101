from math import sqrt
from plotting import *

import random

def mean(x):
     return sum(x)/len(x)

def median(x):
     y = sorted(x)
     return y[(len(x)-1)/2]

def mode(x):
     maxcount = 0.
     m = 0.

     for i in range(len(x)):
          icount = x.count(x[i])
          if icount > maxcount:
               maxcount = icount
               m = x[i]

     return m

def variance(x):
     m = mean(x)

     diff = []
     for i in range(len(x)):
          diff.append((x[i] - m) **2)
     return mean(diff) 

def stddev(x):
     return sqrt(variance(x))

# Fill array with random data
def flip_coin(N):
     data = []
     for i in range(N):
          if random.random() > 0.5:
               data.append(1.)
          else:
               data.append(0.)

     return data

def sample(N):
     return [mean(flip(N)) for x in range(N)]

N = 1000

outcomes=sample(N)
histplot(outcomes,nbins=30)

