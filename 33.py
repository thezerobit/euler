# Mostly boring problem, but wrote a recursive 
# function to reduce a fraction that can be reused later if necessary
 
from math import sqrt
def nt(x):
  if x == 1:
    return 0
  return 1

def is_equiv(a,b,x,y):
  return (b*x) == (a*y)

def is_curious(a, b, v = False):
  stra = str(a)
  strb = str(b)
  for x in [0,1]:
    for y in [0,1]:
      if (stra[x] == strb[y]) and (stra[x] != '0'):
        if is_equiv(a,b,int(stra[nt(x)]),int(strb[nt(y)])):
          return True
  return False

def reduc(a,b):
  for x in xrange(2,int(sqrt(b)) + 1):
    if ((a % x) == 0) and ((b % x) == 0):
      return reduc(a / x, b / x)
  return a,b

proda = 1
prodb = 1

found = 0

for a in xrange(10, 99):
  for b in xrange(a+1, 100):
    if is_curious(a,b):
      print "curious:",a,"/",b
      proda *= a
      prodb *= b

print "final:",proda,"/",prodb

reda, redb = reduc(proda,prodb)  

print "reduced:",reda,"/",redb