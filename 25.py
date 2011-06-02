
fib = 1,1
last = 1
f = 2

while len(str(last)) < 1000:
  last = fib[0] + fib[1]
  fib = fib[1], last
  f += 1

print f
print last 
