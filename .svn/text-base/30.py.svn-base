mystr = '0123456789'
pow5 = {}
for digit in mystr:
  pow5[digit] = int(digit) ** 5

def sumofdigpow(num):
  summ = 0
  for digit in str(num):
    summ += pow5[digit]
  return summ

test = 10

bigsum = 0

while test < 1000000:
  if sumofdigpow(test) == test:
    bigsum += test
    print test, bigsum
  test += 1