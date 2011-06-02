def chainlength(num):
  count = 1
  while(True):
    if num == 1:
      return count
    count += 1
    if (num % 2) == 0:
      num = num / 2
    else:
      num = num * 3 + 1

greatest = 0
num = 0

print chainlength(13)

for n in xrange(1, 1000000):
  length = chainlength(n)
  if length > greatest:
    greatest = length
    num = n

print num
