def is_palindromic(teststr):
  length = len(teststr)
  ntests = length / 2
  for i in range(ntests):
    if teststr[i] != teststr[length - i - 1]:
      return False
  return True

def bin(num):
  res = ''
  while num > 0:
    res = str(num % 2) + res
    num = num >> 1
  return res

def check(num):
  return is_palindromic(str(num)) and is_palindromic(bin(num))

count = 0

for x in xrange(1, 1000000):
  if check(x):
    count += x

print count