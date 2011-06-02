#1
#1  1
#1  2  1
#1  3  3  1
#1  4  6  4  1
#5  10 10 5
#15 20 15
#35 35
#70

def red(l):
  res = []
  for i in xrange(len(l) - 1):
    res.append(l[i] + l[i+1])
  return res

def expand(l):
  l.insert(0,0)
  l.append(0)
  return red(l)

dim = 20

mylist = []
mylist.append(1)

for x in xrange(dim):
  mylist = expand(mylist)

for x in xrange(dim):
  mylist = red(mylist)

print mylist[0]