def fact(x): return (1 if x==0 else x * fact(x-1))
s = str(fact(100))
sum = 0
for d in s:
  sum += int(d)

print sum