def sumofdivisors(num):
  if num == 1:
    return 1
  top = num
  sum = 1
  i = 2
  while i < top:
    if (num % i) == 0:
      top = num / i
      sum += i
      if top > i:
        sum += top
    i += 1
  return sum

#print sumofdivisors(220)
#284

sd = {}
for i in xrange(1, 10001):
  sd[i] = sumofdivisors(i)

grandsum = 0

for x in xrange(1, 10001):
  for y in xrange(x+1, 10001):
    if (sd[x] == y) and (sd[y] == x):
      grandsum += (x + y)

print grandsum