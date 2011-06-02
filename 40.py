def digits_in_order(num):
  return num * ((10 ** num) - (10 ** (num - 1)))

def digit(num):
  num -= 1
  order = 1
  while True:
    digits = digits_in_order(order)
    base = (10 ** (order - 1)) 
    if num < digits:
      div = num / order
      pos = num % order
      hit = base + div
      digit = str(hit)[pos]
      return int(digit)
    else:
      num -= digits
      order += 1

#for x in xrange(1, 20):
#  print x, digit(x)

summ = digit(1) * digit(10) * digit(100) * digit(1000) * digit(10000) * digit(100000) * digit(1000000)
      
print summ