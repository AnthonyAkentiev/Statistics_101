from math import sqrt

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

data = [49., 66, 24, 98, 37, 64, 98, 27, 56, 93, 68, 78, 22, 25, 11]

#print mean(data)

#print median(data)

#print mode(data)

print variance(data)
print stddev(data)
