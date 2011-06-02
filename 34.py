inp = '0123456789'
lookup = {}
def fact(x): return (1 if x==0 else x * fact(x-1))
for digit in inp:
  lookup[digit] = fact(int(digit))

def sumoffact(num):
  summ = 0
  for digit in str(num):
    summ += lookup[digit]
  return summ

bigsum = 0
test = 10

while test < 1000000:
  if test == sumoffact(test):
    bigsum += test
    print test, bigsum
  test += 1