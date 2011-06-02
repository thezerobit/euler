

def ntothen(n):
  product = 1
  for x in xrange(n):
    product *= n
    product %= 10000000000
  return product

sum = 0
for y in xrange(1,1001):
  sum += ntothen(y)

sumstr = str(sum)
print sumstr[-10:]