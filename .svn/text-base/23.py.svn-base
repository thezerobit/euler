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

def isabnum(num):
  if num < 12:
    return False
  elif sumofdivisors(num) > num:
    return True
  return False

print 'calculating abundant nums'
abnums = [x for x in xrange(12, 28124) if sumofdivisors(x) > x]

soa = {}

for x in abnums:
  for y in abnums:
    summ = x + y
    soa[summ] = summ

#print abnums

def issumofabnum(num):
  if num < 24:
    return False
  if num > 28123:
    return True
  global soa
  if num in soa:
    return True
  else:
    return False

count = 0

for x in xrange(1, 28124):
  if not issumofabnum(x):
    count += x

print count