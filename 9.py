import sys
product = 0


for a in range(1, 998):
    for b in range(a, 998):
        c = 1000 - a - b
        if (a*a + b*b) == c*c:
            print "%d %d %d"%(a, b, c)
            product = a * b * c
            print product
            sys.exit(0)
